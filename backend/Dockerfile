FROM ubuntu:18.04

# Get user id and group id from arguments.
ARG UID
ARG GID

# Create user.
RUN groupadd -r serveruser -g $GID && useradd -ms /bin/bash serveruser -u $UID -g $GID

# Install some packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3-minimal python3-setuptools python3-pip netcat && \
  rm -f /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python && \
  rm -f /usr/bin/pip && ln -s /usr/bin/pip3 /usr/bin/pip && \
  pip install django djangorestframework django-filter mysql-connector-python gunicorn

# Copy script.
COPY start.sh /home/serveruser/start.sh
RUN chmod +x /home/serveruser/start.sh

# Copy keys and create main path.
RUN chown -R serveruser:serveruser /home/serveruser

WORKDIR /home/serveruser/vhosts/socialrest

EXPOSE 8000

USER serveruser
CMD /home/serveruser/start.sh
