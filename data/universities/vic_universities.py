"""
Victoria Universities (Additional) – Complete Data
Covers: Deakin, Federation University, La Trobe, Swinburne,
        Victoria University (VU), University of Divinity
Research-based, accurate as of 2025–2026
"""

# ──────────────────────────────────────────────────────────────
# DEAKIN UNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_DEAKIN = {
    "name": "Deakin University",
    "short_name": "Deakin",
    "type": "public",
    "group": "irua",
    "established": 1974,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "Deakin University is a leading Australian university ranked in the global top 250, "
        "with campuses in Melbourne (Burwood), Geelong (Waurn Ponds and Waterfront), Warrnambool, "
        "and a Cloud Campus for fully online students. Deakin is renowned for innovation in "
        "online education, health, business, IT, and engineering. With 61,000+ students, "
        "Deakin is one of Australia's largest universities and consistently ranks among the "
        "best young universities globally."
    ),
    "about": (
        "Deakin's Cloud Campus makes it Australia's leading online university, attracting students "
        "worldwide who need flexible, quality education. The Melbourne Burwood campus is a vibrant "
        "hub 13 km from the CBD, while the Geelong Waterfront campus offers stunning bay views. "
        "Deakin is especially strong in health sciences, nursing, business, cybersecurity, and sport science."
    ),
    "ranking_qs": "#233 World (QS 2025)",
    "ranking_times": "#201–250 World (THE 2024)",
    "total_students": "61,000+",
    "international_students": "20,000+",
    "cost_of_living": "AUD 1,800–2,800/month",
    "popular_courses": "Nursing, Business, IT, Cybersecurity, Nutrition, Education, Engineering",
    "internship_info": (
        "Deakin has 2,400+ industry partners including Epworth Healthcare, Barwon Health, "
        "National Australia Bank, and Deloitte. The DeakinTALENT program supports career "
        "development and industry placements across all campuses."
    ),
    "official_website": "https://www.deakin.edu.au",
    "international_page": "https://www.deakin.edu.au/students/studying/study-support-and-improvement/international-students",
    "scholarship_page": "https://www.deakin.edu.au/courses/fees/scholarship-search",
    "application_portal": "https://www.deakin.edu.au/courses/apply",
}

DEAKIN_CAMPUSES = [
    {
        "name": "Melbourne Burwood Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "221 Burwood Highway, Burwood VIC 3125",
        "description": "Deakin's largest campus, 13 km east of Melbourne CBD, with extensive health, business, and IT faculties.",
        "facilities": "Library, Health Sciences Building, ITLL (IT Living Lab), Student Village, Sports Centre",
        "map_url": "https://maps.google.com/?q=Deakin+University+Burwood+Melbourne",
    },
    {
        "name": "Geelong Waurn Ponds Campus",
        "city": "Geelong",
        "state": "Victoria",
        "is_main": False,
        "address": "75 Pigdons Road, Waurn Ponds VIC 3216",
        "description": "Major campus south of Geelong with engineering, health, and science faculties.",
        "facilities": "Engineering Precinct, Medical School, Research Facilities, Student Housing",
    },
    {
        "name": "Geelong Waterfront Campus",
        "city": "Geelong",
        "state": "Victoria",
        "is_main": False,
        "address": "1 Gheringhap Street, Geelong VIC 3220",
        "description": "Scenic campus on Corio Bay waterfront, home to business and arts programs.",
        "facilities": "Waterfront Library, Business School, Student Services",
    },
    {
        "name": "Cloud Campus (Online)",
        "city": "Online",
        "state": "Victoria",
        "is_main": False,
        "address": "Online – DeakinSync Platform",
        "description": "Fully online campus serving students across Australia and internationally.",
        "facilities": "Online Learning Platform, Virtual Library, 24/7 Student Support",
    },
]

DEAKIN_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing / Health",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31200,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, ICU Nurse, Midwife, Nurse Practitioner",
        "description": "ANMAC-accredited. Clinical placements at Epworth, Barwon Health, and major Melbourne hospitals.",
        "official_url": "https://www.deakin.edu.au/course/bachelor-of-nursing",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Cyber Security",
        "level": "bachelor",
        "field_of_study": "Cybersecurity",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 32600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 72 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Cybersecurity Analyst, Penetration Tester, Security Architect, SOC Analyst",
        "description": "One of Australia's dedicated cybersecurity degrees. Backed by Deakin's Centre for Cyber Security Research.",
        "official_url": "https://www.deakin.edu.au/course/bachelor-of-cyber-security",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Commerce",
        "level": "bachelor",
        "field_of_study": "Business / Commerce",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Accountant, Financial Analyst, Marketing Manager, HR Manager, Business Analyst",
        "description": "AACSB-accredited Deakin Business School. Majors in Accounting, Finance, Marketing, Management, and Economics.",
        "official_url": "https://www.deakin.edu.au/course/bachelor-of-commerce",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 34800,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Cybersecurity Lead, Data Scientist, Solutions Architect",
        "description": "Advanced IT program with specialisations in AI, cybersecurity, and data analytics.",
        "official_url": "https://www.deakin.edu.au/course/master-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 37200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree + minimum 3 years relevant work experience.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Senior Manager, Director, Entrepreneur, Strategy Consultant",
        "description": "Deakin MBA available online or on-campus. Strong focus on digital transformation and leadership.",
        "official_url": "https://www.deakin.edu.au/course/master-of-business-administration",
    },
]

DEAKIN_SCHOLARSHIPS = [
    {
        "name": "Deakin Vice-Chancellor's International Scholarship",
        "type": "merit",
        "coverage": "50% tuition fee reduction for duration of degree",
        "coverage_percentage": 50,
        "eligibility": "Exceptional international students commencing undergraduate or postgraduate coursework at Deakin.",
        "academic_requirement": "Minimum 85% (High Distinction) in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "31 October (February intake); 30 April (July intake)",
        "official_url": "https://www.deakin.edu.au/courses/fees/scholarship-search/deakin-vice-chancellors-international-scholarship",
        "description": "Deakin's most prestigious international scholarship, offering 50% tuition reduction.",
    },
    {
        "name": "Deakin International Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at Deakin.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.deakin.edu.au/courses/fees/scholarship-search/deakin-international-scholarship",
        "description": "Deakin's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# FEDERATION UNIVERSITY AUSTRALIA
# ──────────────────────────────────────────────────────────────
UNIVERSITY_FEDERATION = {
    "name": "Federation University Australia",
    "short_name": "FedUni",
    "type": "public",
    "group": "raa",
    "established": 2014,
    "state": "Victoria",
    "city": "Ballarat",
    "description": (
        "Federation University Australia was formed in 2014 through the merger of the University "
        "of Ballarat and the Monash University Gippsland campus. With campuses in Ballarat, "
        "Gippsland, Brisbane, and Berwick (Melbourne), FedUni serves regional Victoria and "
        "Queensland. Known for its approachable teaching, strong vocational pathways, and "
        "programs in IT, nursing, engineering, and education."
    ),
    "about": (
        "FedUni offers a supportive, student-centred environment with smaller class sizes "
        "than major city universities. Ballarat is a historic gold rush city with excellent "
        "quality of life and a very low cost of living. "
        "The Brisbane campus caters specifically to international students."
    ),
    "ranking_qs": "1001–1200 World (QS 2025)",
    "total_students": "22,000+",
    "international_students": "5,000+",
    "cost_of_living": "AUD 1,200–1,700/month",
    "popular_courses": "IT, Nursing, Business, Engineering, Education, Social Work",
    "official_website": "https://www.federation.edu.au",
    "international_page": "https://www.federation.edu.au/international",
    "scholarship_page": "https://www.federation.edu.au/future-students/fees-and-scholarships/scholarships",
    "application_portal": "https://www.federation.edu.au/future-students/apply",
}

FEDERATION_CAMPUSES = [
    {
        "name": "Ballarat Campus (Mount Helen)",
        "city": "Ballarat",
        "state": "Victoria",
        "is_main": True,
        "address": "University Drive, Mount Helen VIC 3350",
        "description": "FedUni's main campus in historic Ballarat, 110 km north-west of Melbourne.",
        "facilities": "Library, Engineering Labs, Health Sciences, Student Housing, Sports Facilities",
        "map_url": "https://maps.google.com/?q=Federation+University+Ballarat",
    },
    {
        "name": "Brisbane Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": False,
        "address": "Level 2, 160 Ann Street, Brisbane QLD 4000",
        "description": "FedUni's city campus in Brisbane CBD, catering largely to international students.",
        "facilities": "Lecture Rooms, Computer Labs, Student Services",
    },
]

FEDERATION_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 26800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, Network Engineer, IT Consultant, Cybersecurity Analyst",
        "description": "Practical IT degree with industry-focused projects and affordable regional tuition fees.",
        "official_url": "https://www.federation.edu.au/future-students/study/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 27600,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "IT Manager, Cloud Architect, Data Analyst, Cybersecurity Specialist",
        "description": "Affordable postgraduate IT with flexible study and strong industry outcomes.",
        "official_url": "https://www.federation.edu.au/future-students/study/master-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 24800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 55 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Business Analyst, Marketing Manager, HR Coordinator, Accountant",
        "description": "Practical business degree with majors in Accounting, Marketing, Management, and HR.",
        "official_url": "https://www.federation.edu.au/future-students/study/bachelor-of-business",
    },
]

FEDERATION_SCHOLARSHIPS = [
    {
        "name": "FedUni International Academic Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate at FedUni.",
        "academic_requirement": "Minimum 70% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.federation.edu.au/future-students/fees-and-scholarships/scholarships",
        "description": "FedUni's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# LA TROBE UNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_LATROBE = {
    "name": "La Trobe University",
    "short_name": "La Trobe",
    "type": "public",
    "group": "irua",
    "established": 1964,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "La Trobe University is a research-intensive university ranked in the global top 400, "
        "with its main campus in Bundoora (Melbourne) and regional campuses in Bendigo, Albury-Wodonga, "
        "Mildura, Shepparton, and a city campus in Melbourne CBD. "
        "La Trobe is renowned for health sciences, allied health, business, law, and social sciences, "
        "and is a leader in inclusive education and social justice."
    ),
    "about": (
        "La Trobe's Bundoora campus is a large, self-contained community with its own "
        "wildlife sanctuary, hospital (La Trobe Private Hospital), and sports facilities. "
        "The university has a strong focus on equity and access, with one of the highest "
        "proportions of first-generation university students in Victoria."
    ),
    "ranking_qs": "#347 World (QS 2025)",
    "ranking_times": "#301–350 World (THE 2024)",
    "total_students": "37,000+",
    "international_students": "12,000+",
    "cost_of_living": "AUD 1,700–2,500/month",
    "popular_courses": "Nursing, Physiotherapy, Business, Law, Social Work, IT, Biomedical Science",
    "internship_info": (
        "La Trobe's Employability Program connects students with 5,000+ industry partners. "
        "Health students have clinical placements at La Trobe Private Hospital and "
        "Austin Health, among other major Melbourne hospitals."
    ),
    "official_website": "https://www.latrobe.edu.au",
    "international_page": "https://www.latrobe.edu.au/international",
    "scholarship_page": "https://www.latrobe.edu.au/scholarships",
    "application_portal": "https://www.latrobe.edu.au/apply",
}

LATROBE_CAMPUSES = [
    {
        "name": "Bundoora Campus (Melbourne)",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "Plenty Road, Bundoora VIC 3086",
        "description": "La Trobe's main campus, 15 km north of Melbourne CBD. A 235-hectare campus with wildlife reserve.",
        "facilities": "Borchardt Library, Health Sciences, Law School, Wildlife Sanctuary, Sports Park, Student Village",
        "map_url": "https://maps.google.com/?q=La+Trobe+University+Bundoora",
    },
    {
        "name": "Melbourne City Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "360 Collins Street, Melbourne VIC 3000",
        "description": "La Trobe's CBD campus offering postgraduate business and health programs.",
        "facilities": "Business School, Conference Rooms, Student Services",
    },
    {
        "name": "Bendigo Campus",
        "city": "Bendigo",
        "state": "Victoria",
        "is_main": False,
        "address": "Edwards Road, Bendigo VIC 3552",
        "description": "Regional campus serving Victoria's Golden Plains region.",
        "facilities": "Library, Nursing Labs, Dental Clinic, Student Housing",
    },
]

LATROBE_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, ICU Nurse, Community Nurse, Nurse Manager",
        "description": "ANMAC-accredited nursing with clinical placements at Austin Health, Northern Health, and La Trobe Private Hospital.",
        "official_url": "https://www.latrobe.edu.au/courses/bachelor-of-nursing",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31200,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 68 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, Data Analyst, Cybersecurity Analyst, IT Manager",
        "description": "Industry-aligned IT degree with guaranteed industry placement. Majors in cybersecurity, data science, and software engineering.",
        "official_url": "https://www.latrobe.edu.au/courses/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33600,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Cybersecurity Lead, Data Scientist, Solutions Architect",
        "description": "Advanced IT with embedded industry project and global perspective.",
        "official_url": "https://www.latrobe.edu.au/courses/master-of-information-technology",
    },
    {
        "name": "Bachelor of Physiotherapy (Honours)",
        "level": "honours",
        "field_of_study": "Physiotherapy / Allied Health",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 34200,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 88 or equivalent. Sciences required.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Physiotherapist, Sports Physio, Rehabilitation Specialist, Private Practitioner",
        "description": "AHPRA-accredited. Ranked among the best physiotherapy programs in Australia.",
        "official_url": "https://www.latrobe.edu.au/courses/bachelor-of-physiotherapy-honours",
        "is_popular": True,
    },
]

LATROBE_SCHOLARSHIPS = [
    {
        "name": "La Trobe International Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction for full program duration",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate coursework at La Trobe.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.latrobe.edu.au/scholarships/la-trobe-international-excellence-scholarship",
        "description": "La Trobe's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# SWINBURNE UNIVERSITY OF TECHNOLOGY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_SWINBURNE = {
    "name": "Swinburne University of Technology",
    "short_name": "Swinburne",
    "type": "public",
    "group": "atn",
    "established": 1908,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "Swinburne University of Technology is a dual-sector university ranked in the global "
        "top 300, and a member of the Australian Technology Network (ATN). Located in Hawthorn, "
        "Melbourne, Swinburne is known for its strengths in science, technology, engineering, "
        "and business. The university also has a campus in Sarawak, Malaysia, "
        "and is a global leader in astronomy research through the Centre for Astrophysics."
    ),
    "about": (
        "Swinburne's Hawthorn campus is 6 km from Melbourne's CBD in the leafy inner east. "
        "The university has a strong industry engagement model, with Work Integrated Learning "
        "embedded in many degrees. Swinburne is particularly regarded for engineering, "
        "computer science, design, and business analytics programs."
    ),
    "ranking_qs": "#266 World (QS 2025)",
    "ranking_times": "#301–350 World (THE 2024)",
    "total_students": "54,000+",
    "international_students": "18,000+",
    "cost_of_living": "AUD 2,000–3,000/month",
    "popular_courses": "Engineering, Computer Science, Business Analytics, Design, IT, Astrophysics",
    "internship_info": (
        "Swinburne's 'real-world' learning model includes guaranteed industry placements. "
        "Partners include Boeing, Bosch, Siemens, KPMG, and leading Melbourne design firms."
    ),
    "official_website": "https://www.swinburne.edu.au",
    "international_page": "https://www.swinburne.edu.au/study/options/international-students/",
    "scholarship_page": "https://www.swinburne.edu.au/study/costs-scholarships/scholarships/",
    "application_portal": "https://www.swinburne.edu.au/study/apply/",
}

SWINBURNE_CAMPUSES = [
    {
        "name": "Hawthorn Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "John Street, Hawthorn VIC 3122",
        "description": "Swinburne's main campus in Hawthorn, 6 km from Melbourne CBD. Strong engineering and technology precinct.",
        "facilities": "AGSE Building, Engineering Precinct, Advanced Manufacturing Facility, Student Housing, Sport Facilities",
        "map_url": "https://maps.google.com/?q=Swinburne+University+Hawthorn",
    },
    {
        "name": "Croydon Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "Norton Road, Croydon VIC 3136",
        "description": "TAFE and dual-sector programs in Melbourne's eastern suburbs.",
        "facilities": "Trade Workshops, TAFE Facilities",
    },
    {
        "name": "Melbourne CBD Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "470 Bourke Street, Melbourne VIC 3000",
        "description": "CBD campus for selected postgraduate business and law programs.",
        "facilities": "Business School, Conference Rooms",
    },
]

SWINBURNE_COURSES = [
    {
        "name": "Bachelor of Computer Science",
        "level": "bachelor",
        "field_of_study": "Computer Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 36600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 75 or equivalent. Mathematics required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Engineer, Data Scientist, AI Developer, Cybersecurity Analyst",
        "description": "Industry-focused CS degree with guaranteed professional placement. Majors in AI, cybersecurity, games development.",
        "official_url": "https://www.swinburne.edu.au/study/course/bachelor-of-computer-science/",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Engineering (Honours) (Professional)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 38400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 78 or equivalent. Mathematics and Physics required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Mechanical, Electrical, Civil, Aerospace, Robotics Engineer",
        "description": "Engineers Australia accredited. Unique Professional Year includes 12-month industry placement.",
        "official_url": "https://www.swinburne.edu.au/study/course/bachelor-of-engineering-honours-professional/",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 38800,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Director, Cloud Architect, AI Engineer, Data Scientist",
        "description": "Advanced IT program with industry research project. Specialisations in AI, cybersecurity, and data analytics.",
        "official_url": "https://www.swinburne.edu.au/study/course/master-of-information-technology/",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Analyst, Marketing Manager, Accountant, Project Manager",
        "description": "Practical business degree with guaranteed professional placement and majors in Finance, Analytics, and Marketing.",
        "official_url": "https://www.swinburne.edu.au/study/course/bachelor-of-business/",
    },
]

SWINBURNE_SCHOLARSHIPS = [
    {
        "name": "Swinburne International Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction for full program",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at Swinburne.",
        "academic_requirement": "Minimum 75% (Credit) in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.swinburne.edu.au/study/costs-scholarships/scholarships/swinburne-international-excellence-scholarship/",
        "description": "Swinburne's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# VICTORIA UNIVERSITY (VU)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_VU = {
    "name": "Victoria University",
    "short_name": "VU",
    "type": "public",
    "group": "none",
    "established": 1916,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "Victoria University is a dual-sector university with campuses in Melbourne's "
        "CBD and western suburbs, plus a campus in Sydney and an online presence. "
        "VU is known for its innovative VU Block Model – studying one subject at a time "
        "over 4-week blocks – which dramatically improves student success and retention. "
        "The university is particularly strong in nursing, sport science, business, engineering, and law."
    ),
    "about": (
        "VU's unique Block Model means students focus on one unit at a time, completing more "
        "in-depth study with more time for work and personal commitments. "
        "VU's City Flinders campus and Footscray Park campus serve a diverse student body "
        "with strong Western Melbourne industry connections."
    ),
    "ranking_qs": "801–1000 World (QS 2025)",
    "total_students": "50,000+",
    "international_students": "15,000+",
    "cost_of_living": "AUD 1,800–2,700/month",
    "popular_courses": "Nursing, Sport Science, Business, Engineering, IT, Law, Education",
    "official_website": "https://www.vu.edu.au",
    "international_page": "https://www.vu.edu.au/study-at-vu/international-students",
    "scholarship_page": "https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships",
    "application_portal": "https://www.vu.edu.au/study-at-vu/apply-enrol",
}

VU_CAMPUSES = [
    {
        "name": "City Flinders Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "Level 7, 300 Flinders Street, Melbourne VIC 3000",
        "description": "VU's CBD campus on iconic Flinders Street, Melbourne.",
        "facilities": "Library, Business School, Law School, Student Services",
        "map_url": "https://maps.google.com/?q=Victoria+University+Flinders+Street+Melbourne",
    },
    {
        "name": "Footscray Park Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "Ballarat Road, Footscray VIC 3011",
        "description": "VU's main teaching campus in Footscray, 5 km from Melbourne CBD.",
        "facilities": "Sport & Recreation Precinct, Engineering Labs, Health Sciences, Library",
    },
]

VU_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 27600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, Network Engineer, IT Consultant, Data Analyst",
        "description": "IT degree using VU's unique Block Model – study one unit at a time for deeper learning.",
        "official_url": "https://www.vu.edu.au/courses/bachelor-of-information-technology-nbif",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 29400,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "IT Manager, Cybersecurity Analyst, Data Scientist, Solutions Architect",
        "description": "Advanced IT using VU Block Model with specialisations in cybersecurity and data analytics.",
        "official_url": "https://www.vu.edu.au/courses/master-of-information-technology-nmit",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 25200,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 55 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Business Analyst, HR Manager, Marketing Specialist, Accountant",
        "description": "Business degree using VU's innovative Block Model for improved focus and success rates.",
        "official_url": "https://www.vu.edu.au/courses/bachelor-of-business-abbus",
    },
]

VU_SCHOLARSHIPS = [
    {
        "name": "VU International Student Scholarship",
        "type": "merit",
        "coverage": "20% tuition fee reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate or postgraduate study at VU.",
        "academic_requirement": "Minimum 65% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships",
        "description": "VU's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF DIVINITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_DIVINITY = {
    "name": "University of Divinity",
    "short_name": "Divinity",
    "type": "private",
    "group": "none",
    "established": 1910,
    "state": "Victoria",
    "city": "Melbourne",
    "description": (
        "The University of Divinity is Australia's only publicly-accredited university "
        "dedicated exclusively to theology and religious studies. Based in Melbourne, "
        "it operates as a collegial university through 16 affiliated colleges across "
        "Australia and New Zealand, representing Christian, Jewish, and multi-faith traditions. "
        "It offers undergraduate to doctoral programs in theology, ministry, and religious studies."
    ),
    "about": (
        "As a specialist university, Divinity attracts students from across faiths who seek "
        "academic, vocational, or personal growth in theology and ministry. "
        "Programs are delivered through affiliate colleges in Melbourne, Sydney, Brisbane, "
        "Adelaide, and Perth, as well as online."
    ),
    "total_students": "3,000+",
    "international_students": "200+",
    "cost_of_living": "AUD 1,800–2,700/month",
    "popular_courses": "Theology, Divinity, Ministry Studies, Pastoral Care, Religious Education",
    "official_website": "https://www.divinity.edu.au",
    "international_page": "https://www.divinity.edu.au/study/international-students/",
    "scholarship_page": "https://www.divinity.edu.au/study/scholarships/",
    "application_portal": "https://www.divinity.edu.au/study/how-to-apply/",
}

DIVINITY_CAMPUSES = [
    {
        "name": "Parkville (Federated) Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": True,
        "address": "21 Highbury Grove, Kew VIC 3101",
        "description": "Administrative hub and federated campus network across Melbourne and nationally.",
        "facilities": "Library, Administrative Centre, Online Learning Platform",
        "map_url": "https://maps.google.com/?q=University+of+Divinity+Kew+Melbourne",
    },
]

DIVINITY_COURSES = [
    {
        "name": "Bachelor of Theology",
        "level": "bachelor",
        "field_of_study": "Theology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 18400,
        "intake_months": "February, July",
        "academic_requirement": "Year 12 completion or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Minister, Chaplain, Religious Educator, Community Worker, Social Services",
        "description": "Comprehensive undergraduate theology program delivered through affiliate colleges.",
        "official_url": "https://www.divinity.edu.au/study/programs/bachelor-of-theology/",
    },
    {
        "name": "Master of Divinity",
        "level": "master",
        "field_of_study": "Theology / Ministry",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 19200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree in any field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Ordained Minister, Chaplain, Church Leader, Pastoral Counsellor",
        "description": "Professional ministerial degree preparing graduates for ordained ministry and church leadership.",
        "official_url": "https://www.divinity.edu.au/study/programs/master-of-divinity/",
    },
]

DIVINITY_SCHOLARSHIPS = [
    {
        "name": "University of Divinity Scholarship",
        "type": "merit",
        "coverage": "Partial tuition support (varies by college)",
        "coverage_percentage": None,
        "eligibility": "Students demonstrating academic merit and commitment to theological study.",
        "academic_requirement": "Good academic standing",
        "eligible_levels": "Bachelor, Master, PhD",
        "eligible_courses": "Theology programs",
        "deadline": "Contact affiliated college",
        "official_url": "https://www.divinity.edu.au/study/scholarships/",
        "description": "Scholarship support available through affiliated colleges of the University of Divinity.",
    },
]
