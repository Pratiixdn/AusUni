import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

c100 = Course.objects.get(pk=100)
old_fee, old_ielts = c100.tuition_fee_annual, c100.ielts_overall
c100.tuition_fee_annual = "36250"
c100.ielts_overall = "6.0"
c100.ielts_min_band = "6.0"
c100.save()
print(f"[100] {c100.name}: fee {old_fee}->36250, IELTS {old_ielts}/->6.0/6.0")

# [101] MAJOR CORRECTION: "Master of Information Technology" is not Curtin's exact program name.
# The real degree is "Master of Science (Information Systems and Technology)".
c101 = Course.objects.get(pk=101)
old_name = c101.name
c101.name = "Master of Science (Information Systems and Technology)"
c101.slug = "master-of-science-information-systems-and-technology"
c101.tuition_fee_annual = "30750"
c101.ielts_overall = "6.5"
c101.ielts_min_band = "6.0"
c101.save()
print(f"[101] MAJOR CORRECTION: '{old_name}' -> '{c101.name}'")
print(f"    Fee: -> 30750, IELTS: -> 6.5/6.0")
print(f"    Reason: 'Master of Information Technology' is not Curtin's exact program name.")
print(f"    Confirmed real degree via collegedunia (2x confirmed).")

print()
print("CURTIN COMPLETE: 2 of 2 courses verified (1 major rename).")
print("Sources: idp.com, shiksha.com, collegedunia (2x confirmed)")
