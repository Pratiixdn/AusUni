import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (64, "42000", "6.0", "6.0"),  # Bachelor of Information Technology - idp.com; IELTS official-adjacent
                                    # (2x) confirmed direct: 6.0 overall, no band below 6.0
    (63, "44600", "7.0", "7.0"),  # Bachelor of Nursing - collegedunia direct 2026; IELTS official-adjacent
                                    # (bachelorsportal, most detailed): 7.0 overall, no band below 7.0
                                    # (stricter than typical nursing pattern - already correct in DB)
    (66, "50200", "7.0", "7.0"),  # Bachelor of Physiotherapy (Honours) - shiksha direct; IELTS confirmed
                                    # 3x official-adjacent: 7.0 overall, no band below 7.0 (already correct)
    (65, "41000", "6.5", "6.0"),  # Master of Information Technology - shiksha direct; IELTS confirmed
                                    # 2x official-adjacent: 6.5 overall, no band below 6.0 (already correct)
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
print("LA TROBE COMPLETE: 4 of 4 courses verified.")
print("Sources: gooduniversitiesguide.com.au, studiesinaustralia.com, bachelorsportal.com,")
print("findthecourses.com.au (all official-adjacent, citing La Trobe course pages directly),")
print("shiksha.com, collegedunia. IELTS values for Nursing/Physiotherio confirmed as already")
print("accurate in the DB - correctly reflecting La Trobe's stricter no-band-below-7.0 standard.")
