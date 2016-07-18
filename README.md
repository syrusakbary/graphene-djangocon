# Django conference example using Graphene 

This is a integration example of [Graphene](http://graphene-python.org) in Django.

## Structure


The schema (*where all the magic happens*) is in [core/schema.py](./core/schema.py).


## Deploying locally

You can also have your own GraphQL Starwars example running on locally.
Just run the following commands and you'll be all set!

```bash
git clone git@github.com:syrusakbary/graphene-djangocon.git
cd graphene-djangocon

# Install the requirements
pip install -r requirements.txt

# Collect static data
python manage.py collectstatic

# Setup the db and load the fixtures
python manage.py migrate
```

Once you have everything done, just run:

```bash
python manage.py runserver
```

Open your browser and visit [localhost:8080](http://localhost:8080/) et voilá!

**For querying the schema we recomend using [/graphiql](http://localhost:8080/graphiql)**


## Deploying on [Heroku](http://heroku.com)

To get your own GraphQL Starwars example running on Heroku, click the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Fill out the form, and you should be cooking with gas in a few seconds.
