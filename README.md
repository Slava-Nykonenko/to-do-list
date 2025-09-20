# To-Do list
> A simple application for organizing your tasks.

This application provides an easy way to manage your daily tasks, helping you stay organized and productive.

---

## Installing and Getting Started

Follow these steps to get a local development environment set up and running.

### Prerequisites
* Python 3.x
* pip

### Installation
**1. Clone the repository:**
```shell
  git clone https://github.com/Slava-Nykonenko/to-do-list.git
  cd to-do-list/
````

**2. Set up the Python virtual environment:**

Create and activate the virtual environment to manage project dependencies:

```shell
    # Create the virtual environment
    python -m venv venv
```

```shell
    # On macOS/Linux:
    source venv/bin/activate
```

```shell
    # On Windows:
    venv\Scripts\activate
```    

**3. Install dependencies and configure the database:**

```shell
    # Install required packages
    pip install -r requirements.txt

    # Run database migrations
    python manage.py migrate

    # Create an admin account to log in to the dashboard
    python manage.py createsuperuser
```

**4. Initial Configuration:**

Before running the application, you need to set up your environment variables.

Create a file named .env in the root directory. You can copy the example file:

```shell
    cp .env.example .env
```
Open .env and configure your settings. At a minimum, you'll need to update the SECRET_KEY.
```
# A strong, unique secret key
SECRET_KEY='your_secret_key_here'

# Set to False in production
DEBUG=True

# Database URL (SQLite is the default)
DATABASE_URL='sqlite:///db.sqlite3'

# Optional: Email settings for notifications
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'
```

**5. Run the development server:**

```shell
    python manage.py runserver
```

Once executed, your local server will launch the To-Do list dashboard at http://127.0.0.1:8000/. You can log in using the superuser credentials you created earlier.

# Features

- ✅ Create tasks with the following fields:
  - Content: The main body of the task.
  - Creation date and time: Automatically filled upon creation.
  - Deadline: An optional date and time to complete the task.
  - Tags: Multiple tags can be selected to categorize tasks.


- 🏷️ Create tags for your tasks. 
  - A tag has only one field: name.

# Contributing
We welcome contributions! If you'd like to help improve this project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Submit a pull request with a clear description of your changes.

# Links
Repository: https://github.com/Slava-Nykonenko/to-do-list

Issue Tracker: https://github.com/Slava-Nykonenko/to-do-list/issues

For security vulnerabilities, please contact slava.nykon@gmail.com directly instead of using the issue tracker. We appreciate your effort to improve the security of this project.
