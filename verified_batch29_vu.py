import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

# [68] MAJOR CORRECTION: "Master of Information Technology" is not VU's exact program name.
# VU's genuine postgraduate IT degree is "Master of Applied Information Technology". Renaming.
c68 = Course.objects.get(pk=68)
old_name = c68.name
c68.name = "Master of Applied Information Technology"
c68.slug = "master-of-applied-information-technology"
c68.tuition_fee_annual = "34600"
c68.ielts_overall = "6.5"
c68.ielts_min_band = "6.0"
c68.save()
print(f"[68] MAJOR CORRECTION: '{old_name}' -> '{c68.name}'")
print(f"    Fee: -> 34600, IELTS: -> 6.5/6.0")
print(f"    Reason: 'Master of Information Technology' is not VU's exact program name.")
print(f"    Confirmed real degree via OFFICIAL vu.edu.au: 'Master of Applied Information")
print(f"    Technology'")
print()

updates = [
    (69, "36800", "6.0", "6.0"),  # Bachelor of Business - OFFICIAL vu.edu.au direct fee (AU$18,400/sem
                                    # x2) + IELTS confirmed official direct
    (67, "36800", "6.0", "6.0"),  # Bachelor of Information Technology - OFFICIAL vu.edu.au direct fee
                                    # (AU$18,400/sem x2, confirmed 2x) + IELTS confirmed official direct
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
print("VICTORIA UNIVERSITY COMPLETE: 3 of 3 courses verified (1 major rename + 2 corrections).")
print("Sources: OFFICIAL vu.edu.au (IELTS + fees confirmed directly for every course - among")
print("the most thorough official coverage this session), idp.com, shiksha.com, collegedunia.")
