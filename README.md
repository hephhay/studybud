<p align="center">
  <p align="center">
    <a href="https://studybud-social.herokuapp.com" target="_blank">
      <img src="https://studybud-social.herokuapp.com/static/images/logo.svg" alt="JustDjango" height="72">
    </a>
  </p>
</p>

# Django Social Media App

This is very simple social media app with built with Django
You can check it out [here](https://studybud-social.herokuapp.com)

## Screeshots

![ScreenShot](https://i.postimg.cc/TL1RyDQt/1study.png)
![ScreenShot](https://i.postimg.cc/v13YHz71/2study.png)
![ScreenShot](https://i.postimg.cc/wyr9DjGg/3study.png)

![ScreenShot](https://i.postimg.cc/LJk4GRn3/4study.png)
![ScreenShot](https://i.postimg.cc/cKs1Sj3y/5study.png)
![ScreenShot](https://i.postimg.cc/MnJKsXKG/6study.png)

## Project Summary

This App lets you:

	
* Create an Account
* Have an Editable Profile including Avatar
* View rooms and conversions without login
* Create, edit and delete room, topics and conversations
* recover password via a personalized mail
* search for topics, rooms and conversation
* see who is online, offline and last seen
* see recent activies in the app
* see time since events happened

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/activate
```

Then install the project dependencies with

```
pip install -r requirements.txt

```

in your root folder create a `.env` file and fill it up with the following

```
SECRET_KEY=<django secret  key>
DB_NAME=<database name>
DB_USER=<database user>
DB_PASSWORD=<database password>
DB_HOST=<database host>
DB_PORT=<database port>
EMAIL_HOST=<host of smtp provider>
EMAIL_PORT=<smtp port>
EMAIL_USER=<smtp username>
EMAIL_PASSWORD=<smtp password>

```
By default postgres database is used but this can be changed in the `settings.py` by changing `'ENGINE': 'django.db.backends.postgresql_psycopg2'` to any appropiate database

Now you can run the project with this command

```
python manage.py runserver

```

## Support

you can always contact me at [faradaydanfard@gmail.com](mailto:faradaydanfard@gmail.com)

## Conclusion

Thanks enjoy