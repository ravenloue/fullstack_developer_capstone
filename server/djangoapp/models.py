from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    ENGINE_TYPES = [
        ('GAS', 'Gas'),
        ('DIESEL', 'Diesel'),
        ('ELECTRIC', 'Electric'),
        ('HYBRID', 'Hybrid')
    ]

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('MICRO', 'Micro'),
        ('HATCHBACK', 'Hatchback'),
        ('CROSSOVER', 'Crossover'),
        ('COUPE', 'Coupe'),
        ('COUPE SUV', 'Coupe SUV'),
        ('OFF-ROADER', 'Off-Roader'),
        ('PICK-UP', 'Pick-Up'),
        ('MPV', 'MPV'),
        ('VAN', 'Van'),
        ('CAMPER', 'Camper'),
        ('MINIVAN', 'Minivan'),
        ('SPORT', 'Sport'),
        ('CABRIOLET', 'Cabriolet'),
        ('ROADSTER', 'Roadster'),
        ('HYPER', 'Hyper'),
        ('MUSCLE', 'Muscle'),
        ('LIMOUSINE', 'Limousine'),
        ('OPEN WHEEL', 'Open Wheel')
    ]
    
    TRANSMISSION_TYPES = [
        ('AUTO', 'Automatic'),
        ('MANUAL', 'Manual')
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2025, validators=[MaxValueValidator(2025), MinValueValidator(2015)])
    engine_type = models.CharField(max_length=10, choices=ENGINE_TYPES, default='GAS')
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_TYPES, default='AUTO')
    color = models.CharField(max_length=20, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name