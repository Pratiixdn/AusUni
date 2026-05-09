"""
University of Canberra – Complete Data
Research-based, accurate as of 2024
Official source: https://www.canberra.edu.au/
"""

UNIVERSITY = {
    "name": "University of Canberra",
    "short_name": "UC",
    "type": "public",
    "group": "none",
    "established": 1990,
    "state": "ACT",
    "city": "Canberra",
    "description": (
        "The University of Canberra is a dynamic public university located in Bruce, ACT. "
        "Renowned for its practice-based learning, strong industry connections, and student-centred approach, "
        "UC consistently ranks among Australia's top young universities. "
        "With over 13,000 students including a significant international cohort, UC offers industry-linked "
        "programs across health, business, IT, education, law, science, and creative arts."
    ),
    "about": (
        "UC offers practical, career-focused education with built-in industry placements. "
        "The Bruce campus is a vibrant hub with modern facilities including the UC Health Hub – "
        "a teaching hospital – and strong partnerships with ACT Government and industry. "
        "Canberra provides unmatched access to government departments, embassies, and national institutions, "
        "making it ideal for politics, law, policy, and public administration students."
    ),
    "ranking_qs": "601–650 World (QS 2025)",
    "ranking_times": "351–400 (THE Young University Rankings 2024)",
    "total_students": "13,000+",
    "international_students": "3,000+",
    "cost_of_living": "AUD 1,800–2,400/month",
    "popular_courses": "Information Technology, Nursing, Business, Engineering, Law",
    "internship_info": (
        "UC is renowned for industry placements built into degrees. "
        "Partnerships with ACT Government, major hospitals, NBN Co, and Canberra-based companies "
        "provide students with real-world experience. The UC Health Hub offers clinical placements "
        "for nursing and health students."
    ),
    "official_website": "https://www.canberra.edu.au",
    "international_page": "https://www.canberra.edu.au/future-students/international",
    "scholarship_page": "https://www.canberra.edu.au/future-students/scholarships",
    "application_portal": "https://www.canberra.edu.au/future-students/apply",
}

CAMPUSES = [
    {
        "name": "Bruce Campus",
        "city": "Canberra",
        "state": "ACT",
        "is_main": True,
        "address": "University Drive, Bruce ACT 2617, Australia",
        "description": (
            "The main campus of UC located in Bruce, a suburb of Canberra. "
            "It features the UC Health Hub, UC Library, modern lecture theatres, "
            "student accommodation, cafés, sports facilities, and a campus store. "
            "The campus is well-connected by public transport."
        ),
        "facilities": "Library, Health Hub, Sports Centre, Student Housing, Cafés, Bookshop, Career Hub",
        "map_url": "https://maps.google.com/?q=University+of+Canberra+Bruce+ACT",
    },
]

COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent. Minimum 60% in relevant diploma/foundation.",
        "gpa_requirement": "Minimum 3.0/4.0 GPA for transfer students",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": (
            "Software Developer, Systems Analyst, Network Engineer, Cybersecurity Analyst, "
            "IT Project Manager, Database Administrator, Business Analyst"
        ),
        "description": (
            "UC's Bachelor of IT gives you the technical skills and practical experience "
            "needed for a career in technology. You'll complete an industry placement and "
            "choose from majors including Cybersecurity, Data Analytics, and Software Development."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-BIT",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent foundation/diploma qualification.",
        "gpa_requirement": "2.7/4.0 for advanced standing",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": (
            "Business Analyst, Marketing Manager, HR Manager, Financial Analyst, "
            "Management Consultant, Entrepreneur"
        ),
        "description": (
            "A versatile business degree with majors in Accounting, Finance, Marketing, "
            "Human Resource Management, and Management. Industry placements included."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-BBus",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Health / Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33000,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 75 or equivalent. Health background preferred.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": (
            "Registered Nurse (RN), Hospital Nurse, Community Health Nurse, "
            "Mental Health Nurse, Aged Care Nurse"
        ),
        "description": (
            "Accredited by ANMAC. Clinical placements at UC Health Hub and affiliated hospitals. "
            "Graduates are eligible to register with AHPRA."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-BNurs",
    },
    {
        "name": "Bachelor of Laws (LLB)",
        "level": "bachelor",
        "field_of_study": "Law",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33500,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 80 or equivalent; strong English foundation required.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": (
            "Solicitor, Barrister, Legal Counsel, Policy Officer, Government Lawyer, "
            "Compliance Officer, Judge's Associate"
        ),
        "description": (
            "One of Australia's leading law schools, benefiting from Canberra's unique position "
            "as the nation's capital. Students gain access to the High Court of Australia, "
            "federal government departments, and prominent law firms."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-LLB",
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree in IT or related field with minimum 60% average.",
        "gpa_requirement": "2.5/4.0 minimum",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": (
            "IT Manager, Senior Developer, Solutions Architect, Cybersecurity Lead, "
            "Data Scientist, Cloud Architect"
        ),
        "description": (
            "Advanced IT studies with specialisations in Cybersecurity, Data Analytics, "
            "and Software Engineering. Research and coursework pathways available."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-MIT",
        "is_popular": True,
    },
    {
        "name": "Master of Professional Accounting",
        "level": "master",
        "field_of_study": "Accounting / Finance",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31500,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in any discipline. Non-accounting backgrounds welcome.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": (
            "Certified Public Accountant (CPA), Chartered Accountant (CA), "
            "Financial Advisor, Tax Consultant, Auditor, CFO"
        ),
        "description": (
            "Accredited by CPA Australia and Chartered Accountants Australia and New Zealand (CAANZ). "
            "Provides pathway to professional accounting certification. Open to any undergraduate background."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-MPA",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 34000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree + minimum 2 years work experience preferred.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": (
            "Senior Manager, Director, CEO, Business Consultant, Entrepreneur, "
            "Project Manager, Operations Manager"
        ),
        "description": (
            "UC's MBA combines business strategy with leadership, entrepreneurship, and innovation. "
            "Strong connections to Canberra's government and business sector."
        ),
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-MBA",
    },
    {
        "name": "Graduate Certificate in Information Technology",
        "level": "graduate_cert",
        "field_of_study": "Information Technology",
        "duration": "6 months",
        "study_mode": "full_time",
        "tuition_fee_annual": 17500,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree in any field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "IT Business Analyst, Entry-level Developer, IT Support Specialist",
        "description": "Fast-track IT qualification ideal for career changers. Pathway to Master of IT.",
        "official_url": "https://www.canberra.edu.au/future-students/study-at-uc/find-a-course/detail?id=UC-GradCertIT",
    },
]

SCHOLARSHIPS = [
    {
        "name": "UC International Merit Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction per semester",
        "coverage_percentage": 25,
        "eligibility": (
            "International students commencing an undergraduate or postgraduate coursework degree at UC. "
            "Must demonstrate strong academic achievement."
        ),
        "academic_requirement": "Minimum 75% (Distinction average) in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All courses",
        "deadline": "Intake-based – apply with course application",
        "intake_deadline": True,
        "official_url": "https://www.canberra.edu.au/future-students/scholarships/international",
        "description": "UC's flagship merit scholarship for international students offering 25% tuition reduction.",
    },
    {
        "name": "UC Vice-Chancellor's International Scholarship",
        "type": "merit",
        "coverage": "50% tuition fee reduction for full program duration",
        "coverage_percentage": 50,
        "eligibility": (
            "Highly meritorious international students with exceptional academic results. "
            "Competitive selection based on academic record."
        ),
        "academic_requirement": "Minimum 85% (High Distinction average) in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All courses",
        "deadline": "30 November (for February intake); 30 April (for July intake)",
        "official_url": "https://www.canberra.edu.au/future-students/scholarships/international",
        "description": "The most prestigious UC scholarship for international students, covering half of tuition.",
    },
    {
        "name": "UC Health Scholarship",
        "type": "course",
        "coverage": "AUD 5,000 one-time payment",
        "coverage_percentage": None,
        "eligibility": "International students enrolling in UC health programs (Nursing, Physiotherapy, etc.)",
        "academic_requirement": "Strong academic background in science/health",
        "eligible_levels": "Bachelor",
        "eligible_courses": "Nursing, Physiotherapy, Health Science",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.canberra.edu.au/future-students/scholarships/international",
        "description": "Supports international health students with a one-time financial contribution.",
    },
]
