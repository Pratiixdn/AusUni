import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (91, "36720", "6.0", "5.5"),  # Bachelor of Information Technology - idp.com 2026 direct; IELTS
                                    # OFFICIAL cqu.edu.au: 6.0 overall, 5.5 min each component
    (93, "37860", "6.0", "5.5"),  # Bachelor of Engineering Technology (Honours) - shiksha direct exact
    (92, "46080", "6.0", "5.5"),  # Master of Information Technology - idp.com 2026 direct; IELTS
                                    # OFFICIAL postgradaustralia.com.au confirmed: 6.0/5.5
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
print("CQUNIVERSITY COMPLETE: 3 of 3 courses verified.")
print("Sources: OFFICIAL cqu.edu.au (IELTS confirmed directly: 6.0 overall, 5.5 min - this")
print("applies uniformly across CQU courses, an unusually lenient standard vs. most other unis'")
print("6.0 with no sub-band below 6.0), idp.com, shiksha.com, postgradaustralia.com.au")
