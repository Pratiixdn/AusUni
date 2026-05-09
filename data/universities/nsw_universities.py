"""
NSW Universities (Additional) – Complete Data
Covers: ACU, CSU, Macquarie, SCU, UNE, University of Newcastle,
        UTS, UOW, Western Sydney University, Avondale University
Research-based, accurate as of 2025-2026
"""

# ──────────────────────────────────────────────────────────────
# AUSTRALIAN CATHOLIC UNIVERSITY (ACU)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_ACU = {
    "name": "Australian Catholic University",
    "short_name": "ACU",
    "type": "private",
    "group": "none",
    "established": 1991,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "Australian Catholic University is a publicly funded Catholic university with campuses "
        "across Australia in Sydney, Melbourne, Brisbane, Canberra, Ballarat, Adelaide, and Strathfield. "
        "ACU specialises in nursing, midwifery, education, theology, business, law, and social sciences. "
        "With 36,000+ students, it is one of the largest Catholic universities in the English-speaking world."
    ),
    "about": (
        "ACU's mission is guided by Catholic intellectual tradition and social justice values. "
        "The university is highly regarded for health and education programs, with strong clinical "
        "placement networks in hospitals and schools nationwide. International students benefit from "
        "small class sizes and strong pastoral support."
    ),
    "ranking_qs": "651–700 World (QS 2025)",
    "ranking_times": "601–800 World (THE 2024)",
    "total_students": "36,000+",
    "international_students": "5,000+",
    "cost_of_living": "AUD 2,200–3,200/month (Sydney); AUD 1,800–2,500/month (other campuses)",
    "popular_courses": "Nursing, Education, Social Work, Business, Theology, Law",
    "internship_info": (
        "ACU has placement agreements with 3,000+ hospitals, schools, and social service organisations "
        "across Australia. Nursing students undertake 800+ hours of clinical placement."
    ),
    "official_website": "https://www.acu.edu.au",
    "international_page": "https://www.acu.edu.au/about-acu/international-students",
    "scholarship_page": "https://www.acu.edu.au/study-at-acu/fees-and-scholarships/scholarships",
    "application_portal": "https://www.acu.edu.au/study-at-acu/apply",
}

ACU_CAMPUSES = [
    {
        "name": "Strathfield Campus (Sydney)",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": True,
        "address": "25A Barker Road, Strathfield NSW 2135",
        "description": "ACU's main Sydney campus in Strathfield, 14 km from Sydney CBD.",
        "facilities": "Library, Student Hub, Nursing Labs, Chapel, Cafeteria",
        "map_url": "https://maps.google.com/?q=ACU+Strathfield+Sydney",
    },
    {
        "name": "North Sydney Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "8–20 Napier Street, North Sydney NSW 2060",
        "description": "Located in Sydney's North Shore, close to the CBD and business district.",
        "facilities": "Library, Law School, Business School, Student Services",
    },
    {
        "name": "Melbourne Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "115 Victoria Parade, Fitzroy VIC 3065",
        "description": "ACU's Melbourne campus in vibrant Fitzroy, close to the CBD.",
        "facilities": "Health Sciences Labs, Education Faculty, Library",
    },
    {
        "name": "Brisbane Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": False,
        "address": "1100 Nudgee Road, Banyo QLD 4014",
        "description": "ACU Brisbane campus specialising in nursing and education.",
        "facilities": "Clinical Simulation Labs, Education Faculty, Library",
    },
]

ACU_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing / Health",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent. Health background preferred.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, ICU Nurse, Community Health Nurse, Mental Health Nurse",
        "description": (
            "ANMAC-accredited program with 800+ hours of clinical placement across ACU's hospital "
            "network. Graduates are eligible to register with AHPRA across Australia and NZ."
        ),
        "official_url": "https://www.acu.edu.au/course/bachelor-of-nursing",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Education (Primary)",
        "level": "bachelor",
        "field_of_study": "Education",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 27200,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent. Must pass national literacy and numeracy test (LANTITE).",
        "ielts_overall": 7.5,
        "ielts_min_band": 7.0,
        "pte_overall": 73,
        "toefl_ibt": 107,
        "career_outcomes": "Primary School Teacher, Curriculum Developer, Education Coordinator",
        "description": "AITSL-accredited teaching degree with 80 days of professional experience in partner schools.",
        "official_url": "https://www.acu.edu.au/course/bachelor-of-education-primary",
        "is_popular": True,
    },
    {
        "name": "Master of Nursing Practice",
        "level": "master",
        "field_of_study": "Nursing",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30800,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor of Nursing or equivalent. Registered nurse status required.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Nurse Practitioner, Clinical Nurse Specialist, Nurse Manager, Educator",
        "description": "Advanced nursing practice for experienced registered nurses seeking specialist or leadership roles.",
        "official_url": "https://www.acu.edu.au/course/master-of-nursing-practice",
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Analyst, HR Manager, Marketing Manager, Financial Analyst",
        "description": "Ethics-driven business degree with focus on social responsibility, accounting, marketing, and management.",
        "official_url": "https://www.acu.edu.au/course/bachelor-of-business",
    },
]

ACU_SCHOLARSHIPS = [
    {
        "name": "ACU International Student Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction for full program duration",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate coursework at ACU.",
        "academic_requirement": "Minimum 75% (Distinction) in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.acu.edu.au/study-at-acu/fees-and-scholarships/scholarships/international-student-scholarships",
        "description": "ACU's primary merit scholarship for outstanding international students.",
    },
    {
        "name": "ACU Health Sciences International Scholarship",
        "type": "course",
        "coverage": "AUD 5,000 one-time",
        "coverage_percentage": None,
        "eligibility": "International students enrolling in ACU nursing, midwifery, or allied health programs.",
        "academic_requirement": "Strong academic background in science",
        "eligible_levels": "Bachelor",
        "eligible_courses": "Nursing, Midwifery, Allied Health",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.acu.edu.au/study-at-acu/fees-and-scholarships/scholarships",
        "description": "Financial support for international health students at ACU.",
    },
]

# ──────────────────────────────────────────────────────────────
# CHARLES STURT UNIVERSITY (CSU)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_CSU = {
    "name": "Charles Sturt University",
    "short_name": "CSU",
    "type": "public",
    "group": "raa",
    "established": 1989,
    "state": "New South Wales",
    "city": "Bathurst",
    "description": (
        "Charles Sturt University is Australia's largest regional university, with campuses "
        "across NSW, Victoria, and the ACT in Bathurst, Wagga Wagga, Albury-Wodonga, Orange, "
        "Port Macquarie, Dubbo, and Canberra. CSU is renowned for its online learning, "
        "agriculture, nursing, policing, social work, and education programs."
    ),
    "about": (
        "CSU's regional campuses offer a unique study experience — smaller communities, "
        "lower cost of living, and strong connections to regional industries. "
        "CSU is particularly popular for policing studies (partnered with NSW Police), "
        "agriculture, veterinary science, and allied health. "
        "Its online programs attract thousands of students worldwide."
    ),
    "ranking_qs": "1001–1200 World (QS 2025)",
    "total_students": "43,000+",
    "international_students": "4,000+",
    "cost_of_living": "AUD 1,200–1,800/month",
    "popular_courses": "Nursing, Education, Agriculture, Policing, Social Work, IT",
    "internship_info": (
        "CSU has strong placement partnerships with regional hospitals, NSW Police, "
        "schools, and agricultural organisations. Nursing and education students complete "
        "mandatory professional placements."
    ),
    "official_website": "https://www.csu.edu.au",
    "international_page": "https://study.csu.edu.au/international",
    "scholarship_page": "https://study.csu.edu.au/fees-scholarships/scholarships",
    "application_portal": "https://study.csu.edu.au/apply",
}

CSU_CAMPUSES = [
    {
        "name": "Bathurst Campus",
        "city": "Bathurst",
        "state": "New South Wales",
        "is_main": True,
        "address": "Panorama Avenue, Bathurst NSW 2795",
        "description": "CSU's main campus in the historic city of Bathurst, 200 km west of Sydney.",
        "facilities": "Library, Nursing Simulation Centre, Agriculture Farm, Student Accommodation",
        "map_url": "https://maps.google.com/?q=Charles+Sturt+University+Bathurst",
    },
    {
        "name": "Wagga Wagga Campus",
        "city": "Wagga Wagga",
        "state": "New South Wales",
        "is_main": False,
        "address": "Locked Bag 588, Wagga Wagga NSW 2678",
        "description": "Major campus with veterinary science, agriculture, and business faculties.",
        "facilities": "Veterinary Teaching Hospital, Agriculture Farms, Library",
    },
]

CSU_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 27000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Hospital Nurse, Community Health Nurse",
        "description": "ANMAC-accredited nursing degree with placements in regional hospitals across NSW.",
        "official_url": "https://study.csu.edu.au/courses/bachelor-of-nursing",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Agricultural Science",
        "level": "bachelor",
        "field_of_study": "Agriculture",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 26400,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 60 or equivalent. Science background recommended.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Agricultural Scientist, Farm Manager, Agronomist, Agricultural Consultant",
        "description": "One of Australia's leading agriculture degrees. Students work on CSU's real commercial farms.",
        "official_url": "https://study.csu.edu.au/courses/bachelor-of-agricultural-science",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 26400,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "IT Manager, Network Engineer, Cybersecurity Analyst, Data Analyst",
        "description": "Flexible IT master's available fully online or on-campus. Focus on practical industry outcomes.",
        "official_url": "https://study.csu.edu.au/courses/master-of-information-technology",
    },
]

CSU_SCHOLARSHIPS = [
    {
        "name": "CSU International Student Scholarship",
        "type": "merit",
        "coverage": "20% tuition fee reduction per year",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate or postgraduate study at CSU.",
        "academic_requirement": "Minimum 70% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://study.csu.edu.au/fees-scholarships/scholarships/international",
        "description": "CSU's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# MACQUARIE UNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_MACQUARIE = {
    "name": "Macquarie University",
    "short_name": "MQ",
    "type": "public",
    "group": "none",
    "established": 1964,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "Macquarie University is a leading research university located in Sydney's "
        "Macquarie Park innovation district. Ranked in the global top 150, Macquarie "
        "is known for its strengths in actuarial studies, linguistics, finance, law, "
        "medicine, and the natural sciences. The campus features Australia's first "
        "on-campus private hospital — Macquarie University Hospital."
    ),
    "about": (
        "Macquarie's North Ryde campus, adjacent to the Macquarie Park technology corridor "
        "and directly connected to Sydney CBD by Metro, is home to a thriving research "
        "ecosystem and strong industry links. The university hosts MGSM (Macquarie Graduate "
        "School of Management) — one of Australia's top-ranked business schools."
    ),
    "ranking_qs": "#137 World (QS 2025)",
    "ranking_times": "#201–250 World (THE 2024)",
    "total_students": "44,000+",
    "international_students": "18,000+",
    "cost_of_living": "AUD 2,200–3,200/month",
    "popular_courses": "Actuarial Studies, Finance, Law, Medicine, Linguistics, IT",
    "internship_info": (
        "Macquarie has strong industry connections through Macquarie Park's tech and finance hub. "
        "Partners include Optus, Foxtel, Cochlear, and major banks. "
        "The Macquarie University Hospital provides clinical placement for medical students."
    ),
    "official_website": "https://www.mq.edu.au",
    "international_page": "https://www.mq.edu.au/research/phd-and-research-degrees/how-to-apply/international-applicants",
    "scholarship_page": "https://www.mq.edu.au/study/admissions/scholarships",
    "application_portal": "https://www.mq.edu.au/study/admissions/how-to-apply",
}

MACQUARIE_CAMPUSES = [
    {
        "name": "North Ryde Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": True,
        "address": "Balaclava Road, North Ryde NSW 2109",
        "description": "Macquarie's main campus in Sydney's innovation district, served by Macquarie University Metro Station.",
        "facilities": "Macquarie University Hospital, Library, Sport & Aquatic Centre, Campus Hub, Student Housing",
        "map_url": "https://maps.google.com/?q=Macquarie+University+North+Ryde",
    },
]

MACQUARIE_COURSES = [
    {
        "name": "Bachelor of Actuarial Studies",
        "level": "bachelor",
        "field_of_study": "Actuarial Studies / Mathematics",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 40600,
        "intake_months": "February, July",
        "academic_requirement": "ATAR 95+ or equivalent. Excellent Mathematics required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 83,
        "career_outcomes": "Actuary, Risk Analyst, Investment Manager, Insurance Specialist, Data Scientist",
        "description": "One of the world's top-ranked actuarial programs. Accredited by the Institute of Actuaries of Australia.",
        "official_url": "https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-actuarial-studies",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 37800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 80 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 83,
        "career_outcomes": "Software Engineer, Cybersecurity Analyst, Data Scientist, IT Consultant",
        "description": "Industry-aligned IT degree with a strong focus on cybersecurity, data science, and software engineering.",
        "official_url": "https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Data Science",
        "level": "master",
        "field_of_study": "Data Science",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 42200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT, Computer Science, Maths, or Statistics with minimum 65%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 83,
        "career_outcomes": "Data Scientist, Machine Learning Engineer, Business Intelligence Analyst, AI Researcher",
        "description": "Advanced data science degree drawing on Macquarie's strengths in statistics, AI, and computing.",
        "official_url": "https://www.mq.edu.au/study/find-a-course/courses/master-of-data-science",
        "is_popular": True,
    },
    {
        "name": "Master of International Business",
        "level": "master",
        "field_of_study": "Business / International Business",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 39200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree in any field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 83,
        "career_outcomes": "International Trade Manager, Global Marketing Director, Export Manager, Consultant",
        "description": "AACSB-accredited program at MGSM. Focus on global strategy, cross-cultural management, and international trade.",
        "official_url": "https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business",
    },
]

MACQUARIE_SCHOLARSHIPS = [
    {
        "name": "Macquarie University International Scholarship",
        "type": "merit",
        "coverage": "20%–30% tuition reduction (tiered by merit)",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study.",
        "academic_requirement": "Minimum 80% in previous qualification for 20%; 85%+ for 30%",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatically assessed",
        "intake_deadline": True,
        "official_url": "https://www.mq.edu.au/study/admissions/scholarships/international",
        "description": "Tiered merit scholarship providing 20–30% tuition reduction based on academic excellence.",
    },
]

# ──────────────────────────────────────────────────────────────
# SOUTHERN CROSS UNIVERSITY (SCU)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_SCU = {
    "name": "Southern Cross University",
    "short_name": "SCU",
    "type": "public",
    "group": "raa",
    "established": 1994,
    "state": "New South Wales",
    "city": "Lismore",
    "description": (
        "Southern Cross University is an innovative regional university with campuses on "
        "the NSW and Queensland Gold Coast border, including Gold Coast, Lismore, and Coffs Harbour. "
        "SCU uses its unique Accelerated Model — trimesters of 6-week terms — letting students "
        "complete bachelor degrees in 2 years and master's in 1 year."
    ),
    "about": (
        "SCU's Gold Coast campus is a modern, purpose-built facility right next to the beaches "
        "and tourism industry, making it ideal for business, hospitality, and tourism students. "
        "The university is also known for sustainability, marine science, and health sciences."
    ),
    "ranking_qs": "1001–1200 World (QS 2025)",
    "total_students": "22,000+",
    "international_students": "6,000+",
    "cost_of_living": "AUD 1,600–2,200/month",
    "popular_courses": "Business, Nursing, Education, Tourism, Environmental Science, IT",
    "official_website": "https://www.scu.edu.au",
    "international_page": "https://www.scu.edu.au/international/",
    "scholarship_page": "https://www.scu.edu.au/scholarships/",
    "application_portal": "https://www.scu.edu.au/apply/",
}

SCU_CAMPUSES = [
    {
        "name": "Gold Coast Campus",
        "city": "Gold Coast",
        "state": "Queensland",
        "is_main": True,
        "address": "Cnr Smith Street & production Avenue, Bilinga QLD 4225",
        "description": "Stunning beachside campus near Gold Coast Airport. Modern facilities with ocean views.",
        "facilities": "Library, Industry Labs, Student Hub, Health Clinic, Beach Access",
        "map_url": "https://maps.google.com/?q=Southern+Cross+University+Gold+Coast",
    },
    {
        "name": "Lismore Campus",
        "city": "Lismore",
        "state": "New South Wales",
        "is_main": False,
        "address": "Military Road, Lismore NSW 2480",
        "description": "SCU's original campus in the Northern Rivers region of NSW.",
        "facilities": "Library, Science Labs, Environmental Research Centre, Student Housing",
    },
]

SCU_COURSES = [
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "2 years (Accelerated Model)",
        "study_mode": "full_time",
        "tuition_fee_annual": 28000,
        "intake_months": "February, May, September",
        "academic_requirement": "Minimum ATAR 62 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 5.5,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Business Manager, Marketing Specialist, HR Coordinator, Project Manager",
        "description": "Complete in 2 years using SCU's 6-week accelerated model. Three intakes per year.",
        "official_url": "https://www.scu.edu.au/study-at-scu/courses/business/bachelor-of-business/",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "1 year (Accelerated Model)",
        "study_mode": "full_time",
        "tuition_fee_annual": 31200,
        "intake_months": "February, May, September",
        "academic_requirement": "Bachelor's degree + minimum 3 years work experience.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Senior Manager, Director, Entrepreneur, Business Consultant",
        "description": "Australia's fastest MBA — complete in just 1 year using SCU's accelerated 6-week term model.",
        "official_url": "https://www.scu.edu.au/study-at-scu/courses/business/master-of-business-administration/",
        "is_popular": True,
    },
]

SCU_SCHOLARSHIPS = [
    {
        "name": "SCU International Merit Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.scu.edu.au/scholarships/international/",
        "description": "SCU's merit scholarship for high-achieving international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF NEW ENGLAND (UNE)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_UNE = {
    "name": "University of New England",
    "short_name": "UNE",
    "type": "public",
    "group": "raa",
    "established": 1954,
    "state": "New South Wales",
    "city": "Armidale",
    "description": (
        "The University of New England is Australia's oldest rural university, founded in 1954 "
        "in Armidale, a university town in the New England tablelands of NSW. "
        "UNE is Australia's leading provider of distance/online education and "
        "is known for agriculture, law, veterinary science, and the arts. "
        "Over 70% of UNE students study externally (online)."
    ),
    "about": (
        "UNE's beautiful sandstone Armidale campus offers a true university town experience. "
        "With 26,000 students, the vast majority studying online, UNE has decades of expertise "
        "in flexible distance education. Armidale is one of Australia's highest-altitude cities "
        "with a cool climate and strong arts and heritage scene."
    ),
    "ranking_qs": "1001–1200 World (QS 2025)",
    "total_students": "26,000+",
    "international_students": "3,000+",
    "cost_of_living": "AUD 1,100–1,500/month",
    "popular_courses": "Law, Agriculture, Education, Veterinary Science, Arts, Business",
    "official_website": "https://www.une.edu.au",
    "international_page": "https://www.une.edu.au/study/international",
    "scholarship_page": "https://www.une.edu.au/study/scholarships",
    "application_portal": "https://www.une.edu.au/study/apply",
}

UNE_CAMPUSES = [
    {
        "name": "Armidale Campus",
        "city": "Armidale",
        "state": "New South Wales",
        "is_main": True,
        "address": "University Road, Armidale NSW 2351",
        "description": "UNE's beautiful sandstone main campus in Armidale, 570 km north of Sydney.",
        "facilities": "Dixson Library, Veterinary Science Complex, Agricultural Research Farm, Student Accommodation",
        "map_url": "https://maps.google.com/?q=University+of+New+England+Armidale",
    },
]

UNE_COURSES = [
    {
        "name": "Bachelor of Laws (LLB)",
        "level": "bachelor",
        "field_of_study": "Law",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 75 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Solicitor, Barrister, Legal Counsel, Magistrate, Policy Officer",
        "description": "One of Australia's most flexible law degrees – can be studied fully online or on-campus.",
        "official_url": "https://www.une.edu.au/study/courses/bachelor-of-laws",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Agriculture",
        "level": "bachelor",
        "field_of_study": "Agriculture",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 24000,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Farm Manager, Agricultural Scientist, Agronomist, Agricultural Advisor",
        "description": "Practical agriculture degree with working farm experience at UNE's research farms.",
        "official_url": "https://www.une.edu.au/study/courses/bachelor-of-agriculture",
        "is_popular": True,
    },
]

UNE_SCHOLARSHIPS = [
    {
        "name": "UNE International Student Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction for full program",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at UNE.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.une.edu.au/study/scholarships/international",
        "description": "UNE's main merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF NEWCASTLE
# ──────────────────────────────────────────────────────────────
UNIVERSITY_NEWCASTLE = {
    "name": "University of Newcastle",
    "short_name": "UON",
    "type": "public",
    "group": "irua",
    "established": 1965,
    "state": "New South Wales",
    "city": "Newcastle",
    "description": (
        "The University of Newcastle is a research-intensive university ranked in the global "
        "top 200 and a member of the Innovative Research Universities (IRU) group. "
        "Located in Newcastle — Australia's seventh-largest city — UON is known for "
        "engineering, medicine, education, business, and architecture. "
        "The university has campuses in Newcastle (Callaghan), Central Coast, Sydney, and Singapore."
    ),
    "about": (
        "Newcastle is a vibrant coastal city with a lower cost of living than Sydney, "
        "beautiful beaches, and a growing tech and creative economy. UON's Callaghan "
        "campus is a green, sustainable precinct with strong research institutes. "
        "The university has produced Rhodes Scholars and leads research in areas "
        "including cancer, coal seam gas, and sustainable engineering."
    ),
    "ranking_qs": "#197 World (QS 2025)",
    "ranking_times": "#251–300 World (THE 2024)",
    "total_students": "37,000+",
    "international_students": "9,000+",
    "cost_of_living": "AUD 1,500–2,200/month",
    "popular_courses": "Engineering, Medicine, Business, Architecture, Education, IT",
    "internship_info": (
        "UON has industry partnerships with Hunter Valley mining, defence (HMAS Newcastle), "
        "John Hunter Hospital, and BHP. The NeW Space campus in Newcastle CBD provides "
        "co-working spaces and industry connection opportunities."
    ),
    "official_website": "https://www.newcastle.edu.au",
    "international_page": "https://www.newcastle.edu.au/study/international",
    "scholarship_page": "https://www.newcastle.edu.au/study/scholarships",
    "application_portal": "https://www.newcastle.edu.au/study/apply",
}

NEWCASTLE_CAMPUSES = [
    {
        "name": "Callaghan Campus",
        "city": "Newcastle",
        "state": "New South Wales",
        "is_main": True,
        "address": "University Drive, Callaghan NSW 2308",
        "description": "UON's main campus, 10 km from Newcastle CBD. A green 200-hectare campus.",
        "facilities": "Auchmuty Library, Engineering Precinct, Medical School, Sport Facilities, Student Accommodation",
        "map_url": "https://maps.google.com/?q=University+of+Newcastle+Callaghan",
    },
    {
        "name": "NeW Space (City Campus)",
        "city": "Newcastle",
        "state": "New South Wales",
        "is_main": False,
        "address": "55 Auckland Street, Newcastle NSW 2300",
        "description": "Modern CBD campus with co-working spaces and business/architecture programs.",
        "facilities": "Design Studios, Co-working Spaces, Industry Labs",
    },
    {
        "name": "Central Coast Campus",
        "city": "Ourimbah",
        "state": "New South Wales",
        "is_main": False,
        "address": "10 Chittaway Road, Ourimbah NSW 2258",
        "description": "Serves the growing Central Coast region with nursing, business, and arts programs.",
        "facilities": "Library, Nursing Labs, Computer Labs",
    },
]

NEWCASTLE_COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 38500,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 80 or equivalent. Strong Mathematics and Sciences.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Civil, Mechanical, Electrical, Chemical, Environmental Engineer",
        "description": "Engineers Australia accredited. Strong ties to Hunter Valley mining, defence, and infrastructure industries.",
        "official_url": "https://www.newcastle.edu.au/study/undergraduate/engineering",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 72 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, Data Analyst, Cybersecurity Specialist, IT Consultant",
        "description": "Practical IT degree with industry placement. Majors in cybersecurity, data analytics, and software development.",
        "official_url": "https://www.newcastle.edu.au/study/undergraduate/information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 35200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Solutions Architect, Data Scientist, AI Engineer",
        "description": "Advanced IT degree with research and industry project components.",
        "official_url": "https://www.newcastle.edu.au/study/postgraduate/information-technology",
    },
]

NEWCASTLE_SCHOLARSHIPS = [
    {
        "name": "UON International Academic Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction for program duration",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate at UON.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic consideration",
        "intake_deadline": True,
        "official_url": "https://www.newcastle.edu.au/study/scholarships/international",
        "description": "UON's main merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF TECHNOLOGY SYDNEY (UTS)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_UTS = {
    "name": "University of Technology Sydney",
    "short_name": "UTS",
    "type": "public",
    "group": "atn",
    "established": 1988,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "UTS is a leading Australian Technology Network university ranked in the global top 140. "
        "Located in Sydney's CBD adjacent to Central Station, UTS is renowned for its "
        "industry-focused education, cutting-edge campus design by Frank Gehry (the Dr Chau Chak Wing Building), "
        "and strong connections to Sydney's technology, business, and creative sectors. "
        "Over 47,000 students from 130+ countries choose UTS."
    ),
    "about": (
        "UTS's Tech Park campus in Ultimo/Sydney CBD puts students at the heart of Australia's "
        "largest city and technology ecosystem. Graduates are highly regarded by employers — "
        "UTS consistently ranks among Australia's top graduate employment universities. "
        "The university is especially strong in engineering, computer science, business, "
        "design, architecture, and communication."
    ),
    "ranking_qs": "#137 World (QS 2025)",
    "ranking_times": "#201–250 World (THE 2024)",
    "total_students": "47,000+",
    "international_students": "20,000+",
    "cost_of_living": "AUD 2,200–3,500/month",
    "popular_courses": "Engineering, Computer Science, Business, Design, Architecture, Communication",
    "internship_info": (
        "UTS has exceptional industry connections via UTS Industry Connect, "
        "with partners including Atlassian, Google, Cochlear, PwC, and the NSW Government. "
        "The UTS Startups program and innovation hub support entrepreneurship."
    ),
    "official_website": "https://www.uts.edu.au",
    "international_page": "https://www.uts.edu.au/study/international",
    "scholarship_page": "https://www.uts.edu.au/study/scholarships",
    "application_portal": "https://www.uts.edu.au/study/applying-uts",
}

UTS_CAMPUSES = [
    {
        "name": "City Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": True,
        "address": "15 Broadway, Ultimo NSW 2007",
        "description": "UTS's iconic City campus in Sydney CBD/Ultimo, adjacent to Central Station. Features the Frank Gehry-designed Dr Chau Chak Wing Building.",
        "facilities": "UTS Library, Dr Chau Chak Wing Building, UTS Tech Lab, Student Union, Student Housing",
        "map_url": "https://maps.google.com/?q=UTS+University+Technology+Sydney",
    },
    {
        "name": "Haymarket Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "Haymarket NSW 2000",
        "description": "Additional facilities in Sydney's Haymarket precinct.",
        "facilities": "UTS Insearch, Language Centre",
    },
]

UTS_COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 40200,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 85 or equivalent. Mathematics required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Civil, Mechanical, Electrical, Software, Mechatronics Engineer",
        "description": "Engineers Australia accredited. Strong emphasis on real-world industry projects and innovation.",
        "official_url": "https://www.uts.edu.au/study/engineering",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Science in Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 36800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 85 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Engineer, Data Scientist, Cybersecurity Analyst, AI Developer",
        "description": "Industry-led IT degree with sub-majors in AI, cybersecurity, data analytics, and enterprise systems.",
        "official_url": "https://www.uts.edu.au/study/information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 40800,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT/Engineering with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Solutions Architect, Data Scientist, Cloud Engineer",
        "description": "Advanced IT program with industry capstone project. Strong AI and machine learning focus.",
        "official_url": "https://www.uts.edu.au/study/information-technology/postgraduate",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 35600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 82 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Analyst, Financial Analyst, Marketing Manager, HR Manager",
        "description": "AACSB-accredited UTS Business School. Strong industry focus with sub-majors in Finance, Marketing, Analytics, and Management.",
        "official_url": "https://www.uts.edu.au/study/business",
        "is_popular": True,
    },
]

UTS_SCHOLARSHIPS = [
    {
        "name": "UTS International Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction for program duration",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate coursework at UTS.",
        "academic_requirement": "Minimum 80% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatically assessed",
        "intake_deadline": True,
        "official_url": "https://www.uts.edu.au/study/scholarships/international-scholarships",
        "description": "UTS's main merit scholarship for international students offering 25% tuition reduction.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF WOLLONGONG (UOW)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_UOW = {
    "name": "University of Wollongong",
    "short_name": "UOW",
    "type": "public",
    "group": "irua",
    "established": 1975,
    "state": "New South Wales",
    "city": "Wollongong",
    "description": (
        "The University of Wollongong is a globally ranked research university and member of the "
        "Innovative Research Universities (IRU) group. Located just 80 km south of Sydney, "
        "UOW is consistently ranked in the world's top 200 and is highly regarded for "
        "engineering, business, computer science, and health. "
        "It operates the UOWD campus in Dubai and has partnerships worldwide."
    ),
    "about": (
        "Wollongong offers stunning coastal scenery and a lower cost of living than Sydney, "
        "while still being accessible to Sydney by train in about 90 minutes. "
        "UOW's Innovation Campus is a thriving research and business hub. "
        "The university produces some of Australia's top engineering and business graduates."
    ),
    "ranking_qs": "#185 World (QS 2025)",
    "ranking_times": "#251–300 World (THE 2024)",
    "total_students": "30,000+",
    "international_students": "10,000+",
    "cost_of_living": "AUD 1,400–1,900/month",
    "popular_courses": "Engineering, Computer Science, Business, Health, Education, Psychology",
    "official_website": "https://www.uow.edu.au",
    "international_page": "https://www.uow.edu.au/study/international/",
    "scholarship_page": "https://www.uow.edu.au/study/scholarships/",
    "application_portal": "https://www.uow.edu.au/study/apply/",
}

UOW_CAMPUSES = [
    {
        "name": "Wollongong Campus",
        "city": "Wollongong",
        "state": "New South Wales",
        "is_main": True,
        "address": "Northfields Avenue, Wollongong NSW 2522",
        "description": "UOW's main campus in the coastal city of Wollongong, south of Sydney.",
        "facilities": "Library, Innovation Campus, Engineering Precinct, Health & Behavioural Sciences, Student Housing",
        "map_url": "https://maps.google.com/?q=University+of+Wollongong",
    },
    {
        "name": "Sydney Business School",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "Level 29, 321 Kent Street, Sydney NSW 2000",
        "description": "UOW's Sydney CBD campus for postgraduate business programs.",
        "facilities": "Business School, Conference Rooms, Student Lounge",
    },
]

UOW_COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 37000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 80 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Civil, Mechanical, Electrical, Materials, Environmental Engineer",
        "description": "Engineers Australia accredited. Strong industry links to BlueScope Steel and local mining companies.",
        "official_url": "https://www.uow.edu.au/study/courses/",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Computer Science",
        "level": "bachelor",
        "field_of_study": "Computer Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 35400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 78 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Engineer, Cybersecurity Analyst, Data Scientist, AI Developer",
        "description": "Flexible CS degree with majors in cybersecurity, AI, data science, and software engineering.",
        "official_url": "https://www.uow.edu.au/study/courses/",
        "is_popular": True,
    },
]

UOW_SCHOLARSHIPS = [
    {
        "name": "UOW Principal's Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction for full program",
        "coverage_percentage": 25,
        "eligibility": "High-achieving international students commencing undergraduate or postgraduate study.",
        "academic_requirement": "Minimum 80% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.uow.edu.au/study/scholarships/international/",
        "description": "UOW's primary merit scholarship for outstanding international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# WESTERN SYDNEY UNIVERSITY (WSU)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_WSU = {
    "name": "Western Sydney University",
    "short_name": "WSU",
    "type": "public",
    "group": "irua",
    "established": 1989,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "Western Sydney University is a multi-campus university serving Greater Western Sydney, "
        "one of Australia's fastest-growing regions. WSU has campuses in Bankstown, Campbelltown, "
        "Hawkesbury, Parramatta, Penrith, and Sydney CBD. With over 45,000 students, WSU is known "
        "for health sciences, engineering, business, law, and nursing, with a strong focus on "
        "social inclusion and industry partnerships in Western Sydney."
    ),
    "about": (
        "WSU's Parramatta City campus, opened in 2023, is a stunning addition to Sydney's "
        "second CBD. The university has strong ties to the Western Sydney Airport precinct "
        "(Aerotropolis), healthcare hubs at Westmead, and the STEM Industries corridor. "
        "WSU graduates are known for their practical skills and community engagement."
    ),
    "ranking_qs": "751–800 World (QS 2025)",
    "total_students": "45,000+",
    "international_students": "11,000+",
    "cost_of_living": "AUD 1,800–2,500/month",
    "popular_courses": "Nursing, Business, Engineering, IT, Law, Social Work, Physiotherapy",
    "official_website": "https://www.westernsydney.edu.au",
    "international_page": "https://www.westernsydney.edu.au/international",
    "scholarship_page": "https://www.westernsydney.edu.au/scholarships",
    "application_portal": "https://www.westernsydney.edu.au/apply",
}

WSU_CAMPUSES = [
    {
        "name": "Parramatta City Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": True,
        "address": "169 Macquarie Street, Parramatta NSW 2150",
        "description": "Modern urban campus in Parramatta CBD – Sydney's second city.",
        "facilities": "Library, Business School, Innovation Hub, Student Services",
        "map_url": "https://maps.google.com/?q=Western+Sydney+University+Parramatta",
    },
    {
        "name": "Campbelltown Campus",
        "city": "Campbelltown",
        "state": "New South Wales",
        "is_main": False,
        "address": "Narellan Road, Campbelltown NSW 2560",
        "description": "Major health and education campus in South-Western Sydney.",
        "facilities": "Health Sciences Labs, Simulation Centre, Library",
    },
    {
        "name": "Penrith Campus",
        "city": "Penrith",
        "state": "New South Wales",
        "is_main": False,
        "address": "Locked Bag 1797, Penrith NSW 2751",
        "description": "Engineering and computing-focused campus near Western Sydney's growing tech corridor.",
        "facilities": "Engineering Labs, MARCS Institute, Student Hub",
    },
]

WSU_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Hospital Nurse, Community Health Nurse, Aged Care Nurse",
        "description": "ANMAC-accredited. Clinical placements at Westmead, Blacktown, and other major Western Sydney hospitals.",
        "official_url": "https://www.westernsydney.edu.au/bachelor-of-nursing",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Systems and Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 29600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Systems Analyst, IT Consultant, Data Analyst, Software Developer",
        "description": "Practical IT degree with strong Western Sydney industry placement network.",
        "official_url": "https://www.westernsydney.edu.au/bachelor-of-information-systems-technology",
        "is_popular": True,
    },
]

WSU_SCHOLARSHIPS = [
    {
        "name": "WSU International Merit Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at WSU.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.westernsydney.edu.au/scholarships/international",
        "description": "WSU's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# AVONDALE UNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_AVONDALE = {
    "name": "Avondale University",
    "short_name": "Avondale",
    "type": "private",
    "group": "none",
    "established": 1897,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "Avondale University is a small, faith-based university in Cooranbong, NSW, "
        "affiliated with the Seventh-day Adventist Church. Founded in 1897, it is one "
        "of Australia's oldest private universities, offering nursing, education, theology, "
        "arts, and business programs in a peaceful rural setting near Lake Macquarie."
    ),
    "about": (
        "Avondale's beautiful 300-hectare campus at Cooranbong offers a close-knit "
        "academic community. The university is known for its personal care, "
        "small class sizes, and strong nursing program."
    ),
    "total_students": "1,500+",
    "international_students": "200+",
    "cost_of_living": "AUD 1,400–1,800/month",
    "popular_courses": "Nursing, Education, Theology, Business, Arts",
    "official_website": "https://www.avondale.edu.au",
    "international_page": "https://www.avondale.edu.au/study/international-students/",
    "scholarship_page": "https://www.avondale.edu.au/study/scholarships/",
    "application_portal": "https://www.avondale.edu.au/apply/",
}

AVONDALE_CAMPUSES = [
    {
        "name": "Cooranbong Campus",
        "city": "Newcastle",
        "state": "New South Wales",
        "is_main": True,
        "address": "582 Freemans Drive, Cooranbong NSW 2265",
        "description": "Peaceful 300-hectare campus in Cooranbong, near Lake Macquarie and Newcastle.",
        "facilities": "Nursing Labs, Library, Chapel, Student Housing, Farm",
        "map_url": "https://maps.google.com/?q=Avondale+University+Cooranbong",
    },
]

AVONDALE_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 27200,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Hospital Nurse, Community Health Nurse",
        "description": "ANMAC-accredited nursing program in a caring, faith-based environment with personalised learning.",
        "official_url": "https://www.avondale.edu.au/course/bachelor-of-nursing/",
    },
]

AVONDALE_SCHOLARSHIPS = [
    {
        "name": "Avondale University International Scholarship",
        "type": "merit",
        "coverage": "20% tuition reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing an Avondale undergraduate program.",
        "academic_requirement": "Good academic standing",
        "eligible_levels": "Bachelor",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.avondale.edu.au/study/scholarships/",
        "description": "Merit scholarship for international students at Avondale.",
    },
]
