import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
import cloudinary
import cloudinary.uploader


class Command(BaseCommand):
    help = "Uploads all existing local media files to Cloudinary for permanent hosting"

    def handle(self, *args, **options):
        cloudinary_url = getattr(settings, 'CLOUDINARY_URL', None) or os.getenv('CLOUDINARY_URL')
        if not cloudinary_url:
            self.stderr.write(self.style.ERROR("CLOUDINARY_URL is not configured in settings or environment."))
            return

        media_root = Path(settings.MEDIA_ROOT)
        if not media_root.exists():
            self.stdout.write(self.style.WARNING(f"Media root '{media_root}' does not exist."))
            return

        self.stdout.write(self.style.NOTICE(f"Scanning media files in: {media_root} ..."))

        valid_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg', '.pdf'}
        files_to_upload = []

        for root, _, files in os.walk(media_root):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in valid_extensions:
                    rel_path = file_path.relative_to(media_root).as_posix()
                    files_to_upload.append((file_path, rel_path))

        if not files_to_upload:
            self.stdout.write(self.style.WARNING("No media files found to upload."))
            return

        self.stdout.write(f"Found {len(files_to_upload)} files. Starting Cloudinary upload...")

        success_count = 0
        error_count = 0

        for file_path, rel_path in files_to_upload:
            # Cloudinary public_id without extension
            name_without_ext = str(Path(rel_path).with_suffix(''))
            try:
                self.stdout.write(f"Uploading: {rel_path} -> Cloudinary public_id: {name_without_ext} ...")
                res = cloudinary.uploader.upload(
                    str(file_path),
                    public_id=name_without_ext,
                    overwrite=True,
                    resource_type="auto",
                    invalidate=True,
                )
                success_count += 1
                self.stdout.write(self.style.SUCCESS(f"  ✓ Uploaded successfully: {res.get('secure_url')}"))
            except Exception as e:
                error_count += 1
                self.stderr.write(self.style.ERROR(f"  ✗ Failed to upload {rel_path}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"\nCompleted: {success_count} succeeded, {error_count} failed."))
