import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ausuni.settings")
django.setup()
from universities.models import Course

expected = {
    91: ("36720", "6.0", "5.5"), 93: ("37860", "6.0", "5.5"), 92: ("46080", "6.0", "5.5"),
    94: ("36000", "6.0", "5.5"), 95: ("31840", "6.0", "5.5"),
    96: ("26750", "6.0", "6.0"), 97: ("27600", "6.0", "5.0"),
    100: ("36250", "6.0", "6.0"), 101: ("30750", "6.5", "6.0"),
    102: ("44000", "7.0", "7.0"), 103: ("41550", "6.0", "6.0"), 104: ("37150", "6.5", "6.0"),
    106: ("36730", "6.5", "6.0"), 105: ("68400", "6.0", "6.0"), 107: ("36730", "6.0", "6.0"),
    109: ("35283", "6.0", "6.0"), 108: ("36699", "7.0", "7.0"),
    115: ("39600", "6.0", "6.0"), 117: ("40200", "7.0", "6.5"), 116: ("34700", "6.5", "6.0"),
    118: ("29800", "6.0", "5.5"), 119: ("31400", "6.5", "6.0"),
    132: ("31688", "6.0", "6.0"), 133: ("38720", "7.0", "7.0"),
    135: ("40892", "6.0", "5.5"), 137: ("33450", "6.5", "6.0"), 134: ("40892", "6.0", "5.5"), 136: ("32978", "6.5", "6.0"),
}
rename_checks = {97: "Bachelor of Information and Communications Technology",
                 101: "Master of Science (Information Systems and Technology)",
                 102: "Bachelor of Science (Nursing)"}

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
