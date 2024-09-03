# TCP Chatroom

## Overview

This is a real-time chat application developed in Python. It allows multiple clients to connect to a server and send messages within a chatroom environment.

## Requirements

- Python 3.x
- Socket library (standard in Python)
- Threading library (standard in Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/tcp-chatroom.git
    cd tcp-chatroom
    ```

2. Ensure you have Python 3 installed on your system.

## Usage

### Running the Server

1. Navigate to the project directory.
2. Run the server script:
    ```sh
    python server.py
    ```
3. The server will start and listen for incoming connections.

### Running the Client

1. Navigate to the project directory.
2. Run the client script:
    ```sh
    python client.py
    ```
3. Enter your nickname when prompted.

### Admin Commands

- **/kick `<username>`**: Kicks the specified user from the chatroom. Only users with admin privileges can use this command.

### Example Session

1. **Start the Server**:
    ```sh
    python server.py
    ```
    Output:
    ```
    Server is listening on 127.0.0.1:55555
    ```

2. **Start the Client**:
    ```sh
    python client.py
    ```
    Input:
    ```
    Choose your nickname: admin1
    ```

3. **Client Interactions**:
    ```
    admin1: Hello everyone!
    ```

4. **Admin Kicking a User**:
    ```
    /kick user2
    ```

## Code Structure

- **server.py**: Contains the server-side logic to handle client connections, message broadcasting, and admin commands.
- **client.py**: Contains the client-side logic for connecting to the server, sending/receiving messages, and handling user inputs.
