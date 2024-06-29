# JAMES MURPHY API PROJECT

## ${\textsf{\color{goldenrod}PROJECT REPOSITORY - JAMESMURPHY T2A2}}$

[Link To GitHub Repository](https://github.com/SteaneMurphy/JamesMurphy_T1A2)

Clone (HTTPS): https://github.com/SteaneMurphy/JamesMurphy_T1A2

![image](/docs/ProfileImage.jpg)

## ${\textsf{\color{goldenrod}PROJECT DESCRIPTION}}$

This project is a working API Flask web-service using a PostgreSQL backend. It has been designed using MVC and RESTful API architecture with a 3NF (3rd Normal Form) database schema.

## ${\textsf{\color{goldenrod}WHAT IS THIS API?}}$

This API provides data to any front-end application or service in the form of JSON objects. The service is a mock-up SaaS system whereby users can register and login to the system, purchase products through subscriptions and the system invoices the customer for said purchase. Each product comes with attatched licensing. 

This API helps an online business manage customers and the products and services they purchase as well as allowing the business to update or change a product/service at will. The product/service can be offered through a subscription by having the system automate billing and payments.

This solution reduces the amount of contact hours an employee of the business needs to spend organising customer data, preparing invoices and checking subscription and payment statuses by providing the data to automate the procedure.

## ${\textsf{\color{goldenrod}PROJECT TRACKING}}$

All completed and outstanding tasks for this project can be found on its associated [Github Projects board](https://github.com/users/SteaneMurphy/projects/2/views/1).

The project is split into 7 parent tasks, comprised of smaller individual tasks:

- Database Design
- Documentation: Endpoints
- Documentation
- Blueprints
- Main Application/Initialisation
- Models
- Authorisation

![image](/docs/GitHubProjectDatabaseDesign.PNG)

These tasks are tracked across four stages of completion:

- **Backlog:** parent task and associated child tasks have not been started

![image](/docs/GitHubProjectBacklog.PNG)

- **In Progress:** parent task has been started and one or multiple child tasks have been completed

![image](/docs/GitHubProjectInProgress.PNG)

- **Testing:** a parent task and all of its associated child tasks have been completed.The implemented features from this task are now awaiting testing. Further testing tasks may be added to re-test existing working features to ensure they do not break upon new features being added

![image](/docs/GitHubProjectTesting.PNG)

- **Done:** a parent task and its assicated feature is now tested and considered complete

![image](/docs/GitHubProjectDone.PNG)

## ${\textsf{\color{goldenrod}PACKAGES AND DEPENDENCIES}}$

This application uses the following dependencies:

- Flask
- SQLAlchemy
- SQLAlchemy ORM
- Marshmallow
- BCrypt
- JWT Extended
- PostgreSQL

These are only major dependencies, it is recommended that a user installs the full list of dependencies from the "requirements.txt" file included in this repository.

The following are installation instructions to get his application working in your environment.

### CLONE THE REPOSITORY

To clone the repository, please make a directory for the project. This can be done by making a new folder in Windows or by typing the following into a terminal:

```mkdir <directory_path>```

### INSTALL VIRTUAL ENVIRONMENT

The Python Virtual Environment package will allow a user to modify their project environment without affecting the overall system. To install this package, please enter the following command into the terminal:

```pip install venv```

### RUN VIRTUAL ENVIRONMENT

Once the virtual environment package has been installed, we need to create a new virtual environment. To create a new virtual environment, please use the following command:

```python3 -m venv .venv```

This new environment must be activated:

```source .venv/bin/activate```

### INSTALL DEPENDENCIES

Ensuring that you are within the newly created virtual environment, you can safely install the dependencies listed in the "requirements.txt". To iterate over the list and install each package, please use the following terminal command:

```pip install -r requirements.txt```

## ${\textsf{\color{goldenrod}RELATIONAL DATABASE SYSTEMS}}$

## ${\textsf{\color{goldenrod}ORM (OBJECT RELATIONAL MAPPER)}}$

## ${\textsf{\color{goldenrod}ERD (ENTITY RELATIONSHIP DIAGRAM)}}$

![image](/docs/ERD.png)

## ${\textsf{\color{goldenrod}ENTITY MODELS AND RELATIONSHIPS}}$

## ${\textsf{\color{goldenrod}API ENDPOINTS}}$

### ${\textsf{\color{magenta}USERS}}$

#### ${\textsf{\color{lightblue}REGISTER NEW USER ACCOUNT}}$

- URI: ```/users/```
- HTTPS: ```POST```
- BODY:
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string",
    "admin": bool
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}201 CREATED}}$
    ```json
    {
        "date_created": date.today(),
        "email": "string",
        "first_name": "string",
        "id": int,
        "last_login": date.today(),
        "last_name": "string"
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{red}500 INTERNAL SERVER ERROR}}$
    ```json
    {
        "error": "field missing information"
    }
    ```

#### ${\textsf{\color{lightblue}LOGIN TO EXISTING ACCOUNT}}$

- URI: ```/users/login/```
- HTTPS: ```POST```
- BODY:
```json
{
    "email": "string",
    "password": "string",
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //token used is an example JWT token
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTY1NzAyOSwianRpIjoiZTYxMWY5ZjgtNWI4Zi00YTIxLThkODgtZTQyYTQ1ZjUxOWE3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNzE5NjU3MDI5LCJjc3JmIjoiZjM0NmIxNjEtMWE0My00NjE0LTgzMjYtZWFmMzlhMzYxNGY3IiwiZXhwIjoxNzE5NjY0MjI5fQ.E2B2FkIUyfhToriSzG2I87YzRqq8A8spRXN9vLVGbG4"
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "field missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}401 BAD REQUEST}}$
    ```json
    {
        "error": "email and/or password incorrect""
    }
    ```

#### ${\textsf{\color{lightblue}GET ACCOUNT BY USER ID}}$

- URI: ```/users/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "date_created": date,
        "email": "string",
        "first_name": "string",
        "id": int,
        "last_login": date,
        "last_name": "string"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN LIST OF ALL ACCOUNTS}}$

- URI: ```/users/```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
    //entry 1
    "admin": bool,
    "date_created": date,
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "id": int,
    "last_login": date
    }
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```

#### ${\textsf{\color{lightblue}SET ADMIN ROLE FOR AN ACCOUNT}}$

- URI: ```/users/admin/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token```
- BODY:
```json
{
    "admin": bool
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "success": "account admin privileges updated"
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE ACCOUNT DETAILS}}$

- URI: ```/users/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY:
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "date_created": date.today(),
        "email": "string",
        "first_name": "string",
        "id": int,
        "last_login": date.today(),
        "last_name": "string"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE ACCOUNT PASSWORD}}$

- URI: ```/users/credentials/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY:
```json
{
    "password": "string",
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "success": "password updated"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}DELETE A USER ACCOUNT}}$

- URI: ```/users/<int:id>```
- HTTPS: ```DELETE```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {}
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```
    

### ${\textsf{\color{magenta}SUBSCRIPTIONS}}$

#### ${\textsf{\color{lightblue}CREATE NEW SUBSCRIPTION}}$

- URI: ```/subscriptions/```
- HTTPS: ```POST```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY:
```json
{
    "status": bool,
    "plan_id" int,
    "products": [int, int, ...]
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}201 CREATED}}$
    ```json
    {
        "end_date": date,
        "id": int,
        "plan": {
            "description": "string",
            "id": int,
            "length": int,
            "plan_name": "string",
            "price": float,
            "product_limit": int
        },
            "plan_id": int,
            "start_date": date,
            "status": bool,
            "user": {
                "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN EXISTING SUBSCRIPTION BY ID}}$

- URI: ```/subscriptions/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "end_date": date,
        "id": int,
        "plan": {
            "description": "string",
            "id": int,
            "length": int,
            "plan_name": "string",
            "price": float,
            "product_limit": int
        },
            "plan_id": int,
            "start_date": date,
            "status": bool,
            "user": {
                "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN ALL USER SUBSCRIPTIONS}}$

- URI: ```/subscriptions/user/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "end_date": date,
        "id": int,
        "plan": {
            "description": "string",
            "id": int,
            "length": int,
            "plan_name": "string",
            "price": float,
            "product_limit": int
        },
            "plan_id": int,
            "start_date": date,
            "status": bool,
            "user": {
                "id": int
        }
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN ALL SUBSCRIPTIONS (DATABASE)}}$

- URI: ```/subscriptions/```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "end_date": date,
        "id": int,
        "plan": {
            "description": "string",
            "id": int,
            "length": int,
            "plan_name": "string",
            "price": float,
            "product_limit": int
        },
            "plan_id": int,
            "start_date": date,
            "status": bool,
            "user": {
                "id": int
        }
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE AN EXISTING SUBSCRIPTION}}$

- URI: ```/subscriptions/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token```
- BODY:
```json
{
    "status": bool
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "id": int,
        "status": bool,
        "user": {
            "id": int
        }
    }  
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}DELETE A SUBSCRIPTION}}$

- URI: ```/subscriptions/<int:id>```
- HTTPS: ```DELETE```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {}
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

### ${\textsf{\color{magenta}PAYMENTS}}$

#### ${\textsf{\color{lightblue}CREATE A NEW PAYMENT}}$

- URI: ```/payments/<int:id>```
- HTTPS: ```POST```
- HEADER: ```admin: JWT token```
- BODY:
```json
{
    "payment_type": "string"
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}201 CREATED}}$
    ```json
    {
        "amount": float,
        "id": int,
        "payment_date": date.today(),
        "payment_type": "string",
        "subscription": {
            "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN A PAYMENT BY ID}}$

- URI: ```/payments/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "amount": float,
        "id": int,
        "payment_date": date,
        "payment_type": "string",
        "subscription": {
            "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN PAYMENTS BY USER}}$

- URI: ```/payments/user/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "amount": float,
        "id": int,
        "payment_date": date,
        "payment_type": "string",
        "subscription": {
            "id": int
        }
    },
    {
        //entry 2...etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN LIST OF ALL PAYMENTS (DATABASE)}}$

- URI: ```/payments/```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "amount": float,
        "id": int,
        "payment_date": date,
        "payment_type": "string",
        "subscription": {
            "id": int
        }
    },
    {
        //entry 2...etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE A PAYMENT}}$

- URI: ```/payments/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token```
- BODY:
```json
{
	"amount": float,
	"payment_type": "string"
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "amount": float,
        "id": int,
        "payment_date": date,
        "payment_type": "string",
        "subscription": {
            "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}DELETE A PAYMENT}}$

- URI: ```/payments/<int:id>```
- HTTPS: ```DELETE```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {}
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

### ${\textsf{\color{magenta}TICKETS}}$

#### ${\textsf{\color{lightblue}CREATE NEW SUPPORT TICKET}}$

- URI: ```/tickets/```
- HTTPS: ```POST```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY:
```json
{
    "issue_description": "string",
	"status": "string"
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}201 CREATED}}$
    ```json
    {
        "date_created": date,
        "id": int,
        "issue_description": "string",
        "status": "string",
        "user": {
            "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }

#### ${\textsf{\color{lightblue}RETURN TICKET BY ID}}$

- URI: ```/tickets/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "date_created": date,
        "id": int,
        "issue_description": "string",
        "status": "string",
        "user": {
            "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN TICKETS BY USER}}$

- URI: ```/tickets/user/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "date_created": date,
        "id": int,
        "issue_description": "string",
        "status": "string",
        "user": {
            "id": int
        }
    },
    {
        //entry 2...etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN LIST OF ALL TICKETS (DATABASE)}}$

- URI: ```/tickets/```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "date_created": date,
        "id": int,
        "issue_description": "string",
        "status": "string",
        "user": {
            "id": int
        }
    },
    {
        //entry 2...etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE EXISTING SUPPORT TICKET}}$

- URI: ```/tickets/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY:
```json
{
    "issue_description": "string",
	"status": "string"
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "date_created": date,
        "id": int,
        "issue_description": "string",
        "status": "string",
        "user": {
            "id": int
        }
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}DELETE A TICKET}}$

- URI: ```/tickets/<int:id>```
- HTTPS: ```DELETE```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {}
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

### ${\textsf{\color{magenta}PLANS}}$

#### ${\textsf{\color{lightblue}CREATE A NEW PLAN}}$

- URI: ```/plans/```
- HTTPS: ```POST```
- HEADER: ```admin: JWT token```
- BODY:
```json
{
	"plan_name": "string",
	"description": "string",
	"price": float,
	"length": int,
	"product_limit": int
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}201 CREATED}}$
    ```json
    {
        "plan_name": "string",
        "description": "string",
        "price": float,
        "length": int,
        "product_limit": int
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN PLAN BY ID}}$

- URI: ```/plans/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "plan_name": "string",
        "description": "string",
        "price": float,
        "length": int,
        "product_limit": int
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN PLAN BY USER}}$

- URI: ```/plans/user/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "plan_name": "string",
        "description": "string",
        "price": float,
        "length": int,
        "product_limit": int
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN LIST OF ALL PLANS (DATABASE)}}$

- URI: ```/plans/```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "plan_name": "string",
        "description": "string",
        "price": float,
        "length": int,
        "product_limit": int
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE AN EXISTING PLAN}}$

- URI: ```/plans/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token```
- BODY:
    ```json
    {
        "plan_name": "string",
        "description": "string",
        "price": float,
        "length": int,
        "product_limit": int
    }
    ```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "plan_name": "string",
        "description": "string",
        "price": float,
        "length": int,
        "product_limit": int
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

### ${\textsf{\color{magenta}PRODUCTS}}$

#### ${\textsf{\color{lightblue}CREATE A NEW PRODUCT}}$

- URI: ```/products/```
- HTTPS: ```POST```
- HEADER: ```admin: JWT token```
- BODY:
```json
{
	"product_name": "string",
	"description": "string"
}
```
- RESPONSE:
    - ##### ${\textsf{\color{green}201 CREATED}}$
    ```json
    {
        "product_name": "string",
        "id": int,
        "description": "string"
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN PRODUCT BY ID}}$

- URI: ```/products/<int:id>```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "product_name": "string",
        "id": int,
        "description": "string"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN ALL PRODUCTS (DATABASE)}}$

- URI: ```/products/```
- HTTPS: ```GET```
- HEADER: ```admin: JWT token``` or ```acc.owner: JWT token```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {   
        //entry 1
        "product_name": "string",
        "id": int,
        "description": "string"
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

#### ${\textsf{\color{lightblue}UPDATE AN EXISTING PRODUCT}}$

- URI: ```/products/<int:id>```
- HTTPS: ```PUT```
- HEADER: ```admin: JWT token```
- BODY:
    ```json
    {
        "product_name": "string",
        "description": "string"
    }
    ```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "product_name": "string",
        "id": int,
        "description": "string"
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{orange}403 FORBIDDEN}}$
    ```json
    {
        "error": "not authorised to access this resource"
    }
    ```
    - ##### ${\textsf{\color{orange}404 NOT FOUND}}$
    ```json
    {
        "error": "resource not found"
    }
    ```

### ${\textsf{\color{magenta}SUBSCRIPTION DETAILS}}$

#### ${\textsf{\color{lightblue}RETURN SUBSCRIPTION DETAILS BY ID}}$

- URI: ```/subscription-details/<int:id>```
- HTTPS: ```GET```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        "id": int,
        "license": "string",
        "product": {
            "description": "string",
            "id": int,
            "product_name": "string"
        },
        "subscription": {
            "end_date": date,
            "id": int,
            "plan": {
                "description": "string",
                "id": int,
                "length": int,
                "plan_name": "string",
                "price": float,
                "product_limit": int
            },
            "plan_id": int,
            "start_date": "string",
            "status": bool,
            "user": {
                "id": int
            }
        }
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{red}500 INTERNAL SERVER ERROR}}$
    ```json
    {
        "error": "field missing information"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN SUBSCRIPTION DETAILS BY SUBSCRIPTION}}$

- URI: ```/subscription-details/subscription/<int:id>```
- HTTPS: ```GET```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "id": int,
        "license": "string",
        "product": {
            "description": "string",
            "id": int,
            "product_name": "string"
        },
        "subscription": {
            "end_date": date,
            "id": int,
            "plan": {
                "description": "string",
                "id": int,
                "length": int,
                "plan_name": "string",
                "price": float,
                "product_limit": int
            },
            "plan_id": int,
            "start_date": "string",
            "status": bool,
            "user": {
                "id": int
            }
        }
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{red}500 INTERNAL SERVER ERROR}}$
    ```json
    {
        "error": "field missing information"
    }
    ```

#### ${\textsf{\color{lightblue}RETURN ALL SUBSCRIPTION DETAILS (DATABASE)}}$

- URI: ```/subscription-details/```
- HTTPS: ```GET```
- BODY: ```N/A```
- RESPONSE:
    - ##### ${\textsf{\color{green}200 OK}}$
    ```json
    {
        //entry 1
        "id": int,
        "license": "string",
        "product": {
            "description": "string",
            "id": int,
            "product_name": "string"
        },
        "subscription": {
            "end_date": date,
            "id": int,
            "plan": {
                "description": "string",
                "id": int,
                "length": int,
                "plan_name": "string",
                "price": float,
                "product_limit": int
            },
            "plan_id": int,
            "start_date": "string",
            "status": bool,
            "user": {
                "id": int
            }
        }
    },
    {
        //entry 2... etc
    }
    ```
    - ##### ${\textsf{\color{orange}400 BAD REQUEST}}$
    ```json
    {
        "error": "bad request: body missing information"
    }
    ```
    - ##### ${\textsf{\color{red}500 INTERNAL SERVER ERROR}}$
    ```json
    {
        "error": "field missing information"
    }
    ```
