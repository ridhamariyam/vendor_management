
# Vendor Management System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

The Vendor Management System is a Django-based web application that facilitates vendor management, purchase order tracking, and performance metric monitoring. This system comprises several modules, each serving a specific purpose.

## Features

### Vendor Profile Management:
- Create, retrieve, update, and delete vendor profiles.
- Store vendor information including name, contact details, address, and unique vendor code.

### Purchase Order Tracking:
- Create, retrieve, update, and delete purchase orders.
- Track details of each purchase order including PO number, vendor reference, order date, items, quantity, and status.
- Filter purchase orders by vendor.

### Vendor Performance Evaluation:
- Calculate performance metrics for vendors including:
  - On-Time Delivery Rate
  - Quality Rating
  - Response Time
  - Fulfillment Rate
- Display vendor performance metrics.

# Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Modules](#modules)
5. [Authentication](#authentication)
6. [Vendors](#vendors)
7. [Purchase Orders](#purchase-orders)
8. [Performance Tracking](#performance-tracking)
9. [Requirements](#requirements)

## Installation

To set up the Vendor Management System, follow these steps:

 1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd vendor_management
    ```

 2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

 3. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

 4. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

 5. **Access the application:**

    Once the server is running, you can access the application at `http://localhost:8000` in your web browser.

## Usage

To use the Vendor Management System, follow these steps:

1. **Access the system through the provided URLs.**
2. **Obtain an authentication token** by making a POST request to `/token/` with valid credentials.
3. **Use the token** to access protected endpoints, such as vendor creation (`/vendors/`) and purchase order management (`/purchase_orders/`).

## API Endpoints

### Authentication

- `/token/`: Obtain an authentication token.
- `/signup/`: Register a new user.

### Vendors

- `/vendors/`: List and create vendors.
- `/vendors/<int:id>/`: Retrieve, update, and delete a specific vendor.
- `/vendors/<int:id>/performance`: Retrieve the performance metrics of a specific vendor.

### Purchase Orders

- `/purchase_orders/`: List and create purchase orders.
- `/purchase_orders/<int:id>/`: Retrieve, update, and delete a specific purchase order.
- `/purchase_orders/<int:id>/acknowledge`: Acknowledge receipt of a purchase order.
- `/purchase_orders/<int:id>/delivered`: Mark a purchase order as delivered.
- `/purchase_orders/<int:id>/addrating`: Add a quality rating to a purchase order.

### Performance Tracking

- `/vendors/`: List and create vendors.
- `/vendors/<int:id>/performance`: Retrieve the performance metrics of a specific vendor.

## Modules

### Authentication

The system uses Django SimpleJWT for token-based authentication. The provided MyTokenObtainPairView allows users to obtain JWT tokens, and the UserRegister view enables user registration.

### Vendors

Manage vendors through the VendorView and VendorDetailsView classes. Retrieve vendor performance metrics with the VendorPerformanceView.

### Purchase Orders

Handle purchase orders using PurchaseOrderView for listing and creation, and PurchaseOrderCRUDView for retrieval, updating, and deletion. Acknowledge, deliver, and rate purchase orders using additional endpoints.

### Performance Tracking

Retrieve vendor performance metrics through the VendorPerformanceView.

## Requirements

The system requires the following dependencies, listed in the `requirements.txt` file.

## Contact

If you have any concerns or feedback, feel free to reach out:

- Email: [ridhamariyam44@gmail.com](mailto:ridhamariyam44@gmail.com)
- LinkedIn: [Ridha Mariyam](https://www.linkedin.com/in/ridha-mariyam/)
