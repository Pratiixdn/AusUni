import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ausuni.settings')
django.setup()

with open('data_export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

from universities.models import State, City, University, Campus, Course, Scholarship

def truncate_strings(row, max_len=50):
    return {k: v[:max_len] if isinstance(v, str) and len(v) > max_len else v for k, v in row.items()}

print('Importing states...')
for row in data['universities_state']:
    State.objects.get_or_create(pk=row['id'], defaults=row)
print(f"  Done: {State.objects.count()} states")

print('Importing cities...')
for row in data['universities_city']:
    state = State.objects.get(pk=row['state_id'])
    row2 = {k: v for k, v in row.items() if k != 'state_id'}
    City.objects.get_or_create(pk=row['id'], defaults={**row2, 'state': state})
print(f"  Done: {City.objects.count()} cities")

print('Importing universities...')
for row in data['universities_university']:
    state = State.objects.get(pk=row['state_id'])
    city = City.objects.get(pk=row['city_id']) if row['city_id'] else None
    row2 = {k: v for k, v in row.items() if k not in ('state_id', 'city_id')}
    row2 = truncate_strings(row2)
    University.objects.get_or_create(pk=row['id'], defaults={**row2, 'state': state, 'city': city})
print(f"  Done: {University.objects.count()} universities")

print('Importing campuses...')
for row in data['universities_campus']:
    uni = University.objects.get(pk=row['university_id'])
    state = State.objects.get(pk=row['state_id'])
    city = City.objects.get(pk=row['city_id']) if row['city_id'] else None
    row2 = {k: v for k, v in row.items() if k not in ('university_id', 'state_id', 'city_id')}
    row2 = truncate_strings(row2)
    Campus.objects.get_or_create(pk=row['id'], defaults={**row2, 'university': uni, 'state': state, 'city': city})
print(f"  Done: {Campus.objects.count()} campuses")

print('Importing courses...')
for row in data['universities_course']:
    uni = University.objects.get(pk=row['university_id'])
    row2 = {k: v for k, v in row.items() if k != 'university_id'}
    row2 = truncate_strings(row2)
    Course.objects.get_or_create(pk=row['id'], defaults={**row2, 'university': uni})
print(f"  Done: {Course.objects.count()} courses")

print('Importing scholarships...')
for row in data['universities_scholarship']:
    uni = University.objects.get(pk=row['university_id'])
    row2 = {k: v for k, v in row.items() if k != 'university_id'}
    row2 = truncate_strings(row2)
    Scholarship.objects.get_or_create(pk=row['id'], defaults={**row2, 'university': uni})
print(f"  Done: {Scholarship.objects.count()} scholarships")

print('All done!')