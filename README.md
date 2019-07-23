# pypublisher

*Modern Blog application written in Python*

******************************************************************************
## Installation
******************************************************************************
1. Open Terminal/Console.
2. Install Pipenv.
    - More details about Pipenv [here](http://docs.pipenv.org/en/latest/).
    - Run command ``$ pip install --user pipenv``.
3. Create Pipenv environment.
    - Go to the main directory **pypublisher/**.
    - Run command ``pipenv --python 3.7``.
4. Activate the environment.
    - Go to the main directory **pypublisher/**(if you are not in).
    - Run command ``pipenv shell``.
5. Install all dependencies for a project.
    - Go to the main directory **pypublisher/**(if you are not in).
    - Run command ``pipenv install``.
    - You can check installed dependencies by typing ``pipenv graph``.
6. You must have installed [MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/).


******************************************************************************
## Setup project settings
******************************************************************************
1. Open MySQL database.
    - By using a terminal/GUI application like **MySQL Workbench** or another one.
2. Create a database.
    - Run command ``CREATE DATABASE yourdatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;``.
3. Open ``mysql.cnf`` file.
    - ```
        [client]
        database = your-database
        user = your-database-user
        password = your-database-user-password
        default-character-set = utf8mb4
      ```
4. Put your credentials.


******************************************************************************
## Starting the application
******************************************************************************
1. Go to the main directory **pypublisher/**(if you are not in).
2. Activate virtual environment(if you are not).
    - Run command ``pipenv shell``.
3. Run command ``python manage.py runserver``.
    - The local server will be started ``http://127.0.0.1:8000/``.
    ```
    NOTE
        If you are running the application for the first time,
        you are going to see a message in red color like:

        "You have 15 unapplied migration(s).
        Your project may not work properly until you apply the
        migrations for app(s): admin, auth, blog, contenttypes,
        sessions....."
    ```
4. Run command ``python manage.py migrate`` to apply the migrations.
5. You're ready to use the application!


******************************************************************************
## Testing the application
******************************************************************************
1. Go to the main directory **pypublisher/**(if you are not in).
2. Execute tests.
    - Run command ``coverage run manage.py test``.
3. Produce a textual summary report in the Terminal/Console.
    - Run command ``coverage report``.
    - Covered files can be omitted with command ``coverage report --skip-covered``.
4. Produce an HTML report.
    - Run command ``coverage html``.
    - In the main directory **pypublisher/** will be created folder **coverage_html_report/** containing the report.
    - Open file 'index.html' in the browser from the **coverage_html_report/** directory.
5. In the main directory **pypublisher/** there is a file **.coveragerc**, where all configuration settings for the **coverage** tool are lying.
    - The [file](https://coverage.readthedocs.io/en/v4.5.x/config.html) settings can be extended/modified.
6. To erase the collected coverage data, use the erase command ``coverage erase``.
