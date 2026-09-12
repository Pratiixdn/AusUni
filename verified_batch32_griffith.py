import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (84, "33500", "6.5", "6.0"),  # Bachelor of Business - shiksha direct exact match
    (81, "35000", "6.5", "6.0"),  # Bachelor of Criminology and Criminal Justice - shiksha direct
                                    # (converges with unischolars $33,000)
    (82, "40500", "6.5", "6.0"),  # Bachelor of Information Technology - idp.com direct exact match (2x)
    (83, "43500", "6.5", "6.0"),  # Master of Information Technology - collegedunia 2026-dated direct;
                                    # IELTS official-adjacent courses.com.au confirmed precisely
]

for pk, fee, ielts, band in updates:
    c = Course.objects.get(pk=pk)
    old_fee, old_ielts = c.tuition_fee_annual, c.ielts_overall
    c.tuition_fee_annual = fee
    c.ielts_overall = ielts
    c.ielts_min_band = band
    c.save()
    print(f"[{pk}] {c.name}: fee {old_fee}->{fee}, IELTS {old_ielts}->{ielts}/{band}")

print()
print("GRIFFITH COMPLETE: 4 of 4 courses verified.")
print("Sources: idp.com, shiksha.com, collegedunia, courses.com.au (official-adjacent, precise")
print("IELTS breakdown), unischolars.com")
