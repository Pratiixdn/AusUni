"""
Australian National University (ANU) – Complete Data
Research-based, accurate as of 2024
Official source: https://www.anu.edu.au/
"""

UNIVERSITY = {
    "name": "Australian National University",
    "short_name": "ANU",
    "type": "public",
    "group": "go8",
    "established": 1946,
    "state": "ACT",
    "city": "Canberra",
    "description": (
        "The Australian National University is Australia's national research university and consistently "
        "ranks as Australia's #1 university. Founded by an act of parliament in 1946, ANU is uniquely "
        "positioned in Canberra – Australia's capital – offering unparalleled access to government, "
        "embassies, and policy institutions. ANU has produced more Australian prime ministers, "
        "Nobel laureates, and Rhodes Scholars than any other Australian university."
    ),
    "about": (
        "ANU's beautiful 358-hectare campus in the heart of Canberra is a bush capital delight. "
        "Known for its research excellence in politics, international relations, economics, law, science, "
        "and environment, ANU draws the best minds globally. If you're interested in policy, "
        "diplomacy, research, or public service, there is no better place in Australia."
    ),
    "ranking_qs": "#30 World (QS 2025)",
    "ranking_times": "#67 World (THE 2024)",
    "total_students": "25,000+",
    "international_students": "8,000+",
    "cost_of_living": "AUD 1,800–2,400/month",
    "popular_courses": "Politics, International Relations, Law, Economics, Computer Science, Engineering",
    "internship_info": (
        "ANU students have direct access to federal government departments, embassies, "
        "Parliament House, and major research institutes including CSIRO and AIHW. "
        "The ANU Careers & Employability Centre facilitates internship placements across sectors."
    ),
    "official_website": "https://www.anu.edu.au",
    "international_page": "https://www.anu.edu.au/study/apply/international-applicants",
    "scholarship_page": "https://www.anu.edu.au/study/scholarships",
    "application_portal": "https://www.anu.edu.au/study/apply",
}

CAMPUSES = [
    {
        "name": "Acton Campus",
        "city": "Canberra",
        "state": "ACT",
        "is_main": True,
        "address": "Acton ACT 2601, Australia",
        "description": (
            "ANU's main campus located in Acton, Canberra, covering 358 hectares of landscaped grounds. "
            "Features include the Chifley Library, ANU Museum of Art, residential colleges, "
            "and world-class research institutes."
        ),
        "facilities": "Chifley Library, ANU Museum of Art, Residential Colleges, Sports Union, Research School Buildings",
        "map_url": "https://maps.google.com/?q=Australian+National+University+Acton+Canberra",
    },
]

COURSES = [
    {
        "name": "Bachelor of Politics, Philosophy and Economics",
        "level": "bachelor",
        "field_of_study": "Politics / Philosophy / Economics",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 46500,
        "intake_months": "February",
        "academic_requirement": "ATAR 95+ or equivalent. Outstanding academic record.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 80,
        "career_outcomes": "Policy Officer, Diplomat, Economist, Political Adviser, Journalist, NGO Director",
        "description": "ANU's flagship social sciences program. Combines political theory, philosophy, and economics in Canberra's policy heartland.",
        "official_url": "https://www.anu.edu.au/study/courses/bachelor-of-politics-philosophy-economics",
        "is_popular": True,
    },
    {
        "name": "Bachelor of Computer Science (Advanced)",
        "level": "bachelor",
        "field_of_study": "Computer Science",
        "duration": "3 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 47900,
        "intake_months": "February",
        "academic_requirement": "ATAR 96+ or equivalent. Strong Maths background.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 80,
        "career_outcomes": "Software Engineer, AI Researcher, Cryptographer, Cybersecurity Specialist",
        "description": "Research-led CS degree with specialisations in AI, computer systems, and theory. Access to ANU's top-ranked CS research group.",
        "official_url": "https://www.anu.edu.au/study/courses/bachelor-of-advanced-computing",
        "is_popular": True,
    },
    {
        "name": "Master of Computing",
        "level": "master",
        "field_of_study": "Computer Science",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 47900,
        "intake_months": "February, July",
        "academic_requirement": "Bachelor's in CS/IT with minimum 65%.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 80,
        "career_outcomes": "Senior Developer, Research Scientist, AI Engineer, Tech Lead",
        "description": "ANU's postgraduate CS program with strong research and industry components.",
        "official_url": "https://www.anu.edu.au/study/courses/master-of-computing",
        "is_popular": True,
    },
    {
        "name": "Master of International Affairs",
        "level": "master",
        "field_of_study": "International Relations",
        "duration": "2 years",
        "study_mode": "full_time",
        "tuition_fee_annual": 43800,
        "intake_months": "February",
        "academic_requirement": "Bachelor's in any field with min 65%. Work experience preferred.",
        "ielts_overall": 6.5,
        "ielts_min_band": 6.0,
        "pte_overall": 58,
        "toefl_ibt": 80,
        "career_outcomes": "Diplomat, Policy Analyst, UN Officer, NGO Director, Government Adviser",
        "description": "Taught at the ANU Crawford School of Public Policy – ranked #1 in Australia and #7 globally for public policy.",
        "official_url": "https://www.anu.edu.au/study/courses/master-of-international-affairs",
    },
]

SCHOLARSHIPS = [
    {
        "name": "ANU Chancellor's International Scholarship",
        "type": "merit",
        "coverage": "35% tuition fee reduction for full degree",
        "coverage_percentage": 35,
        "eligibility": "High-achieving international students commencing undergraduate or postgraduate study.",
        "academic_requirement": "Outstanding academic record – equivalent to top 5% of graduating class",
        "eligible_levels": "Bachelor, Master",
        "eligible_courses": "All ANU programs",
        "deadline": "31 October (February intake)",
        "official_url": "https://www.anu.edu.au/study/scholarships/find-a-scholarship/anu-chancellors-international-scholarship",
        "description": "ANU's premier merit scholarship offering 35% tuition reduction.",
    },
    {
        "name": "ANU University Research Scholarship",
        "type": "merit",
        "coverage": "Full tuition + AUD 29,000 annual stipend",
        "coverage_percentage": 100,
        "eligibility": "International PhD/MPhil research students with exceptional research proposal.",
        "academic_requirement": "First-class honours or equivalent Master's degree",
        "eligible_levels": "PhD",
        "eligible_courses": "Research degrees",
        "deadline": "31 October (main round)",
        "official_url": "https://www.anu.edu.au/study/scholarships/find-a-scholarship/anu-university-research-scholarship",
        "description": "Full scholarship including tuition and living stipend for research degree candidates.",
    },
]
