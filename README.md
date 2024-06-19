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

#### ${\textsf{\color{red}REGISTER A NEW USER ACCOUNT}}$
*Create a new user account in the database with the submitted details*

- URI: ```/users/register```
- HTTPS: ```POST```
- HEADER: Not Applicable
- AUTHORISATION: None
- BODY:
```json
{
    "first_name": "string",
    "last_name": "string",
    "phone": "string",
    "email": "string",
    "password": "string",
}
```
- SUCCESSFUL RESPONSE: 
    - ```201 Created```

```json
{
    "response": "User registration successful" 
}
```
- FAILED RESPONSE:
    - ```400 Bad Request```

```json
{
    "response": "User registration failed"
}
```
<br>

#### ${\textsf{\color{red}USER ACCOUNT LOGIN}}$
*Log user into system with supplied credentials. Returns a bearer JWT token*

- URI: ```/users/login```
- HTTPS: ```POST```
- HEADER: Not Applicable
- AUTHORISATION: ${\textsf{\color{red}User Acccount Credentials}}$
- BODY:
```json
{
    "email": "string",
    "password": "string",
}
```
- SUCCESSFUL RESPONSE: 
    - ```200 OK```

```json
{
    //example token provided
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "repsonse": "User login successful",
}
```
- FAILED RESPONSE:
    - ```401 Unauthorised```

```json
{
    "response": "User login failed"
}
```
<br>

#### ${\textsf{\color{red}UPDATE USER DETAILS}}$
*User may update account details using submitted details and user ID*

- URI: ```/users/update/<int:id>```
- HTTPS: ```PUT```
- HEADER: ${\textsf{\color{red}JWT Bearer Token}}$
- AUTHORISATION: ${\textsf{\color{red}User}}$
- BODY:
```json
{
    "first_name": "string",
    "last_name": "string",
    "phone": "string",
    "email": "string",
    "password": "string",
}
```
- SUCCESSFUL RESPONSE: 
    - ```200 OK```

```json
{
    "response": "User Details Updated Successfully" 
}
```
- FAILED RESPONSE:
    - ```401 Unauthorised```
    - ```404 Not Found```

```json
{
    "response": "Not Authorised"
}
```
```json
{
    "response": "Not Found"
}
```
<br>

#### ${\textsf{\color{red}ACCOUNT DELETION}}$
*Admin may delete a specific user account via an user ID*

- URI: ```/users/delete/<int:id>```
- HTTPS: ```GET```
- HEADER: ${\textsf{\color{red}JWT Bearer Token}}$
- AUTHORISATION: ${\textsf{\color{red}Admin}}$
- SUCCESSFUL RESPONSE: 
    - ```200 OK```

```json
{
    "response": "User <int:id> deleted successfully" 
}
```
- FAILED RESPONSE:
    - ```401 Unauthorised```
    - ```404 Not Found```

```json
{
    "response": "Unauthorised Access"
}
```
```json
{
    "response": "User Does Not Exist"
}
```
<br>

#### ${\textsf{\color{red}GET USER DETAILS BY ID}}$
*Returns user details by submitted ID*

- URI: ```/users/<int:id>```
- HTTPS: ```GET```
- HEADER: ${\textsf{\color{red}JWT Bearer Token}}$
- AUTHORISATION: ${\textsf{\color{red}User}}$
- SUCCESSFUL RESPONSE: 
    - ```200 OK```

```json
{
    "first_name": "string",
    "last_name": "string",
    "phone": "string",
    "email": "string",
}
```
- FAILED RESPONSE:
    - ```401 Not Authorised```
    - ```404 Not Found```

```json
{
    "response": "Not Authorised"
}
```
```json
{
    "response": "Not Found"
}
```
<br>

#### ${\textsf{\color{red}GET ALL USERS DETAILS}}$
*Returns user details by submitted ID*

- URI: ```/users```
- HTTPS: ```GET```
- HEADER: ${\textsf{\color{red}JWT Bearer Token}}$
- AUTHORISATION: ${\textsf{\color{red}Admin}}$
- SUCCESSFUL RESPONSE: 
    - ```200 OK```

```json
[
    {
        //user 1
        "user_ID": "integer",
        "first_name": "string",
        "last_name": "string",
        "phone": "string",
        "email": "string",
    },
    {
        //user 2
        "user_ID": "integer",
        "first_name": "string",
        "last_name": "string",
        "phone": "string",
        "email": "string",
    },
    ///etc for all users in database
]
```
- FAILED RESPONSE:
    - ```401 Not Authorised```
    - ```404 Not Found```

```json
{
    "response": "Not Authorised"
}
```
```json
{
    "response": "Not Found"
}
```
<br>

### ${\textsf{\color{magenta}SUBSCRIPTIONS}}$

#### ${\textsf{\color{red}CREATE SUBSCRIPTION}}$
*Create a new subscription type*

- URI: ```/subscriptions```
- HTTPS: ```POST```
- HEADER: ${\textsf{\color{red}JWT Bearer Token}}$
- AUTHORISATION: ${\textsf{\color{red}Admin}}$
- SUCCESSFUL RESPONSE: 
    - ```200 OK```

```json
[
    {
        //user 1
        "subscription_ID": "integer",
        "first_name": "string",
        "last_name": "string",
        "phone": "string",
        "email": "string",
    },
    {
        //user 2
        "user_ID": "integer",
        "first_name": "string",
        "last_name": "string",
        "phone": "string",
        "email": "string",
    },
    ///etc for all users in database
]
```
- FAILED RESPONSE:
    - ```401 Not Authorised```
    - ```404 Not Found```

```json
{
    "response": "Not Authorised"
}
```
```json
{
    "response": "Not Found"
}
```
<br>

- Create Subscription (Admin Only)
- Update Subscription (Admin Only)
- Get Subscription By ID
- Delete Subscription (Admin Only)
- Get All Subscriptions

### ${\textsf{\color{magenta}PAYMENTS}}$

### ${\textsf{\color{magenta}PRODUCTS}}$

### ${\textsf{\color{magenta}PLANS}}$

### ${\textsf{\color{magenta}TICKETS}}$