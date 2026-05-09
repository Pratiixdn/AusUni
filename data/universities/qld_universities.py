"""
Queensland Universities (Additional) – Complete Data
Covers: Bond University, CQUniversity, Griffith University,
        James Cook University, UniSQ, University of the Sunshine Coast
Research-based, accurate as of 2025–2026
"""

# ──────────────────────────────────────────────────────────────
# BOND UNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_BOND = {
    "name": "Bond University",
    "short_name": "Bond",
    "type": "private",
    "group": "none",
    "established": 1989,
    "state": "Queensland",
    "city": "Gold Coast",
    "description": (
        "Bond University is Australia's first private non-profit university and one of the most "
        "highly regarded private institutions in the country. Located on the Gold Coast, Bond "
        "operates a unique three-semester year (January, May, September), allowing students to "
        "complete a three-year degree in just two years. Known for small class sizes, personalised "
        "learning, and exceptional student experience, Bond excels in law, business, health, "
        "film, and communications."
    ),
    "about": (
        "Bond's Gold Coast campus is a stunning resort-style precinct with world-class facilities. "
        "Its law school consistently ranks #1 in Australia for student experience and graduate "
        "employment. The university has produced many prominent lawyers, business leaders, and "
        "media personalities. With only 6,000 students, Bond offers an intimate academic community."
    ),
    "ranking_qs": "451–500 World (QS 2025)",
    "ranking_times": "601–800 World (THE 2024)",
    "total_students": "6,500+",
    "international_students": "3,000+",
    "cost_of_living": "AUD 1,800–2,500/month",
    "popular_courses": "Law, Business, Health Sciences, Film & Television, Architecture, IT",
    "internship_info": (
        "Bond's accelerated model and strong alumni network provide rapid pathways to employment. "
        "Law students participate in the Bond Law Clinic. Business students access Gold Coast's "
        "tourism, finance, and tech industries."
    ),
    "official_website": "https://www.bond.edu.au",
    "international_page": "https://www.bond.edu.au/study/international-students",
    "scholarship_page": "https://www.bond.edu.au/future-students/scholarships",
    "application_portal": "https://www.bond.edu.au/future-students/apply",
}

BOND_CAMPUSES = [
    {
        "name": "Gold Coast Campus",
        "city": "Gold Coast",
        "state": "Queensland",
        "is_main": True,
        "address": "14 University Drive, Robina QLD 4226",
        "description": "Bond's stunning resort-style campus in Robina, Gold Coast. Adjacent to Robina Town Centre and public transport.",
        "facilities": "Bond Library, Law School, Medical & Health Sciences Building, Film Studios, Sports Hub, Student Village",
        "map_url": "https://maps.google.com/?q=Bond+University+Gold+Coast",
    },
]

BOND_COURSES = [
    {
        "name": "Bachelor of Laws (LLB)",
        "level": "bachelor",
        "field_of_study": "Law",
        "duration": "2 years (3 semesters/year)",
        "study_mode": "full_time",
        "tuition_fee_annual": 44852,
        "intake_months": "January, May, September",
        "academic_requirement": "Minimum ATAR 80 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Solicitor, Barrister, Legal Counsel, Corporate Lawyer, Judge's Associate",
        "description": "Ranked #1 Law School in Australia for student experience (Good Universities Guide). Completed in 2 years with three intakes per year.",
        "official_url": "https://www.bond.edu.au/future-students/study/degrees/bachelor-laws",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "2 years (accelerated)",
        "study_mode": "full_time",
        "tuition_fee_annual": 36780,
        "intake_months": "January, May, September",
        "academic_requirement": "Minimum ATAR 72 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Manager, Entrepreneur, Financial Analyst, Marketing Manager",
        "description": "Complete a business degree in 2 years. AACSB-accredited Bond Business School with majors in Finance, Marketing, Entrepreneurship, and Management.",
        "official_url": "https://www.bond.edu.au/future-students/study/degrees/bachelor-business",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "2 years (accelerated)",
        "study_mode": "full_time",
        "tuition_fee_annual": 34440,
        "intake_months": "January, May, September",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, Data Analyst, Cybersecurity Specialist, IT Manager",
        "description": "Accelerated IT degree completed in 2 years with industry placement and cybersecurity focus.",
        "official_url": "https://www.bond.edu.au/future-students/study/degrees/bachelor-information-technology",
    },
]

BOND_SCHOLARSHIPS = [
    {
        "name": "Bond University International Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction for duration of program",
        "coverage_percentage": 25,
        "eligibility": "International students commencing an undergraduate or postgraduate degree at Bond.",
        "academic_requirement": "Minimum 80% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.bond.edu.au/future-students/scholarships",
        "description": "Bond's primary merit scholarship for international students.",
    },
    {
        "name": "Bond Vice-Chancellor's Scholarship",
        "type": "merit",
        "coverage": "50% tuition reduction",
        "coverage_percentage": 50,
        "eligibility": "Exceptional academic achievers commencing at Bond.",
        "academic_requirement": "Top 5% equivalent academic results",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "31 October (January intake); 31 March (May intake)",
        "official_url": "https://www.bond.edu.au/future-students/scholarships",
        "description": "Bond's most prestigious scholarship for outstanding international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# CQUNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_CQU = {
    "name": "CQUniversity",
    "short_name": "CQU",
    "type": "public",
    "group": "raa",
    "established": 1967,
    "state": "Queensland",
    "city": "Rockhampton",
    "description": (
        "CQUniversity (formerly Central Queensland University) is Australia's most campus-rich "
        "university, with 23 locations across Australia including major cities such as Brisbane, "
        "Sydney, Melbourne, Adelaide, and Cairns, as well as regional Queensland campuses in "
        "Rockhampton, Bundaberg, Gladstone, and Mackay. "
        "CQU specialises in IT, engineering, nursing, business, education, and online learning."
    ),
    "about": (
        "CQU's wide campus network means students can study almost anywhere in Australia. "
        "The university is committed to equity and access, and has one of Australia's largest "
        "online student bodies. Low tuition fees relative to capital city universities make "
        "CQU an attractive option for international students."
    ),
    "ranking_qs": "1001–1200 World (QS 2025)",
    "total_students": "35,000+",
    "international_students": "8,000+",
    "cost_of_living": "AUD 1,400–2,200/month",
    "popular_courses": "IT, Nursing, Engineering, Business, Education, Social Work",
    "official_website": "https://www.cqu.edu.au",
    "international_page": "https://www.cqu.edu.au/international",
    "scholarship_page": "https://www.cqu.edu.au/fees-scholarships/scholarships",
    "application_portal": "https://www.cqu.edu.au/how-to-apply",
}

CQU_CAMPUSES = [
    {
        "name": "Rockhampton Campus",
        "city": "Rockhampton",
        "state": "Queensland",
        "is_main": True,
        "address": "Bruce Highway, Rockhampton QLD 4702",
        "description": "CQU's original campus in Rockhampton, Central Queensland.",
        "facilities": "Library, Engineering Labs, Mining Simulation, Student Housing",
        "map_url": "https://maps.google.com/?q=CQUniversity+Rockhampton",
    },
    {
        "name": "Brisbane Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": False,
        "address": "160 Ann Street, Brisbane QLD 4000",
        "description": "Modern CBD campus in Brisbane catering primarily to international students.",
        "facilities": "Library, IT Labs, Student Services",
    },
    {
        "name": "Sydney Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "400 Kent Street, Sydney NSW 2000",
        "description": "Sydney CBD campus for selected undergraduate and postgraduate programs.",
        "facilities": "Computer Labs, Study Rooms, Student Services",
    },
]

CQU_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 25600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, Network Engineer, IT Consultant, Cybersecurity Analyst",
        "description": "Affordable IT degree with majors in cybersecurity, software development, and networking.",
        "official_url": "https://www.cqu.edu.au/courses/undergraduate/information-technology/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 27200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "IT Manager, Systems Analyst, Cloud Engineer, Data Analyst",
        "description": "Advanced IT with industry project available across multiple CQU campuses.",
        "official_url": "https://www.cqu.edu.au/courses/postgraduate/information-technology/master-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Engineering Technology (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Engineering Technologist, Mining Engineer, Civil Technologist, Project Manager",
        "description": "Practical engineering technology degree with strong mining, civil, and electrical streams.",
        "official_url": "https://www.cqu.edu.au/courses/undergraduate/engineering/bachelor-of-engineering-technology-honours",
    },
]

CQU_SCHOLARSHIPS = [
    {
        "name": "CQUniversity International Merit Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction for full program",
        "coverage_percentage": 25,
        "eligibility": "International students with strong academic results commencing at CQU.",
        "academic_requirement": "Minimum 70% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.cqu.edu.au/fees-scholarships/scholarships/international",
        "description": "CQU's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# GRIFFITH UNIVERSITY
# ──────────────────────────────────────────────────────────────
UNIVERSITY_GRIFFITH = {
    "name": "Griffith University",
    "short_name": "Griffith",
    "type": "public",
    "group": "irua",
    "established": 1971,
    "state": "Queensland",
    "city": "Brisbane",
    "description": (
        "Griffith University is a progressive, research-intensive university with five campuses "
        "across South East Queensland — Nathan and South Bank in Brisbane, Southport and Gold Coast "
        "on the Gold Coast, and Logan. Ranked in the global top 250, Griffith is known for its "
        "strengths in criminology, law, environment, business, health, music, and the arts. "
        "With 53,000+ students, it is one of Australia's largest universities."
    ),
    "about": (
        "Griffith's South Bank campus, on the banks of the Brisbane River opposite the CBD, "
        "is one of Australia's most beautifully located. The Queensland Conservatorium of Music "
        "and Griffith Film School are world-renowned specialist schools. "
        "The Gold Coast campus sits between the city and the beach, offering a vibrant student lifestyle."
    ),
    "ranking_qs": "#239 World (QS 2025)",
    "ranking_times": "#251–300 World (THE 2024)",
    "total_students": "53,000+",
    "international_students": "14,000+",
    "cost_of_living": "AUD 1,700–2,500/month",
    "popular_courses": "Criminology, Law, Business, Nursing, IT, Music, Environment, Education",
    "internship_info": (
        "Griffith has 4,000+ industry partners. Students access placements in hospitals, "
        "Queensland Police, courts, media organisations, and environmental agencies. "
        "The Griffith Business School has strong corporate partnerships."
    ),
    "official_website": "https://www.griffith.edu.au",
    "international_page": "https://www.griffith.edu.au/international",
    "scholarship_page": "https://www.griffith.edu.au/scholarships",
    "application_portal": "https://www.griffith.edu.au/apply",
}

GRIFFITH_CAMPUSES = [
    {
        "name": "South Bank Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": True,
        "address": "Griffith University, South Bank QLD 4101",
        "description": "Griffith's stunning South Bank campus adjacent to the Brisbane River, Cultural Centre, and QPAC.",
        "facilities": "Queensland Conservatorium, Griffith Film School, Pharmacy School, Library",
        "map_url": "https://maps.google.com/?q=Griffith+University+South+Bank+Brisbane",
    },
    {
        "name": "Nathan Campus",
        "city": "Brisbane",
        "state": "Queensland",
        "is_main": False,
        "address": "170 Kessels Road, Nathan QLD 4111",
        "description": "Griffith's main Brisbane campus, 12 km south of CBD. Large research campus with health and business faculties.",
        "facilities": "Library, Health Sciences, Law School, Environmental Research, Sports Facilities",
    },
    {
        "name": "Gold Coast Campus",
        "city": "Gold Coast",
        "state": "Queensland",
        "is_main": False,
        "address": "Gold Coast Campus, Southport QLD 4222",
        "description": "Griffith's Gold Coast campus in Southport, near the beach and Broadwater.",
        "facilities": "Business School, IT Labs, Student Hub, Gold Coast Health Precinct",
    },
]

GRIFFITH_COURSES = [
    {
        "name": "Bachelor of Criminology and Criminal Justice",
        "level": "bachelor",
        "field_of_study": "Criminology / Law",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 29600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 68 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Police Officer, Corrections Officer, Policy Analyst, Legal Researcher, Social Worker",
        "description": "Griffith's internationally renowned criminology program. Direct pathways to Queensland Police and justice agencies.",
        "official_url": "https://www.griffith.edu.au/criminology-law/bachelor-criminology-criminal-justice",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 68 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, IT Consultant, Data Analyst, Cybersecurity Analyst",
        "description": "Industry-connected IT degree with majors in cybersecurity, data analytics, and software engineering.",
        "official_url": "https://www.griffith.edu.au/it-engineering/bachelor-information-technology",
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
        "career_outcomes": "IT Manager, Cloud Architect, Data Scientist, AI Engineer",
        "description": "Advanced IT degree with industry project. Specialisations in AI, cybersecurity, and data analytics.",
        "official_url": "https://www.griffith.edu.au/it-engineering/master-information-technology",
    },
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Analyst, Marketing Manager, Financial Analyst, HR Manager",
        "description": "AACSB-accredited Griffith Business School. Majors in Accounting, Marketing, Finance, Management.",
        "official_url": "https://www.griffith.edu.au/business-government/bachelor-business",
        "is_popular": True,
    },
]

GRIFFITH_SCHOLARSHIPS = [
    {
        "name": "Griffith International Merit Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at Griffith.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based – automatic assessment",
        "intake_deadline": True,
        "official_url": "https://www.griffith.edu.au/scholarships/griffith-international-merit-scholarship",
        "description": "Griffith's primary international merit scholarship.",
    },
    {
        "name": "Griffith Vice-Chancellor's Scholarship",
        "type": "merit",
        "coverage": "50% tuition reduction",
        "coverage_percentage": 50,
        "eligibility": "Outstanding international students commencing undergraduate or postgraduate study.",
        "academic_requirement": "Top academic achiever – equivalent 85%+",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "31 October (February intake); 30 April (July intake)",
        "official_url": "https://www.griffith.edu.au/scholarships",
        "description": "Griffith's most prestigious scholarship for exceptional international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# JAMES COOK UNIVERSITY (JCU)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_JCU = {
    "name": "James Cook University",
    "short_name": "JCU",
    "type": "public",
    "group": "irua",
    "established": 1970,
    "state": "Queensland",
    "city": "Townsville",
    "description": (
        "James Cook University is a research-intensive university ranked in the global top 250, "
        "with campuses in Townsville and Cairns in tropical North Queensland, and Singapore. "
        "JCU is the world's leading university for tropical research and education, with strengths "
        "in marine biology, environmental science, medicine, nursing, and business. "
        "The Great Barrier Reef is JCU's living laboratory."
    ),
    "about": (
        "JCU offers a unique study experience in tropical Australia, with the Great Barrier Reef "
        "and rainforest as living classrooms. The Townsville campus features the Australian Institute "
        "of Tropical Health and Medicine. JCU's Singapore campus makes it an internationally connected "
        "institution with a strong Asia-Pacific focus."
    ),
    "ranking_qs": "#239 World (QS 2025)",
    "ranking_times": "#301–350 World (THE 2024)",
    "total_students": "22,000+",
    "international_students": "6,000+",
    "cost_of_living": "AUD 1,400–1,900/month",
    "popular_courses": "Marine Biology, Environmental Science, Medicine, Nursing, Business, IT",
    "official_website": "https://www.jcu.edu.au",
    "international_page": "https://www.jcu.edu.au/international-students",
    "scholarship_page": "https://www.jcu.edu.au/scholarships",
    "application_portal": "https://www.jcu.edu.au/courses-and-study/applying-to-jcu",
}

JCU_CAMPUSES = [
    {
        "name": "Townsville Campus (Douglas)",
        "city": "Townsville",
        "state": "Queensland",
        "is_main": True,
        "address": "1 James Cook Drive, Douglas QLD 4814",
        "description": "JCU's main campus in Townsville, tropical North Queensland. Near the Great Barrier Reef.",
        "facilities": "Library, Marine Research Facilities, Medical School, AITHM, Student Village, Sport",
        "map_url": "https://maps.google.com/?q=James+Cook+University+Townsville",
    },
    {
        "name": "Cairns Campus",
        "city": "Cairns",
        "state": "Queensland",
        "is_main": False,
        "address": "14-88 McGregor Road, Smithfield QLD 4878",
        "description": "JCU's Cairns campus, gateway to the Daintree Rainforest and Great Barrier Reef.",
        "facilities": "Library, Health Sciences, Environmental Research, Computer Labs",
    },
]

JCU_COURSES = [
    {
        "name": "Bachelor of Marine Biology",
        "level": "bachelor",
        "field_of_study": "Marine Biology / Environmental Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 34000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent. Biology and Chemistry recommended.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Marine Biologist, Reef Researcher, Conservation Scientist, Environmental Consultant",
        "description": "World-class marine biology degree with field research on the Great Barrier Reef. Globally top-ranked in the field.",
        "official_url": "https://www.jcu.edu.au/courses-and-study/courses/bachelor-of-marine-biology",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, IT Consultant, Data Analyst, Network Engineer",
        "description": "IT degree in tropical Australia with cybersecurity, data analytics, and software development majors.",
        "official_url": "https://www.jcu.edu.au/courses-and-study/courses/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Data Science",
        "level": "master",
        "field_of_study": "Data Science",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 32000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT, Science, or Maths with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Data Scientist, Machine Learning Engineer, Business Intelligence Analyst",
        "description": "Advanced data science applying big data to tropical ecology, health, and business problems.",
        "official_url": "https://www.jcu.edu.au/courses-and-study/courses/master-of-data-science",
    },
]

JCU_SCHOLARSHIPS = [
    {
        "name": "JCU International Student Scholarship",
        "type": "merit",
        "coverage": "15%–25% tuition fee reduction (tiered)",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate or postgraduate study at JCU.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.jcu.edu.au/scholarships/jcu-international-student-scholarship",
        "description": "JCU's tiered merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF SOUTHERN QUEENSLAND (UniSQ)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_UNISQ = {
    "name": "University of Southern Queensland",
    "short_name": "UniSQ",
    "type": "public",
    "group": "raa",
    "established": 1967,
    "state": "Queensland",
    "city": "Toowoomba",
    "description": (
        "UniSQ (formerly University of Southern Queensland) is a leading regional university "
        "with campuses in Toowoomba, Ipswich, and Springfield (Brisbane), and a strong online presence. "
        "UniSQ is particularly known for engineering, IT, education, business, and agriculture. "
        "The university operates one of Australia's most advanced agricultural research facilities "
        "and is a leader in flexible online education."
    ),
    "about": (
        "Toowoomba, Queensland's second-largest inland city, offers an affordable and relaxed lifestyle. "
        "UniSQ's Springfield campus gives students access to Brisbane's south-west growth corridor. "
        "The university has a strong reputation in engineering and space technology research."
    ),
    "ranking_qs": "801–1000 World (QS 2025)",
    "total_students": "30,000+",
    "international_students": "5,000+",
    "cost_of_living": "AUD 1,300–1,800/month",
    "popular_courses": "Engineering, IT, Business, Education, Nursing, Agriculture",
    "official_website": "https://www.unisq.edu.au",
    "international_page": "https://www.unisq.edu.au/international",
    "scholarship_page": "https://www.unisq.edu.au/study/fees-scholarships/scholarships",
    "application_portal": "https://www.unisq.edu.au/study/apply",
}

UNISQ_CAMPUSES = [
    {
        "name": "Toowoomba Campus",
        "city": "Toowoomba",
        "state": "Queensland",
        "is_main": True,
        "address": "West Street, Toowoomba QLD 4350",
        "description": "UniSQ's main campus in the Garden City of Toowoomba, 130 km west of Brisbane.",
        "facilities": "Library, Engineering Labs, Agricultural Research, Student Accommodation",
        "map_url": "https://maps.google.com/?q=University+of+Southern+Queensland+Toowoomba",
    },
    {
        "name": "Springfield Campus",
        "city": "Springfield",
        "state": "Queensland",
        "is_main": False,
        "address": "37 Sinnathamby Boulevard, Springfield Central QLD 4300",
        "description": "Modern campus in Brisbane's fast-growing south-west corridor.",
        "facilities": "Library, IT Labs, Business School, Student Services",
    },
]

UNISQ_COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 72 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Civil, Mechanical, Electrical, Agricultural Engineer",
        "description": "Engineers Australia accredited. Strong agricultural and civil engineering streams.",
        "official_url": "https://www.unisq.edu.au/study/degrees/bachelor-of-engineering-honours",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28400,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "IT Manager, Data Analyst, Cybersecurity Analyst",
        "description": "Advanced IT available fully online or on-campus with cybersecurity and data science focus.",
        "official_url": "https://www.unisq.edu.au/study/degrees/master-of-information-technology",
        "is_popular": True,
    },
]

UNISQ_SCHOLARSHIPS = [
    {
        "name": "UniSQ International Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at UniSQ.",
        "academic_requirement": "Minimum 70% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.unisq.edu.au/study/fees-scholarships/scholarships/international",
        "description": "UniSQ's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF THE SUNSHINE COAST (UniSC)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_UNISC = {
    "name": "University of the Sunshine Coast",
    "short_name": "UniSC",
    "type": "public",
    "group": "raa",
    "established": 1996,
    "state": "Queensland",
    "city": "Sunshine Coast",
    "description": (
        "UniSC (formerly University of the Sunshine Coast) is a young, dynamic university "
        "on Queensland's beautiful Sunshine Coast. With campuses at Sippy Downs, Noosa, "
        "Caboolture, Fraser Coast, and Moreton Bay, UniSC serves South East Queensland's "
        "fast-growing coastal communities. Known for its innovative teaching, sustainability "
        "focus, and strengths in health, business, education, IT, and engineering."
    ),
    "about": (
        "UniSC's Sippy Downs campus, a short drive from the beach, offers a relaxed coastal "
        "lifestyle with modern facilities. The university is known for its high student "
        "satisfaction ratings and genuine community connection. UniSC is one of Australia's "
        "fastest-growing universities."
    ),
    "ranking_qs": "651–700 World (QS 2025)",
    "total_students": "17,000+",
    "international_students": "3,000+",
    "cost_of_living": "AUD 1,600–2,200/month",
    "popular_courses": "Business, Nursing, Education, Engineering, IT, Sustainability, Tourism",
    "official_website": "https://www.unisc.edu.au",
    "international_page": "https://www.unisc.edu.au/study/international-students",
    "scholarship_page": "https://www.unisc.edu.au/study/costs-and-scholarships/scholarships",
    "application_portal": "https://www.unisc.edu.au/study/how-to-apply",
}

UNISC_CAMPUSES = [
    {
        "name": "Sippy Downs Campus",
        "city": "Sunshine Coast",
        "state": "Queensland",
        "is_main": True,
        "address": "90 Sippy Downs Drive, Sippy Downs QLD 4556",
        "description": "UniSC's main campus in Sippy Downs, 15 minutes from Mooloolaba Beach.",
        "facilities": "Library, Health Sciences, Engineering Labs, Student Accommodation, Sports Facilities",
        "map_url": "https://maps.google.com/?q=University+of+Sunshine+Coast+Sippy+Downs",
    },
    {
        "name": "Noosa Campus",
        "city": "Noosa",
        "state": "Queensland",
        "is_main": False,
        "address": "Cnr Eenie Creek Road & Noosa Parade, Noosaville QLD 4566",
        "description": "Boutique campus in the beautiful Noosa region for selected programs.",
        "facilities": "Library, Lecture Rooms, Student Services",
    },
]

UNISC_COURSES = [
    {
        "name": "Bachelor of Business",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 26800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 62 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Business Manager, Marketing Specialist, Accountant, Entrepreneur",
        "description": "Sunshine Coast business degree with majors in Marketing, Accounting, Finance, and Management.",
        "official_url": "https://www.unisc.edu.au/study/find-a-course/business",
        "is_popular": True,
    },
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
        "career_outcomes": "Software Developer, Data Analyst, IT Consultant, Cybersecurity Analyst",
        "description": "Practical IT degree on the Sunshine Coast with majors in cybersecurity and data analytics.",
        "official_url": "https://www.unisc.edu.au/study/find-a-course/information-technology",
    },
]

UNISC_SCHOLARSHIPS = [
    {
        "name": "UniSC International Merit Scholarship",
        "type": "merit",
        "coverage": "20% tuition fee reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate or postgraduate study at UniSC.",
        "academic_requirement": "Minimum 70% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.unisc.edu.au/study/costs-and-scholarships/scholarships/international",
        "description": "UniSC's main merit scholarship for international students.",
    },
]
