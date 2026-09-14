import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (109, "35283", "6.0", "6.0"),  # Bachelor of Business Administration - collegedunia (Notre Dame
                                     # Australia, distinct from US Notre Dame in mixed results); IELTS
                                     # OFFICIAL idp.com direct: 6.0 overall, no band below 6.0
    (108, "36699", "7.0", "7.0"),  # Bachelor of Nursing - collegedunia (3x confirmed, same figure);
                                     # IELTS matches DB exactly (already correct)
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
print("NOTRE DAME COMPLETE: 2 of 2 courses verified.")
print("Sources: idp.com (IELTS direct official), collegedunia (fee, confirmed 3x consistent)")
