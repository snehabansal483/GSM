# Grocery Management System

A full-stack web application for managing grocery store inventory, orders, and user accounts with Flask backend and Bootstrap frontend.

## Features

- **User Authentication**:
  - Secure user registration and login
  - Session management
- **Inventory Management**:
  - View all products with details
  - Add new products to inventory
  - Remove products from system
- **Order Processing**:
  - Create new orders
  - View all order history
- **Unit of Measure Management**:
  - Manage different measurement units for products
- **Responsive Design**: Works on desktop and mobile devices
- **REST API**: Complete CRUD operations via REST endpoints

## Technologies Used

### Backend
- Python Flask
- MySQL
- Flask-CORS
- python-dotenv

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- jQuery

### Database
- MySQL

### DevOps & Deployment  
- **CI/CD:** GitHub Actions  
- **Hosting & Deployment:**  
  - Render (Backend Hosting)  
  - Railway (Database Hosting)  
  - Netlify (Frontend Hosting)
 
## Live Demo

[View Live Application](https://grocerymanage.netlify.app/)

> **Note**: The backend service on Render may take ~30 seconds to respond on first request due to cold start.

## API Endpoints

| Method | Endpoint               | Description                          |
|--------|------------------------|--------------------------------------|
| POST   | /register              | Register new user                    |
| POST   | /login                 | User login                           |
| GET    | /getUOM                | Get all units of measure             |
| GET    | /getProducts           | Get all products                     |
| POST   | /insertProduct         | Add new product                      |
| POST   | /deleteProduct         | Remove product                       |
| GET    | /getAllOrders          | Get all orders                       |
| POST   | /insertOrder           | Create new order                     |

## Installation

### Prerequisites
- Python 3.8+
- MySQL 8+
- pip
- Node.js (for optional frontend tooling)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/grocery-management-system.git
cd grocery-management-system
```

2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Set Up Environment Variables

Create a `.env` file in the root directory with your database configuration:

```env
DATABASE_URL=mysql://username:password@hostname:port/database_name
```

## Initialize the Database

1. Create a MySQL database.
2. Run the SQL scripts from the `database/` directory to set up tables.

## Run the Application

```bash
python app.py
```

The application should now be running at [http://localhost:5000](http://localhost:5000).

### Screenshots  
- **Login Page**  
  <img src="screenshots/login.png" alt="Login" width="400">  
- **Dashboard**
 ![Dashboard](screenshots/dashboard.png)
- **Product Management**
 ![Product](screenshots/manage-products.png)
- **New Product**
 ![Product](screenshots/new-products.png)
- **Order Management**
 ![Order](screenshots/new-order.png)

### Future Enhancements  
- Product category management  
- Barcode scanning integration  
- Sales reporting and analytics  
- Multi-user role support (admin, staff)  
- Inventory alerts for low stock  

### Contact  
- **Email:** snehabansal481@gmail.com
- **GitHub:** [Sneha Bansal](https://github.com/snehabansal483)  
