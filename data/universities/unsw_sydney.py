"""
UNSW Sydney – Complete Data
Research-based, accurate as of 2024
Official source: https://www.unsw.edu.au/
"""

UNIVERSITY = {
    "name": "UNSW Sydney",
    "short_name": "UNSW",
    "type": "public",
    "group": "go8",
    "established": 1949,
    "state": "New South Wales",
    "city": "Sydney",
    "description": (
        "UNSW Sydney (University of New South Wales) is a world-leading research university "
        "and member of the Group of Eight. Ranked in the global top 20 by several metrics, "
        "UNSW is renowned for its engineering, computer science, business, and law programs. "
        "Located in Kensington, Sydney, it hosts over 65,000 students from 130+ countries."
    ),
    "about": (
        "UNSW is at the cutting edge of technology and innovation, with the UNSW Engineering "
        "Faculty ranked #1 in Australia. The business school (UNSW Business School) is triple-accredited "
        "(AACSB, EQUIS, AMBA). UNSW's proximity to Sydney CBD, technology hubs, and major hospitals "
        "creates unparalleled industry connections. Notable alumni include Nobel laureates and Fortune 500 leaders."
    ),
    "ranking_qs": "#19 World (QS 2025)",
    "ranking_times": "#63 World (THE 2024)",
    "total_students": "65,000+",
    "international_students": "26,000+",
    "cost_of_living": "AUD 2,200–3,500/month",
    "popular_courses": "Engineering, Computer Science, Business, Law, Medicine, Architecture",
    "internship_info": (
        "UNSW's Co-op Program is one of Australia's most respected industry engagement programs. "
        "Students spend 18 months in industry placements with companies like Google, Atlassian, "
        "Commonwealth Bank, KPMG, and major engineering firms."
    ),
    "official_website": "https://www.unsw.edu.au",
    "international_page": "https://www.unsw.edu.au/study/international-students",
    "scholarship_page": "https://www.scholarships.unsw.edu.au",
    "application_portal": "https://www.apply.unsw.edu.au",
}

CAMPUSES = [
    {
        "name": "Kensington Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": True,
        "address": "High Street, Kensington NSW 2033, Australia",
        "description": (
            "UNSW's main campus spanning 38 hectares in Kensington, just 6 km from Sydney CBD. "
            "Modern facilities including the Tyree Energy Technologies Building, UNSW Library, "
            "and vibrant campus life with student housing and retail."
        ),
        "facilities": "UNSW Library, Engineering Precinct, Scientia Building, Student Accommodation, Roundhouse, Sports Fields",
        "map_url": "https://maps.google.com/?q=UNSW+Sydney+Kensington",
    },
    {
        "name": "Paddington Campus (Art & Design)",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "Greens Road, Paddington NSW 2021",
        "description": "Home to UNSW Art & Design (formerly COFA). Located in Sydney's artistic hub.",
        "facilities": "Design Studios, Galleries, Workshop Spaces, Library",
    },
    {
        "name": "Canberra Campus (UNSW Canberra/ADFA)",
        "city": "Canberra",
        "state": "ACT",
        "is_main": False,
        "address": "Northcott Drive, Campbell ACT 2612",
        "description": "UNSW Canberra at the Australian Defence Force Academy. Defence and engineering focus.",
        "facilities": "Defence Research Labs, Engineering Facilities, Library, Campus Accommodation",
    },
]

COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 49500,
        "intake_months": "February, September",
        "academic_requirement": "ATAR 90+ or equivalent. Mathematics and Physics required.",
        "gpa_requirement": "3.5/4.0 for advanced entry",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Civil, Software, Electrical, Mining, Mechanical, Chemical Engineer",
        "description": (
            "Ranked #1 Engineering in Australia (QS). Specialisations in Civil, Mechanical, "
            "Electrical, Software, Mining, Chemical, and Photovoltaics Engineering."
        ),
        "official_url": "https://www.unsw.edu.au/study/undergraduate/bachelor-of-engineering-honours",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Computer Science",
        "level": "bachelor",
        "field_of_study": "Computer Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 48000,
        "intake_months": "February, September",
        "academic_requirement": "ATAR 96+ or equivalent. Strong Mathematics required.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Software Engineer, AI Researcher, Data Scientist, Tech Entrepreneur",
        "description": (
            "Ranked #1 CS in Australia (QS). Specialisations in AI, Cybersecurity, Data Science, "
            "and Software Engineering. Access to UNSW's AI Institute."
        ),
        "official_url": "https://www.unsw.edu.au/study/undergraduate/bachelor-of-computer-science",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Commerce",
        "level": "bachelor",
        "field_of_study": "Business / Commerce",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 44500,
        "intake_months": "February, September",
        "academic_requirement": "ATAR 94+ or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Investment Banker, CPA, Marketing Director, Economist, Management Consultant",
        "description": (
            "Triple-accredited UNSW Business School. Majors in Accounting, Finance, Marketing, "
            "Economics, Information Systems, and Business Law."
        ),
        "official_url": "https://www.unsw.edu.au/study/undergraduate/bachelor-of-commerce",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 47500,
        "intake_months": "February, September",
        "academic_requirement": "Bachelor's degree in IT/Engineering/Science. Min 60% average.",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "IT Manager, Cloud Architect, Data Engineer, AI Researcher",
        "description": "Advanced IT coursework with focus on AI, cloud infrastructure, and network security.",
        "official_url": "https://www.unsw.edu.au/study/postgraduate/master-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 55000,
        "intake_months": "February",
        "academic_requirement": "Bachelor's degree + minimum 5 years work experience.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "CEO, Strategy Director, Consultant, Entrepreneur",
        "description": "UNSW MBA is one of Australia's most rigorous and globally connected executive programs.",
        "official_url": "https://www.business.unsw.edu.au/study/degrees/mba",
    },
]

SCHOLARSHIPS = [
    {
        "name": "UNSW International Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction for duration of study",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at UNSW.",
        "academic_requirement": "Outstanding academic results in final year of study",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Automatically assessed at time of application",
        "intake_deadline": True,
        "official_url": "https://www.scholarships.unsw.edu.au/scholarship/1702000122",
        "description": "UNSW's primary merit scholarship providing 25% tuition reduction.",
    },
    {
        "name": "UNSW Engineering International Scholarship",
        "type": "course",
        "coverage": "AUD 10,000 per year",
        "coverage_percentage": None,
        "eligibility": "International students enrolled in UNSW Engineering programs.",
        "academic_requirement": "Strong STEM background; minimum 85% equivalent",
        "eligible_levels": "Bachelor",
        "eligible_courses": "Engineering programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.scholarships.unsw.edu.au",
        "description": "Annual support for engineering international students.",
    },
]
