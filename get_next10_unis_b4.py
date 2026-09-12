import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import University, Course

# batch1 (top 10) + batch2 (10) + batch3 (10) - excluding all done ids
done_ids = {14,2,13,38,22,1,35,30,39,23,        # batch 1
            3,4,5,6,7,8,9,10,11,12,             # batch 2
            15,16,17,18,19,20,21,24,25,26}      # batch 3

unis = University.objects.exclude(id__in=done_ids).order_by('id')

print(f"Total universities remaining after 30 done: {unis.count()}")
print()

count = 0
for u in unis:
    courses = Course.objects.filter(university=u)
    print(f"=== {u.name} (id={u.id}) — {courses.count()} courses ===")
    for c in courses:
        print(f"  [{c.pk}] {c.name} — fee:{c.tuition_fee_annual} IELTS:{c.ielts_overall}/{c.ielts_min_band}")
    print()
    count += 1

print(f"Showing all {count} remaining universities.")
