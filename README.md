## BUCKETLIST DJANGO API APPLICATION

According to Merriam-Webster Dictionary, a Bucket List is a list of things that one has not done 
before but wants to do before dying. This project aims at implementing an API for an online Bucket 
list service using Django.

Users will be able to register, and use the service to create their bucketlists, with bucketlist 
items that they will be able to edit, and update as necessary.

It utilizes create, Read, Update update and Delete (CRUD) operations to create, read, update, 
and delete bucketlist and bucketlist items on the server using the REST framework and JSON.

### Definitions

**Bucketlist**- A broad wishlist of things one desires to accomplish, experience or engage in 
before they die. This may include:
 
 * Travel the world.
 * Live a healthy lifestyle.
 * Give back to society.
 * Learn programming
 * ETC.
 
**Bucketlist Items**- These are the specific activities/steps taken towards actualizing the 
specific bucketlist as defined above. Examples of bucketlist for _Travel the World_ might include:
* Visit the Maldives
* Live in Jamaica for a year
* Swim with the dolphines in Wasini.


**API**- (Application Program Interface) provides a blueprint for how software 
programs interacts with each other.

**JSON**-(Javascript Object Notation) is a light-weight format that facilitates interchange of 
data between different systems or, case in point, software. It is intended to be universal and 
thus allows consumption of data by any program regardless of the programming language it is 
written in. Sample JSON data is represented as a key:value dictionary as below

```json
{
"user_email": "dan@gmail.com",
"user_password": "Qwerty1234"
}
```

**REST**-(REpresentational State Transfer) is way of building API's. The five main principles the
 implementation of REST are:

* Everything is a resource.
* Every resource has a unique identifier.
* Use simple and uniform interfaces.
* Communication is done by representation.
* Aim to be Stateless.


### CODE STYLE
This project complies with [pep8](https://www.python.org/dev/peps/pep-0008/) except 
for line length which is set at 100 characters.

## Installation

THis application runs on Python 3 or later.
Clone this repo, cd into the `djangoBucketlist` directory and run the following:
 1. python3 manage.py makemigrations
 2. python3 manage.py migrate
 3. `python manage.py runserver`
 
Access the service at `http://127.0.0.1:8000/bucketlists` in your browser.

## Usage
### Endpoints

**POST** `/api/v1/auth/register` - Register a user.

**POST** `/api/v1/auth/login` - Login user.

**POST** `/api/v1/bucketlists/` - Create a new bucket list.

**GET** `/api/v1/bucketlists/` - Retrieve all the created bucket lists.

**GET** `/api/v1/bucketlists/<bucket_id>` - Get a single bucket list.

**PUT** `/api/v1/bucketlists/<bucket_id>` - Update a single bucket list.

**DELETE** `/api/v1/bucketlists/<bucket_id>` | Delete single bucket list. |
