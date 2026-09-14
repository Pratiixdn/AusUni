import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import University, Course

# Every pk touched across the whole project (batches 1-45)
touched_pks = {
    # top 10 (48)
    47,46,50,49,48,9,8,7,11,10,40,39,41,45,43,42,44,121,120,122,123,76,75,77,
    3,2,1,6,5,4,110,111,114,113,112,98,99,125,124,127,126,131,130,128,129,79,78,80,
    # batch 2 (27)
    15,13,12,14,16,17,18,19,21,20,22,24,23,26,25,30,28,27,29,32,31,33,34,35,37,36,38,
    # batch 3 (34)
    51,52,53,57,54,55,56,60,59,58,62,61,64,63,66,65,69,67,68,72,70,71,73,74,84,81,82,83,86,85,87,89,90,88,
    # batch 4 (35)
    91,93,92,94,95,96,97,100,101,102,103,104,106,105,107,109,108,115,117,116,118,119,132,133,135,137,134,136,
}
print(f"Total touched pks tracked: {len(touched_pks)}")
print()

all_courses = Course.objects.all()
print(f"TOTAL COURSES IN DATABASE: {all_courses.count()}")
print()

untouched = []
for c in all_courses:
    if c.pk not in touched_pks:
        untouched.append(c)

print(f"UNTOUCHED COURSES: {len(untouched)}")
print()

if untouched:
    # group by university
    from collections import defaultdict
    by_uni = defaultdict(list)
    for c in untouched:
        by_uni[c.university.name].append(c)

    for uni_name in sorted(by_uni.keys()):
        courses = by_uni[uni_name]
        print(f"=== {uni_name} — {len(courses)} untouched ===")
        for c in courses:
            print(f"  [{c.pk}] {c.name} — fee:{c.tuition_fee_annual} IELTS:{c.ielts_overall}/{c.ielts_min_band}")
        print()

print(f"Total universities in DB: {University.objects.count()}")
print(f"Total courses in DB: {all_courses.count()}")
print(f"Touched: {all_courses.count() - len(untouched)}")
print(f"Remaining: {len(untouched)}")
