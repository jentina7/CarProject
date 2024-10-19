from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    last_name = models.CharField(max_length=16, null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18),
                                                       MaxValueValidator(80)])
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region="KG")

    def __str__(self):
        return f" {self.name} - {self.last_name}"


class Brand(models.Model):
    brand_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.brand_name


class CarModel(models.Model):
    model_name = models.CharField(max_length=16, unique=True)
    brand = models.ForeignKey(Brand, related_name="car_model", on_delete=CASCADE)


class Car(models.Model):
    car_name = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, related_name="cars", on_delete=CASCADE)
    model = models.ForeignKey(CarModel, related_name="cars", on_delete=CASCADE)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date = models.DateField(auto_now=False)
    mileage = models.PositiveSmallIntegerField(default=0)
    CAR_CHOICES = (
        ("hatchback", "Hatchback"),
        ("micro_compact_car", "Micro compact car"),
        ("station_wagon", "Station wagon"),
        ("landau", "Landau"),
        ("pickup", "Pickup"),
        ("van", "Van"),
        ("minivan", "Minivan"),
        ("sports_car", "Sports car"),
        ("sedan", "Sedan"),
        ("cabriolet", "Cabriolet"),
        ("off-road_car", "Off-road car"),
        ("limousine", "Limousine"),
        ("coupe", "Coupe"),
        ("crossover", "Crossover"),
        ("sedan", "Sedan"),
    )
    car_body = models.CharField(max_length=16, choices=CAR_CHOICES, default="sedan", null=True, blank=True)
    COLOR_CHOICES = (
        ("white", "White"),
        ("black", "Black"),
        ("grey", "Grey"),
        ("blue", "Blue"),
        ("red", "Red"),
        ("pink", "Pink"),
        ("green", "Green"),
        ("yellow", "Yellow"),
        ("orange", "Orange"),
        ("purple", "Purple"),
    )
    color = models.CharField(max_length=16, choices=COLOR_CHOICES, default="white", null=True, blank=True)
    ENGINE_CHOICES = (
        ("petrol", "Petrol"),
        ("diesel", "Diesel"),
        ("gas", "Gas"),
        ("electric_engines", "Electric engines"),
        ("hybrid_installation", "Hybrid installation"),
    )
    engine = models.CharField(max_length=16, choices=ENGINE_CHOICES, default="petrol", null=True, blank=True)
    TRANSMISSION_CHOICES =(
        ("manual", "Manual"),
        ("automatic", "Automatic"),
        ("robotic", "Robotic"),
        ("variable", "Variable"),
    )
    transmission = models.CharField(max_length=16, choices=TRANSMISSION_CHOICES, default="manual", null=True, blank=True)
    CAR_DRIVE_CHOICES = (
        ("rear", "Rear"),
        ("front", "Front"),
        ("four-wheel", "Four-wheel"),
    )
    drive = models.CharField(max_length=16, choices=CAR_DRIVE_CHOICES, default="rear", null=True, blank=True)
    RULE_CHOICES = (
        ("left", "Left"),
        ("right", "Right"),
    )
    rule = models.CharField(max_length=16, choices=RULE_CHOICES , default="left", null=True, blank=True)
    CONDITION_CHOICES = (
        ("new", "New"),
        ("used", "Used"),
    )
    condition = models.CharField(max_length=16, choices=CONDITION_CHOICES , default="new", null=True, blank=True)
    EXCHANGE_CHOICES = (
        ("possible", "Possible"),
        ("impossible", "Impossible"),
    )
    exchange = models.CharField(max_length=16, choices=EXCHANGE_CHOICES , default="possible", null=True, blank=True)
    active = models.BooleanField(default=True)
    REGION_CHOICES =(
        ("bishkek", "Bishkek"),
        ("chui", "Chui"),
        ("yssyk-kol", "Yssyk-kol"),
        ("naryn", "Naryn"),
        ("osh", "Osh"),
        ("talas", "Talas"),
        ("jalal-abad", "Jalal-abad"),
        ("batken", "Batken"),
    )
    region = models.CharField(max_length=16, choices=REGION_CHOICES , default="bishkek", null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.car_name


class CarPhotos(models.Model):
    car = models.ForeignKey(Car, related_name="car", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car_images/")
