import logging
from django.apps import AppConfig
from django.db.models.signals import post_migrate

logger = logging.getLogger(__name__)


def auto_load_seed_data(sender, **kwargs):
    """Automatically populate database with seed data if fresh database"""
    try:
        from core.models import BusinessProfile
        from products.models import Product
        if not Product.objects.exists():
            from django.core.management import call_command
            logger.info("Empty database detected. Restoring initial seed data from seed_data.json...")
            call_command('loaddata', 'seed_data.json')
            logger.info("Seed data loaded successfully!")
    except Exception as e:
        logger.warning("Auto seed data load skipped or encountered error: %s", e)


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(auto_load_seed_data, sender=self)
