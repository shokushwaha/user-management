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
