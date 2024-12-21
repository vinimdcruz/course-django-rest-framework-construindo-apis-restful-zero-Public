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

# Create a superuser to access the Django admin interface
python manage.py createsuperuser  
```

#### Chapter 2: Creating models and serializers


Sinta-se à vontade para explorar, sugerir melhorias e compartilhar ideias! 😊