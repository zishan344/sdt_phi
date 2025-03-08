# PhiMart - E-commerce Project

PhiMart is an e-commerce platform built with Django and Django REST Framework. This project provides a comprehensive API for managing products, categories, orders, and user authentication.

## Project Structure

```
.gitignore
db.sqlite3
manage.py
requirements.txt
token.json
.vscode/
    settings.json
api/
    __init__.py
    admin.py
    apps.py
    models.py
    permissions.py
    tests.py
    urls.py
    views.py
    __pycache__/
    migrations/
fixtures/
    product_data.json
media/
    products/
order/
    __init__.py
    admin.py
    apps.py
    models.py
    serializers.py
    services.py
    tests.py
    views.py
    __pycache__/
    migrations/
phi_venv/
    pyvenv.cfg
    Include/
    Lib/
    Scripts/
    share/
phiMart/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
product/
    __init__.py
    admin.py
    apps.py
    models.py
    serializers.py
    tests.py
    views.py
    __pycache__/
    migrations/
users/
    __init__.py
    admin.py
    apps.py
    models.py
    serializers.py
    tests.py
    views.py
    __pycache__/
    migrations/
```

## Prerequisites

- Python 3.8 or higher
- Django 5.1.4
- Node.js (for frontend development, if applicable)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/zishan344/phimart.git
   cd phimart
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv phi_venv
   source phi_venv/bin/activate  # On Windows use `phi_venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply the migrations:

   ```sh
   python manage.py migrate
   ```

5. Load initial data:

   ```sh
   python manage.py loaddata fixtures/product_data.json
   ```

6. Create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage

### API Endpoints

- **User Authentication**

  - `POST /auth/jwt/create/`: Obtain JWT token
  - `POST /auth/users/`: Register a new user

- **Product Management**

  - `GET /api/v1/products/`: List all products
  - `POST /api/v1/products/`: Create a new product (Admin only)

- **Order Management**
  - `GET /api/v1/orders/`: List all orders (Admin only)
  - `POST /api/v1/orders/`: Create a new order

## API Documentation

The API documentation is available at `/swagger/` and `/redoc/` endpoints.

## Features

- **User Authentication**: User registration, login, and JWT authentication.
- **Product Management**: CRUD operations for products and categories.
- **Order Management**: Create and manage orders and cart items.
- **Admin Panel**: Django admin interface for managing the application.

## Testing

To run the tests, use the following command:

```sh
python manage.py test
```

## Deployment

To deploy the application, follow these steps:

1. Set up a production environment.
2. Configure the database settings in `phiMart/settings.py`.
3. Collect static files:

   ```sh
   python manage.py collectstatic
   ```

4. Apply the migrations:

   ```sh
   python manage.py migrate
   ```

5. Start the server:

   ```sh
   python manage.py runserver
   ```

## Troubleshooting

- **Issue**: Unable to connect to the database.

  - **Solution**: Check the database settings in `phiMart/settings.py` and ensure the database server is running.

- **Issue**: Static files not loading.
  - **Solution**: Ensure you have run `python manage.py collectstatic` and the static files are being served correctly.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djoser](https://djoser.readthedocs.io/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [yourname@phimart.com](mailto:zishan@phimart.com).
