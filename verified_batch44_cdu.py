import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (132, "31688", "6.0", "6.0"),  # Bachelor of Information Technology - shiksha + alfabetaglobal
                                     # (2x confirmed, same figure); IELTS matches DB (general CDU
                                     # standard, no conflict found)
    (133, "38720", "7.0", "7.0"),  # Bachelor of Nursing - OFFICIAL cdu.edu.au course page direct:
                                     # $38,720 (2026 annual tuition); IELTS confirmed multiple official-
                                     # adjacent sources (collegedunia, mystudyoffers): 7.0 (matches DB)
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
print("CHARLES DARWIN COMPLETE: 2 of 2 courses verified.")
print("Sources: OFFICIAL cdu.edu.au (course page direct for Nursing fee), shiksha.com,")
print("alfabetaglobal.com, collegedunia, mystudyoffers.com")
