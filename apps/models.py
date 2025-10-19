from django.db.models import CharField, URLField, PositiveIntegerField, DecimalField, TextField, Model


class Food(Model):
    name = CharField(max_length=255)
    image = URLField()
    calories = PositiveIntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)
    brand = CharField(max_length=100)
    category = CharField(max_length=100)
    nutrition_grade = CharField(max_length=1)
    description = TextField()

    def __str__(self):
        return f"{self.name} ({self.brand})"
