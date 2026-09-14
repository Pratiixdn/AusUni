import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

updates = [
    (115, "39600", "6.0", "6.0"),  # Bachelor of Information Technology - shiksha + alfabetaglobal
                                     # (plain degree, direct exact match); IELTS official-adjacent
                                     # studyabroadcourses.org direct confirmed
    (117, "40200", "7.0", "6.5"),  # Bachelor of Nursing - shiksha direct (matches Pre-Registration
                                     # variant "first-year tuition fee" exactly); IELTS OFFICIAL
                                     # flinders.edu.au direct: 7.0 overall, 7.0 speaking/reading/
                                     # listening, 6.5 writing
    (116, "34700", "6.5", "6.0"),  # Master of Information Technology - OFFICIAL flinders.edu.au
                                     # postgraduate fee page direct: $34,700 (2026, plain MIT); IELTS
                                     # confirmed idp.com direct (matches DB)
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
print("FLINDERS COMPLETE: 3 of 3 courses verified.")
print("Sources: OFFICIAL flinders.edu.au (postgraduate fee page direct for MIT, IELTS breakdown")
print("direct for Nursing), shiksha.com, idp.com, alfabetaglobal.com, studyabroadcourses.org")
