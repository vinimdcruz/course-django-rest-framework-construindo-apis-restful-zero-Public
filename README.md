# Django Rest Framework: Beginning the Learning Journey

Hello :)

This repository marks the beginning of my learning journey with the Django Rest Framework (DRF). Here, you'll find examples, experiments, and notes related to the main features and best practices of this powerful tool for building APIs in Django.

## Goals
- Explore the fundamental features of DRF.
- Develop simple APIs to solidify learning.
- Document lessons learned throughout the process. 

## Content
- Code examples.
- Explanatory notes and comments.
- Useful links for documentation and references.

### Explanatory Notes and Comments
Below is a list of commands used during the course, organized by chapter:

On Mac, in the bash_profile file, add this line at the end: alias python=python3 to create an alias.
Then, run the command source ~/.bash_profile to update the shell with the latest changes.


#### Chapter 1: Getting to Know the Django Rest Framework
```
# Create a virtual environment to centralize all project dependencies
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  

# Install a specific version of Django
pip install Django==5.1.4  

# Create a new Django project in the current directory
django-admin startproject setup .  

# Create a new app named 'escola'
python manage.py startapp escola  

# Start the development server
python manage.py runserver  

# Install additional dependencies for the Django Rest Framework
pip install djangorestframework  # Core library for DRF
pip install markdown             # Enables Markdown support for the browsable API
pip install django-filter        # Adds filtering support for APIs  

# Save installed dependencies to a requirements file
pip freeze > requirements.txt  

# Apply database migrations
python manage.py makemigrations  
```

#### Chapter 2: Creating models and serializers
# Create a superuser to access the Django admin interface
python manage.py createsuperuser  

# Start the development server
python manage.py runserver  

#Docs about serializers
https://www.django-rest-framework.org/api-guide/serializers/

# Testing the models in Django Shell
>>> from escola.models import Estudante
#Before import EstudanteSerializer,I had to setup the python path
export PYTHONPATH=$PYTHONPATH:/Users/viniciusmoreira/Projects/courses/alura/escola
>>> from escola.serializers import EstudanteSerializer
>>> queryset = Estudante.objects.all()
>>> queryset
<QuerySet [<Estudante: Vini>, <Estudante: Mari>]>
>>> serializador = EstudanteSerializer(queryset, many=True)
>>> serializador.data
serializador.data
>>> serializador.data
[{'id': 1, 'nome': 'Vini', 'email': 'vini@vini.com', 'cpf': '22222222222', 'data_nascimento': '1989-10-02', 'numero_celular': '219999999999'}, {'id': 2, 'nome': 'Mari', 'email': 'mari@mari.com', 'cpf': '11111111111', 'data_nascimento': '1991-01-01', 'numero_celular': '21988888888'}]
>>> 
```

#### Chapter 3: Working with viewsets
# In this chapter we created some routes for students and courses

#### Chapter 4: Adding resources to the API
# In this chapter we added registration's viewset, serializer, route and admin page

#### Chapter 5: Adding Authentication
# In this chapter we added authentication and permissions to resources, and to the main API page

Feel free to explore, suggest improvements, and share ideas! 😊