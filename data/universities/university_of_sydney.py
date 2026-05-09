"""
University of Sydney – Complete Data
Research-based, accurate as of 2024
Official source: https://www.sydney.edu.au/
"""

UNIVERSITY = {
    "name": "University of Sydney",
    "short_name": "USYD",
    "type": "public",
    "group": "go8",
    "established": 1850,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "The University of Sydney, founded in 1850, is Australia's first university and one of the "
        "world's leading research institutions. A proud member of the Group of Eight (Go8), USYD "
        "consistently ranks among the top 50 universities worldwide. Located in the heart of Sydney, "
        "the university offers over 350 undergraduate and 500 postgraduate programs across 9 faculties."
    ),
    "about": (
        "USYD's iconic sandstone campus in Camperdown is one of the most beautiful university campuses "
        "in the world. Students benefit from world-class research facilities, a prestigious alumni network "
        "(including former Australian Prime Ministers), and unparalleled access to Sydney's dynamic business, "
        "finance, and cultural scene. The university has a strong global reputation and its degrees are "
        "recognised by employers around the world."
    ),
    "ranking_qs": "#18 World (QS 2025)",
    "ranking_times": "#54 World (THE 2024)",
    "total_students": "75,000+",
    "international_students": "25,000+",
    "cost_of_living": "AUD 2,200–3,500/month",
    "popular_courses": "Medicine, Law, Engineering, Business, Computer Science, Architecture",
    "internship_info": (
        "USYD has extensive industry partnerships with major Australian and multinational companies. "
        "The Careers Centre facilitates placements, internships, and graduate programs. "
        "Sydney's position as Australia's business capital provides access to finance, consulting, "
        "technology, and media industries."
    ),
    "official_website": "https://www.sydney.edu.au",
    "international_page": "https://www.sydney.edu.au/study/international-students.html",
    "scholarship_page": "https://www.sydney.edu.au/scholarships/e/international-scholarships.html",
    "application_portal": "https://apply.sydney.edu.au",
}

CAMPUSES = [
    {
        "name": "Camperdown/Darlington Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": True,
        "address": "Camperdown NSW 2006, Australia",
        "description": (
            "The iconic main campus spanning 72 hectares in Sydney's inner city. "
            "Features Gothic Revival sandstone buildings, the Quadrangle, Fisher Library, "
            "numerous museums, and modern research facilities. "
        ),
        "facilities": "Fisher Library, Quadrangle, Sports & Aquatic Centre, Health & Medical Precinct, Student Accommodation, Retail",
        "map_url": "https://maps.google.com/?q=University+of+Sydney+Camperdown",
    },
    {
        "name": "Cumberland Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "75 East Street, Lidcombe NSW 2141",
        "description": "Home to the Faculty of Medicine and Health allied health programs.",
        "facilities": "Simulation Labs, Clinical Training Rooms, Library",
    },
    {
        "name": "Mallett Street Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "88 Mallett Street, Camperdown NSW 2050",
        "description": "Nursing and midwifery clinical training campus.",
        "facilities": "Clinical Skills Labs, Simulation Suites",
    },
]

COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 48500,
        "intake_months": "February",
        "academic_requirement": "High school completion with strong Mathematics and Sciences. ATAR 90+ or equivalent.",
        "gpa_requirement": "3.5/4.0 for transfer",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": (
            "Civil Engineer, Mechanical Engineer, Electrical Engineer, Software Engineer, "
            "Aerospace Engineer, Project Engineer, Consultant"
        ),
        "description": (
            "Accredited by Engineers Australia. Choose from majors including Civil, Mechanical, "
            "Electrical, Software, Chemical, and Aerospace Engineering. Industry placements included."
        ),
        "official_url": "https://www.sydney.edu.au/courses/degrees/bachelor-of-engineering-honours.html",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Computer Science and Technology",
        "level": "bachelor",
        "field_of_study": "Computer Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 44500,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 90 or equivalent. Mathematics required.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": (
            "Software Engineer, Data Scientist, Machine Learning Engineer, "
            "Cybersecurity Analyst, Systems Architect"
        ),
        "description": (
            "Cutting-edge CS program covering algorithms, AI/ML, cybersecurity, and software engineering. "
            "Strong industry connections in Sydney's tech ecosystem."
        ),
        "official_url": "https://www.sydney.edu.au/courses/degrees/bachelor-of-computer-science-and-technology.html",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Commerce",
        "level": "bachelor",
        "field_of_study": "Business / Commerce",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 44500,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 90 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": (
            "Investment Banker, Financial Analyst, Accountant, Management Consultant, "
            "Marketing Director, Economist"
        ),
        "description": (
            "USYD Business School is AACSB-accredited. Choose from majors in Finance, Accounting, "
            "Marketing, Economics, and International Business. Access to Sydney's CBD financial district."
        ),
        "official_url": "https://www.sydney.edu.au/courses/degrees/bachelor-of-commerce.html",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 48000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT, Computer Science, or related field. Minimum 65%.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": (
            "Senior Software Engineer, Data Scientist, AI Engineer, Solutions Architect, "
            "IT Director, CTO"
        ),
        "description": "Advanced coursework in AI, cloud computing, cybersecurity, and data science.",
        "official_url": "https://www.sydney.edu.au/courses/degrees/master-of-information-technology.html",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 54000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree + minimum 3 years professional work experience.",
        "ielts_overall": 7.5,
        "ielts_min_band": 7.0,
        "pte_overall": 73,
        "toefl_ibt": 107,
        "career_outcomes": "C-suite Executive, Director, Senior Consultant, Entrepreneur, Board Member",
        "description": (
            "Sydney MBA is ranked among the best in Australia and Asia-Pacific. "
            "Strong alumni network in finance, consulting, and technology."
        ),
        "official_url": "https://www.sydney.edu.au/business/study/postgraduate/mba.html",
    },
    {
        "name": "Master of Architecture",
        "level": "master",
        "field_of_study": "Architecture",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 44000,
        "intake_months": "February",
        "academic_requirement": "Bachelor of Design or Architecture with minimum 65% average.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Architect, Urban Designer, Interior Designer, Project Manager",
        "description": "Accredited by AACA. Studio-based learning with exposure to Sydney's rich architectural landscape.",
        "official_url": "https://www.sydney.edu.au/courses/degrees/master-of-architecture.html",
    },
]

SCHOLARSHIPS = [
    {
        "name": "University of Sydney International Scholarship (USydIS)",
        "type": "merit",
        "coverage": "Full tuition fee waiver for duration of degree",
        "coverage_percentage": 100,
        "eligibility": (
            "Exceptional international students with outstanding academic achievement. "
            "Highly competitive – limited places available each year."
        ),
        "academic_requirement": "Top academic results in previous qualification (typically 90%+ equivalent)",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most undergraduate and postgraduate programs",
        "deadline": "31 October (for February intake); 31 March (for July intake)",
        "official_url": "https://www.sydney.edu.au/scholarships/e/international-scholarships.html",
        "description": "USYD's most prestigious international scholarship covering full tuition.",
    },
    {
        "name": "Faculty of Engineering International Scholarship",
        "type": "course",
        "coverage": "AUD 10,000 per year",
        "coverage_percentage": None,
        "eligibility": "International students commencing engineering programs.",
        "academic_requirement": "Strong academic background in STEM subjects",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All Engineering programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.sydney.edu.au/engineering/study/scholarships.html",
        "description": "Annual financial support for engineering international students.",
    },
    {
        "name": "Sydney Achiever International Scholarship",
        "type": "merit",
        "coverage": "AUD 5,000 one-time",
        "coverage_percentage": None,
        "eligibility": "International students with strong academic results commencing undergraduate study.",
        "academic_requirement": "Top 15% of cohort in previous qualification",
        "eligible_levels": "Bachelor",
        "eligible_courses": "All courses",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.sydney.edu.au/scholarships/e/international-scholarships.html",
        "description": "Merit recognition for high-achieving international undergraduates.",
    },
]
