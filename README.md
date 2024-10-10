
# One Stop Solutions

One Stop Solutions is a Django-based e-commerce platform that provides a comprehensive solution for purchasing a wide variety of products, including iPhones, iPads, laptops, and MacBooks.

## Features

- **Product Management**: Browse and view detailed descriptions of products.
- **Cart Functionality**: Add products to the cart, manage quantities, and review items.
- **Order Management**: Place orders and view order history.
- **User Authentication**: Sign up, log in, and manage user profiles.
- **Payment Gateway**: Seamless payment processing.
- **Email Notifications**: Receive confirmation emails for orders placed.

## Project Structure

```
OneStopSolutions/
├── OneStopSolutions/        # Project settings and configuration
├── auth_app/                # Authentication-related views and models
├── cart/                    # Shopping cart functionality
├── iphone/                  # iPhone product category
├── ipad/                    # iPad product category
├── laptop/                  # Laptop product category
├── macbook/                 # MacBook product category
├── media/                   # Media files for product images
├── static/                  # Static assets like CSS and JS
├── templates/               # HTML templates for the frontend
├── manage.py                # Django's management script
├── requirements.txt         # List of Python dependencies
└── .gitignore               # Ignored files for Git
```

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/24sagar/onestop.git
   ```

2. **Navigate into the project directory**:

   ```bash
   cd onestop
   ```

3. **Create a virtual environment**:

   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment**:

   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     .\env\Scriptsctivate
     ```

5. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

7. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` in your browser to view the homepage.
- Sign up or log in to explore the full range of features.
- Browse products, add them to your cart, and proceed with checkout.

## Contributing

Feel free to contribute to the project by submitting pull requests or opening issues to discuss improvements and feature requests.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Author

[Sagar](https://github.com/24sagar)
