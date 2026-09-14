import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course
from django.db import connection

# Try multiple ways to count, in case something is filtering silently
print("Method 1: Course.objects.all().count()")
print(Course.objects.all().count())
print()

print("Method 2: Course.objects.count()")
print(Course.objects.count())
print()

print("Method 3: raw SQL count on the actual table")
with connection.cursor() as cursor:
    cursor.execute(f"SELECT COUNT(*) FROM {Course._meta.db_table}")
    print(cursor.fetchone()[0])
print()

print(f"Table name being queried: {Course._meta.db_table}")
print(f"App label: {Course._meta.app_label}")
print(f"Database alias in use: {Course.objects.db}")
print()

# Check if there's a default manager filtering something out (soft-delete, is_active, etc)
print("Model fields:")
for f in Course._meta.get_fields():
    print(f"  {f.name}")
