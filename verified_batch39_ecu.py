import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

# [102] MAJOR CORRECTION: "Bachelor of Nursing" doesn't exactly match ECU's degree name.
# ECU's real undergrad nursing degree is "Bachelor of Science (Nursing)".
c102 = Course.objects.get(pk=102)
old_name = c102.name
c102.name = "Bachelor of Science (Nursing)"
c102.slug = "bachelor-of-science-nursing"
c102.tuition_fee_annual = "44000"
c102.ielts_overall = "7.0"
c102.ielts_min_band = "7.0"
c102.save()
print(f"[102] MAJOR CORRECTION: '{old_name}' -> '{c102.name}'")
print(f"    Fee: -> 44000, IELTS: -> 7.0/7.0 (already correct)")
print(f"    Reason: 'Bachelor of Nursing' doesn't exactly match ECU's program name.")
print(f"    Confirmed real degree via idp.com direct: 'Bachelor of Science (Nursing)'")
print()

updates = [
    (103, "41550", "6.0", "6.0"),  # Bachelor of Science (Cybersecurity) - shiksha direct exact match;
                                     # IELTS matches DB (general ECU standard)
    (104, "37150", "6.5", "6.0"),  # Master of Cybersecurity - unischolars direct exact match; IELTS
                                     # confirmed multiple sources (matches DB)
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
print("EDITH COWAN COMPLETE: 3 of 3 courses verified (1 major rename).")
print("Sources: idp.com, shiksha.com, unischolars.com, topuniversities.com")
