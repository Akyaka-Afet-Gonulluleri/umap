FROM python:3.8.13-bullseye

# Copy in your requirements file
RUN apt-get update && apt-get install -y \
    gdal-bin \
 && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
WORKDIR /app
ADD . /app


ENV UMAP_SETTINGS=/app/umap/settings/docker.py
ENV STATIC_ROOT=/app/static
ENV MEDIA_ROOT=/app/data
RUN umap collectstatic
RUN umap compress

# uWSGI will listen on this port
EXPOSE 8000

# Start uWSGI
ENTRYPOINT ["./docker-entrypoint.sh"]