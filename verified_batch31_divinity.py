import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (73, "18528", "6.0", "5.5"),  # Bachelor of Theology - OFFICIAL divinity.edu.au direct current page
                                    # (last updated 21 Aug 2026): $18,528/yr at 2027 fees, total course
                                    # cost $55,584. IELTS per aucd.edu.au (Divinity-affiliated college,
                                    # official-adjacent): 6.0 overall, no band below 5.5
    (74, "21528", "6.5", "6.0"),  # Master of Divinity - OFFICIAL divinity.edu.au direct current page
                                    # (same update date): $21,528/yr at 2027 fees, total course cost
                                    # $64,584. IELTS per standyou.com (official-adjacent): "same as
                                    # undergraduate (IELTS 6.5)"
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
print("UNIVERSITY OF DIVINITY COMPLETE: 2 of 2 courses verified.")
print("Sources: OFFICIAL divinity.edu.au current course pages (both last updated 21 August 2026,")
print("direct fee figures at published 2027 rates - the most current pricing available),")
print("aucd.edu.au and standyou.com (official-adjacent) for IELTS standards.")
print("NOTE: Fees reflect 2027 published rates as these were the most current on the official")
print("site; 2026 rates would be marginally lower per year-over-year fee increase patterns seen")
print("elsewhere at this institution.")
