# JAMES MURPHY API PROJECT

## ${\textsf{\color{goldenrod}PROJECT REPOSITORY - JAMESMURPHY T2A2}}$

[Link To GitHub Repository](https://github.com/SteaneMurphy/JamesMurphy_T1A2)

Clone (HTTPS): https://github.com/SteaneMurphy/JamesMurphy_T1A2

![image](/docs/ProfileImage.jpg)

## ${\textsf{\color{goldenrod}PROJECT DESCRIPTION}}$

This project is a working API Flask web-service using a PostgreSQL backend. It has been designed using MVC and RESTful API architecture with a 3NF (3rd Normal Form) database schema.

## ${\textsf{\color{goldenrod}WHAT IS THIS API?}}$

This API provides data to any front-end application or service in the form of JSON objects. The 

## ${\textsf{\color{goldenrod}PROJECT TRACKING}}$

All completed and outstanding tasks for this project can be found on its associated [Github Projects board](https://github.com/users/SteaneMurphy/projects/2/views/1).

## ${\textsf{\color{goldenrod}PACKAGES AND DEPENDENCIES}}$

## ${\textsf{\color{goldenrod}RELATIONAL DATABASE SYSTEMS}}$

## ${\textsf{\color{goldenrod}ORM (OBJECT RELATIONAL MAPPER)}}$

## ${\textsf{\color{goldenrod}ERD (ENTITY RELATIONSHIP DIAGRAM)}}$

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
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.             eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
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

#### ${\textsf{\color{red}UPDATE USER DETAILS}}$
*User may update account details using submitted details and user ID*

- URI: ```/users/update/<int:id>```
- HTTPS: ```POST```
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

- Create Subscription (Admin Only)
- Update Subscription (Admin Only)
- Get Subscription By ID
- Delete Subscription (Admin Only)
- Get All Subscriptions

### ${\textsf{\color{magenta}INVOICES}}$

- Create Invoice (Billing Only)
- Get Invoice By ID
- Update Invoice (Billing Only)
- Delete Invoice (Billing Only)
- Get All Invoices

### ${\textsf{\color{magenta}PRODUCTS}}$

- Create Product (Admin Only)
- Delete Product (Admin Only)
- Update Product Details (Admin Only)
- Get Product Details By ID
- Get All Products

### ${\textsf{\color{magenta}LICENCES}}$

- Create Product Licence
- Check Product Licence
- Delete Product Licence By ID

### ${\textsf{\color{magenta}PURCHASE HISTORY}}$

- Create New Purchase History
- Get User Purchase History By ID
- Update User Purchase History
- Delete User Purchase History
- Get All Purchase History