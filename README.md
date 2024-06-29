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

Alongside productivity boosts, a SaaS product has a high chance of increasing business income due to its customer ease-of-use, ability to adapt to the market and offer the ability to subscribe to a service rather than paying an expensive upfront fee. This structure is seen in popular software like the Adobe suite, which in times past, used to cost thoudands of dollars per seat.

Other benefits include software that runs on the web or from the cloud, removing the need for high IT costs and managing licenses, freeing up staff to hot-desk or work remotely.

In 2024 (Vena Solutions, 2024, *74 SaaS Statistics, Trends and Benchmarks for 2024*, accessed, 20 June 2024, https://www.venasolutions.com/blog/saas-statistics):

- 73% of business surveyed, said that they spend too much time manually doing tasks that may be able to be automated

- 60% of surveyed business claim to be budgeting to spend 'more on software' in the coming year

- 50% of those surveyed mentioned they will increase their use of cloud providers in the coming years

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

It is possible that further tasks will be added as issues are encountered throughtout the project.

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
- JWT Extended

    - Flask is a web service/framework that is used to create the API. It interacts between the database and the python programming language allowing the creation of endpoints, blueprints, routes and custom error handling. The Flask application also provides an authentication library (Flask JWT Extended) to help with JWT token authentication on specific routes and endpoints.

- SQLAlchemy
- SQLAlchemy ORM

    - SQLAlchemy is a mapping library that can map SQL database tables to python objects in the Flask application. SQLAlchemy is used across different databases and help manage databse operations like queries and data retrieval across the API - examples being the use of the 'Mapped' or 'mapped_column' functions to turn attributes into objects. Using the extended ORM library, SQLAlchemy can manage relationships between tables and entities reprensenting one-to-one, one-to-many, etc.

- Marshmallow

    - Marshmallow is a library that helps convert the python objects and data types used in the API, into browser-readable JSON objects - serialisation/deserialisation. Marshmallow can also be used to validate data that is collected in body requests at endpoints, for example, a password submission can be subjected to rules about its length or character composition. Through the use of 'Schemas' and the 'Meta' class, Marshmallow can be used to specify the exact output structure when returing a JSON object.

- BCrypt

    - Bcrypt is a library that provides simple encryption and password hashing functions to the API. A user password (or any string) can be encrypted before storage. This password can further be checked against the encrpyted stored password without unsafely having to decrpyt said password. This sort of security is essential for any web-facing API that uses sensitive data.

- PostgreSQL

    - PostgreSQL is an open-source relational database system. Due to its open-source nature, the database is extensible and many different third-party services and libraries can be used in conjunction with the database.

These are only major dependencies, it is recommended that a user installs the full list of dependencies from the "requirements.txt" file included in this repository.

The following are installation instructions to get his application working in your environment.

## ${\textsf{\color{goldenrod}SETTING UP THE SERVICE}}$

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

### INSOMNIA HTTPS REQUESTS

Included in the documents folder is a list of endpoints that can be imported into the Insomnia API software. This can help if you don't want to manually create HTTPS body requests and URIs.

### RUNNING THE DATABASE

You will need to create a new postgreSQL database and fill out the database details in the ```.env.sample``` including databse username and password. The ```.env.sample``` will need its file extenstion changed to ```.env``` by removing the ```.sample``` extenstion

### FLASK COMMAND LINE COMMANDS

To seed the database or run an instance of the the Flask service. Please use the following commands in terminal, when in the project folder.

```Flask cli create``` - recreates and seeds the database

```Flask run``` - runs the Flask local service

The local service runs on ```HTTPS://127.0.0.1/5000```

### ADMIN ACCOUNT

You cannot create an admin account from accoutn creation and will need to use the existing admin account when the database is seeded. This admin account can make other accounts, admin by using the appropriate endpoint.

```HTTPS://127.0.0.1/5000/users/login/```

```json
{
    "email": "admin_email_1",
    "password": "testpassword123"
}
```

## ${\textsf{\color{goldenrod}RELATIONAL DATABASE SYSTEMS}}$

PostgreSQL was the database used for this API. Whilst it is a powerful and open-source system, it also has its drawbacks including in its use as a relational database system.

### BENEFITS

- PostgreSQL is open-source and therefore free. Due to this, the software is not limited by vision is quite extensible, allowing for the use of a multitude of third-party services, packages and libraries.

- This database uses 'ACID' (Atomicity, Consistency, Isolation, Durability). In short, it ensures that each database transaction is treated as a single instance, meaning that in the case of an error, the database can fall-back to its previous state. Postgres ensures that each end of a transaction force the use of the original data type, increasing reliability.

- The database has access to multiple built in security features allowing users to be authenicated down to specific tables within a system.

### DRAWBACKS

- Configuring the database to work with thrid-party software and libraries can be time consuming and complicated. Proprietary database software tends to have all required features built-in.

- Postgres is a relational database and thus uses MVCC (multi-concurrency) meaning that it stores multiple versions of data at any one time as part of its reliability and 'ACID' compliance. This can lead to much more storage space required for very large databases.

- Dead fields and data are not automatically cleaned up out of a Postgres database and manual cleaning called 'vacuuming' must be undertaken periodically. This can slow down system resources considerably and does not allow database transactions to take place during this process. This may not be suitable for systems that can have no down-time.

## ${\textsf{\color{goldenrod}ORM (OBJECT RELATIONAL MAPPER)}}$

SQLAlchemy is the ORM (Object-Relational Mapping) system used in this API. The ORM allowed access to read and manipulate the database using python objects rather than SQL language.

SQLAlchemy allows the creation of database schemas or tables directly within the API using python classes. This was extended with the uses of the 'Declarative' and 'Mapped' extenstions to SQLAlchemy. Columns and data types can be created directly inside a python class in a similar fashion to how the tables would look within the database. As follows is a code example utilising specific data types, primary and foreign keys, attribute creation and mapping.

![image](/docs/SQLAlchemy1.png)

SQlAlchemy also helps support relationships between database tables through the use of the 'relationship' and 'ForeignKey' function and types. These relationships can be back-referenced to parent tables and help facilitate cascade deletes. The ORM supports one-to-one, many-to-one and many-to-many relationship types.

![image](/docs/SQLAlchemy2.png)

SQLAlchemy also allows for database querying and retrieval of data as well as database session management. The database queries are abstracted from the base SQL query and easier to use. For all intents and purposes, the ORM keeps the SQL syntax similar with terms like 'select', 'join' and 'where'.

The database session can be managed with terms like 'session.commit' and 'session.flush'.

![image](/docs/SQLAlchemy3.png)

## ${\textsf{\color{goldenrod}ERD (ENTITY RELATIONSHIP DIAGRAM)}}$

The following is an ERD diagram for the proposed database system used by this API. The ERD has been normalised to 3rd normal form (3NF). All tables have had duplication removed and have a unique id to their respective entity. Each table has its proposed data types, constraints and relationships notated. A unique id can appear on another table as a foreign key (FK) associating the two tables together.

I arrived at the the 3NF by normalising the data through the 1st normal form (1NF) and 2nd normal form (2NF) respectively.

### 1NF

Each attribute in the table (row and column) should be unique without duplication. Each attribute was reduced to a singular format, for example, each row in the 'product' table contains a singular 'product' not multiple 'products'. Each table was assigned a primary key, in the case of this ERD, they are all ID values.

### 2NF

For 2nd normal form, each attribute that was not a key was made 'independent', that is it is only dependent on the primary key in the table it appears, it does not rely on another table's primary key when being referenced. An example of this is the date values in the 'user' table. They can only be accessed by using the primary key in the 'users' table, they are independent of the other tables.

### 3NF

All duplication has been removed. Tables that rely on each other in a many-to-many relationship are abstracted by having their primary keys appear as combination-keys in an association table, for example, the subscription_id, product_id and license attributes in the 'subscription_details' table.

![image](/docs/Key.png)

![image](/docs/ERD.png)

## ${\textsf{\color{goldenrod}ENTITY MODELS AND RELATIONSHIPS}}$

Before and during development of the API, multiple relationships were identified and developed between the entity models:

- User/Subscription: a one-to-zero/many relationship. One user may have zero or multiple seperate subscriptions at any one time. The PK(user_id) is a FK in the subscription table. This relationship allows for a database query that returns all subscriptions owned by a specific user.

![image](/docs/UserSubscription1.png)

![image](/docs/UserSubscription2.png)

- Subscription/Payment: a one-to-one/many relationship. One subscription may have one or multiple payments. This would look like either the first payment or a history of previous payments made against a specific subscription. The PK(subscription_id) is a FK in the payment table. This relationship allows for a database query that can return a specific payment or all the payments for a particular user and/or subscription.

![image](/docs/PaymentSubscription1.png)

![image](/docs/PaymentSubscription2.png)

- Subscription/Plan: a one-to-one/many relationship. As the plans are a static object in the database, simply listing available plan types, they are used multiple times for each new subscription. This means that one plan can have multiple associated subscriptions. The PK(plan_id) is a FK in the subscription table. This relationship allows for a database query that can return what plan a specific subscription is using or a list of all plans a user many have attatched to their account.

![image](/docs/PlanSubscription1.png)

![image](/docs/PlanSubscription2.png)

- User/SupportTicket: a one-to-zero/many relationship. A user may zero or many support tickets open at any one time. The PK(user_id) is a FK in the ticket table, associating a user with each support ticket. This relationship allows a database query that can return all support tickets associated with a specific user account.

![image](/docs/UserTicket1.png)

![image](/docs/UserTicket2.png)

- Subscription/Subscription_Details: a one-to-one/many relationship. This is one-half of a many-to-many relationship with the product table. As a product can appear in multiple subscriptions they are made unqiue by an association table. One FK(subscription_id) may be associated with many different FK(product_id). This relationship allow for a subscription to be associated with more than one product at a time and allows for database queries that can list all products associated to said subscription.

- Product/Subscription_Details: a one-to-one/many relationship. As explained above, this is the other half of a many-to-many relationship between the subscription and product tables. Please see above for relationship and database query explanations.

![image](/docs/SubscriptionDetails3.png)

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
