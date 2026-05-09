"""
University of Melbourne – Complete Data
Research-based, accurate as of 2024
Official source: https://www.unimelb.edu.au/
"""

UNIVERSITY = {
    "name": "University of Melbourne",
    "short_name": "UniMelb",
    "type": "public",
    "group": "go8",
    "established": 1853,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "The University of Melbourne is Australia's second oldest university, founded in 1853, "
        "and consistently ranks among the world's top 35 universities. A Group of Eight member, "
        "UniMelb is renowned for its Melbourne Model – a unique curriculum combining a broad "
        "undergraduate degree with graduate professional entry. Over 65,000 students from "
        "150+ countries choose UniMelb for its prestige, research excellence, and Melbourne's lifestyle."
    ),
    "about": (
        "UniMelb's Parkville campus, located just 3 km from Melbourne's CBD, is a heritage-listed "
        "masterpiece set in beautifully landscaped gardens. The university's triple-accredited Melbourne "
        "Business School, world-renowned Melbourne Law School, and top-ranked Melbourne Medical School "
        "make it the destination of choice for high achievers. Melbourne itself is repeatedly named "
        "the world's most liveable city."
    ),
    "ranking_qs": "#13 World (QS 2025)",
    "ranking_times": "#33 World (THE 2024)",
    "total_students": "65,000+",
    "international_students": "28,000+",
    "cost_of_living": "AUD 2,000–3,200/month",
    "popular_courses": "Medicine, Law, Business, Engineering, Computer Science, Architecture",
    "internship_info": (
        "UniMelb's internship program connects students with 3,000+ employers including "
        "McKinsey, Goldman Sachs, Google, and government agencies. The Melbourne Careers "
        "Hub facilitates mentoring, networking, and placement programs."
    ),
    "official_website": "https://www.unimelb.edu.au",
    "international_page": "https://study.unimelb.edu.au/how-to-apply/international-student-applications",
    "scholarship_page": "https://scholarships.unimelb.edu.au",
    "application_portal": "https://study.unimelb.edu.au/how-to-apply",
}

CAMPUSES = [
    {
        "name": "Parkville Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "Grattan Street, Parkville VIC 3010, Australia",
        "description": (
            "UniMelb's iconic main campus spanning 35 hectares in Parkville, 3 km from Melbourne CBD. "
            "A heritage-listed Victorian-era campus with lush gardens, modern research facilities, "
            "and vibrant student life. Directly adjacent to Royal Melbourne Hospital and "
            "other major medical and research institutes."
        ),
        "facilities": "Baillieu Library, Melbourne Connect, Medical Precinct, Residential Colleges, Union House, Sports Facilities",
        "map_url": "https://maps.google.com/?q=University+of+Melbourne+Parkville",
    },
    {
        "name": "Burnley Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "500 Yarra Boulevard, Richmond VIC 3121",
        "description": "Home to the Faculty of Science's ecosystem and horticulture programs.",
        "facilities": "Research Gardens, Glasshouses, Ecological Research Facilities",
    },
    {
        "name": "Southbank Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "234 St Kilda Road, Southbank VIC 3006",
        "description": "Home to the Melbourne Conservatorium of Music and Victorian College of the Arts.",
        "facilities": "Concert Halls, Performance Studios, Art Galleries, Recording Studios",
    },
]

COURSES = [
    {
        "name": "Bachelor of Science",
        "level": "bachelor",
        "field_of_study": "Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 43000,
        "intake_months": "February",
        "academic_requirement": "ATAR 85+ or equivalent. Relevant science subjects required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Researcher, Data Scientist, Environmental Scientist, Biotechnologist, Pharmacologist",
        "description": "Broad science foundation with majors in Biology, Chemistry, Physics, Maths, Ecology, and Neuroscience.",
        "official_url": "https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-science/",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Commerce",
        "level": "bachelor",
        "field_of_study": "Business / Commerce",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 43000,
        "intake_months": "February",
        "academic_requirement": "ATAR 92+ or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Investment Banker, CPA, Economist, Marketing Director, Financial Analyst",
        "description": "Triple-accredited Melbourne Business School. Majors in Finance, Accounting, Marketing, Actuarial Studies.",
        "official_url": "https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-commerce/",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "1.5–2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 45000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT/CS with minimum 65%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Data Scientist, Solutions Architect, AI Engineer",
        "description": "Melbourne's elite IT master's with specialisations in AI, Cybersecurity, Computing, and IoT.",
        "official_url": "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/",
        "is_popular": True,
    },
    {
        "name": "Master of Engineering (Software)",
        "level": "master",
        "field_of_study": "Software Engineering",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 46500,
        "intake_months": "February",
        "academic_requirement": "Bachelor's in Engineering/CS with minimum 65%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Architect, DevOps Engineer, Tech Lead, ML Engineer",
        "description": "Engineers Australia accredited. Focuses on modern software design, agile practices, and distributed systems.",
        "official_url": "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software/",
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 58000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree + minimum 5 years professional experience.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Senior Executive, Director, Entrepreneur, Strategy Consultant",
        "description": "Melbourne Business School MBA. Globally ranked, with strong alumni in Asia-Pacific finance and business.",
        "official_url": "https://mbs.edu/mba",
    },
]

SCHOLARSHIPS = [
    {
        "name": "Melbourne International Undergraduate Scholarship",
        "type": "merit",
        "coverage": "50% tuition fee reduction for full degree",
        "coverage_percentage": 50,
        "eligibility": "International students commencing undergraduate degrees at UniMelb.",
        "academic_requirement": "Top 5% academic results in home country",
        "eligible_levels": "Bachelor",
        "eligible_courses": "Most undergraduate programs",
        "deadline": "31 October (February intake)",
        "official_url": "https://scholarships.unimelb.edu.au/awards/melbourne-international-undergraduate-scholarship",
        "description": "UniMelb's prestigious undergraduate scholarship for exceptional international students.",
    },
    {
        "name": "Melbourne Graduate Scholarship",
        "type": "merit",
        "coverage": "AUD 10,000 one-time",
        "coverage_percentage": None,
        "eligibility": "International students commencing graduate coursework with strong academic record.",
        "academic_requirement": "Distinction average (75%+) in bachelor's degree",
        "eligible_levels": "Master",
        "eligible_courses": "Most master's programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://scholarships.unimelb.edu.au",
        "description": "Merit-based financial support for high-achieving international master's students.",
    },
]
