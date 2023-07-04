# LittleLemonAPI
## About this Course
Delve deeper into the processes and concepts behind APIs and their infrastructure. Explore the key concepts that underpin API development and the principles of representational state transfer architectural style (REST) architecture. Build basic API and REST data backbones for web apps using Django. Discover emerging API technology and practice other ways to build and work with APIs. Finally, you will test, optimize and develop documentation for an API.

By the end of this course you will be able to:

- Work with and build APIs
-	Build basic API and REST data backbones for web apps using Django
-	Discover emerging API technology 
-	Test, optimize and develop documentation for an API

## Capabilities
- [x] The admin can assign users to the manager group
- [x] You can access the manager group with an admin token
- [x] The admin can add menu items 
- [x] The admin can add categories
- [x] Managers can log in 
- [x] Managers can update the item of the day
- [x] Managers can assign users to the delivery crew
- [x] Managers can assign orders to the delivery crew
- [x] The delivery crew can access orders assigned to them
- [x] The delivery crew can update an order as delivered
- [x] Customers can register
- [x] Customers can log in using their username and password and get access tokens
- [x] Customers can browse all categories 
- [x] Customers can browse all the menu items at once
- [x] Customers can browse menu items by category
- [x] Customers can paginate menu items
- [x] Customers can sort menu items by price
- [x] Customers can add menu items to the cart
- [x] Customers can access previously added items in the cart
- [x] Customers can place orders
- [x] Customers can browse their own orders

## API Endpoints
API Endpoints:

### User Registration and Token Generation Endpoints:
-	/api/users
-	/api/users/users/me/
-	/token/login/

### Menu Item Endpoints:
-	/api/menu-items
-	/api/menu-items
-	/api/menu-items/{menuItem}
-	/api/menu-items/{menuItem}
-	/api/menu-items
-	/api/menu-items
-	/api/menu-items/{menuItem}
-	/api/menu-items/{menuItem}
-	/api/menu-items/{menuItem}

### User group management endpoints:
-	/api/groups/manager/users
-	/api/groups/manager/users
-	/api/groups/manager/users/{userId}
-	/api/groups/delivery-crew/users
-	/api/groups/delivery-crew/users
-	/api/groups/delivery-crew/users/{userId}

### Cart management endpoints:
-	/api/cart/menu-items
-	/api/cart/menu-items
-	/api/cart/menu-items

### Order management endpoints:
-	/api/orders
-	/api/orders
-	/api/orders/{orderId}
-	/api/orders
-	/api/orders/{orderId}
-	/api/orders/{orderId}
-	/api/orders
-	/api/orders/{orderId}

## Running the API
1. Prepare your virtual environment and install all dependencies using the following commands:

- `cd LittleLemon`

- `pipenv shell`

- `pipenv install`

2. Run the app using these commands:

- `python manage.py makemigrations `

- `python manage.py migrate`

- `python manage.py runserver`
