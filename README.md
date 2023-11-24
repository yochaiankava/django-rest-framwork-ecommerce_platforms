 Django REST Framework Ecommerce Food Shop

This is a basic e-commerce website built as a starting point for an online store. The project aims to provide fundamental functionality for showcasing products and enabling customers to make purchases.

Features
Display a catalog of products with details such as name, price, and image.
Allow customers to add products to their shopping cart.
Provide for customers to review and confirm their orders & a checkout process that close the purchase & save to DB.
Provide for customers to review their purchases history.
Handle user authentication for creating accounts and logging in.
Admin panel for managing products, orders, and customer information.
Getting Started
Clone the repository: git clone https://github.com/yochaiankava/django-rest-framwork-ecommerce_platforms.git
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: venv\Scripts\activate
Install dependencies: pip install -r requirements.txt
Apply database migrations: python manage.py migrate
Create a superuser for accessing the admin panel: python manage.py createsuperuser
Run the development server: python manage.py runserver
Usage
Access the admin panel at http://localhost:8000/admin and log in using the superuser credentials.
Add products through the admin panel.
Browse the products on the main site and add them to the cart.
Proceed to the checkout process and confirm the order.
Review order history and customer information through the admin panel.
Admin Details:
user name-yochai password-1234

Special Button Actions:
checkout button-will finish purchase & will change purchase cart status to "closed"

Render URL-

