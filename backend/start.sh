# Create user.
cd /home/serveruser/vhosts/socialrest/api

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Make migrations
echo "Make database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.filter(username="admin").exists() or \
    User.objects.create_superuser("admin", "admin@example.com", "admin")
EOF

# Start Gunicorn processes.
echo Starting Gunicorn.
exec gunicorn api.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2
    --capture-output --enable-stdio-inheritance --log-level=debug --access-logfile=- --log-file=-
