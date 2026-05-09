"""
WA / SA / NT / TAS Universities – Complete Data
Covers: ECU, Murdoch, Notre Dame (WA), Adelaide University (merged),
        Flinders, Torrens, CDU, UTAS
Research-based, accurate as of 2025–2026
"""

# ──────────────────────────────────────────────────────────────
# EDITH COWAN UNIVERSITY (ECU) – Western Australia
# ──────────────────────────────────────────────────────────────
UNIVERSITY_ECU = {
    "name": "Edith Cowan University",
    "short_name": "ECU",
    "type": "public",
    "group": "irua",
    "established": 1991,
    "state": "Western Australia",
    "city": "Perth",
    "description": (
        "Edith Cowan University is a student-centred university in Perth, WA, with campuses "
        "in Joondalup, Mount Lawley, and Bunbury. A member of the Innovative Research Universities "
        "group, ECU consistently ranks among the world's top 300 young universities. "
        "Renowned for nursing, cybersecurity, creative arts, education, and engineering, "
        "ECU has over 33,000 students including a significant international cohort."
    ),
    "about": (
        "ECU's Joondalup campus is located 25 km north of Perth CBD in a growing commercial precinct. "
        "The university is particularly noted for its world-class Cybersecurity Cooperative Research Centre "
        "and one of Australia's best nursing programs. ECU has a strong commitment to equity and "
        "community engagement in Western Australia."
    ),
    "ranking_qs": "#336 World (QS 2025)",
    "ranking_times": "#401–500 World (THE 2024)",
    "total_students": "33,000+",
    "international_students": "9,000+",
    "cost_of_living": "AUD 1,800–2,500/month",
    "popular_courses": "Nursing, Cybersecurity, Education, Engineering, Creative Arts, Business, IT",
    "internship_info": (
        "ECU's Cybersecurity Cooperative Research Centre (CRC) connects IT students with "
        "government and industry. Nursing students have clinical placements at Joondalup Health Campus "
        "and major Perth hospitals."
    ),
    "official_website": "https://www.ecu.edu.au",
    "international_page": "https://www.ecu.edu.au/future-students/international",
    "scholarship_page": "https://www.ecu.edu.au/scholarships",
    "application_portal": "https://www.ecu.edu.au/future-students/apply",
}

ECU_CAMPUSES = [
    {
        "name": "Joondalup Campus",
        "city": "Perth",
        "state": "Western Australia",
        "is_main": True,
        "address": "270 Joondalup Drive, Joondalup WA 6027",
        "description": "ECU's main campus, 25 km north of Perth CBD, adjacent to Joondalup City Centre.",
        "facilities": "Library, Cybersecurity Lab, Nursing Simulation Centre, Student Hub, Sport Facilities",
        "map_url": "https://maps.google.com/?q=Edith+Cowan+University+Joondalup",
    },
    {
        "name": "Mount Lawley Campus",
        "city": "Perth",
        "state": "Western Australia",
        "is_main": False,
        "address": "2 Bradford Street, Mount Lawley WA 6050",
        "description": "Arts, education, and creative industries campus 5 km north-east of Perth CBD.",
        "facilities": "Arts Studios, Education Faculty, Library, Chapels",
    },
]

ECU_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Hospital Nurse, Community Health Nurse, Nurse Manager",
        "description": "ANMAC-accredited with clinical placements at Joondalup Health Campus and major Perth hospitals.",
        "official_url": "https://www.ecu.edu.au/degrees/courses/bachelor-of-nursing",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Science (Cybersecurity)",
        "level": "bachelor",
        "field_of_study": "Cybersecurity",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31200,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 68 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Cybersecurity Analyst, Penetration Tester, Security Architect, Digital Forensics Investigator",
        "description": "Backed by ECU's Security Research Institute and Cybersecurity CRC. Top-ranked in WA for cybersecurity.",
        "official_url": "https://www.ecu.edu.au/degrees/courses/bachelor-of-science-cybersecurity",
        "is_popular": True,
    },
    {
        "name": "Master of Cybersecurity",
        "level": "master",
        "field_of_study": "Cybersecurity",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33600,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT, CS, or Engineering with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Cybersecurity Lead, SOC Manager, Security Architect, CISO",
        "description": "Advanced cybersecurity degree backed by ECU's internationally recognised research centre.",
        "official_url": "https://www.ecu.edu.au/degrees/courses/master-of-cybersecurity",
        "is_popular": True,
    },
]

ECU_SCHOLARSHIPS = [
    {
        "name": "ECU International Student Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at ECU.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based – automatic consideration",
        "intake_deadline": True,
        "official_url": "https://www.ecu.edu.au/scholarships/international",
        "description": "ECU's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# MURDOCH UNIVERSITY – Western Australia
# ──────────────────────────────────────────────────────────────
UNIVERSITY_MURDOCH = {
    "name": "Murdoch University",
    "short_name": "Murdoch",
    "type": "public",
    "group": "none",
    "established": 1975,
    "state": "Western Australia",
    "city": "Perth",
    "description": (
        "Murdoch University is a progressive public university in Perth's southern suburbs, "
        "with a main campus in Murdoch and a campus in Mandurah. Known for veterinary science, "
        "law, health sciences, business, engineering, and environmental science. "
        "Murdoch has a strong international student community and emphasises sustainability "
        "and real-world learning."
    ),
    "about": (
        "Murdoch's main campus is adjacent to Fremantle's vibrant culture and Perth's "
        "southern suburbs. The university is particularly renowned for its Veterinary School "
        "— one of only two in WA — and its Harry Perkins Institute for Medical Research partnership."
    ),
    "ranking_qs": "531–540 World (QS 2025)",
    "total_students": "22,000+",
    "international_students": "9,000+",
    "cost_of_living": "AUD 1,800–2,500/month",
    "popular_courses": "Veterinary Science, Law, IT, Business, Engineering, Psychology, Nursing",
    "official_website": "https://www.murdoch.edu.au",
    "international_page": "https://www.murdoch.edu.au/study/international-students",
    "scholarship_page": "https://www.murdoch.edu.au/study/scholarships",
    "application_portal": "https://www.murdoch.edu.au/study/apply",
}

MURDOCH_CAMPUSES = [
    {
        "name": "Murdoch Campus",
        "city": "Perth",
        "state": "Western Australia",
        "is_main": True,
        "address": "90 South Street, Murdoch WA 6150",
        "description": "Murdoch's main campus in Perth's southern suburbs, 17 km from the CBD.",
        "facilities": "Library, Veterinary Teaching Hospital, Engineering Labs, Animal Health Centre, Student Housing",
        "map_url": "https://maps.google.com/?q=Murdoch+University+Perth",
    },
]

MURDOCH_COURSES = [
    {
        "name": "Bachelor of Veterinary Biology / Doctor of Veterinary Medicine",
        "level": "bachelor",
        "field_of_study": "Veterinary Science",
        "duration": "5 years (double degree)",
        "study_mode": "full_time",
        "tuition_fee_annual": 56700,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 90+ or equivalent. Biology and Chemistry required.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Veterinarian, Animal Scientist, Zoo Vet, Agricultural Vet, Researcher",
        "description": "One of only two veterinary schools in WA. Accredited by the AVBC. Students work in Murdoch's on-campus Veterinary Teaching Hospital.",
        "official_url": "https://www.murdoch.edu.au/study/courses/ug-bachelor-veterinary-biology-doctor-veterinary-medicine",
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
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, Cybersecurity Analyst, Data Analyst, IT Manager",
        "description": "Industry-relevant IT degree with cybersecurity, data analytics, and cloud computing specialisations.",
        "official_url": "https://www.murdoch.edu.au/study/courses/ug-bachelor-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "1.5–2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 32800,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Cybersecurity Lead, Data Scientist, Solutions Architect",
        "description": "Advanced IT with specialisations in cybersecurity and data analytics.",
        "official_url": "https://www.murdoch.edu.au/study/courses/pg-master-information-technology",
    },
]

MURDOCH_SCHOLARSHIPS = [
    {
        "name": "Murdoch International Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition fee reduction",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.murdoch.edu.au/study/scholarships/international",
        "description": "Murdoch's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF NOTRE DAME AUSTRALIA – Western Australia
# ──────────────────────────────────────────────────────────────
UNIVERSITY_NOTREDAME = {
    "name": "The University of Notre Dame Australia",
    "short_name": "Notre Dame",
    "type": "private",
    "group": "none",
    "established": 1989,
    "state": "Western Australia",
    "city": "Perth",
    "description": (
        "The University of Notre Dame Australia is a private Catholic university with campuses "
        "in Fremantle, Broome, and Sydney. Founded in 1989, Notre Dame offers degrees in "
        "medicine, nursing, philosophy, theology, law, business, education, and arts. "
        "The university is distinguished by small class sizes, personal mentoring, and a "
        "Catholic intellectual tradition that values faith, reason, and service."
    ),
    "about": (
        "Notre Dame's Fremantle campus occupies a stunning heritage precinct in the heart of "
        "Old Fremantle — one of Australia's best-preserved Victorian port towns. "
        "The university's medical school is particularly renowned, producing graduates "
        "who serve regional and remote communities across WA."
    ),
    "total_students": "12,000+",
    "international_students": "1,500+",
    "cost_of_living": "AUD 1,800–2,500/month",
    "popular_courses": "Medicine, Nursing, Law, Business, Education, Theology, Philosophy",
    "official_website": "https://www.notredame.edu.au",
    "international_page": "https://www.notredame.edu.au/study/international-students",
    "scholarship_page": "https://www.notredame.edu.au/study/student-services/scholarships",
    "application_portal": "https://www.notredame.edu.au/study/apply",
}

NOTREDAME_CAMPUSES = [
    {
        "name": "Fremantle Campus",
        "city": "Perth",
        "state": "Western Australia",
        "is_main": True,
        "address": "19 Mouat Street, Fremantle WA 6160",
        "description": "Notre Dame's main campus in historic Fremantle, 20 km south of Perth CBD.",
        "facilities": "Library, Medical School, Nursing Simulation Centre, Chapel, Heritage Precinct",
        "map_url": "https://maps.google.com/?q=Notre+Dame+University+Fremantle",
    },
    {
        "name": "Sydney Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "104 Broadway, Chippendale NSW 2008",
        "description": "Notre Dame's Sydney campus near the University of Sydney, specialising in medicine, nursing, and education.",
        "facilities": "Medical School, Nursing Labs, Library, Chapel",
    },
]

NOTREDAME_COURSES = [
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28800,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Hospital Nurse, Community Health Nurse",
        "description": "ANMAC-accredited nursing in a values-based, faith-informed environment.",
        "official_url": "https://www.notredame.edu.au/study/courses/bachelor-of-nursing",
    },
    {
        "name": "Bachelor of Business Administration",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 26400,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 65 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Business Manager, HR Manager, Marketing Specialist, Project Manager",
        "description": "Ethics-centred business degree with majors in Accounting, Management, Marketing, and HR.",
        "official_url": "https://www.notredame.edu.au/study/courses/bachelor-of-business-administration",
    },
]

NOTREDAME_SCHOLARSHIPS = [
    {
        "name": "Notre Dame International Student Scholarship",
        "type": "merit",
        "coverage": "20% tuition fee reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate study at Notre Dame.",
        "academic_requirement": "Good academic standing",
        "eligible_levels": "Bachelor",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.notredame.edu.au/study/student-services/scholarships",
        "description": "Notre Dame's scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# ADELAIDE UNIVERSITY – South Australia (NEW 2026 Merger)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_ADELAIDE = {
    "name": "Adelaide University",
    "short_name": "Adelaide",
    "type": "public",
    "group": "go8",
    "established": 2026,
    "state": "South Australia",
    "city": "Adelaide",
    "description": (
        "Adelaide University is the newly merged entity formed in 2026 through the historic "
        "amalgamation of the University of Adelaide (est. 1874) and the University of South "
        "Australia (est. 1991). As a Group of Eight member (inheriting the University of Adelaide's "
        "status), Adelaide University is South Australia's premier research institution and one of "
        "Australia's largest universities, with over 80,000 students. "
        "The merger combines the research prestige of the University of Adelaide with the industry "
        "focus and scale of UniSA."
    ),
    "about": (
        "Adelaide University inherits a dual legacy: the University of Adelaide's North Terrace "
        "heritage campus and the University of South Australia's City West, City East, Mawson Lakes, "
        "and Magill campuses. Adelaide itself offers exceptional quality of life, an affordable "
        "lifestyle, and world-class food and wine culture. The merged university is set to be "
        "Australia's third-largest university."
    ),
    "ranking_qs": "Top 100 World (inheriting University of Adelaide legacy – QS 2025)",
    "ranking_times": "#101–125 World (THE 2024, University of Adelaide legacy)",
    "total_students": "80,000+",
    "international_students": "22,000+",
    "cost_of_living": "AUD 1,600–2,200/month",
    "popular_courses": "Engineering, Medicine, Law, Business, IT, Wine Science, Architecture, Nursing",
    "internship_info": (
        "Adelaide University's merged structure provides extraordinary industry connections, "
        "combining the University of Adelaide's ties to defence, mining, wine, and government, "
        "with UniSA's partnerships in health, education, and tech industries. "
        "The new university is developing the Adelaide University Village in the heart of the CBD."
    ),
    "official_website": "https://adelaide.edu.au",
    "international_page": "https://adelaide.edu.au/study/international",
    "scholarship_page": "https://adelaide.edu.au/scholarships",
    "application_portal": "https://adelaide.edu.au/apply",
}

ADELAIDE_CAMPUSES = [
    {
        "name": "North Terrace Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": True,
        "address": "North Terrace, Adelaide SA 5005",
        "description": "Heritage sandstone campus on Adelaide's cultural boulevard, inherited from the University of Adelaide.",
        "facilities": "Barr Smith Library, Bonython Hall, Engineering Precinct, Medical School, Law School",
        "map_url": "https://maps.google.com/?q=University+of+Adelaide+North+Terrace",
    },
    {
        "name": "City West Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": False,
        "address": "55 North Terrace, Adelaide SA 5000",
        "description": "Modern city campus inherited from UniSA. Business, design, and health programs.",
        "facilities": "Jeffrey Smart Building, Business School, Design Studios, Library",
    },
    {
        "name": "Mawson Lakes Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": False,
        "address": "Mawson Lakes Boulevard, Mawson Lakes SA 5095",
        "description": "Technology and engineering campus in Adelaide's north, adjacent to the Technology Park.",
        "facilities": "Engineering Labs, IT Facilities, Science Precinct",
    },
    {
        "name": "Magill Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": False,
        "address": "St Bernards Road, Magill SA 5072",
        "description": "Education and arts campus in Adelaide's eastern suburbs.",
        "facilities": "Education Faculty, Arts Studios, Library",
    },
]

ADELAIDE_COURSES = [
    {
        "name": "Bachelor of Engineering (Honours)",
        "level": "honours",
        "field_of_study": "Engineering",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 43000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 85 or equivalent. Maths and Physics required.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Civil, Mechanical, Electrical, Mining, Chemical, Aerospace Engineer",
        "description": "Engineers Australia accredited. Strong defence, mining, and oil/gas industry links in SA.",
        "official_url": "https://adelaide.edu.au/degrees/bachelor-of-engineering",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 36000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 75 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Engineer, Cybersecurity Analyst, Data Scientist, IT Manager",
        "description": "Combined IT capability from both legacy universities with industry-led projects.",
        "official_url": "https://adelaide.edu.au/degrees/bachelor-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 39000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 65%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Solutions Architect, Data Scientist, AI Engineer",
        "description": "Advanced IT combining the research strengths of both legacy universities.",
        "official_url": "https://adelaide.edu.au/degrees/master-of-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration (MBA)",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 42000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree + minimum 3 years work experience.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Senior Manager, Director, Entrepreneur, Consultant",
        "description": "Adelaide MBA combining the AACSB-accredited Adelaide Business School with UniSA Business School strength.",
        "official_url": "https://adelaide.edu.au/degrees/master-of-business-administration",
    },
    {
        "name": "Bachelor of Wine Science",
        "level": "bachelor",
        "field_of_study": "Wine Science / Viticulture",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 38000,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 70 or equivalent. Chemistry recommended.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Winemaker, Viticulturist, Wine Scientist, Wine Educator, Wine Consultant",
        "description": "The world-renowned Waite Campus wine science program, in the heart of Australia's wine country.",
        "official_url": "https://adelaide.edu.au/degrees/bachelor-of-wine-science",
        "is_popular": True,
    },
]

ADELAIDE_SCHOLARSHIPS = [
    {
        "name": "Adelaide University International Excellence Scholarship",
        "type": "merit",
        "coverage": "25%–50% tuition reduction (tiered by merit)",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at Adelaide University.",
        "academic_requirement": "Minimum 80% for 25%; 85%+ for higher tiers",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://adelaide.edu.au/scholarships/international",
        "description": "Adelaide University's tiered merit scholarship for international students.",
    },
    {
        "name": "Adelaide University Research Scholarship",
        "type": "merit",
        "coverage": "Full tuition + AUD 29,500 annual living stipend",
        "coverage_percentage": 100,
        "eligibility": "International PhD/MPhil research students with outstanding research proposal.",
        "academic_requirement": "First-class honours or equivalent Master's degree",
        "eligible_levels": "PhD",
        "eligible_courses": "Research degrees",
        "deadline": "31 October (main round)",
        "official_url": "https://adelaide.edu.au/scholarships/postgrad-research",
        "description": "Full research scholarship including tuition and living stipend for doctoral students.",
    },
]

# ──────────────────────────────────────────────────────────────
# FLINDERS UNIVERSITY – South Australia
# ──────────────────────────────────────────────────────────────
UNIVERSITY_FLINDERS = {
    "name": "Flinders University",
    "short_name": "Flinders",
    "type": "public",
    "group": "irua",
    "established": 1966,
    "state": "South Australia",
    "city": "Adelaide",
    "description": (
        "Flinders University is a research university ranked in the global top 400, located "
        "in Bedford Park, southern Adelaide. A member of the Innovative Research Universities group, "
        "Flinders is known for medicine, health, law, education, engineering, IT, and the arts. "
        "The university has a strong social justice ethos and is particularly respected for "
        "its medical research, especially in ageing, palliative care, and cancer biology."
    ),
    "about": (
        "Flinders' Bedford Park campus sits on the southern slopes of the Adelaide Hills, "
        "20 km from the CBD. The Tonsley campus, purpose-built in a former Mitsubishi plant, "
        "is a thriving innovation hub for engineering and IT. Flinders is notable for "
        "its collaborative industry relationships and high graduate employment rates."
    ),
    "ranking_qs": "#384 World (QS 2025)",
    "ranking_times": "#401–500 World (THE 2024)",
    "total_students": "30,000+",
    "international_students": "8,000+",
    "cost_of_living": "AUD 1,600–2,200/month",
    "popular_courses": "Medicine, Nursing, Law, IT, Engineering, Education, Psychology",
    "official_website": "https://www.flinders.edu.au",
    "international_page": "https://www.flinders.edu.au/study/international",
    "scholarship_page": "https://www.flinders.edu.au/study/fees-scholarships/scholarships",
    "application_portal": "https://www.flinders.edu.au/study/apply",
}

FLINDERS_CAMPUSES = [
    {
        "name": "Bedford Park Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": True,
        "address": "Sturt Road, Bedford Park SA 5042",
        "description": "Flinders' main campus in southern Adelaide on the slopes of the Adelaide Hills.",
        "facilities": "Medical Centre, Law School, Library, Flinders Living, Student Hub",
        "map_url": "https://maps.google.com/?q=Flinders+University+Bedford+Park+Adelaide",
    },
    {
        "name": "Tonsley Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": False,
        "address": "1284 South Road, Tonsley SA 5042",
        "description": "Innovative technology campus in repurposed Mitsubishi manufacturing plant.",
        "facilities": "Engineering Labs, IT Facilities, Industry Co-location Hub",
    },
]

FLINDERS_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 33000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 68 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Software Developer, Cybersecurity Analyst, Data Analyst, IT Consultant",
        "description": "Industry-focused IT at Flinders Tonsley campus — purpose-built innovation hub with industry co-tenants.",
        "official_url": "https://www.flinders.edu.au/study/courses/bachelor-information-technology",
        "is_popular": True,
    },
    {
        "name": "Master of Information Technology",
        "level": "master",
        "field_of_study": "Information Technology",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 36000,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in IT or related field with minimum 60%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "IT Manager, Cloud Architect, Data Scientist, Cybersecurity Lead",
        "description": "Advanced IT at Tonsley Innovation District. Strong AI and cybersecurity focus.",
        "official_url": "https://www.flinders.edu.au/study/courses/master-information-technology",
    },
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 30800,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 70 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Hospital Nurse, Community Nurse, Aged Care Nurse",
        "description": "ANMAC-accredited. Clinical placements at Flinders Medical Centre and SA hospitals.",
        "official_url": "https://www.flinders.edu.au/study/courses/bachelor-nursing",
        "is_popular": True,
    },
]

FLINDERS_SCHOLARSHIPS = [
    {
        "name": "Flinders International Excellence Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction for full program",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at Flinders.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.flinders.edu.au/study/fees-scholarships/scholarships/international",
        "description": "Flinders' primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# TORRENS UNIVERSITY AUSTRALIA – South Australia
# ──────────────────────────────────────────────────────────────
UNIVERSITY_TORRENS = {
    "name": "Torrens University Australia",
    "short_name": "Torrens",
    "type": "private",
    "group": "none",
    "established": 2014,
    "state": "South Australia",
    "city": "Adelaide",
    "description": (
        "Torrens University Australia is a private university with campuses in Adelaide, "
        "Brisbane, Melbourne, and Sydney. Founded in 2014, Torrens is known for its "
        "industry-focused programs in business, design, health, education, media, and IT. "
        "The university uses a project-based learning model and small class sizes to "
        "deliver practical, career-ready education."
    ),
    "about": (
        "Torrens operates multiple brands including Billy Blue College of Design and "
        "Think Education Group. Its campuses are typically located in city CBDs, "
        "providing immediate access to industry. Torrens is particularly popular for "
        "creative industries, business, and health programs."
    ),
    "total_students": "12,000+",
    "international_students": "5,000+",
    "cost_of_living": "AUD 1,600–2,200/month (Adelaide); AUD 2,000–3,000/month (Sydney/Melbourne)",
    "popular_courses": "Business, Design, IT, Health Sciences, Media, Education",
    "official_website": "https://www.torrens.edu.au",
    "international_page": "https://www.torrens.edu.au/international",
    "scholarship_page": "https://www.torrens.edu.au/scholarships",
    "application_portal": "https://www.torrens.edu.au/apply",
}

TORRENS_CAMPUSES = [
    {
        "name": "Adelaide Campus",
        "city": "Adelaide",
        "state": "South Australia",
        "is_main": True,
        "address": "88 Wakefield Street, Adelaide SA 5000",
        "description": "Torrens' Adelaide CBD campus in the heart of the city.",
        "facilities": "Design Studios, Computer Labs, Student Hub, Library",
        "map_url": "https://maps.google.com/?q=Torrens+University+Adelaide",
    },
    {
        "name": "Sydney Campus",
        "city": "Sydney",
        "state": "New South Wales",
        "is_main": False,
        "address": "Level 1, 220 George Street, Sydney NSW 2000",
        "description": "Torrens' Sydney CBD campus near Circular Quay.",
        "facilities": "Design Studios, Computer Labs, Student Services",
    },
    {
        "name": "Melbourne Campus",
        "city": "Melbourne",
        "state": "Victoria",
        "is_main": False,
        "address": "Level 1, 11 Bouverie Street, Carlton VIC 3053",
        "description": "Torrens' Melbourne campus near Melbourne CBD.",
        "facilities": "Design Studios, IT Labs, Student Hub",
    },
]

TORRENS_COURSES = [
    {
        "name": "Bachelor of Business Administration",
        "level": "bachelor",
        "field_of_study": "Business",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 24000,
        "intake_months": "February, May, September",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Business Manager, Marketing Manager, Project Manager, HR Manager",
        "description": "Project-based business degree with majors in Marketing, Management, Entrepreneurship, and Finance.",
        "official_url": "https://www.torrens.edu.au/courses/business/bachelor-of-business-administration",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 26400,
        "intake_months": "February, May, September",
        "academic_requirement": "Bachelor's degree + 2 years work experience.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Senior Manager, Business Director, Consultant, Entrepreneur",
        "description": "Affordable MBA with flexible study and industry-project focus.",
        "official_url": "https://www.torrens.edu.au/courses/business/master-of-business-administration",
        "is_popular": True,
    },
]

TORRENS_SCHOLARSHIPS = [
    {
        "name": "Torrens International Scholarship",
        "type": "merit",
        "coverage": "20% tuition reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate or postgraduate study at Torrens.",
        "academic_requirement": "Good academic standing",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.torrens.edu.au/scholarships",
        "description": "Torrens University's merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# CHARLES DARWIN UNIVERSITY (CDU) – Northern Territory
# ──────────────────────────────────────────────────────────────
UNIVERSITY_CDU = {
    "name": "Charles Darwin University",
    "short_name": "CDU",
    "type": "public",
    "group": "raa",
    "established": 2003,
    "state": "Northern Territory",
    "city": "Darwin",
    "description": (
        "Charles Darwin University is the Northern Territory's only university, with campuses "
        "in Darwin and Alice Springs. CDU is a dual-sector institution offering vocational (TAFE) "
        "and higher education in a unique tropical environment. "
        "Known for its Indigenous Australian studies, environment, health, business, and engineering programs. "
        "CDU plays a critical role in educating NT communities and has a strong focus on "
        "Indigenous Australian engagement and remote learning."
    ),
    "about": (
        "Darwin is a multicultural tropical city with a vibrant outdoor lifestyle, "
        "close to Kakadu National Park, Litchfield, and Asia. CDU students enjoy a "
        "unique study environment unlike anywhere else in Australia. "
        "The university has significant defence connections through its proximity to "
        "RAAF Base Darwin and Robertson Barracks."
    ),
    "total_students": "22,000+",
    "international_students": "2,000+",
    "cost_of_living": "AUD 1,500–2,000/month",
    "popular_courses": "Nursing, Education, Business, Engineering, IT, Indigenous Studies, Environmental Science",
    "official_website": "https://www.cdu.edu.au",
    "international_page": "https://www.cdu.edu.au/international",
    "scholarship_page": "https://www.cdu.edu.au/scholarships",
    "application_portal": "https://www.cdu.edu.au/future-students/apply",
}

CDU_CAMPUSES = [
    {
        "name": "Casuarina Campus (Darwin)",
        "city": "Darwin",
        "state": "Northern Territory",
        "is_main": True,
        "address": "Ellengowan Drive, Casuarina NT 0810",
        "description": "CDU's main campus in Casuarina, 9 km north of Darwin CBD. Tropical setting with modern facilities.",
        "facilities": "Library, Engineering Precinct, Health Sciences, TAFE Facilities, Student Housing",
        "map_url": "https://maps.google.com/?q=Charles+Darwin+University+Casuarina+Darwin",
    },
    {
        "name": "Alice Springs Campus",
        "city": "Alice Springs",
        "state": "Northern Territory",
        "is_main": False,
        "address": "93 Greatorex Road, Alice Springs NT 0870",
        "description": "CDU campus in Alice Springs, Red Centre. Strong focus on Indigenous community engagement.",
        "facilities": "Library, TAFE Facilities, Community Learning Spaces",
    },
]

CDU_COURSES = [
    {
        "name": "Bachelor of Information Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 24800,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, Network Engineer, IT Consultant, Systems Administrator",
        "description": "Affordable IT degree in tropical Darwin. Available on-campus and online.",
        "official_url": "https://www.cdu.edu.au/study/course/bachelor-information-technology-bitec1",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Nursing",
        "level": "bachelor",
        "field_of_study": "Nursing",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 25600,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 7.0,
        "ielts_min_band": 7.0,
        "pte_overall": 65,
        "toefl_ibt": 94,
        "career_outcomes": "Registered Nurse, Remote Area Nurse, Hospital Nurse, Community Health Nurse",
        "description": "ANMAC-accredited. Unique opportunity for remote and tropical nursing placements across the NT.",
        "official_url": "https://www.cdu.edu.au/study/course/bachelor-nursing-bnurs1",
        "is_popular": True,
    },
]

CDU_SCHOLARSHIPS = [
    {
        "name": "CDU International Student Scholarship",
        "type": "merit",
        "coverage": "20% tuition reduction",
        "coverage_percentage": 20,
        "eligibility": "International students commencing undergraduate or postgraduate study at CDU.",
        "academic_requirement": "Minimum 65% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.cdu.edu.au/scholarships/international",
        "description": "CDU's primary merit scholarship for international students.",
    },
]

# ──────────────────────────────────────────────────────────────
# UNIVERSITY OF TASMANIA (UTAS)
# ──────────────────────────────────────────────────────────────
UNIVERSITY_UTAS = {
    "name": "University of Tasmania",
    "short_name": "UTAS",
    "type": "public",
    "group": "raa",
    "established": 1890,
    "state": "Tasmania",
    "city": "Hobart",
    "description": (
        "The University of Tasmania is one of Australia's oldest universities, founded in 1890 "
        "in Hobart. UTAS is a research-intensive university ranked in the global top 300 and "
        "known for its unique strengths in Antarctic and Southern Ocean research, marine science, "
        "law, business, health, engineering, and the arts. With campuses in Hobart, Launceston, "
        "and Burnie, UTAS serves all of Tasmania's communities."
    ),
    "about": (
        "Tasmania is one of the world's most pristine natural environments — a UNESCO World Heritage "
        "wilderness — making UTAS the ideal university for environmental and marine science. "
        "Hobart's quality of life, affordable housing, arts scene (MONA), and proximity to Antarctica "
        "make it a uniquely appealing study destination. UTAS hosts the Australian Antarctic Division headquarters."
    ),
    "ranking_qs": "#281 World (QS 2025)",
    "ranking_times": "#251–300 World (THE 2024)",
    "total_students": "26,000+",
    "international_students": "6,000+",
    "cost_of_living": "AUD 1,400–1,900/month",
    "popular_courses": "Marine Science, Environmental Science, Law, Business, Nursing, IT, Engineering",
    "internship_info": (
        "UTAS students access unique research opportunities through the Institute for Marine "
        "and Antarctic Studies (IMAS), the Menzies Institute for Medical Research, and "
        "partnerships with the Australian Antarctic Division and Tasmanian Government."
    ),
    "official_website": "https://www.utas.edu.au",
    "international_page": "https://www.utas.edu.au/international",
    "scholarship_page": "https://www.utas.edu.au/scholarships",
    "application_portal": "https://www.utas.edu.au/study/applications",
}

UTAS_CAMPUSES = [
    {
        "name": "Sandy Bay Campus (Hobart)",
        "city": "Hobart",
        "state": "Tasmania",
        "is_main": True,
        "address": "Private Bag 55, Hobart TAS 7001",
        "description": "UTAS's main campus in Sandy Bay, Hobart, overlooking the Derwent River.",
        "facilities": "Morris Miller Library, Law School, Engineering, Medical Research Centre, Student Union",
        "map_url": "https://maps.google.com/?q=University+of+Tasmania+Sandy+Bay+Hobart",
    },
    {
        "name": "Launceston Campus",
        "city": "Launceston",
        "state": "Tasmania",
        "is_main": False,
        "address": "Newnham Drive, Newnham TAS 7248",
        "description": "Major campus serving northern Tasmania with health, business, and education programs.",
        "facilities": "Nursing Simulation Centre, Agriculture, Student Housing, Library",
    },
    {
        "name": "Cradle Coast Campus (Burnie)",
        "city": "Burnie",
        "state": "Tasmania",
        "is_main": False,
        "address": "Mooreville Road, Burnie TAS 7320",
        "description": "Cradle Coast campus serving north-west Tasmania.",
        "facilities": "Library, Nursing Labs, Community Spaces",
    },
]

UTAS_COURSES = [
    {
        "name": "Bachelor of Marine and Antarctic Science",
        "level": "bachelor",
        "field_of_study": "Marine Science / Antarctic Studies",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 32800,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 68 or equivalent. Biology and Maths recommended.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Marine Scientist, Ocean Researcher, Environmental Consultant, Antarctic Scientist",
        "description": "One of the world's leading marine and Antarctic science programs. Students access the RV Investigator research vessel and work with the Australian Antarctic Division.",
        "official_url": "https://www.utas.edu.au/courses/college-of-sciences-and-engineering/courses/p3j-bachelor-of-marine-and-antarctic-science",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Information and Communication Technology",
        "level": "bachelor",
        "field_of_study": "Information Technology",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28000,
        "intake_months": "February, July",
        "academic_requirement": "Minimum ATAR 60 or equivalent.",
        "ielts_overall": 6.0,
        "ielts_min_band": 6.0,
        "pte_overall": 50,
        "toefl_ibt": 60,
        "career_outcomes": "Software Developer, Network Engineer, Data Analyst, IT Support Specialist",
        "description": "Affordable ICT degree in beautiful Tasmania with cybersecurity and data analytics majors.",
        "official_url": "https://www.utas.edu.au/courses/college-of-sciences-and-engineering/courses/k3a-bachelor-of-ict",
        "is_popular": True,
    },
    {
        "name": "Master of Business Administration",
        "level": "master",
        "field_of_study": "Business Administration",
        "duration": "1.5 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 31200,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's degree + 3 years work experience.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Senior Manager, Director, Consultant, Business Leader",
        "description": "Tasmania School of Business & Economics MBA with focus on sustainability and regional leadership.",
        "official_url": "https://www.utas.edu.au/courses/tsbe/courses/p3mba-master-of-business-administration",
    },
    {
        "name": "Bachelor of Laws (LLB)",
        "level": "bachelor",
        "field_of_study": "Law",
        "duration": "4 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 28800,
        "intake_months": "February",
        "academic_requirement": "Minimum ATAR 82 or equivalent.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 79,
        "career_outcomes": "Solicitor, Barrister, Legal Counsel, Magistrate, Policy Officer",
        "description": "One of Australia's oldest law schools (1893). Strong connections to Tasmanian judiciary and government.",
        "official_url": "https://www.utas.edu.au/courses/law/courses/p3l-bachelor-of-laws",
    },
]

UTAS_SCHOLARSHIPS = [
    {
        "name": "UTAS International Scholarship",
        "type": "merit",
        "coverage": "25% tuition reduction for full program",
        "coverage_percentage": 25,
        "eligibility": "International students commencing undergraduate or postgraduate study at UTAS.",
        "academic_requirement": "Minimum 75% in previous qualification",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "Most programs",
        "deadline": "Intake-based",
        "intake_deadline": True,
        "official_url": "https://www.utas.edu.au/scholarships/international",
        "description": "UTAS's primary merit scholarship for international students.",
    },
    {
        "name": "UTAS Research (Tasmania Graduate Research) Scholarship",
        "type": "merit",
        "coverage": "Full tuition + AUD 29,000 annual stipend",
        "coverage_percentage": 100,
        "eligibility": "International PhD and research master's students with outstanding research proposal.",
        "academic_requirement": "First-class honours or equivalent",
        "eligible_levels": "PhD",
        "eligible_courses": "Research degrees",
        "deadline": "31 October (main round)",
        "official_url": "https://www.utas.edu.au/scholarships/research",
        "description": "Full scholarship including tuition and living stipend for doctoral research students.",
    },
]
