# Generated by Django 3.2 on 2021-06-28 16:27

from django.conf import settings
from django.db import migrations

from model_bakery import baker

NAMES = {
    "William",
    "Noah",
    "Emma",
    "Amelia",
    "Mia",
    "Lucas",
    "Alexander",
    "Henry",
    "James",
    "Sophia"
}

def create_demo_users(apps, schema_editor):
    if settings.ENVIRONMENT is settings.TESTING:
        return

    Company = apps.get_model("core", "Company")
    User = apps.get_model("users", "User")
    company = Company.objects.get(code="adslab")

    # Delete user if exists
    User.objects.all().delete()

    for name in NAMES:
        baker.make(
            "users.User",
            name=f"{name} Doe",
            company_id=company.id,
        )

def reverse_create_demo_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_remove_user_uuid_null"),
    ]

    operations = [migrations.RunPython(create_demo_users, reverse_code=reverse_create_demo_users)]
