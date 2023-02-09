# Pipeline API

## Project Setup

1. Navigate to where you want to clone the repo in your terminal
1. Clone Repo on to Local Machine

    ```shell
    # HTTPS
    git clone https://github.com/Repped-In-Tech/pipeline-be.git
    ```

    ```shell
    # SSH
    git clone git@github.com:Repped-In-Tech/pipeline-be.git
    ```

1. Open Cloned Project

    ```shell
    cd pipeline-be; code .;
    ```

1. Create Virtual Envirunment

    ```shell
    pipenv shell
    ```

1. Select interpreter within vscode
    - Open your Command Palette
    - Search for "Python: Select Interpreter"
    - Find the interpreter that includes `pipeline-be-` in the name. If you can't see it off hand, click on the refresh button that's on top of the search bar to the right.

1. Install Dependencies

    ```shell
    pipenv install
    ```

1. Run Migrations

    ```shell
    python manage.py migrate
    ```

1. Start Project

    ```shell
    python manage.py runserver
    ```

1. View the API

    ```shell
    Performing system checks...

    System check identified no issues (0 silenced).
    February 09, 2023 - 15:41:00
    Django version 4.1.6, using settings 'pipeline.settings'
    Starting development server at http://127.0.0.1:8000/ # <= API URL
    Quit the server with CONTROL-C.
    ```

## Documentation

To view the API Documentation, start the server and go to "http://127.0.0.1:8000/docs/#"
