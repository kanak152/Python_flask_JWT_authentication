# Flask Blueprint Example with JWT Authentication

## Author

**Kanak Sachan**

## Date

2024-05-19

## Description

A basic definition of Flask Blueprint with JWT (JSON Web Token) authentication. In Flask, Blueprints are a way to organize your application into smaller and reusable modules. They help you structure your app by grouping related routes and functions together. This is especially useful for large applications.

## Why Use Blueprints?

- **Modularity**: Allows you to break your application into smaller, manageable pieces.
- **Reusability**: Blueprints can be reused across different projects.
- **Organization**: Helps keep your codebase organized and clean.

## Why Use JWT Authentication?

- **Security**: Provides a secure way to authenticate users without maintaining session information on the server.
- **Scalability**: Stateless nature of JWT makes it easy to scale the application.
- **Flexibility**: JWT tokens can be used for authentication across different domains.

## Project Structure

## Explanation

### `application/__init__.py`

- Create a Blueprint named `application`.
- Import the routes from the `routes.py` file within the `application` package.

### `application/routes.py`

- Define routes for the home page and APIs using the `application` Blueprint.
- Add JWT authentication to protect API routes.

### `templates/index.html`

- Simple HTML file that will be rendered when accessing the home page.

### `app.py`

- Create the Flask application instance.
- Configure JWT authentication.
- Register the `application` Blueprint with the Flask app.
- Run the app, making it accessible from any IP address on port 5000.

## How to Run the Application

1. **Navigate to your project directory** in the command line.
2. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```sh
   python app.py
   ```
4. **Open a web browser** and go to `http://127.0.0.1:5000/` to see the "Hello, World!" message.

## JWT Authentication

### Login

- To get a JWT token, make a POST request to the `/api/login` endpoint with the following JSON body:
  ```json
  {
    "username": "testuser",
    "password": "testpassword"
  }
  ```
- Example using `curl`:
  ```sh
  curl -X POST http://127.0.0.1:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'
  ```

### Access Protected Routes

- Use the JWT token in the `Authorization` header with the value `Bearer <your_jwt_token>` to access protected routes.

#### Example using `curl`

```sh
curl -X GET http://127.0.0.1:5000/api/items \
-H "Authorization: Bearer your_jwt_token"

```
