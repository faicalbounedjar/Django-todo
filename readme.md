# Todo App with django :

## Description :

Django-todo is a simple yet comprehensive To-Do list application built using Django and Django REST Framework. This project aims to 
showcase best practices in organization, documentation, and implementation

## Features :  

- CRUD Operations: Create, Read, Update, and Delete tasks effortlessly.
- RESTful API: Utilizing Django REST Framework, the application provides a robust API for seamless integration with other applications.
- Organization: The project structure adheres to Django's recommended layout, ensuring scalability and maintainability.
- Testing: Comprehensive test suites are included to validate the functionality of the application and ensure reliability.

## Project Structure:
```
Django-todo/
│
├── todo_site(the project)/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── dev.py
│   │   └── prod.py
│   │
│   ├── __init__.py
│   ├── urls.py
│   └── ...
│
├── todo(the app)/
│   ├── admin/
│   ├── api/
│   │   ├── serializers/
│   │   └── views
│   ├── tests/
│   ├── models/
│   ├── __init__.py
│   ├── apps.py
│   └── urls.py
│
├── setup.py
└── manage.py
```


## Prerequisites :
Before you begin, ensure you have the following installed on your system:
- Python (version 3.6 or higher)
- Download and Install the requirements by runing this command :

    ```
    pip install .
    ```
## Setup Instructions : 
**Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Django-todo.git
   ```

**Navigate to the Project Directory:**

```
cd todo_site
```

**Create a Virtual Environment:**

```
py -m venv venv
```

**Activate the Virtual Environment:**
- windows

    ```
    venv\Scripts\activate
    ```
- mac

    ```
    source venv/bin/activate
    ```

**Install Dependencies:**

```
pip install .
```

**Database Setup:**

- Open todo_site/settings/dev.py
- Configure your database settings
- By default, Django-todo is configured to use SQLite

**Migrate Database:**

```
python manage.py migrate
```

**Create a Superuser (Optional):**

```
python manage.py createsuperuser
```

**Run the Development Server:**

```
python manage.py runserver
```

## Usage :
- **Create Task (POST):**

  - Endpoint: `/`
  - Description: Create a new task.
  - Request Body:
    ```json
    {
      "title": "Task Title",
      "details": "Task details"
    }
    ```
  - Response:
    - Status Code: `200 ok`
    - Response Body:
      ```json
      {
        "id": 1,
        "title": "Task Title",
        "details": "Task details",
        "checked": false
      }
      ```

- **Retrieve All Tasks (GET):**

  - Endpoint: `/`
  - Description: Retrieve a list of all tasks.
  - Response:
    - Status Code: `200 OK`
    - Response Body:
      ```json
      [
        {
          "id": 1,
          "title": "Task Title 1",
          "details": "Task details 1",
          "checked": false
        },
        {
          "id": 2,
          "title": "Task Title 2",
          "details": "Task details 2",
          "checked": true
        },
        ...
      ]
      ```

- **Update Task (PUT/PATCH):**

  - Endpoint: `/update/<int:pk>/`
  - Description: Check or uncheck a task .
  - Response:
    - Status Code: `200 OK`
    - Response Body:
      ```json
      {
        "id": 1,
        "title": "Updated Task Title",
        "description": "Updated Task Description",
        "checked": true
      }
      ```

- **Delete Task (DELETE):**

  - Endpoint: `/del/<int:pk>/`
  - Description: Delete a specific task.
  - Response:
    - Status Code: `200 ok`


## Upcoming Updates :

- User Authentication: Users can register, log in, and manage their to-do lists securely.
- Create Collab Todos between users
- link the project with a next js app (done)
