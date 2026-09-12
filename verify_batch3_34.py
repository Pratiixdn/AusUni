import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

expected = {
    51: ("40320", "6.5", "6.0"), 52: ("51840", "6.5", "6.0"), 53: ("41280", "6.5", "6.0"),
    57: ("42567", "6.0", "6.0"), 54: ("40960", "6.0", "6.0"), 55: ("47320", "6.5", "6.0"), 56: ("42240", "6.5", "6.0"),
    60: ("44000", "6.0", "6.0"), 59: ("41000", "6.0", "6.0"), 58: ("44000", "7.0", "6.5"), 62: ("42400", "6.5", "6.0"), 61: ("44200", "6.5", "6.0"),
    64: ("42000", "6.0", "6.0"), 63: ("44600", "7.0", "7.0"), 66: ("50200", "7.0", "7.0"), 65: ("41000", "6.5", "6.0"),
    69: ("36800", "6.0", "6.0"), 67: ("36800", "6.0", "6.0"), 68: ("34600", "6.5", "6.0"),
    72: ("26300", "6.0", "6.0"), 70: ("41400", "6.0", "6.0"), 71: ("41400", "6.0", "6.0"),
    73: ("18528", "6.0", "5.5"), 74: ("21528", "6.5", "6.0"),
    84: ("33500", "6.5", "6.0"), 81: ("35000", "6.5", "6.0"), 82: ("40500", "6.5", "6.0"), 83: ("43500", "6.5", "6.0"),
    86: ("32960", "6.0", "6.0"), 85: ("22575", "6.0", "6.0"), 87: ("34500", "6.5", "6.0"),
    89: ("63120", "6.5", "6.0"), 90: ("49445", "6.5", "6.0"), 88: ("63120", "7.0", "6.5"),
}
rename_checks = {68: "Master of Applied Information Technology"}

def num_eq(a, b):
    try: return float(a) == float(b)
    except (TypeError, ValueError): return str(a) == str(b)

print(f"{'PK':<5} {'NAME':<45} {'FEE':<10} {'IELTS':<8} {'BAND':<6} {'STATUS'}")
print("-" * 90)
ok = mismatch = missing = 0
for pk, (efee, eielts, eband) in expected.items():
    try:
        c = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        print(f"{pk:<5} {'<NOT FOUND>':<45} MISSING"); missing += 1; continue
    problems = []
    if not num_eq(c.tuition_fee_annual, efee): problems.append(f"fee={c.tuition_fee_annual} want {efee}")
    if not num_eq(c.ielts_overall, eielts): problems.append(f"ielts={c.ielts_overall} want {eielts}")
    if not num_eq(c.ielts_min_band, eband): problems.append(f"band={c.ielts_min_band} want {eband}")
    if pk in rename_checks and c.name != rename_checks[pk]: problems.append(f"name='{c.name}' want '{rename_checks[pk]}'")
    status = "OK" if not problems else "MISMATCH: " + "; ".join(problems)
    ok += 1 if not problems else 0
    mismatch += 0 if not problems else 1
    print(f"{pk:<5} {c.name[:44]:<45} {str(c.tuition_fee_annual):<10} {str(c.ielts_overall):<8} {str(c.ielts_min_band):<6} {status}")
print("-" * 90)
print(f"OK: {ok}   MISMATCH: {mismatch}   MISSING: {missing}   TOTAL CHECKED: {len(expected)}")
