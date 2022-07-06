<p align="center">
<img width="400" src="https://static.redcrypt.ml/logo_banner.svg"><br>
<h1 align="center"> Re-Dcrypt</h1></p>
<p align="center">Cryptic Hunt</p>



## Run Locally

To deploy this project
1.  Rename `.env.example` to `.env`
2.  Install the dependencies
    `pip install -r requirements.txt`
3.  Run database migrations
    `python manage.py migrate`
4.  Create superuser
    `python manage.py createsuperuser`
5.  Collect Static
    `python manage.py collectstatic`
6.  Load Admin panel customization data
    `python manage.py loaddata data.json`
7.  Run server
    `python manage.py runserver`
8. Visit Admin Panel at:
    http://127.0.0.1:8000/honeypot/

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_Authorization`

`SENTRY_DSN`

`EMAIL_HOST_USER`

`EMAIL_HOST_PASSWORD`

`DISCORD_LOGGING_WEBHOOK`

`HCAPTCHA_SITEKEY`

`HCAPTCHA_SECRET`

`MAINTENANCE_MODE`

## Tech Stack

**Frontend:** TailwindCSS

**Server:** Python, Django

**Database:** SQLite

## Authors

- [@rachit1601](https://www.github.com/rachit1601)

