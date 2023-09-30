# Smart-Teachr-project

This is a Python application that utilizes several modules and tools to achieve its functionality. Below, you'll find a brief overview of each module and tool used in this project.

## Modules Used

### FastAPI
- Description: FastAPI is a modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints.
- GitHub Repository: [FastAPI on GitHub](https://github.com/tiangolo/fastapi)
- Installation: Use the following command to install FastAPI:
  ```bash
  pip install fastapi

### Starlette
- Description: Starlette is a lightweight ASGI framework/toolkit for building high-performance asyncio services.
- GitHub Repository: [Starlette on GitHub](https://github.com/encode/starlette)
- Installation: Use the following command to install Starlette:
  ```bash
  pip install starlette

### NiceGUI
- Description: NiceGUI is a Python library for creating interactive web-based user interfaces.
- GitHub Repository: [NiceGUI on GitHub](https://github.com/nicegui/nicegui)
- Installation: Use the following command to install NiceGUI:
  ```bash
  pip install nicegui

### aioMySQL
- Description: aioMySQL is an asynchronous MySQL client library for Python.
- GitHub Repository: [aioMySQL on GitHub](https://github.com/aio-libs/aiomysql)
- Installation: Use the following command to install aioMySQL:
  ```bash
  pip install aiomysql

### MySQL Connector
- Description: MySQL Connector/Python is a MySQL driver for Python.
- GitHub Repository: [MySQL Connector/Python on GitHub](https://github.com/mysql/mysql-connector-python)
- Installation: Use the following command to install MySQL Connector:
  ```bash
  pip install mysql-connector-python

## Tools Used

### PyCharm Professional
- Description: PyCharm Professional is an integrated development environment (IDE) for Python development with advanced features and support for web development, databases, and more.
- Website: [PyCharm Professional](https://www.jetbrains.com/pycharm/)

### MySQL
- Description: MySQL is an open-source relational database management system used for storing and retrieving data.
- Website: [MySQL](https://www.mysql.com/)

## Database Setup

To get started with the Smart-Teachr-project, follow these steps to import the necessary SQL file into your MySQL database.

1. **Download the SQL file for our project database**: [project.sql](https://github.com/Den-ctrl/Smart-Teachr-project/blob/main/project.sql).

2. **Import SQL File**:

   - Open a terminal and log in to MySQL:

     ```bash
     mysql -u username -p
     ```

     Replace `username` with your MySQL username.

   - Create a new database (if not already created):

     ```sql
     CREATE DATABASE project;
     ```

   - Use the newly created database:

     ```sql
     USE project;
     ```

   - Import the SQL file:

     ```bash
     mysql -u username -p project < path/to/project.sql
     ```

## Running the Application

To run the Smart-Teachr-project, follow these steps:

1. **Navigate to the Project Directory**:

   Open a command prompt (CMD) or terminal and use the `cd` command to navigate to the directory where you have cloned or downloaded the project. For example:

   ```bash
   cd path/to/smart-teachr-project

2. **Activate the Virtual Environment**:

   If you're using a virtual environment (venv), activate it by running the appropriate activation command. For example, on Windows:

   ```bash
   cd path/to/smart-teachr-project
   ```
   
   On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Run the main.py Script**:

   Once the virtual environment is activated, you can run the main.py script. Use the following command:

   ```bash
   python main.py
   ```

4. **Access the Application**:

   After running the main.py script, you should be able to access the application through your web browser by navigating to the appropriate URL (e.g., http://localhost:8000).

5. **Login Credentials**:

   When prompted for login credentials, use the following default values:

    - Username: user1
    - Password: pass1

    You can change these credentials as needed for your application.

   

