from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os

class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    def ready(self):
        from django.contrib.auth import get_user_model

        def create_superuser(sender, **kwargs):
            if os.environ.get("CREATE_SUPERUSER") == "1":
                User = get_user_model()
                username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
                email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@gmail.com")
                password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(username, email, password)

        post_migrate.connect(create_superuser, sender=self)