FROM python:3.9-alpine
COPY stocks_products /app
RUN pip3 install -r /app/requirements.txt
WORKDIR /app
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]