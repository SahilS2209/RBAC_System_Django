This is a Role-Based Access Control (RBAC) system built using Django to manage user permissions and access control for your web application

RBAC allows you to define roles and assign permissions to those roles, enabling a fine-grained control over what users can do within the system

There are 3 roles: \
1. Admin \
2. User \
3. Viewer

These are the functionalities:

1. Admin: \
   Add user \
   Update user \
   Delete user \
   View users \
   Add api \
   Update api \
   Delete api \
   View apis \
   Map user to apis 

2. User: \
   Add api \
   Update api \
   Delete api \
   View mapped apis 

3. Viewer: \
   View all apis

When the user is authenticated(logged in), a JWT token is generated and it is saved in the database(Postgresql)

The token will expire in 1 day

To run this:

Requirements:

python>=3.6,<4.0 \
Django>=3.0,<4.0 \
djangorestframework>=3.12,<4.0 \
djangorestframework-simplejwt>=4.10,<5.0 \
django-cors-headers>=3.7,<4.0

git clone https://github.com/SahilS2209/RBAC_System_Django.git \
cd myproj 

pip install -r requirements.txt

settings.py: 

DATABASES = { \
    'default': { \
        'ENGINE': 'django.db.backends.postgresql', \
        'NAME': 'your_db_name', \     
        'USER': 'your_user_name', \        
        'PASSWORD': 'your_password', \
        'HOST': 'localhost', \                  
        'PORT': '5432', \                           
    } \
}

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

There are 11 apis created for this

You can test the apis in Postman







