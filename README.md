### Address App

This simple django app serves as an example docker environment for a blog post.

It has address book fields you can fill in in the admin panel.


## Set up

Run the following commands to build the project.

```
git clone https://github.com/skyride/python-docker-compose
cd python-docker-compose
docker-compose pull
docker-compose build
cp example.env .env
```

Now populate `.env` with secrets, then run the following. You will be prompted
to enter details for your new superuser account.

```
docker-compose run --rm app ./manage.py migrate
docker-compose run --rm app ./manage.py createsuperuser
docker-compose up
```

The application will now be up and running at [http://localhost:8000/admin](http://localhost:8000/admin).
