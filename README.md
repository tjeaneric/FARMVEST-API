
<!-- Generated with Nexin Django powered API template -->

# FARMVESTNG API

The idea is for an app that will link local farmers to investors so they can get much needed resources to expand their production. The app will work as an intermediary between investors and farmers. The app will sort for farmers, verify them and view their profiles for investors to see. The investors will have a determined rate of return for their investment.

<!-- Default instructions -->

## GET STARTED

> If anything goes wrong, you can ask Jean Eric TUYISHIMIRE for further assistance.

**Database**

This project is pre-configured with postgres. Follow this documentation on how to get started with postgres.

> [Install Postgres on Linux/Windows/Mac](http://postgresguide.com/setup/install.html)

After creating user(s) and database for this project, create a _**DATABASE URL**_, and add it to the **DATABASE_URL** in **settings.ini** file.

The url must be formatted as this example bellow:

> postgres://user:password@host:port/db_name

_For localhost, host is **localhost**, and default port is **5432**_

**Clone the project**
<br><br>
Using SSH

```bash
git clone git@github.com:zuri-training/farmvestng-be-pjt-67.git
```

or using HTTPS

```bash
git clone https://github.com/zuri-training/farmvestng-be-pjt-67.git
```

**Switch to farmvestbe branch**

```bash
git checkout farmvestbe
```

**Create virtualenv**

```bash
virtualenv -p python3 venv
```

**Activate the virtualenv**

```bash
source venv/bin/activate
```

**Install requirements**

```bash
pip install -r requirements.txt
```

**Generate [settings.ini](#) file** (For windows users, create the file manually):

```bash
cat settings.ini.example > settings.ini
```

\*Open **[settings.ini](#)** file, and fill in all necessary **values.\***

**Migrate**

```bash
python manage.py migrate
```

**Runserver**

```bash
python manage.py runserver
```

**Running tests**

```bash
python manage.py test
```

**Working with Celery**

Celery is mainly used to perform background tasks which are usually not meant to be part of the request - response cycle.

> [Celery documentation](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

**Working with Celery Beat**

Celery beat is used to perform periodic tasks automatically.

> [Celery beat documentation](https://django-celery-beat.readthedocs.io/en/latest/)

**Deployment**

Django applications can be deployed in many ways, and on many different servers. Here are some useful documentations for some popular servers.

> [Ningx/gunicorn/postgresql on ubuntu server](https://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/)

> [Heroku](https://devcenter.heroku.com/categories/working-with-django)
