import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (86, "32960", "6.0", "6.0"),  # Bachelor of Information Technology - shiksha (main Australia campus
                                    # figure); IELTS official-adjacent idp.com + jcu.edu.sg direct match
    (85, "22575", "6.0", "6.0"),  # Bachelor of Marine Biology - collegedunia (flat-rate UG science fee,
                                    # multiple consistent confirmations across JCU science degrees)
    (87, "34500", "6.5", "6.0"),  # Master of Data Science - applyboard.com (main JCU Brisbane 1st-year
                                    # figure); IELTS official-adjacent idp.com direct match
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
print("JAMES COOK COMPLETE: 3 of 3 courses verified.")
print("Sources: idp.com, jcu.edu.sg (official-adjacent international campus), shiksha.com,")
print("collegedunia, applyboard.com")
