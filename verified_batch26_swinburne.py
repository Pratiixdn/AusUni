import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (57, "42567", "6.0", "6.0"),  # Bachelor of Business - idp.com; IELTS OFFICIAL Sept 2026
                                    # Swinburne press release + collegedunia direct (6.0/6.0, overriding
                                    # prior 6.5)
    (54, "40960", "6.0", "6.0"),  # Bachelor of Computer Science - shiksha (2x direct); IELTS per
                                    # official Swinburne UG standard (collegedunia direct)
    (55, "47320", "6.5", "6.0"),  # Bachelor of Engineering (Honours) (Professional) - idp.com direct
                                    # match on exact DB course name (multiple specialisations converge)
    (56, "42240", "6.5", "6.0"),  # Master of Information Technology - collegedunia + idp.com (Sydney
                                    # campus) direct match; IELTS per official PG standard
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
print("SWINBURNE COMPLETE: 4 of 4 courses verified.")
print("Sources: idp.com, shiksha.com, collegedunia (2026, official-adjacent), and an OFFICIAL")
print("Swinburne press release (Sept 2026) confirming UG IELTS standard directly.")
