# User Management API

## Overview

This API manages user-related functionalities, including registration, login, profile retrieval, updating, and account deletion, password reset with rate limiting.

## Base URL

The base URL for all endpoints is `https://localhost`.

## Authentication

API endpoints require authentication. Use a valid access token in the `Authorization` header.

## Endpoints

### Register User

- **Endpoint:** `POST /users/register`
- **Description:** Creates a new user profile with provided user details.
- **Request:**
  ```json
  {
    "username": "string",
    "email": "string",
    "full_name": "string"
  }
- **Response:**
  ```json
  {
     "message": "User registered successfully"
  }


### Login User

- **Endpoint:** `POST /users/login`
- **Description:** Allows users to log in using email and password.
- **Request:**
  ```json
  {
     "email": "string",
  "password": "string"
  }
- **Response:**
  ```json
  {
    "user_id": "string"
  }



### Get User Profile

- **Endpoint:** `GET /users/profile/{user_id}   `
- **Description:** Fetches user profile details based on user ID.
- **Response:**
  ```json
  {
   "username": "string",
  "email": "string",
  "full_name": "string",
  "created_at": "timestamp"
  }




### Update User Profile

- **Endpoint:** `PUT /users/profile/{user_id}`
- **Description:** Modifies user profile information.
- **Request:**
  ```json
  {
    "username": "string",
  "email": "string",
  "full_name": "string"
  }
- **Response:**
  ```json
  {
    "message": "User profile updated successfully"
  }


### Delete User Account

- **Endpoint:** `DELETE /users/profile/{user_id}`
- **Description:**  Deletes the user account and associated profile.
- **Response:**
  ```json
  {
    "message": "User account deleted successfully"
  }



### Reset Password

- **Endpoint:** `POST /users/reset-password`
- **Description:** Sends a password reset link to the user's email.
- **Request:**
  ```json
  {
      "email": "string"
  }
- **Response:**
  ```json
  {
     "message": "Password reset link sent to email"
  }


## Error Handling
The API responds with appropriate HTTP status codes and error messages. Refer to individual endpoint descriptions for details on error responses.   




## Rate Limiting
Each endpoint is rate-limited to 5 requests per minute to prevent abuse.

