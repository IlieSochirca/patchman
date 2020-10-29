# Blog Project Implementation with Django 3.0, Python 3.8 and Docker used for Containerization
## This project was implement as a small assessment
### Steps I followed to create it
- Create a working directory for this project
- Start a django project named `blog` with 2 more apps there: one for `post` and another for `reply`. I think 2 separate apps are needed for the beginning to separate 
from start the scope of each app and keep things related to reply feature or post feature in separate contexts.
- I have Docker installed on my personal computer and I use a `Dockerfile` for any project I am doing. 
This way I am sure there is a separate environment for each project and I can install any dependecies I need which will not stay on my computer and by simply deleting the Docker image and container I am removing everything related to it.
- Dockerfile was created with all the steps necessary to build a python project. 
- There is also a `requirements.txt` file that lists all project dependencies. In our case it's `django` and `gunicorn`.
- I used gunicorn as I think we need a HTTP server in front of django app that will serve the client. We can use for growing app performance and concurrent requests for future uses, like increasing the number of process that run the same app. 
- I used to create a `docker-compose.yml` file that is an orchestration tool used to build and run applications in a quicker way. It has 1 service at the moment there, 
but in the future we could add there another service for a separate DB like Postgres or Redis, another one for mailing service and so on.
- Once I have this setup, I ran: `docker-compose up --build` that is building if there is no previous build for this Docker image and after that starting the services. 
In our case, our Django app.
- Regarding Django application, I began with setting up our `settings` file where I add 2 more apps(post and reply) inside `INSTALLED_APPS`, otherwise they are not tracked.
- For each of this apps, I created a `model` that is actually the Database represantation of a object.
- In order to see the applications models in the Django Admin page I had to register them inside `admin.py` files for each app.
- A next step would be to create a superuser that will be used to access the Django Admin Panel by following the steps while docker container of our app is running:
1. docker ps and taker the <container_id> from there
2. docker exec -it <container_id> python manage.py createsuperuser and follow the steps to create one.
- I created `templates` directory that contains all `.html` templates used to render information to the user. 
There is a `base.html` template that is inherited but each other file, as it contains the common elements from out app pages.
- I also modified `settings.py` file to show our project where do we place the Templates.
- I continued to create the views for each of our page and a forms where was needed.
- For each present we have an url mapped to a view inside `urls.py`. This way, when an url is hit, the application is checking which view to call and proceeds with it.
