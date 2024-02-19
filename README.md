# COURSES
Eduplatform is a web application built with Django, designed to provide educational services.
Requirements: Docker, Docker Compose
git clone https://github.com/Katsiarynna/COURSES.git
cd eduplatform
Create a .env file in the root directory based on the provided .env.example file and fill in the required environment variables.
Build and start the Docker containers: docker-compose up -d --build
Access the application at http://localhost:8000 in your web browser.

Project Structure:
Dockerfile: Configuration for building the Docker image.
docker-compose.yml: Configuration for Docker Compose to manage the containers.
entrypoint.sh: Shell script to execute tasks when the container starts.
pyproject.toml: Poetry project configuration file.
README.md: This file providing information about the project.
eduplatform/: Django project directory.
eduplatform/: Main Django project settings.
chat/: Directory for chat functionality.
testing_system/: Directory for testing system functionality.
mentorship/: Directory for mentorship functionality.
This project uses PostgreSQL as the database backend. To configure PostgreSQL: Ensure you have PostgreSQL installed on your system or use the provided Docker configuration.

Dependencies: 
Python 3.10
Django 5.0.1
Django REST Framework 3.14.0
Python-dotenv 1.0.1
Psycopg2 2.9.9
Pillow 10.2.0
Mentorship 0.0.1
Channels 4.0.0
Channels-Redis 4.2.0

Development Dependencies
Black 24.1.1
Isort 5.13.2
Flake8 7.0.0

To run tests, use the following command: python manage.py test

Contributions are welcome! Please feel free to open issues or submit pull requests.
