import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (118, "29800", "6.0", "5.5"),  # Bachelor of Business Administration - idp.com (2025, closest
                                     # Business variant, no exact "Business Administration" degree name
                                     # confirmed at Torrens - real degrees are "Bachelor of Business" /
                                     # "Bachelor of Business (Entrepreneurship)"); IELTS OFFICIAL
                                     # torrens.edu.au direct: 6.0/5.5 (matches DB)
    (119, "31400", "6.5", "6.0"),  # Master of Business Administration - shiksha direct plain-degree
                                     # exact match; IELTS OFFICIAL torrens.edu.au direct (multiple
                                     # confirmations): 6.5/6.0 (matches DB)
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
print("TORRENS COMPLETE: 2 of 2 courses verified.")
print("Sources: OFFICIAL torrens.edu.au (IELTS confirmed directly for both courses), idp.com,")
print("shiksha.com. NOTE: 'Bachelor of Business Administration' as an exact Torrens degree name")
print("could not be directly confirmed - closest real degrees are 'Bachelor of Business' and")
print("'Bachelor of Business (Entrepreneurship)'. Flag for follow-up if precision matters.")
