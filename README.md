# Chat-Room Project
Chat-Room is a real-time chatting application created using Django Channels, which allows users to create groups, send messages, and access previous chat history when joining a group. Authentication is required for users to send messages, and Django Channels authentication is used for this purpose. The application leverages WebSockets to enable real-time communication between users within the same group.

## Table of Contents
Installation
Features
Technologies Used
Usage
How it Works
Contributing
Installation
## Follow these steps to set up the Chat-Room application:

### Clone the repository from GitHub:

git clone https://github.com/your-username/Chat-Room.git

cd Chat-Room

### Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate    # On Windows, use: venv\Scripts\activate

### Install the required dependencies:

pip install -r requirements.txt

### Perform database migrations:

python manage.py migrate
### Start the development server:
python manage.py runserver

The application should now be accessible at http://localhost:8000/.

## Features
### User Authentication:

Users need to log in or authenticate to access the chat functionality.

Django Channels authentication is used for securing WebSocket connections.

### Group Creation:

Users can create new groups with unique names.

### Real-Time Chatting:

Messages are sent and received in real-time using Django Channels and WebSockets.

### Chat History:

All chat messages in a particular group are saved.

When a new user joins a group, they can see the previous chat history of that group.

## Technologies Used

The Chat-Room application is built using the following technologies:

Django: A high-level Python web framework used for building the backend.

Django Channels: Extends Django to handle WebSockets and other asynchronous protocols.

Channels Authentication: Used for authenticating users for WebSocket connections.

Redis: A message broker required for Django Channels' asynchronous features.

## Usage
Open your web browser and navigate to the application's URL (e.g., http://localhost:8000/).

If you are a new user, you need to sign up to create an account.

Once logged in, you can create a new group with a unique name.

After creating a group, you can invite other users to join by sharing the group name with them.

Users can send and receive messages in real-time within the group.

When a new user joins the group, they can see the chat history and catch up with the previous messages.

## How it Works
The Chat-Room application uses Django Channels to enable real-time communication. When a user logs in, they are authenticated using Django Channels authentication. Once authenticated, the user can create a group and send messages in that group.

Messages sent by users are transmitted over WebSocket connections, allowing for real-time message delivery. The chat history for each group is saved in the database, and when a new user joins a group, the previous chat history is fetched and displayed.

## Contributing
Contributions to the Chat-Room project are welcome! If you find any issues or want to add new features, feel free to open a pull request.

Fork the repository on GitHub.
Create a new branch.
Make your changes and commit them.
Push the branch to your fork.
Open a pull request and describe the changes you've made.