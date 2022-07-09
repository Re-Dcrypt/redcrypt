FROM python:3
WORKDIR /app
COPY . .
ARG PASS
ENV PASS=$PASS
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic
EXPOSE 8000
CMD ["gunicorn","triviaquiz.wsgi","--bind","0.0.0.0:8000"]
