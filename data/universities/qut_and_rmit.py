"""
Queensland University of Technology (QUT) – Complete Data
Research-based, accurate as of 2024
Official source: https://www.qut.edu.au/
"""

UNIVERSITY_QUT = {
    "name": "Queensland University of Technology",
    "short_name": "QUT",
    "type": "public",
    "group": "atn",
    "established": 1989,
    "state": "Queensland",
    "city": "Brisbane",
    "description": (
        "QUT – 'A university for the real world' – is one of Australia's largest and most innovative "
        "universities. A member of the Australian Technology Network (ATN), QUT is renowned for its "
        "practical, industry-focused education in technology, business, law, health, and creative industries. "
        "With campuses in Brisbane's CBD and inner suburbs, QUT has 50,000+ students from 100+ countries."
    ),
    "about": (
        "QUT's Gardens Point campus, situated on the Brisbane River, offers stunning views of the city. "
        "The Creative Industries Precinct (The Cube) is a world-leading facility. QUT has exceptional "
        "industry partnerships with Queensland Government, QUT spinoff companies, and major Brisbane employers. "
        "Its law school is consistently ranked among Australia's best."
    ),
    "ranking_qs": "381–400 World (QS 2025)",
    "ranking_times": "401–500 World (THE 2024)",
    "total_students": "50,000+",
    "international_students": "12,000+",
    "cost_of_living": "AUD 1,800–2,500/month",
    "popular_courses": "IT, Business, Law, Engineering, Creative Industries, Education",
    "internship_info": (
        "QUT's Work Integrated Learning program is among Australia's best. Students undertake "
        "mandatory industry placements with companies like Boeing, Rio Tinto, EY, and government agencies."
    ),
    "official_website": "https://www.qut.edu.au",
    "international_page": "https://www.qut.edu.au/international",
    "scholarship_page": "https://www.qut.edu.au/study/fees-and-scholarships/scholarships-and-bursaries",
    "application_portal": "https://www.qut.edu.au/study/applying",
}

QUT_CAMPUSES = [
    {
        "name": "Gardens Point Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": True,
        "address": "2 George Street, Brisbane QLD 4000",
        "description": "QUT's main campus located on the banks of the Brisbane River, in the heart of Brisbane CBD.",
        "facilities": "QUT Library, Law School, Engineering Precinct, Science & Engineering Centre, Student Accommodation",
        "map_url": "https://maps.google.com/?q=QUT+Gardens+Point+Brisbane",
    },
    {
        "name": "Kelvin Grove Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": False,
        "address": "Victoria Park Road, Kelvin Grove QLD 4059",
        "description": "Home to QUT Creative Industries, Health, and Education faculties.",
        "facilities": "Creative Industries Precinct (The Cube), Health Clinics, Education Facilities, Urban Village",
    },
]

QUT_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 35900,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 72 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 5.5,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, Data Analyst, Cybersecurity Specialist, IT Consultant",
        "description": "Industry-focused IT degree with majors in Computer Science, Cybersecurity, Data Analytics, and IT Management.",
        "official_url": "https://www.qut.edu.au/courses/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 32300,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 5.5,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Business Analyst, Marketing Manager, Accountant, HR Manager, Entrepreneur",
        "description": "AACSB-accredited QUT Business School. Majors in Accounting, Finance, Marketing, HR, and Entrepreneurship.",
        "official_url": "https://www.qut.edu.au/courses/bachelor-of-business",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 35400,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Director, Solutions Architect, AI Engineer, Data Scientist",
        "description": "Advanced IT program with industry capstone project. Specialisations in AI, Security, and Data Science.",
        "official_url": "https://www.qut.edu.au/courses/master-of-information-technology",
        "is_popular": True,
    },
]

QUT_SCHOLARSHIPS = [
    {
        "name": "QUT Excellence Scholarship – International",
        "type": "merit",
        "coverage": "AUD 6,000 per year",
        "coverage_percentage": None,
        "eligibility": "International students commencing full-time undergraduate or postgraduate study.",
        "academic_requirement": "Minimum 75% or Distinction average in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All courses",
        "deadline": "Intake-based – automatic consideration",
        "intake_deadline": True,
        "official_url": "https://www.qut.edu.au/study/fees-and-scholarships/scholarships-and-bursaries/qut-excellence-scholarship-international",
        "description": "QUT's primary merit scholarship for international students.",
    },
]


# ============================================================
# RMIT University
# ============================================================

UNIVERSITY_RMIT = {
    "name": "RMIT University",
    "short_name": "RMIT",
    "type": "public",
    "group": "atn",
    "established": 1887,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "RMIT University (Royal Melbourne Institute of Technology) is a global university of "
        "technology, design and enterprise. A member of the Australian Technology Network, "
        "RMIT has campuses in Melbourne, Vietnam, Spain, and a research and industry presence worldwide. "
        "Known for its practical, industry-focused programs, RMIT is particularly strong in "
        "design, architecture, engineering, business, and creative arts."
    ),
    "about": (
        "RMIT's Melbourne City campus is located in the heart of Melbourne's CBD – "
        "Australia's design and cultural capital. Students have instant access to Melbourne's "
        "world-class tech, fashion, architecture, and business scenes. RMIT has over 95,000 "
        "students globally and strong industry partnerships with companies like Adobe, Telstra, "
        "and major Melbourne architecture firms."
    ),
    "ranking_qs": "192 World (QS 2025)",
    "ranking_times": "401–500 World (THE 2024)",
    "total_students": "95,000+ (global)",
    "international_students": "20,000+",
    "cost_of_living": "AUD 2,000–3,000/month",
    "popular_courses": "Architecture, Engineering, Design, Business, IT, Fashion",
    "internship_info": (
        "RMIT's Work Integrated Learning program is deeply embedded in all programs. "
        "Industry partners include Arup, Lendlease, Accenture, National Australia Bank, "
        "and major design and technology companies."
    ),
    "official_website": "https://www.rmit.edu.au",
    "international_page": "https://www.rmit.edu.au/study-with-us/international-students",
    "scholarship_page": "https://www.rmit.edu.au/study-with-us/applying-to-rmit/scholarships",
    "application_portal": "https://www.rmit.edu.au/study-with-us/applying-to-rmit",
}

RMIT_CAMPUSES = [
    {
        "name": "City Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "124 La Trobe Street, Melbourne VIC 3000",
        "description": "RMIT's iconic City campus in Melbourne CBD – the core of RMIT's academic life.",
        "facilities": "Swanston Library, Design Hub, RMIT Gallery, Student Union, IT Labs, Maker Spaces",
        "map_url": "https://maps.google.com/?q=RMIT+University+Melbourne+CBD",
    },
    {
        "name": "Bundoora Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "Plenty Road, Bundoora VIC 3083",
        "description": "Health, science, and engineering programs. Located in Melbourne's northern suburbs.",
        "facilities": "Health Clinics, Science Labs, Engineering Workshops, Sports Oval",
    },
]

RMIT_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 37440,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, Network Engineer, Data Analyst, Cybersecurity Analyst",
        "description": "Industry-led IT program based in Melbourne's tech hub. Majors in Network, Software, and Data Analytics.",
        "official_url": "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor/bachelor-of-information-technology-bp162",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Architecture (Honours)",
        "level": "honours",
        "field_of_study": "Architecture",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 40320,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 78 or equivalent. Portfolio required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Registered Architect, Urban Planner, Interior Designer, Project Manager",
        "description": "AACA-accredited. Studio-based learning in Melbourne's vibrant architectural scene. RMIT is ranked #1 Architecture in Australia (QS).",
        "official_url": "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor/bachelor-of-architecture-honours-bh120",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 38400,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Solutions Architect, Cloud Engineer, Data Scientist",
        "description": "Advanced IT degree with embedded industry projects and leadership development.",
        "official_url": "https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-information-technology-mc268",
        "is_popular": True,
    },
]

RMIT_SCHOLARSHIPS = [
    {
        "name": "RMIT Vice-Chancellor's International Excellence Scholarship",
        "type": "merit",
        "coverage": "30% tuition fee reduction for full degree",
        "coverage_percentage": 30,
        "eligibility": "High-achieving international students commencing an RMIT undergraduate or postgraduate degree.",
        "academic_requirement": "Distinction average (75%+) in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.rmit.edu.au/study-with-us/applying-to-rmit/scholarships/rmit-vice-chancellors-international-excellence-scholarship",
        "description": "RMIT's flagship merit scholarship for outstanding international students.",
    },
]
