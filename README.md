# Django Project README

## Overview
This Django project is designed to manage clients, projects, and user assignments within a system. It provides REST APIs for various operations such as creating clients, adding projects, assigning users to projects, etc.

## Functionality
The project implements the following functionalities:
- Registering clients
- Fetching client information
- Editing and deleting client information
- Adding new projects for a client and assigning users to those projects
- Retrieving assigned projects for logged-in users

## Setup
To set up and run the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone [<repository_url>](https://github.com/saroshan/-design-APIS-for-the-machine-test-using-Django-REST-framework)
    ```

2. Navigate to the project directory:
    ```bash
    cd [<project_directory>](https://github.com/saroshan/-design-APIS-for-the-machine-test-using-Django-REST-framework)
    ```

3. Install dependencies (it's recommended to use a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser (if you want to access the Django admin):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the Django admin interface at `http://localhost:8000/admin/` to create users, clients, projects, etc., or use the provided REST APIs.

## API Endpoints
- **List/Create Clients**: `/clients/`
- **Retrieve/Update/Delete Client**: `/clients/<id>/`
- **List/Create Projects for a Client**: `/clients/<id>/projects/`
- **Retrieve/Update/Delete Project**: `/clients/<id>/projects/<id>/`

## Authentication and Authorization
The project uses token-based authentication. Users need to obtain an access token by providing their username and password through the `/api/token/` endpoint. Once authenticated, users can access protected endpoints by including the token in the request headers as `Authorization: Bearer <access_token>`.

## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).






admin login deatils:


username= admin
password= 123

