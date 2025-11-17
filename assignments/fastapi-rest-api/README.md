# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and build RESTful APIs using the FastAPI framework in Python. You will create endpoints, handle requests and responses, and implement basic CRUD operations for a simple resource.

## 📝 Tasks

### 🛠️ FastAPI Project Setup

#### Description
Set up a new FastAPI project. Install FastAPI and Uvicorn, and create a basic application with a root endpoint.

#### Requirements
Completed program should:
- Install FastAPI and Uvicorn
- Create a main application file (e.g., main.py)
- Implement a root endpoint (`/`) that returns a welcome message

### 🛠️ CRUD Endpoints for a Resource

#### Description
Implement RESTful endpoints for a resource (e.g., `items`). Support creating, reading, updating, and deleting items using FastAPI's path and query parameters.

#### Requirements
Completed program should:
- Define a Pydantic model for the resource
- Implement endpoints for:
  - Creating a new item (`POST /items`)
  - Reading all items (`GET /items`)
  - Reading a single item by ID (`GET /items/{item_id}`)
  - Updating an item (`PUT /items/{item_id}`)
  - Deleting an item (`DELETE /items/{item_id}`)
- Return appropriate status codes and messages

### 🛠️ API Documentation & Testing

#### Description
Explore FastAPI's automatic API documentation and test your endpoints using the interactive docs.

#### Requirements
Completed program should:
- Access the interactive API docs at `/docs`
- Test all endpoints using the documentation UI
- Ensure all endpoints work as expected
