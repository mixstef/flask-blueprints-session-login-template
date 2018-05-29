# Flask with Blueprints + session login template
A plain old session login template, using mongodb as user credentials' storage.

## Initialization
Follow these steps to initialize your working environment.

### Fork and clone repository

a) Fork this repository. This will allow you to work on your own repository. **No pull request is needed**.

b) Log into the development machine. Clone your forked repository there:

	mkdir my-app
	cd my-app
	git clone <your-github-path> .

**NOTE:** `<your-github-path>` must be replaced by the path to your own repository!


### Prepare the virtual environment (venv)

Being at the project's root folder, enter the following commands at terminal:

	virtualenv venv -p python3
	. venv/bin/activate
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt 

### Create folder with env vars
In project's top folder create a new subfolder `secrets`. This must not be put under version control! In this new folder create a file `env_vars` with the following content:

	export MY_APP_PORT=<your-assigned-port>
	export MY_APP_PREFIX=/<your-assigned-prefix>
	export MY_APP_MONGODB_NAME=<your-db-name>
	export MY_APP_SECRET_KEY=<your-secret-phrase>	
	
	export FLASK_APP=myapp

**NOTE:** `<your-assigned-port>` and `<your-assigned-prefix>` must be replaced by the actual data provided to you!. Moreover, `<your-db-name>` should begin with `<your-assigned-prefix>`.

## Running the test server
Before running the server you should activate venv (if not already active):

	. venv/bin/activate

Enter the following commands to start the testing flask server (with reloading):

	. secrets/env_vars
	flask run --reload --host=0.0.0.0 --port $MY_APP_PORT


