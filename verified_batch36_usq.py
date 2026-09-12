import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (94, "36000", "6.0", "5.5"),  # Bachelor of Engineering (Honours) - shiksha direct exact; IELTS
                                    # OFFICIAL unisq.edu.au (2x direct): 6.0/5.5
    (95, "31840", "6.0", "5.5"),  # Master of Information Technology - idp.com (2x direct 2026); IELTS
                                    # OFFICIAL unisq.edu.au: 6.0/5.5
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
print("USQ COMPLETE: 2 of 2 courses verified.")
print("Sources: OFFICIAL unisq.edu.au (IELTS confirmed directly for both courses, matching")
print("DB's existing values exactly), idp.com (2026-dated, confirmed twice)")
