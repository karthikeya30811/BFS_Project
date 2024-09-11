## Horizon Bank Web Application

Horizon Bank is a web application developed as a skill development project using Django, HTML, and CSS.

## Features

- View account balances and transactions
- Transfer funds between accounts
- Pay bills online
- Apply for loans and credit cards
- Manage account settings

## Setup and Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/karthikeya30811/BFS_Project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd PFSD-BFS
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access Horizon Bank.

## Live Demo

Check out the live demo of Horizon Bank [here](https://venky.pythonanywhere.com/).

## Contributors


