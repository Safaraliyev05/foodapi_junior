FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate && python manage.py import_products && python manage.py runserver 0.0.0.0:8000"]
