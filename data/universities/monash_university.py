"""
Monash University – Complete Data
Research-based, accurate as of 2024
Official source: https://www.monash.edu/
"""

UNIVERSITY = {
    "name": "Monash University",
    "short_name": "Monash",
    "type": "public",
    "group": "go8",
    "established": 1958,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "Monash University is Australia's largest university and a proud member of the Group of Eight. "
        "Ranked among the top 50 universities in the world, Monash has campuses across Melbourne, "
        "Malaysia, South Africa, and India, making it one of the most globally connected universities. "
        "With over 86,000 students from 170+ countries, it offers more than 300 courses across "
        "10 faculties spanning medicine, engineering, business, law, and the arts."
    ),
    "about": (
        "Monash is known for its cutting-edge research, diverse campus culture, and strong graduate outcomes. "
        "The Clayton campus is a self-contained city with world-class research institutes, startup hubs, "
        "and sports facilities. Monash graduates are highly sought after by employers globally. "
        "The university is especially strong in pharmacy, medicine, engineering, and business."
    ),
    "ranking_qs": "#37 World (QS 2025)",
    "ranking_times": "#77 World (THE 2024)",
    "total_students": "86,000+",
    "international_students": "32,000+",
    "cost_of_living": "AUD 2,000–3,000/month",
    "popular_courses": "Medicine, Engineering, Business, Pharmacy, Law, Computer Science",
    "internship_info": (
        "Monash has an extensive Work Integrated Learning (WIL) program with 2,000+ industry partners. "
        "The Monash Industry Placement Program connects students with leading companies including "
        "Deloitte, Boeing, BHP, and major Melbourne hospitals."
    ),
    "official_website": "https://www.monash.edu",
    "international_page": "https://www.monash.edu/international",
    "scholarship_page": "https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/international",
    "application_portal": "https://www.monash.edu/study/apply",
}

CAMPUSES = [
    {
        "name": "Clayton Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "Wellington Road, Clayton VIC 3800, Australia",
        "description": (
            "Monash's main and largest campus, located 25 km south-east of Melbourne CBD. "
            "A sprawling 100-hectare campus with research institutes, medical school, law school, "
            "student accommodation, restaurants, and sports facilities."
        ),
        "facilities": "Matheson Library, Monash Sport, Medical Precinct, Research Institutes, Student Accommodation, Retail Precinct",
        "map_url": "https://maps.google.com/?q=Monash+University+Clayton",
    },
    {
        "name": "Caulfield Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "900 Dandenong Road, Caulfield East VIC 3145",
        "description": "Home to Business, Arts, and Information Technology faculties. Located 13 km from Melbourne CBD.",
        "facilities": "Caulfield Library, Business School, IT Labs, Student Services",
        "map_url": "https://maps.google.com/?q=Monash+University+Caulfield",
    },
    {
        "name": "Parkville Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "381 Royal Parade, Parkville VIC 3052",
        "description": "Home to the Monash Institute of Pharmaceutical Sciences. In Melbourne's medical precinct.",
        "facilities": "Pharmaceutical Labs, Research Centres",
    },
]

COURSES = [
    {
        "name": "Bachelor of Computer Science",
        "level": "bachelor",
        "field_of_study": "Computer Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 42600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 85 or equivalent. Strong Mathematics background required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Engineer, AI/ML Engineer, Data Scientist, Cybersecurity Analyst, Game Developer",
        "description": (
            "One of Australia's top CS degrees with specialisations in AI, cybersecurity, data science, "
            "and software engineering. Industry projects and hackathons integrated."
        ),
        "official_url": "https://www.monash.edu/study/courses/find-a-course/2024/computer-science-c2000",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 39700,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 80 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Analyst, Marketing Manager, Financial Analyst, Management Consultant",
        "description": (
            "Monash Business School is AACSB and EQUIS accredited – among the top 1% globally. "
            "Specialisations in Accounting, Finance, Marketing, Management, and Econometrics."
        ),
        "official_url": "https://www.monash.edu/study/courses/find-a-course/2024/business-b2000",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 46600,
        "intake_months": "February",
        "academic_requirement": "ATAR 90+ or equivalent. Strong Mathematics and Physics.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Mechanical, Civil, Electrical, Chemical, Aerospace, Software Engineer",
        "description": "Accredited by Engineers Australia. Multiple specialisations with capstone industry project.",
        "official_url": "https://www.monash.edu/study/courses/find-a-course/2024/engineering-honours-e3001",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 40400,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree in IT/CS or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Solutions Architect, Data Scientist, Cybersecurity Lead",
        "description": "Advanced IT program with research and industry project components. Specialise in AI, cloud, or security.",
        "official_url": "https://www.monash.edu/study/courses/find-a-course/2024/information-technology-s3002",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 48600,
        "intake_months": "February",
        "academic_requirement": "Bachelor's + minimum 5 years work experience (3 years managerial).",
        "ielts_overall": 7.0,
        "ielts_min_band": 6.5,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "CEO, Director, Senior Manager, Entrepreneur, Management Consultant",
        "description": "Monash MBA is ranked #1 in Australia by The Economist. Strong focus on global leadership.",
        "official_url": "https://www.monash.edu/business/programs/mba",
    },
    {
        "name": "Master of Pharmacy",
        "level": "master",
        "field_of_study": "Pharmacy",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 44100,
        "intake_months": "February",
        "academic_requirement": "Bachelor's in Pharmacy or related health science with minimum 65%.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Pharmacist, Clinical Pharmacist, Pharmaceutical Researcher, Drug Safety Officer",
        "description": (
            "Monash is globally ranked #1 for Pharmacy. Located at the Parkville campus in Melbourne's "
            "medical precinct, providing unmatched clinical and research opportunities."
        ),
        "official_url": "https://www.monash.edu/study/courses/find-a-course/2024/pharmacy-s5003",
    },
    {
        "name": "Graduate Diploma in Information Technology",
        "level": "graduate_diploma",
        "field_of_study": "Information Technology",
        "duration": "1 year",
        "study_mode": "full_time",
        "tuition_fee_annual": 37200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in any discipline.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Support, Junior Developer, Business Analyst, IT Coordinator",
        "description": "Ideal pathway for non-IT graduates entering the technology industry. Leads to MIT.",
        "official_url": "https://www.monash.edu/study/courses/find-a-course/2024/information-technology-s4002",
    },
]

SCHOLARSHIPS = [
    {
        "name": "Monash International Merit Scholarship",
        "type": "merit",
        "coverage": "AUD 10,000 per year (up to 4 years for undergraduate)",
        "coverage_percentage": None,
        "eligibility": "International students commencing undergraduate or postgraduate study at Monash.",
        "academic_requirement": "Minimum 85% average in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All courses",
        "deadline": "Intake-based – applied automatically at admission",
        "intake_deadline": True,
        "official_url": "https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/international/monash-international-merit-scholarship",
        "description": "Monash's flagship scholarship providing AUD 10,000/year to high-achieving international students.",
    },
    {
        "name": "Monash Elite Athlete Scholarship",
        "type": "merit",
        "coverage": "AUD 5,000 one-time + academic support",
        "coverage_percentage": None,
        "eligibility": "International students who compete at national or international level in sport.",
        "academic_requirement": "Satisfactory academic standing",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All courses",
        "deadline": "31 October (February intake)",
        "official_url": "https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/international",
        "description": "Supports high-performance athletes balancing sport and study.",
    },
    {
        "name": "Monash Graduate Scholarship",
        "type": "merit",
        "coverage": "20% tuition fee reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing a master's degree with strong undergraduate results.",
        "academic_requirement": "Distinction average (75%+) in bachelor's degree",
        "eligible_levels": "Master",
        "eligible_courses": "Most master's programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/international",
        "description": "Tuition reduction for academically meritorious international postgraduate students.",
    },
]
