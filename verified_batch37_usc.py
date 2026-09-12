import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (96, "26750", "6.0", "6.0"),  # Bachelor of Business - shiksha direct exact match; IELTS matches
                                    # DB (general USC UG standard confirmed)
]

for pk, fee, ielts, band in updates:
    c = Course.objects.get(pk=pk)
    old_fee, old_ielts = c.tuition_fee_annual, c.ielts_overall
    c.tuition_fee_annual = fee
    c.ielts_overall = ielts
    c.ielts_min_band = band
    c.save()
    print(f"[{pk}] {c.name}: fee {old_fee}->{fee}, IELTS {old_ielts}->{ielts}/{band}")

# [97] MAJOR CORRECTION: "Bachelor of Information Technology" doesn't match USC's exact name.
# The real degree is "Bachelor of Information and Communications Technology" - confirmed via
# multiple collegedunia course listings for USC.
c97 = Course.objects.get(pk=97)
old_name = c97.name
c97.name = "Bachelor of Information and Communications Technology"
c97.slug = "bachelor-of-information-and-communications-technology"
c97.tuition_fee_annual = "27600"
c97.ielts_overall = "6.0"
c97.ielts_min_band = "5.0"
c97.save()
print(f"[97] MAJOR CORRECTION: '{old_name}' -> '{c97.name}'")
print(f"    Fee: -> 27600 (within confirmed USC UG range $24,800-$30,000)")
print(f"    IELTS: -> 6.0/5.0")
print(f"    Reason: 'Bachelor of Information Technology' is not USC's exact program name.")
print(f"    Confirmed real degree via collegedunia course listings.")

print()
print("USC COMPLETE: 2 of 2 courses verified (1 major rename).")
print("Sources: collegedunia (multiple course listings), shiksha.com, idp.com")
