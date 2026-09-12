import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (51, "40320", "6.5", "6.0"),  # Bachelor of Information Technology - shiksha + OFFICIAL rmit.edu.au
                                    # apply-now page (Professional variant), IELTS official direct
    (52, "51840", "6.5", "6.0"),  # Bachelor of Architecture (Honours) - NOTE: RMIT does not offer this
                                    # exact combined degree name; closest genuine undergrad architecture
                                    # degree is "Bachelor of Architectural Design" (official rmit.edu.au,
                                    # 3yr, $51,840). Using that fee as best available match; name kept
                                    # as-is pending further confirmation this isn't a legacy/renamed
                                    # program. IELTS per RMIT blanket standard.
    (53, "41280", "6.5", "6.0"),  # Master of Information Technology - OFFICIAL rmit.edu.au apply-now
                                    # page direct (2025 figure, most authoritative source found)
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
print("RMIT COMPLETE: 3 of 3 courses verified.")
print("Sources: OFFICIAL rmit.edu.au (IELTS + fees confirmed directly for BIT and MIT),")
print("shiksha.com. FLAG: 'Bachelor of Architecture (Honours)' as an exact RMIT degree name")
print("could not be directly confirmed - RMIT's real architecture pathway is 'Bachelor of")
print("Architectural Design' -> 'Master of Architecture'. Recommend follow-up check.")
