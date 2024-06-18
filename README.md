# JAMES MURPHY API PROJECT

## ${\textsf{\color{blue}PROJECT REPOSITORY - JAMESMURPHY T2A2}}$

[Link To GitHub Repository](https://github.com/SteaneMurphy/JamesMurphy_T1A2)

Clone (HTTPS): https://github.com/SteaneMurphy/JamesMurphy_T1A2

![image](/docs/ProfileImage.jpg)

## ${\textsf{\color{blue}PROJECT DESCRIPTION}}$

This project is a working API Flask web-service using a PostgreSQL backend. It has been designed using MVC and RESTful API architecture with a 3NF (3rd Normal Form) database schema.

## ${\textsf{\color{blue}WHAT IS THIS API?}}$

This API provides data to any front-end application or service in the form of JSON objects. The 

## ${\textsf{\color{blue}PROJECT TRACKING}}$

All completed and outstanding tasks for this project can be found on its associated [Github Projects board](https://github.com/users/SteaneMurphy/projects/2/views/1).

## ${\textsf{\color{blue}PACKAGES AND DEPENDENCIES}}$

## ${\textsf{\color{blue}RELATIONAL DATABASE SYSTEMS}}$

## ${\textsf{\color{blue}ORM (OBJECT RELATIONAL MAPPER)}}$

## ${\textsf{\color{blue}ERD (ENTITY RELATIONSHIP DIAGRAM)}}$

## ${\textsf{\color{blue}ENTITY MODELS AND RELATIONSHIPS}}$

## ${\textsf{\color{blue}API ENDPOINTS}}$

### ${\textsf{\color{blue}USERS}}$

#### ${\textsf{\color{pink}REGISTER A NEW USER ACCOUNT}}$
- URI: ```/register```
- HTTPS: ```POST```
- BODY:
```json
{
    "first_name": "string",
    "last_name": "string",
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

#### *USER ACCOUNT LOGIN*
- URI: ```/login```
- HTTPS: ```POST```
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
    "response": "User login successful" 
}
```
- FAILED RESPONSE:
    - ```401 Unauthorised```

```json
{
    "response": "User login failed"
}
```
- Account Deletion
- Update User Details
- Get User Details By ID
- Get All Users

### SUBSCRIPTIONS

- Create Subscription (Admin Only)
- Update Subscription (Admin Only)
- Get Subscription By ID
- Delete Subscription (Admin Only)
- Get All Subscriptions

### INVOICES

- Create Invoice (Billing Only)
- Get Invoice By ID
- Update Invoice (Billing Only)
- Delete Invoice (Billing Only)
- Get All Invoices

### PRODUCTS

- Create Product (Admin Only)
- Delete Product (Admin Only)
- Update Product Details (Admin Only)
- Get Product Details By ID
- Get All Products

### LICENCES

- Create Product Licence
- Check Product Licence
- Delete Product Licence By ID

### PURCHASE HISTORY

- Create New Purchase History
- Get User Purchase History By ID
- Update User Purchase History
- Delete User Purchase History
- Get All Purchase History