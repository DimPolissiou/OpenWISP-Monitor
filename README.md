##### Installation
1. Requirements: any supported version of python and [pip] (optionally [pipenv]).
2. Clone the repo.
3. *(OPTIONAL)* If not using pipenv, set up a virtual environment using [virtualenv].
4. `pip install -r requirements.txt` OR `pipenv install -r requirements.txt`.
5. Create a settings.py file inside the openwisp_monitor directory.
6. Run migrations with `python manage.py migrate`.
7. Collect static files with `python manage.py collectstatic`.
8. Run the development server with `python manage.py runserver 0.0.0.0:8080`.

##### Settings

You can use `example_settings.py` as a template to create your own settings file.
Here are some settings you will probably need to change:

- SECRET_KEY : You can use `generate_secret_key.py` to generate a secret key.
- ALLOWED_HOSTS: See the relevant paragraph on the django docs [https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts].
- DATABASES: See the relevant paragraph on the django docs [https://docs.djangoproject.com/en/1.10/ref/settings/#databases].
- TIME_ZONE: If using collectd, make sure there is no timezone mismatch.
- NETJSONCONFIG_SHARED_SECRET: Choose a password arbitrarily. You will need to use this shared secret when attempting to register a new device with the server.
- CAS_SERVER_URL: A URL point to the CAS server you will be using.
- AFFILIATION_FIELD: The name of an attribute returned by the CAS server. This field will be used to determine wether two users belong to the same affiliation.
- COLLECTD_RRD_DIR: A path to the directory used by collectd to store RRD file. Ignore this if you are not using collectd.

[pip]:[https://pip.pypa.io/en/stable/]
[pipenv]:[https://github.com/pypa/pipenv]
[virtualenv]:[https://virtualenv.pypa.io/en/stable/]