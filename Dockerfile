FROM python:3.8

WORKDIR /app

# Shell/Ops Tools
RUN apt-get update && \
    apt-get install -y bash vim nano postgresql-client
RUN pip install --no-cache-dir flake8 "uWSGI<2.1"


# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy our codebase into the container
COPY . .

# Collectstatic, fake these values because our codebase makes them required.
ARG SECRET_KEY=collectstatic
ARG DB_HOST=
ARG DB_NAME=
ARG DB_USER=
ARG DB_PASSWORD=
ARG REDIS_URL=
ARG AWS_S3_REGION_NAME=
ARG AWS_ACCESS_KEY_ID=
ARG AWS_SECRET_ACCESS_KEY=
ARG AWS_STORAGE_BUCKET_NAME=
RUN ./manage.py collectstatic

# Ops Parameters
ENV WORKERS=2
ENV PORT=8000

CMD uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module address_book.wsgi:application
