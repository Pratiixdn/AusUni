"""
Management command – seeds ALL 43 Australian universities.
Run: python manage.py seed_universities
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from universities.models import State, City, University, Campus, Course, Scholarship


class Command(BaseCommand):
    help = 'Seed the database with ALL Australian university data'

    def handle(self, *args, **options):
        self.stdout.write('\n🌏 Seeding AusUni – all Australian universities...\n')
        self._create_states()
        self._create_cities()
        self._seed_all()
        self.stdout.write('\n✅ Done!')
        self.stdout.write(f'   Universities : {University.objects.count()}')
        self.stdout.write(f'   Courses      : {Course.objects.count()}')
        self.stdout.write(f'   Scholarships : {Scholarship.objects.count()}\n')

    # ── States ────────────────────────────────────────────────
    def _create_states(self):
        self.stdout.write('📍 States...')
        for d in [
            ('New South Wales','NSW','Sydney','Australia\'s most populous state. Home to USYD (#18), UNSW (#19), UTS, Macquarie, Newcastle, Wollongong, WSU, ACU, CSU, SCU, UNE, and Avondale University.'),
            ('Victoria','VIC','Melbourne','Home to Melbourne – world\'s most liveable city. UniMelb (#13), Monash (#37), RMIT, Swinburne, Deakin, La Trobe, VU, Federation, and University of Divinity.'),
            ('Queensland','QLD','Brisbane','The Sunshine State. 2032 Olympic host. UQ (#40), QUT, Griffith, JCU, Bond, CQU, UniSQ, and UniSC.'),
            ('Western Australia','WA','Perth','Largest state. Growing tech/mining hub. UWA (#72), Curtin (#185), ECU, Murdoch, Notre Dame.'),
            ('South Australia','SA','Adelaide','Wine country. Affordable lifestyle. Adelaide University (merged Go8), Flinders, Torrens.'),
            ('Australian Capital Territory','ACT','Canberra','National capital. ANU (#30) and University of Canberra.'),
            ('Tasmania','TAS','Hobart','Island state with UNESCO wilderness. UTAS – world leader in Antarctic research.'),
            ('Northern Territory','NT','Darwin','Tropical frontier. CDU serves Darwin and Alice Springs.'),
        ]:
            State.objects.update_or_create(slug=slugify(d[0]),defaults={'name':d[0],'abbreviation':d[1],'capital':d[2],'description':d[3]})
        self.stdout.write('  ✓ 8 states/territories')

    # ── Cities ────────────────────────────────────────────────
    def _create_cities(self):
        self.stdout.write('🏙️  Cities...')
        cities = [
            ('Sydney','New South Wales','AUD 2,200–3,500/month'),
            ('Newcastle','New South Wales','AUD 1,500–2,200/month'),
            ('Wollongong','New South Wales','AUD 1,400–1,900/month'),
            ('Bathurst','New South Wales','AUD 1,100–1,500/month'),
            ('Wagga Wagga','New South Wales','AUD 1,100–1,500/month'),
            ('Armidale','New South Wales','AUD 1,100–1,500/month'),
            ('Lismore','New South Wales','AUD 1,200–1,600/month'),
            ('Cooranbong','New South Wales','AUD 1,200–1,600/month'),
            ('Melbourne','Victoria','AUD 2,000–3,200/month'),
            ('Geelong','Victoria','AUD 1,400–1,900/month'),
            ('Ballarat','Victoria','AUD 1,200–1,700/month'),
            ('Bendigo','Victoria','AUD 1,200–1,600/month'),
            ('Brisbane','Queensland','AUD 1,800–2,800/month'),
            ('Gold Coast','Queensland','AUD 1,700–2,500/month'),
            ('Sunshine Coast','Queensland','AUD 1,600–2,200/month'),
            ('Townsville','Queensland','AUD 1,300–1,800/month'),
            ('Cairns','Queensland','AUD 1,300–1,800/month'),
            ('Rockhampton','Queensland','AUD 1,100–1,500/month'),
            ('Toowoomba','Queensland','AUD 1,200–1,600/month'),
            ('Springfield','Queensland','AUD 1,600–2,200/month'),
            ('Noosa','Queensland','AUD 1,700–2,400/month'),
            ('Perth','Western Australia','AUD 1,800–2,600/month'),
            ('Fremantle','Western Australia','AUD 1,700–2,400/month'),
            ('Adelaide','South Australia','AUD 1,600–2,200/month'),
            ('Canberra','Australian Capital Territory','AUD 1,800–2,400/month'),
            ('Hobart','Tasmania','AUD 1,400–1,900/month'),
            ('Launceston','Tasmania','AUD 1,200–1,600/month'),
            ('Burnie','Tasmania','AUD 1,100–1,400/month'),
            ('Darwin','Northern Territory','AUD 1,500–2,100/month'),
            ('Alice Springs','Northern Territory','AUD 1,300–1,800/month'),
            ('Online','Victoria','N/A – Online Study'),
        ]
        n = 0
        for name, state_name, cost in cities:
            try:
                state = State.objects.get(name=state_name)
                City.objects.update_or_create(slug=slugify(name),state=state,defaults={'name':name,'cost_of_living':cost})
                n += 1
            except State.DoesNotExist:
                pass
        self.stdout.write(f'  ✓ {n} cities')

    # ── Master university list ────────────────────────────────
    def _seed_all(self):
        self.stdout.write('\n🏛️  Universities...\n')
        for grp_name, loader in self._get_loaders():
            self.stdout.write(f'  ── {grp_name}')
            for uni, campuses, courses, schols in loader():
                self._seed_one(uni, campuses, courses, schols)

    def _get_loaders(self):
        return [
            ('NSW – Core (USYD, UNSW)', self._load_nsw_core),
            ('NSW – Additional', self._load_nsw_extra),
            ('VIC – Core (Monash, UniMelb, RMIT)', self._load_vic_core),
            ('VIC – Additional', self._load_vic_extra),
            ('QLD – Core (UQ, QUT)', self._load_qld_core),
            ('QLD – Additional', self._load_qld_extra),
            ('WA – All', self._load_wa),
            ('SA – All', self._load_sa),
            ('ACT – All (ANU, UC)', self._load_act),
            ('NT – All (CDU)', self._load_nt),
            ('TAS – All (UTAS)', self._load_tas),
        ]

    # ── Loader helpers ─────────────────────────────────────────
    def _load_nsw_core(self):
        try:
            from data.universities import university_of_sydney as m; yield m.UNIVERSITY, m.CAMPUSES, m.COURSES, m.SCHOLARSHIPS
        except ImportError: pass
        try:
            from data.universities import unsw_sydney as m; yield m.UNIVERSITY, m.CAMPUSES, m.COURSES, m.SCHOLARSHIPS
        except ImportError: pass

    def _load_nsw_extra(self):
        try:
            from data.universities import nsw_universities as m
            for u,ca,co,sc in [
                (m.UNIVERSITY_UTS,m.UTS_CAMPUSES,m.UTS_COURSES,m.UTS_SCHOLARSHIPS),
                (m.UNIVERSITY_MACQUARIE,m.MACQUARIE_CAMPUSES,m.MACQUARIE_COURSES,m.MACQUARIE_SCHOLARSHIPS),
                (m.UNIVERSITY_NEWCASTLE,m.NEWCASTLE_CAMPUSES,m.NEWCASTLE_COURSES,m.NEWCASTLE_SCHOLARSHIPS),
                (m.UNIVERSITY_UOW,m.UOW_CAMPUSES,m.UOW_COURSES,m.UOW_SCHOLARSHIPS),
                (m.UNIVERSITY_WSU,m.WSU_CAMPUSES,m.WSU_COURSES,m.WSU_SCHOLARSHIPS),
                (m.UNIVERSITY_ACU,m.ACU_CAMPUSES,m.ACU_COURSES,m.ACU_SCHOLARSHIPS),
                (m.UNIVERSITY_CSU,m.CSU_CAMPUSES,m.CSU_COURSES,m.CSU_SCHOLARSHIPS),
                (m.UNIVERSITY_SCU,m.SCU_CAMPUSES,m.SCU_COURSES,m.SCU_SCHOLARSHIPS),
                (m.UNIVERSITY_UNE,m.UNE_CAMPUSES,m.UNE_COURSES,m.UNE_SCHOLARSHIPS),
                (m.UNIVERSITY_AVONDALE,m.AVONDALE_CAMPUSES,m.AVONDALE_COURSES,m.AVONDALE_SCHOLARSHIPS),
            ]: yield u,ca,co,sc
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    def _load_vic_core(self):
        for mod_name, u_attr, ca_attr, co_attr, sc_attr in [
            ('monash_university','UNIVERSITY','CAMPUSES','COURSES','SCHOLARSHIPS'),
            ('university_of_melbourne','UNIVERSITY','CAMPUSES','COURSES','SCHOLARSHIPS'),
        ]:
            try:
                import importlib; m = importlib.import_module(f'data.universities.{mod_name}')
                yield getattr(m,u_attr),getattr(m,ca_attr),getattr(m,co_attr),getattr(m,sc_attr)
            except ImportError: pass
        try:
            from data.universities import qut_and_rmit as m
            yield m.UNIVERSITY_RMIT,m.RMIT_CAMPUSES,m.RMIT_COURSES,m.RMIT_SCHOLARSHIPS
        except ImportError: pass

    def _load_vic_extra(self):
        try:
            from data.universities import vic_universities as m
            for u,ca,co,sc in [
                (m.UNIVERSITY_SWINBURNE,m.SWINBURNE_CAMPUSES,m.SWINBURNE_COURSES,m.SWINBURNE_SCHOLARSHIPS),
                (m.UNIVERSITY_DEAKIN,m.DEAKIN_CAMPUSES,m.DEAKIN_COURSES,m.DEAKIN_SCHOLARSHIPS),
                (m.UNIVERSITY_LATROBE,m.LATROBE_CAMPUSES,m.LATROBE_COURSES,m.LATROBE_SCHOLARSHIPS),
                (m.UNIVERSITY_VU,m.VU_CAMPUSES,m.VU_COURSES,m.VU_SCHOLARSHIPS),
                (m.UNIVERSITY_FEDERATION,m.FEDERATION_CAMPUSES,m.FEDERATION_COURSES,m.FEDERATION_SCHOLARSHIPS),
                (m.UNIVERSITY_DIVINITY,m.DIVINITY_CAMPUSES,m.DIVINITY_COURSES,m.DIVINITY_SCHOLARSHIPS),
            ]: yield u,ca,co,sc
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    def _load_qld_core(self):
        yield from self._load_uq()
        try:
            from data.universities import qut_and_rmit as m
            yield m.UNIVERSITY_QUT,m.QUT_CAMPUSES,m.QUT_COURSES,m.QUT_SCHOLARSHIPS
        except ImportError: pass

    def _load_uq(self):
        yield (
            {'name':'University of Queensland','short_name':'UQ','type':'public','group':'go8',
             'established':1909,'state':'Queensland','city':'Brisbane',
             'description':'The University of Queensland is a Group of Eight research university ranked #40 in the world (QS 2025). Located at the stunning heritage St Lucia campus on the Brisbane River, UQ is renowned for bioscience, engineering, business, law, and health. With 57,000+ students from 140+ countries, it is one of Australia\'s most internationally connected universities.',
             'about':'UQ\'s sandstone St Lucia campus on the Brisbane River is among Australia\'s most beautiful. The university has produced breakthrough research including the HPV cancer vaccine.',
             'ranking_qs':'#40 World (QS 2025)','ranking_times':'#77 World (THE 2024)',
             'total_students':'57,000+','international_students':'20,000+',
             'cost_of_living':'AUD 1,800–2,600/month',
             'popular_courses':'Bioscience, Engineering, Business, Law, IT, Medicine',
             'official_website':'https://www.uq.edu.au',
             'international_page':'https://future-students.uq.edu.au/international',
             'scholarship_page':'https://scholarships.uq.edu.au',
             'application_portal':'https://future-students.uq.edu.au/apply'},
            [{'name':'St Lucia Campus','city':'Brisbane','state':'Queensland','is_main':True,
              'address':'Campbell Road, St Lucia QLD 4072',
              'description':'114-hectare heritage sandstone campus on the Brisbane River.',
              'facilities':'Duhig Library, Great Court, Health Sciences, Engineering, Sports Facilities',
              'map_url':'https://maps.google.com/?q=University+of+Queensland+St+Lucia'},
             {'name':'Gatton Campus','city':'Toowoomba','state':'Queensland','is_main':False,
              'address':'Gatton QLD 4343','description':'Agricultural and veterinary sciences campus.'}],
            [{'name':'Bachelor of Engineering (Honours)','level':'honours','field_of_study':'Engineering',
              'duration':'4 years','tuition_fee_annual':45864,'intake_months':'February, July',
              'academic_requirement':'ATAR 90+ or equivalent.','ielts_overall':6.5,'ielts_min_band':6.0,
              'pte_overall':58,'toefl_ibt':87,
              'career_outcomes':'Mechanical, Chemical, Civil, Electrical, Mining Engineer',
              'description':'Engineers Australia accredited. 10+ specialisations. Industry capstone project.',
              'official_url':'https://www.uq.edu.au/study/program.html?acad_prog=2055','is_popular':True},
             {'name':'Bachelor of Business Management','level':'bachelor','field_of_study':'Business',
              'duration':'3 years','tuition_fee_annual':38064,'intake_months':'February, July',
              'academic_requirement':'Minimum ATAR 85 or equivalent.','ielts_overall':6.5,'ielts_min_band':6.0,
              'pte_overall':58,'toefl_ibt':87,
              'career_outcomes':'Business Analyst, Marketing Manager, HR Manager, Consultant',
              'description':'AACSB-accredited UQ Business School.',
              'official_url':'https://www.uq.edu.au/study/program.html?acad_prog=2003','is_popular':True},
             {'name':'Master of Information Technology','level':'master','field_of_study':'Information Technology',
              'duration':'2 years','tuition_fee_annual':43824,'intake_months':'February, July',
              'academic_requirement':'Bachelor\'s in IT or related field.','ielts_overall':6.5,'ielts_min_band':6.0,
              'pte_overall':58,'toefl_ibt':87,'career_outcomes':'IT Manager, Cloud Architect, Data Scientist',
              'description':'Advanced IT with cybersecurity and AI specialisations.',
              'official_url':'https://www.uq.edu.au/study/program.html?acad_prog=5560','is_popular':True}],
            [{'name':'UQ International Scholarship','type':'merit','coverage':'25% tuition fee reduction',
              'coverage_percentage':25,'eligibility':'International students commencing UQ programs.',
              'academic_requirement':'Distinction average','eligible_levels':'Bachelor, Master',
              'eligible_courses':'Most programs','deadline':'Intake-based','intake_deadline':True,
              'official_url':'https://scholarships.uq.edu.au/scholarship/uq-international-scholarship',
              'description':'UQ\'s primary merit scholarship for international students.'}]
        )

    def _load_qld_extra(self):
        try:
            from data.universities import qld_universities as m
            for u,ca,co,sc in [
                (m.UNIVERSITY_GRIFFITH,m.GRIFFITH_CAMPUSES,m.GRIFFITH_COURSES,m.GRIFFITH_SCHOLARSHIPS),
                (m.UNIVERSITY_JCU,m.JCU_CAMPUSES,m.JCU_COURSES,m.JCU_SCHOLARSHIPS),
                (m.UNIVERSITY_BOND,m.BOND_CAMPUSES,m.BOND_COURSES,m.BOND_SCHOLARSHIPS),
                (m.UNIVERSITY_CQU,m.CQU_CAMPUSES,m.CQU_COURSES,m.CQU_SCHOLARSHIPS),
                (m.UNIVERSITY_UNISQ,m.UNISQ_CAMPUSES,m.UNISQ_COURSES,m.UNISQ_SCHOLARSHIPS),
                (m.UNIVERSITY_UNISC,m.UNISC_CAMPUSES,m.UNISC_COURSES,m.UNISC_SCHOLARSHIPS),
            ]: yield u,ca,co,sc
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    def _load_wa(self):
        # UWA and Curtin inline
        yield (
            {'name':'University of Western Australia','short_name':'UWA','type':'public','group':'go8',
             'established':1911,'state':'Western Australia','city':'Perth',
             'description':'The University of Western Australia is a Group of Eight member ranked #72 in the world. Located on the Swan River in Crawley, UWA is known for mining engineering, medicine, business, and law.',
             'about':'UWA\'s Crawley campus overlooking the Swan River is one of Australia\'s most scenic.',
             'ranking_qs':'#72 World (QS 2025)','ranking_times':'#151–175 World (THE 2024)',
             'total_students':'25,000+','international_students':'8,000+',
             'cost_of_living':'AUD 1,800–2,600/month',
             'popular_courses':'Mining Engineering, Medicine, Business, Law, Science, IT',
             'official_website':'https://www.uwa.edu.au',
             'international_page':'https://www.uwa.edu.au/students/studyoptions/international',
             'scholarship_page':'https://www.uwa.edu.au/students/scholarships',
             'application_portal':'https://www.uwa.edu.au/students/apply'},
            [{'name':'Crawley Campus','city':'Perth','state':'Western Australia','is_main':True,
              'address':'35 Stirling Highway, Crawley WA 6009',
              'description':'UWA main campus on the Swan River, 5 km from Perth CBD.',
              'facilities':'Reid Library, Engineering, Medical School, Law School, Sports Park',
              'map_url':'https://maps.google.com/?q=University+of+Western+Australia+Crawley'}],
            [{'name':'Bachelor of Engineering (Honours)','level':'honours','field_of_study':'Engineering',
              'duration':'4 years','tuition_fee_annual':42000,'intake_months':'February',
              'academic_requirement':'ATAR 88+ or equivalent.','ielts_overall':6.5,'ielts_min_band':6.0,
              'pte_overall':58,'toefl_ibt':82,'career_outcomes':'Mining, Civil, Mechanical, Electrical Engineer',
              'description':'Engineers Australia accredited. World-renowned mining engineering.',
              'official_url':'https://www.uwa.edu.au/study/courses-and-careers/find-a-course','is_popular':True},
             {'name':'Master of Information Technology','level':'master','field_of_study':'Information Technology',
              'duration':'1.5 years','tuition_fee_annual':40000,'intake_months':'February, July',
              'academic_requirement':'Bachelor\'s in IT/CS.','ielts_overall':6.5,'ielts_min_band':6.0,
              'pte_overall':58,'toefl_ibt':82,'career_outcomes':'IT Manager, Solutions Architect, Data Scientist',
              'description':'Advanced IT with data analytics and cybersecurity focus.',
              'official_url':'https://www.uwa.edu.au/study/courses-and-careers/find-a-course'}],
            [{'name':'UWA International Excellence Scholarship','type':'merit',
              'coverage':'AUD 8,000 per year','coverage_percentage':None,
              'eligibility':'International students with outstanding results.','academic_requirement':'85%+',
              'eligible_levels':'Bachelor, Master','eligible_courses':'Most programs',
              'deadline':'31 October (February intake)',
              'official_url':'https://www.uwa.edu.au/students/scholarships',
              'description':'Annual merit scholarship for international students.'}]
        )
        yield (
            {'name':'Curtin University','short_name':'Curtin','type':'public','group':'atn',
             'established':1987,'state':'Western Australia','city':'Perth',
             'description':'Curtin University is WA\'s largest university, ATN member, ranked #185 world. Global campuses in Malaysia, Singapore, and Dubai. Known for mining engineering, nursing, business, and IT.',
             'about':'Curtin\'s Bentley campus has a vibrant international community and strong WA resources-sector links.',
             'ranking_qs':'#185 World (QS 2025)','ranking_times':'#201–250 World (THE 2024)',
             'total_students':'58,000+ (global)','international_students':'18,000+',
             'cost_of_living':'AUD 1,800–2,500/month',
             'popular_courses':'Mining Engineering, Nursing, Business, IT, Architecture',
             'official_website':'https://www.curtin.edu.au',
             'international_page':'https://www.curtin.edu.au/study/why-curtin/international-students/',
             'scholarship_page':'https://study.curtin.edu.au/scholarships-and-prizes/',
             'application_portal':'https://study.curtin.edu.au/applying/'},
            [{'name':'Bentley Campus','city':'Perth','state':'Western Australia','is_main':True,
              'address':'Kent Street, Bentley WA 6102',
              'description':'Curtin\'s main Perth campus, 7 km from CBD.',
              'facilities':'Robertson Library, Engineering Precinct, Health Sciences, Sports Centre',
              'map_url':'https://maps.google.com/?q=Curtin+University+Bentley+Perth'}],
            [{'name':'Bachelor of Information Technology','level':'bachelor','field_of_study':'Information Technology',
              'duration':'3 years','tuition_fee_annual':32800,'intake_months':'February, July',
              'academic_requirement':'Minimum ATAR 70.','ielts_overall':6.0,'ielts_min_band':6.0,
              'pte_overall':50,'toefl_ibt':60,
              'career_outcomes':'Software Developer, IT Consultant, Data Analyst, Cybersecurity Analyst',
              'description':'IT with Cloud Computing, AI, and Cybersecurity majors.',
              'official_url':'https://study.curtin.edu.au/offering/course-ug-bachelor-of-information-technology--b-scin/','is_popular':True},
             {'name':'Master of Information Technology','level':'master','field_of_study':'Information Technology',
              'duration':'2 years','tuition_fee_annual':34000,'intake_months':'February, July',
              'academic_requirement':'Bachelor\'s in IT.','ielts_overall':6.5,'ielts_min_band':6.0,
              'pte_overall':58,'toefl_ibt':79,'career_outcomes':'IT Manager, Solutions Architect, Cloud Engineer',
              'description':'Advanced IT with professional internship.',
              'official_url':'https://study.curtin.edu.au/offering/course-pg-master-of-information-technology--g-scin3/','is_popular':True}],
            [{'name':'Curtin International Scholarship','type':'merit','coverage':'25% tuition reduction',
              'coverage_percentage':25,'eligibility':'International students commencing at Curtin.',
              'academic_requirement':'75%+','eligible_levels':'Bachelor, Master','eligible_courses':'All',
              'deadline':'Intake-based','intake_deadline':True,
              'official_url':'https://study.curtin.edu.au/scholarships-and-prizes/international/',
              'description':'Curtin\'s primary merit scholarship.'}]
        )
        # ECU, Murdoch, Notre Dame from file
        try:
            from data.universities import wa_sa_nt_tas_universities as m
            for u,ca,co,sc in [
                (m.UNIVERSITY_ECU,m.ECU_CAMPUSES,m.ECU_COURSES,m.ECU_SCHOLARSHIPS),
                (m.UNIVERSITY_MURDOCH,m.MURDOCH_CAMPUSES,m.MURDOCH_COURSES,m.MURDOCH_SCHOLARSHIPS),
                (m.UNIVERSITY_NOTREDAME,m.NOTREDAME_CAMPUSES,m.NOTREDAME_COURSES,m.NOTREDAME_SCHOLARSHIPS),
            ]: yield u,ca,co,sc
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    def _load_sa(self):
        try:
            from data.universities import wa_sa_nt_tas_universities as m
            for u,ca,co,sc in [
                (m.UNIVERSITY_ADELAIDE,m.ADELAIDE_CAMPUSES,m.ADELAIDE_COURSES,m.ADELAIDE_SCHOLARSHIPS),
                (m.UNIVERSITY_FLINDERS,m.FLINDERS_CAMPUSES,m.FLINDERS_COURSES,m.FLINDERS_SCHOLARSHIPS),
                (m.UNIVERSITY_TORRENS,m.TORRENS_CAMPUSES,m.TORRENS_COURSES,m.TORRENS_SCHOLARSHIPS),
            ]: yield u,ca,co,sc
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    def _load_act(self):
        try:
            from data.universities import australian_national_university as m
            yield m.UNIVERSITY,m.CAMPUSES,m.COURSES,m.SCHOLARSHIPS
        except ImportError: pass
        try:
            from data.universities import university_of_canberra as m
            yield m.UNIVERSITY,m.CAMPUSES,m.COURSES,m.SCHOLARSHIPS
        except ImportError: pass

    def _load_nt(self):
        try:
            from data.universities import wa_sa_nt_tas_universities as m
            yield m.UNIVERSITY_CDU,m.CDU_CAMPUSES,m.CDU_COURSES,m.CDU_SCHOLARSHIPS
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    def _load_tas(self):
        try:
            from data.universities import wa_sa_nt_tas_universities as m
            yield m.UNIVERSITY_UTAS,m.UTAS_CAMPUSES,m.UTAS_COURSES,m.UTAS_SCHOLARSHIPS
        except ImportError as e:
            self.stdout.write(self.style.WARNING(f'    ⚠ {e}'))

    # ── Core seed helper ──────────────────────────────────────
    def _seed_one(self, uni_data, campuses_data, courses_data, scholarships_data):
        try:
            state = State.objects.get(name=uni_data['state'])
        except State.DoesNotExist:
            # Fallback: try matching by abbreviation (e.g. "ACT" → "Australian Capital Territory")
            try:
                state = State.objects.get(abbreviation=uni_data['state'])
            except State.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"    ✗ Unknown state: {uni_data['state']}"))
                return

        city = City.objects.filter(name=uni_data.get('city',''), state=state).first() or \
               City.objects.filter(name=uni_data.get('city','')).first()

        uni, created = University.objects.update_or_create(
            slug=slugify(uni_data['name']),
            defaults={
                'name': uni_data['name'],
                'short_name': uni_data.get('short_name', ''),
                'state': state, 'city': city,
                'institution_type': uni_data.get('type', 'public'),
                'group_affiliation': uni_data.get('group', 'none'),
                'established_year': uni_data.get('established'),
                'description': uni_data.get('description', ''),
                'about': uni_data.get('about', ''),
                'ranking_qs': uni_data.get('ranking_qs', ''),
                'ranking_times': uni_data.get('ranking_times', ''),
                'total_students': uni_data.get('total_students', ''),
                'international_students': uni_data.get('international_students', ''),
                'cost_of_living': uni_data.get('cost_of_living', ''),
                'popular_courses': uni_data.get('popular_courses', ''),
                'internship_info': uni_data.get('internship_info', ''),
                'official_website': uni_data.get('official_website', ''),
                'international_page': uni_data.get('international_page', ''),
                'scholarship_page': uni_data.get('scholarship_page', ''),
                'application_portal': uni_data.get('application_portal', ''),
                'is_featured': uni_data.get('group') in ['go8', 'atn'],
            }
        )
        icon = '✓' if created else '→'
        self.stdout.write(
            f'    {icon} {uni.name} | {len(courses_data)} courses, {len(scholarships_data)} scholarships'
        )

        for c in campuses_data:
            cc = City.objects.filter(name=c.get('city','')).first()
            cs = State.objects.filter(name=c.get('state','')).first() or state
            Campus.objects.update_or_create(
                university=uni, slug=slugify(c['name']),
                defaults={'name':c['name'],'city':cc,'state':cs,
                          'is_main':c.get('is_main',False),'address':c.get('address',''),
                          'description':c.get('description',''),'facilities':c.get('facilities',''),
                          'map_url':c.get('map_url','')}
            )

        for course in courses_data:
            Course.objects.update_or_create(
                university=uni, slug=slugify(course['name']),
                defaults={
                    'name':course['name'],'level':course.get('level','bachelor'),
                    'field_of_study':course.get('field_of_study',''),
                    'duration':course.get('duration',''),
                    'study_mode':course.get('study_mode','full_time'),
                    'tuition_fee_annual':course.get('tuition_fee_annual'),
                    'intake_months':course.get('intake_months',''),
                    'academic_requirement':course.get('academic_requirement',''),
                    'gpa_requirement':course.get('gpa_requirement',''),
                    'ielts_overall':course.get('ielts_overall'),
                    'ielts_min_band':course.get('ielts_min_band'),
                    'pte_overall':course.get('pte_overall'),
                    'toefl_ibt':course.get('toefl_ibt'),
                    'career_outcomes':course.get('career_outcomes',''),
                    'description':course.get('description',''),
                    'official_url':course.get('official_url',''),
                    'is_popular':course.get('is_popular',False),
                }
            )

        for schol in scholarships_data:
            Scholarship.objects.update_or_create(
                university=uni, slug=slugify(schol['name']),
                defaults={
                    'name':schol['name'],
                    'scholarship_type':schol.get('type','merit'),
                    'coverage':schol.get('coverage',''),
                    'coverage_percentage':schol.get('coverage_percentage'),
                    'eligibility':schol.get('eligibility',''),
                    'academic_requirement':schol.get('academic_requirement',''),
                    'eligible_courses':schol.get('eligible_courses',''),
                    'eligible_levels':schol.get('eligible_levels',''),
                    'deadline':schol.get('deadline',''),
                    'intake_deadline':schol.get('intake_deadline',False),
                    'official_url':schol.get('official_url',''),
                    'description':schol.get('description',''),
                }
            )
