
# Re-Dcrypt

Cryptic Hunt

## Run Locally

To deploy this project
1.  Rename `.env.example` to `.env`
2.  Install the dependencies
    `pip install -r requirements.txt`
3.  Run database migrations
    `python manage.py migrate`
4.  Create superuser
    `python manage.py createsuperuser`
5.  Load Admin panel customization data
    `python manage.py loaddata data.json`
6.  Run server
    `python manage.py runserver`
7. Visit Admin Panel at:
    http://127.0.0.1:8000/honeypot/

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_Authorization`

`SENTRY_DSN`


## Tech Stack

**Frontend:** TailwindCSS

**Server:** Python, Django

**Database:** SQLite

## Authors

- [@rachit1601](https://www.github.com/rachit1601)

