A sample django based application which handles application submition from users. Admin interface has setup too where admin can view applications and can accept and reject on the same.

Python/Django versions: Python 3+ and Django 1.9

Backend connected: Mysql

Application has been developed using Django framework which provides both user and admin interface for applications. Requirements txt has been used to gather all required packages over here and can install once using pip. Modiying the requirements file can always effect in rerunning the pip requirements installation.

Django effects:

1. Forms
2. Models
3. Views
4. Routes
5. Templating
6. Admin

Setup:

1. Clone the repo
2. Setup virtual environment(ex: virtualenv -p python3 env)
3. Activate it(source env/bin/activate)
4. pip install -r requirements.txt (pip with latest version based on python3)
5. python3 manage.py migrate
5. python3 manage.py createsuperuser (to create admin user credentials in local)
6. python3 manage.py runserver

Hit the browser with,

1. http://localhost:8000/
2. http://localhost:8000/admin
