

# Vendor Management API Documentation

## Overview

The Vendor Management API provides endpoints for managing vendors, purchase orders, and tracking vendor performance. This API is built using Django and Django Rest Framework.

## Authentication

All API endpoints require authentication. To access protected endpoints, clients must include a valid authentication token in the request headers.

### Obtain Authentication Token

**Endpoint:** `/token/`

- **Method:** `POST`
- **Description:** Obtain an authentication token by providing valid credentials.
- **Request:**
  - Parameters:
    - `username`: User's username.
    - `password`: User's password.
- **Response:**
  - Successful response:
    ```json
    {
      "access": "your_access_token",
      "refresh": "your_refresh_token"
    }
    ```

### User Registration

**Endpoint:** `/signup/`

- **Method:** `POST`
- **Description:** Register a new user. This is how creating a new vendor. this endpoint automatically create vendor profile and user profile at the same time.
- **Request:**
  - Parameters:
    - `username`: New user's username.
    - `password`: New user's password.
    - 
- **Response:**
  - Successful response:
    ```json
    {
      "message": "User registered successfully"
    }
    ```

## Vendors

### List and Create Vendors

**Endpoint:** `/vendors/`

- **Method:** `GET` (List Vendors)
- **Description:** List all vendors.
- **Response:**
  - Successful response (For `GET` method):
    ```json
    [
      {
        "id": 1,
        "name": "Vendor 1",
        "other_field": "value"
        // Additional vendor fields
      },
      // ... other vendors
    ]
    ```
  - Successful response (For `POST` method):
    ```json
    {
      "id": 2,
      "name": "Vendor 2",
      "other_field": "value"
      // Additional vendor fields
    }
    ```

### Retrieve, Update, and Delete Vendor

**Endpoint:** `/vendors/<int:id>/`

- **Method:** `GET` (Retrieve), `PUT` (Update), `DELETE` (Delete)
- **Description:** Retrieve, update, or delete a specific vendor by ID.
- **Request:** (For `PUT` method)
  - Parameters:
    - `name`: Updated vendor name.
    - Update any additional vendor parameters if required.
- **Response:**
  - Successful response (For `GET` method):
    ```json
    {
      "id": 1,
      "name": "Vendor 1",
      "other_field": "value"
      // Additional vendor fields
    }
    ```

## Purchase Orders

### List and Create Purchase Orders

**Endpoint:** `/purchase_orders/`

- **Method:** `GET` (List Purchase Orders), `POST` (Create Purchase Order)
- **Description:** List all purchase orders or create a new purchase order.
- **Request:** (For `POST` method)
  - Parameters:
    - `vendor`: Vendor ID.
    - `other_field`: Other purchase order fields.
- **Response:**
  - Successful response (For `GET` method):
    ```json
    [
      {
        "id": 1,
        "vendor": 1,
        "other_field": "value"
        // Additional purchase order fields
      },
      // ... other purchase orders
    ]
    ```
  - Successful response (For `POST` method):
    ```json
    {
      "id": 2,
      "vendor": 2,
      "other_field": "value"
      // Additional purchase order fields
    }
    ```

### Retrieve, Update, and Delete Purchase Order

**Endpoint:** `/purchase_orders/<int:id>/`

- **Method:** `GET` (Retrieve), `PUT` (Update), `DELETE` (Delete)
- **Description:** Retrieve, update, or delete a specific purchase order by ID.
- **Request:** (For `PUT` method)
  - Parameters:
    - `vendor`: Updated vendor ID.
    - `other_field`: Updated purchase order fields.
- **Response:**
  - Successful response (For `GET` method):
    ```json
    {
      "id": 1,
      "vendor": 1,
      "other_field": "value"
      // Additional purchase order fields
    }
    ```

### Acknowledge Purchase Order

**Endpoint:** `/purchase_orders/<int:id>/acknowledge`

- **Method:** `POST`
- **Description:** Acknowledge receipt of a purchase order.
- **Response:**
  - Successful response:
    ```json
    {
      "id": 1,
      "vendor": 1,
      "acknowledgment_date": "2023-01-01T12:00:00Z",
      // Additional purchase order fields
    }
    ```

### Deliver Purchase Order

**Endpoint:** `/purchase_orders/<int:id>/delivered`

- **Method:** `POST`
- **Description:** Mark a purchase order as delivered.
- **Response:**
  - Successful response:
    ```json
    {
      "id": 1,
      "vendor": 1,
      "status": "completed",
      // Additional purchase order fields
    }
    ```

### Add Quality Rating to Purchase Order

**Endpoint:** `/purchase_orders/<int:id>/addrating`

- **Method:** `POST`
- **Description:** Add a quality rating to a purchase order.
- **Request:**
  - Parameters:
    - `qualityRating`: Quality rating (integer).
- **Response:**
  - Successful response:
    ```json
    {
      "id": 1,
      "vendor": 1,
      "quality_rating": 8,
      // Additional purchase order fields
    }
    ```

## Performance Tracking

### Retrieve Vendor Performance Metrics

**Endpoint:** `/vendors/<int:id>/performance`

- **Method:** `GET`
- **Description:** Retrieve the performance metrics of a specific vendor by ID.
- **Response:**
  - Successful response:
    ```json
    {
      "vendor_id": 1,
      "average_response_time": 24.5,
      "on_time_delivery_rate": 85.5,
      "fulfillment_rate": 92.3,
      "quality_rating_avg": 8.7,
      // Additional performance metrics
    }
    ```
