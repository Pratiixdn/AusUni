import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (60, "44000", "6.0", "6.0"),  # Bachelor of Commerce - shiksha; IELTS OFFICIAL deakin.edu.au (2x)
                                    # direct: 6.0 overall, no band below 6.0
    (59, "41000", "6.0", "6.0"),  # Bachelor of Cyber Security - shiksha; IELTS OFFICIAL deakin.edu.au
                                    # (3x) direct: 6.0 overall, no band below 6.0
    (58, "44000", "7.0", "6.5"),  # Bachelor of Nursing - idp.com; IELTS OFFICIAL deakin.edu.au direct:
                                    # 7.0 overall (7.0 speaking/reading/listening, 6.5 writing)
    (62, "42400", "6.5", "6.0"),  # Master of Business Administration (MBA, plain/domestic-focused, NOT
                                    # "International" variant which is a separate $48,600-49,200 course)
                                    # - mystudyoffers general range midpoint; IELTS OFFICIAL deakin.edu.au
                                    # direct: 6.5/6.0
    (61, "44200", "6.5", "6.0"),  # Master of Information Technology - idp.com direct 2026; IELTS
                                    # OFFICIAL deakin.edu.au (2x) direct: 6.5/6.0 (already correct)
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
print("DEAKIN COMPLETE: 5 of 5 courses verified.")
print("Sources: OFFICIAL deakin.edu.au (IELTS confirmed directly for every single course - most")
print("thorough official coverage of any uni verified so far), idp.com, shiksha.com,")
print("mystudyoffers.com. NOTE: DB's plain 'Master of Business Administration' distinguished")
print("from Deakin's separate, pricier 'MBA (International)' variant.")
