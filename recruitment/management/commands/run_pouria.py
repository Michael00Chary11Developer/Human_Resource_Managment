from typing import Any
from django.core.management.base import BaseCommand, CommandError
import subprocess

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        subprocess.call(['python3','manage.py','runserver','0.0.0.0:8000'])
        