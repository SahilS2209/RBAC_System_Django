from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import API, Role, StorableToken, MyUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound
from .serializers import UserSerializer, APISerializer, MapSerializer
from django.db.models import Q

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully.'})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = MyUser.objects.filter(username=username).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        storable_token = StorableToken.objects.create(user=user, token=str(refresh.access_token))
        storable_token.save()
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token})
    return Response({'error': 'Invalid credentials.'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user(request):
    if request.user.role.name == 'Admin':
        username = request.data.get('username')
        password = request.data.get('password')
        role_id = request.data.get('role') 
        
        if MyUser.objects.filter(username=username).exists():
            return Response({'detail': 'User with this username already exists', 'code': 'user_already_exists'}, status=400)

        role = Role.objects.get(id=role_id)
        user = MyUser(username=username, role=role)
        user.set_password(password)
        user.save()
        return Response({'message': 'User added successfully.'})

    return Response({'detail': 'You are not authorized to perform this action.', 'code': 'not_authorized'}, status=401)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_user(request, user_id):
    if request.user.role.name == 'Admin':
        try:
            user = MyUser.objects.get(id=user_id)
            user.delete()
            return Response({'message': 'User removed successfully.'})
        except MyUser.DoesNotExist:
            raise NotFound("User not found.")
    else:
        raise PermissionDenied("You are not authorized to remove users.")

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    if request.user.role.name == 'Admin':
        try:
            user = MyUser.objects.get(id=user_id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except MyUser.DoesNotExist:
            raise NotFound("User not found.")
    else:
        raise PermissionDenied("You are not authorized to update users.")
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_api(request):
    if request.user.role.name == 'Admin' or request.user.role.name == 'User':
        serializer = APISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'API added successfully.'})
        return Response(serializer.errors, status=400)
    else:
        raise PermissionDenied("You are not authorized to add APIs.")

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_api(request, api_id):
    if request.user.role.name == 'Admin' or request.user.role.name == 'User':
        try:
            api = API.objects.get(id=api_id)
            serializer = APISerializer(api, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'API updated successfully.'})
            return Response(serializer.errors, status=400)
        except API.DoesNotExist:
            raise NotFound("API not found.")
    else:
        raise PermissionDenied("You are not authorized to update APIs.")

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_api(request, api_id):
    if request.user.role.name == 'Admin' or request.user.role.name == 'User':
        try:
            api = API.objects.get(id=api_id)
        except API.DoesNotExist:
            raise NotFound("API not found.")

        # Check if the API is mapped to any user
        if api.myuser_set.exists():
            return Response({'error': 'API is mapped to one or more users. Cannot delete.'}, status=403)

        api.delete()
        return Response({'message': 'API deleted successfully.'})
    else:
        raise PermissionDenied("You are not authorized to delete APIs.")
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_users(request):
    if request.user.role.name == 'Admin':
        users = MyUser.objects.all()
        serializer = MapSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': 'You are not authorized to view users.'}, status=403)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def map_api_to_user(request):
    username = request.data.get('username')
    api_id = request.data.get('api_id')

    try:
        user = MyUser.objects.get(username=username)
    except MyUser.DoesNotExist:
        return Response({'message': 'User not found.'}, status=400)

    try:
        api = API.objects.get(id=api_id)
    except API.DoesNotExist:
        return Response({'message': 'API not found.'}, status=400)

    # Only the admin can map APIs to users
    if request.user.role.name == 'Admin':
        user.mapped_apis.add(api)
        return Response({'message': 'API mapped to user successfully.'})
    else:
        return Response({'message': 'You are not authorized to perform this action.'}, status=403)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_api(request):
    role_name = request.user.role.name

    if role_name == 'Admin':
        apis = API.objects.all()
    elif role_name == 'User':
        # Get APIs that are mapped to the user or created by the user
        apis = API.objects.filter(Q(myuser=request.user) | Q(created_by=request.user))
    else:  # Viewer role
        apis = API.objects.all()

    serializer = APISerializer(apis, many=True)
    return Response(serializer.data)