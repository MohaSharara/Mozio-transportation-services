from django.db import models
from django.contrib.gis.db import models

LANGUAGE = [
    ('ENG', 'English'),
    ('ZH', 'Mandarin/Chinese'),
    ('HIN', 'Hindi'),
    ('SPA', 'Spanish'),
    ('FRA', 'French'),
    ('AR', 'Arabic'),
    ('BEN', 'Bengali'),
    ('RU', 'Russian'),
    ('POR', 'Portuguese'),
    ('IND', 'Indonesian'),
    ('DEU', 'German'),
    ('JPN', 'Japanese'),
]

CURRENCY = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('JPY', 'Japanese Yen'),
    ('GBP', 'British Pound Sterling'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CHF', 'Swiss Franc'),
    ('CNH', 'Chinese Renminbi'),
    ('HKD', 'Hong Kong dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('MXN', 'Mexican Peso'),
    ('INR', 'Indian Rupee'),
    ('AED', 'UAE Dirham'),
    ('EGP', 'Egyptian Pound'),
    ('ARS', 'Argentine Peso'),
    ('BRL', 'Brazilian Real'),
]


class Provider(models.Model):
    name = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14, unique=True)
    language = models.CharField(max_length=3, choices=LANGUAGE)
    currency = models.CharField(max_length=3, choices=CURRENCY)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="service_areas"
    )
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    information = models.PolygonField()

    class Meta:
        unique_together = (("provider", "name", ),
                           ("provider", "information", ))

    def __str__(self):
        return self.name
