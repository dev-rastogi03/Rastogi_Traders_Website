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

username = "admin"
email = "admin@rastogitraders.in"
password = "adminpassword123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✓ Superuser '{username}' created successfully with password '{password}'")
else:
    print(f"ℹ️ Superuser '{username}' already exists.")
