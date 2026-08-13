# Day 14
# WebSockets, Rate Limiting, HTTPS Headers,
# Input Sanitization, HTTP Internals, curl & HTTPie


# ============================================================
# 1. WebSockets
# ============================================================

# WebSocket allows the client and server to communicate
# continuously without creating a new HTTP request every time.

# It is mainly used for:
# - Chat applications
# - Live notifications
# - Real-time updates
# - Online games


# -------------------------
# WebSocket Route
# -------------------------

# We use @app.websocket() to create a WebSocket route.

from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    message = await websocket.receive_text()

    await websocket.send_text(
        f"You sent: {message}"
    )


# Example:
#
# Client connects to:
# ws://127.0.0.1:8000/ws
#
# Client sends:
# Hello
#
# Server sends:
# You sent: Hello


# -------------------------
# Connect
# -------------------------

# accept() is used to accept the WebSocket connection.

await websocket.accept()


# -------------------------
# Receive Message
# -------------------------

message = await websocket.receive_text()

# Example:
#
# Client sends:
# "Hello"
#
# message = "Hello"


# -------------------------
# Send Message
# -------------------------

await websocket.send_text("Hello from server")


# Example:
#
# Client sends:
# "Hi"
#
# Server sends:
# "Hello from server"


# -------------------------
# Disconnect
# -------------------------

# We can handle a client disconnecting using
# WebSocketDisconnect.

from fastapi import WebSocketDisconnect


@app.websocket("/chat")
async def chat(websocket: WebSocket):

    await websocket.accept()

    try:

        while True:

            message = await websocket.receive_text()

            await websocket.send_text(message)

    except WebSocketDisconnect:

        print("Client disconnected")


# When the client closes the connection:
#
# Client
#   ↓
# Disconnect
#   ↓
# WebSocketDisconnect
#   ↓
# "Client disconnected"


# -------------------------
# Broadcast
# -------------------------

# Broadcast means sending the same message
# to multiple connected clients.


connected_clients = []


@app.websocket("/chat")
async def chat(websocket: WebSocket):

    await websocket.accept()

    connected_clients.append(websocket)

    try:

        while True:

            message = await websocket.receive_text()

            for client in connected_clients:

                await client.send_text(message)

    except WebSocketDisconnect:

        connected_clients.remove(websocket)


# Example:
#
# Nitin sends:
# "Hello everyone"
#
# Server sends the same message to:
#
# Rahul
# Amit
# Nitin
#
# This is called broadcasting.


# ============================================================
# 2. Rate Limiting
# ============================================================

# Rate limiting means limiting the number of requests
# a user can make within a specific period.

# Example:
#
# A user can make only 5 requests per minute.


# Example:

request_count = 0

if request_count >= 5:

    print("Too many requests")

else:

    request_count += 1

    print("Request allowed")


# If the user makes more than the allowed requests:
#
# Response:
#
# 429 Too Many Requests


# Why use Rate Limiting?
#
# - Prevent too many requests
# - Protect the server
# - Prevent API abuse
# - Reduce unnecessary traffic


# ============================================================
# 3. HTTPS Headers
# ============================================================

# HTTPS headers provide additional security to web applications.


# -------------------------
# HSTS
# -------------------------

# HSTS = HTTP Strict Transport Security
#
# It tells the browser to use HTTPS instead of HTTP.


# Example:

Strict-Transport-Security: max-age=31536000


# Example:
#
# User tries:
#
# http://example.com
#
# Browser uses:
#
# https://example.com


# -------------------------
# CSP
# -------------------------

# CSP = Content Security Policy
#
# It controls which resources can be loaded
# by the browser.


# Example:

Content-Security-Policy: default-src 'self'


# This means:
#
# By default, allow resources only from
# the same website.


# ============================================================
# 4. Input Sanitization
# ============================================================

# Input sanitization means checking and cleaning
# user input before using it.


# Example:

name = input("Enter your name: ")

name = name.strip()

print(name)


# If user enters:

# "   Nitin   "

# After strip():

# "Nitin"


# We can also validate input.


age = 22

if age < 0:

    print("Invalid age")

else:

    print("Valid age")


# FastAPI/Pydantic also helps with input validation.


from pydantic import BaseModel


class Student(BaseModel):

    name: str
    age: int


# Valid input:

student = Student(
    name="Nitin",
    age=22
)


# Invalid input:

student = Student(
    name="Nitin",
    age="hello"
)

# Pydantic will raise a validation error.


# ============================================================
# 5. HTTP Internals
# ============================================================

# HTTP works using a Request and Response model.


# Client
#    ↓
# HTTP Request
#    ↓
# Server
#    ↓
# HTTP Response
#    ↓
# Client


# -------------------------
# HTTP Request
# -------------------------

# Example:

GET /students HTTP/1.1

Host: 127.0.0.1:8000

Accept: application/json


# Request contains:
#
# Method
# URL
# Headers
# Body


# -------------------------
# HTTP Response
# -------------------------

# Example:

HTTP/1.1 200 OK

Content-Type: application/json


{
    "name": "Nitin",
    "age": 22
}


# Response contains:
#
# Status Code
# Headers
# Body


# ============================================================
# 6. HTTP Methods
# ============================================================


# GET
# Used to read data.

GET /students


# POST
# Used to create data.

POST /students


# PUT
# Used to update existing data.

PUT /students/1


# PATCH
# Used to partially update data.

PATCH /students/1


# DELETE
# Used to delete data.

DELETE /students/1


# ============================================================
# 7. curl
# ============================================================

# curl is a command-line tool used to test APIs.


# -------------------------
# GET Request
# -------------------------

# curl http://127.0.0.1:8000/students


# -------------------------
# POST Request
# -------------------------

# curl -X POST http://127.0.0.1:8000/students


# -------------------------
# POST with JSON
# -------------------------

# curl -X POST http://127.0.0.1:8000/students \
# -H "Content-Type: application/json" \
# -d '{"id":1,"name":"Nitin","age":22,"course":"Python"}'


# Example Response:

# {
#     "message": "Student created successfully"
# }


# ============================================================
# 8. HTTPie
# ============================================================

# HTTPie is another command-line tool for testing APIs.
# It is generally easier to read than curl.


# -------------------------
# GET Request
# -------------------------

# http GET http://127.0.0.1:8000/students


# -------------------------
# POST Request
# -------------------------

# http POST http://127.0.0.1:8000/students \
# id:=1 name=Nitin age:=22 course=Python


# -------------------------
# Get One Student
# -------------------------

# http GET http://127.0.0.1:8000/students/1


# ============================================================
# Quick Summary
# ============================================================

# WebSocket       -> Real-time two-way communication
# WebSocket Route -> URL used for WebSocket connection
# accept()        -> Accept WebSocket connection
# receive_text()  -> Receive message
# send_text()     -> Send message
# Disconnect      -> Handle closed connection
# Broadcast       -> Send message to multiple clients
#
# Rate Limiting   -> Limit number of requests
# HSTS            -> Force HTTPS
# CSP             -> Control allowed resources
# Sanitization    -> Clean/validate user input
# HTTP            -> Request and response communication
# curl            -> Test APIs from terminal
# HTTPie          -> Test APIs using simpler commands