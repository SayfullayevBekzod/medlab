from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model,
    IntegerField,
    CharField,
    TextChoices,
    TextField,
    ManyToManyField,
    ImageField,
    ForeignKey,
    CASCADE,
    DateField,
)


# class User(AbstractUser):
#     pass


class Gender(TextChoices):
    MALE = "Male", "male"
    FEMALE = "Female", "female"


class Count(Model):
    doctor = IntegerField(default=0)
    departments = IntegerField(default=0)
    labs = IntegerField(default=0)
    awards = IntegerField(default=0)

    def __str__(self):
        return str(self.doctor)


class Disease(Model):
    title = CharField(max_length=128)

    def __str__(self):
        return self.title


class Patient(Model):
    fullname = CharField(max_length=128)
    age = IntegerField()
    gender = CharField(max_length=6, choices=Gender.choices, null=True)
    disease_id = ForeignKey(Disease, CASCADE, related_name="patients")

    def __str__(self):
        return self.fullname


class Icon(Model):
    name = CharField(max_length=128)
    link = CharField(max_length=128)

    def __str__(self):
        return self.name


class Doctor(Model):
    fullname = CharField(max_length=128)
    foto = ImageField(upload_to="media/", default="media/default.jpg")
    job = CharField(max_length=128)
    body = TextField()
    # icon = ManyToManyField(Icon, related_name="doctor", null=True)
    link = CharField(max_length=128)

    def __str__(self):
        return self.fullname


class PatientDoctor(Model):
    name = CharField(max_length=128)
    age = IntegerField()
    sickness = TextField(null=True)
    doctor = ForeignKey(Doctor, CASCADE, related_name="doctors")
    appointment_date = DateField()

    def __str__(self):
        return self.name


class Department(Model):
    title = CharField(max_length=128)
    description = TextField()
    body = TextField()
    image = ImageField(upload_to="media/", default="media/default.jpg")

    def __str__(self):
        return self.title
