# Django REST Framework example

This repo contains the starting point to create a REST API based
on Django REST Framework.

# Check the full explanation video (GR)
[![REST API σε Python με Django #65, live](https://img.youtube.com/vi/CtoXgtlTpTI/0.jpg)](https://www.youtube.com/watch?v=CtoXgtlTpTI)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/) installed

# Run

Run in root folder,
~~~
cp .env.example .env
docker-compose build && docker-compose up -d
~~~~

Add vhost to your /etc/hosts file,
~~~~
127.0.0.1 www.socialrest.local
~~~~

Check http://www.socialrest.local/admin on your browser,
~~~~
login as admin/admin
~~~~

Check http://www.socialrest.local/api/blogs on postman,
~~~~
authenticate as admin/admin
~~~~

To stop it, go to root folder and type,
~~~~
docker-compose down
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)
