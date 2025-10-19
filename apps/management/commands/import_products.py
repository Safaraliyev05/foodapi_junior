import json
from django.core.management.base import BaseCommand
from apps.models import Food  # adjust if your model path is different


class Command(BaseCommand):
    help = "Import product data from Products.json into the database"

    def handle(self, *args, **options):
        try:
            with open("Products.json", "r", encoding="utf-8") as f:
                products = json.load(f)
        except FileNotFoundError:
            self.stderr.write("❌ Products.json not found.")
            return

        created_count = 0
        for p in products:
            obj, created = Food.objects.get_or_create(
                name=p["name"],
                defaults={
                    "image": p["image"],
                    "calories": p["calories"],
                    "price": p["price"],
                    "brand": p["brand"],
                    "category": p["category"],
                    "nutrition_grade": p["nutrition_grade"],
                    "description": p["description"],
                },
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {created_count} new products"))
