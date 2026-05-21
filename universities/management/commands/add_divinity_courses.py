import os
import re
from django.core.management.base import BaseCommand
from universities.models import University, Course, State, City
from django.utils.text import slugify

DATA = """
Undergraduate Certificate in Divinity FT/PT 0.5 26 1 UG 4 2,184 N/A N/A 8,736
Diploma in Theology FT/PT 1 52 4 UG 8 2,184 N/A 17,472 17,472
Diploma in Ministry FT/PT 1 52 4 UG 8 2,184 N/A 17,472 17,472
Advanced Diploma in Philosophy FT/PT 2 104 8 UG 8 2,184 N/A 17,472 34,944
Advanced Diploma in Theology and Ministry FT/PT 2 104 8 UG 8 2,184 N/A 17,472 34,944
Bachelor of Counselling * FT/PT 3 52 9 UG 8 2,184 N/A 17,472 52,416
Bachelor of Ministry FT/PT 3 156 9 UG 8 2,184 N/A 17,472 52,416
Bachelor of Theology FT/PT 3 156 9 UG 8 2,184 N/A 17,472 52,416
Graduate Certificate in Children and Families Ministry FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Divinity FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Education and Theology FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Leadership *** FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Professional Supervision PT 0.5 26 2 PG 4 2,538 N/A N/A 10,152
Graduate Certificate in Research Methodology FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Spiritual Care FT/PT 0.5 26 2 PG 6 1,692 N/A N/A 10,152
Graduate Certificate in Spirituality FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Teaching Religious Education ** FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Certificate in Theology FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Graduate Diploma in Divinity FT/PT 1 52 3 PG 6 3,384 N/A 20,304 20,304
Graduate Diploma in Pastoral and Spiritual Care FT/PT 1 52 3 PG 6 3,384 N/A 20,304 20,304
Graduate Diploma in Philosophy FT/PT 1 52 3 PG 6 3,384 N/A 20,304 20,304
Graduate Diploma in Professional Supervision PT 1 52 3 PG 8 2,538 N/A 20,304 20,304
Graduate Diploma in Spiritual Direction FT/PT 1 52 3 PG 6 3,384 N/A 20,304 20,304
Graduate Diploma in Spirituality FT/PT 1 52 3 PG 6 3,384 N/A 20,304 20,304
Graduate Diploma in Theology FT/PT 1 52 3 PG 6 3,384 N/A 20,304 20,304
Master of Divinity FT/PT 3 156 9 PG 6 3,384 N/A 20,304 60,912
Master of Education and Theology FT/PT 1.5 78 4.5 PG 6 3,384 N/A 20,304 30,456
Master of Pastoral and Spiritual Care FT/PT 2 104 6 PG 6 3,384 N/A 20,304 40,608
Master of Philosophical Studies FT/PT 2 104 6 PG 6 3,384 N/A 20,304 40,608
Master of Spiritual Direction FT/PT 2 104 6 PG 6 3,384 N/A 20,304 40,608
Master of Spirituality FT/PT 2 104 6 PG 6 3,384 N/A 20,304 40,608
Master of Theological Studies FT/PT 2 104 6 PG 6 3,384 N/A 20,304 40,608
Master of Theology FT/PT 2 104 5 PG 6 3,384 N/A 20,304 33,840
Master of Philosophy FT/PT 1.5 78 4 HDR N/A N/A 10,152 20,304 30,456
Doctor of Philosophy FT/PT 3 156 8 HDR N/A N/A 10,152 20,304 60,912
Doctor of Professional Practice PT 3 156 8 HDR N/A N/A 10,152 20,304 60,912
Graduate Certificate in Teaching Meditation~ FT/PT 0.5 26 2 PG 3 3,384 N/A N/A 10,152
Doctor of Theology~ FT/PT 3 156 8 HDR N/A N/A 10,152 20,304 60,912
Doctor of Ministry~ FT/PT 3 156 8 HDR N/A N/A 10,152 20,304 60,912
"""

class Command(BaseCommand):
    help = 'Seeds courses for University of Divinity'

    def handle(self, *args, **kwargs):
        state, _ = State.objects.get_or_create(name='Victoria', abbreviation='VIC', slug='victoria')
        city, _ = City.objects.get_or_create(name='Melbourne', slug='melbourne', state=state)
        
        uni, created = University.objects.get_or_create(
            name='University of Divinity',
            defaults={
                'slug': 'university-of-divinity',
                'state': state,
                'city': city,
                'institution_type': 'public_university',
                'description': 'The University of Divinity is an Australian collegiate university specialising in divinity.',
                'is_featured': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created {uni.name}"))
        else:
            self.stdout.write(f"Found {uni.name}")

        lines = [line.strip() for line in DATA.strip().split('\n') if line.strip()]
        
        courses_added = 0
        for line in lines:
            line = line.replace('~', '').replace('*', '').strip()
            
            # Find Mode
            match = re.search(r'\s+(FT/PT|FT|PT)\s+', line)
            if not match:
                continue
            
            mode_str = match.group(1)
            name = line[:match.start()].strip()
            
            # Extract duration and fee
            rest_of_line = line[match.end():].split()
            duration_str = rest_of_line[0]
            
            try:
                duration_val = float(duration_str)
                duration = f"{duration_val} years" if duration_val >= 1 else f"{int(duration_val*12)} months"
            except:
                duration = duration_str

            # Find level
            if ' UG ' in line:
                if 'Bachelor' in name: level = 'bachelor'
                elif 'Certificate' in name: level = 'certificate'
                else: level = 'diploma'
            elif ' PG ' in line:
                if 'Master' in name: level = 'master'
                elif 'Diploma' in name: level = 'graduate_diploma'
                else: level = 'graduate_cert'
            elif ' HDR ' in line:
                level = 'phd'
            else:
                level = 'certificate'

            tokens = line.split()
            total_fee_str = tokens[-1].replace(',', '')
            annual_fee_str = tokens[-2].replace(',', '')
            
            total_fee = float(total_fee_str) if total_fee_str.isdigit() else 0.0
            
            if annual_fee_str.isdigit():
                annual_fee = float(annual_fee_str)
            else:
                # If annual fee is N/A, try to calculate from total fee and duration
                try:
                    if duration_val > 0:
                        annual_fee = total_fee / duration_val
                    else:
                        annual_fee = total_fee
                except:
                    annual_fee = total_fee

            # Use realistic defaults for international English requirements
            if level == 'bachelor' or level == 'diploma':
                ielts = 6.0
                pte = 50
            else:
                ielts = 6.5
                pte = 58

            import hashlib
            slug_hash = hashlib.md5(name.encode()).hexdigest()[:5]
            slug = slugify(f"{uni.slug}-{name}")[:44] + f"-{slug_hash}"

            course, c_created = Course.objects.update_or_create(
                university=uni,
                name=name,
                defaults={
                    'slug': slug,
                    'level': level,
                    'field_of_study': 'Theology and Divinity',
                    'duration': duration,
                    'tuition_fee_annual': annual_fee,
                    'ielts_overall': ielts,
                    'pte_overall': pte,
                    'academic_requirement': 'Standard university entry requirements apply.',
                }
            )
            if c_created:
                courses_added += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully added/updated {courses_added} courses for {uni.name}."))
