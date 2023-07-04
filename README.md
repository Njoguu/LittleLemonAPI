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

## Running the API
1. Prepare your virtual environment and install all dependencies using the following commands:

- `cd LittleLemon`

- `pipenv shell`

- `pipenv install`

2. Run the app using these commands:

- `python manage.py makemigrations `

- `python manage.py migrate`

- `python manage.py runserver`

## API Endpoints
### Postman Collection: LittleLemon API
After running the E-Commerce application, a Postman Collection containing all available API endpoints is provided for your convenience. To utilize Postman collection, you can easily fork it into your own Postman workspace. This allows you to have your own copy of the collection, which you can modify and customize according to your specific needs.

To fork the Postman collection, please follow the steps below:
1. Ensure that you have Postman installed on your computer. If you don't have it yet, you can download it from the [official website](https://www.postman.com/downloads/).
2. Open Postman and log in to your account. If you don't have an account, you can create one for free.
3. Once you're logged in, click on the Collections tab located in the left sidebar.
4. In the collections view, click on the New button to create a new collection.
5. Give your new collection a meaningful name, such as "LittleLemon API Fork."
6. Now, click on the Import button located at the top right corner of the collections view.
7. In the Import dialog, select the Link tab.
8. Copy the link to the E-Commerce API collection you wish to fork.
9. Paste the link into the Link field in the Import dialog.
10. Click on the Import button to initiate the forking process.

Postman will create a copy of the LittleLemonAPI collection and add it to your workspace. You can now see the newly imported collection listed in your collections view.

The collection is organized into folders, making it easy to navigate and locate the specific endpoints you need. Each folder corresponds to a specific area of functionality within the LittleLemonAPI application.

Please refer to the documentation provided within each folder for detailed information about the available endpoints, their parameters, and the expected responses.

Feel free to explore the endpoints, test different API requests.
