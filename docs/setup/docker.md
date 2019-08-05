# Docker guide

*In these sections, I'll guide you on how to install, setup, run and test the project through Docker containers.*


******************************************************************************
## Prerequisites
******************************************************************************
1. You must have installed [Docker](https://docs.docker.com/install/).
2. You must have installed [Docker Compose](https://docs.docker.com/compose/install/).


******************************************************************************
## Installation
******************************************************************************
1. Open Terminal/Console.
2. Go to the main directory **pypublisher/**(if you are not in).
3. The project contains two docker specific files.
    - **Dockerfile** - defines an application’s image content via one or more build commands that configure that image. Once built, you can run the image in a container.
    - **docker-compose.yml** - describes the services that make our app.
4. **OPTIONAL**: Open the **docker-compose.yml** file.
    - There is a configuration for the database service called **'db'**.
    - ```
        db:
        image: mysql:5.7
        ports:
          - "3308:3306"
        environment:
          - MYSQL_ROOT_PASSWORD=your-root-user-password
      ```
    - This line ```MYSQL_ROOT_PASSWORD=your-root-user-password```, we're defining а password for the MySQL **'root'** user, it will be used to access for the first time freshly installed MySQL into the Docker. You can change the password or use the defined one.
5. Run command ``docker build`` to build the application's image.
6. Run command ``docker-compose up`` to run the application's image in a container.


******************************************************************************
## Setup project settings
******************************************************************************
1. Execute the creation of the database into the **'db'** service container
    - Run command ``docker exec -it pypublisher_db_1 mysql -h db -u root -p -e "CREATE DATABASE yourdatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;".
      ``.
3. Open ``mysql.cnf`` file.
    - ```
        [client]
        database = your-database
        user = your-database-user
        password = your-database-user-password
        host = db
        port = 3306
        default-character-set = utf8mb4
      ```
4. Put your credentials.


******************************************************************************
## Starting the application
******************************************************************************
1. Run command ``docker-compose up`` to run the application's image in a container.
    - The local server will be started ``http://0.0.0.0:80/``.
    ```
    NOTE
        If you are running the application for the first time,
        you are going to see a message in red color like:

        "You have 15 unapplied migration(s).
        Your project may not work properly until you apply the
        migrations for app(s): admin, auth, blog, contenttypes,
        sessions....."
    ```
2. Run command ``docker exec -it pypublisher_web_1 python manage.py migrate`` to apply the migrations.
3. Access the application through browser ``http://localhost:8000/``.
4. You're ready to use the application!


******************************************************************************
## Testing the application
******************************************************************************
2. Execute tests.
    - Run command ``docker exec -it pypublisher_web_1 coverage run manage.py test``.
3. Produce a textual summary report in the Terminal/Console.
    - Run command ``docker exec -it pypublisher_web_1 coverage report``.
    - Covered files can be omitted with the command ``docker exec -it pypublisher_web_1 coverage report --skip-covered``.
3. To erase the collected coverage data, use the erase command ``docker exec -it pypublisher_web_1 coverage erase``.
