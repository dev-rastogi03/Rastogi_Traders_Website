"""
Helper script to create a default superuser for Rastogi Traders Django Admin.
Username: admin
Password: adminpassword123
"""

import os
import sys
import django

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@rastogitraders.in")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "adminpassword123")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✓ Superuser '{username}' created successfully.")
else:
    print(f"ℹ️ Superuser '{username}' already exists.")

