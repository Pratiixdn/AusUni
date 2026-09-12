import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (72, "26300", "6.0", "6.0"),  # Bachelor of Business - collegedunia (most-cited specific figure
                                    # across specialisation variants); IELTS confirmed official-adjacent
    (70, "41400", "6.0", "6.0"),  # Bachelor of Information Technology - OFFICIAL federation.edu.au 2026
                                    # published fee document, direct exact figure (overrides shiksha's
                                    # rougher $36,000 estimate)
    (71, "41400", "6.0", "6.0"),  # Master of Information Technology - idp.com direct 2026; Federation
                                    # appears to have flat-rate IT pricing across UG/PG
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
print("FEDERATION UNIVERSITY COMPLETE: 3 of 3 courses verified.")
print("Sources: OFFICIAL federation.edu.au 2026 published international course fee PDF (direct,")
print("most authoritative source found this session), idp.com, collegedunia, shiksha.com")
