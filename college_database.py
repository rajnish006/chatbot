1# ============================================================
#              CAREERPATH AI — COLLEGE DATABASE
#       College details, courses, and entrance exams
# ============================================================


# -------------------- COLLEGE DATABASE --------------------
# Each college has: name, location, type, courses, fees,
# placements, selection process, and website.

colleges = [

    # ---------- IITs (Engineering) ----------
    {
        "name": "IIT Bombay",
        "location": "Mumbai, Maharashtra",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "Ph.D.", "BS", "Dual Degree"],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Chemical", "Aerospace", "Civil", "Metallurgy"],
        "fees": "2-2.5 Lakh per year",
        "total_fees": "8-10 Lakh (4 years)",
        "placements": {
            "avg_package": "21 LPA",
            "highest_package": "2.3 Crore",
            "top_recruiters": ["Google", "Microsoft", "Goldman Sachs", "Amazon", "Apple"],
            "placement_rate": "95%",
        },
        "selection": "JEE Advanced rank",
        "entrance_exam": "JEE Advanced",
        "ranking": "NIRF #1 (Engineering)",
        "website": "www.iitb.ac.in",
    },
    {
        "name": "IIT Delhi",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "Ph.D.", "Dual Degree"],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Textile", "Chemical", "Biotech"],
        "fees": "2-2.5 Lakh per year",
        "total_fees": "8-10 Lakh (4 years)",
        "placements": {
            "avg_package": "20 LPA",
            "highest_package": "2.1 Crore",
            "top_recruiters": ["Google", "Microsoft", "Adobe", "Samsung", "Intel"],
            "placement_rate": "93%",
        },
        "selection": "JEE Advanced rank",
        "entrance_exam": "JEE Advanced",
        "ranking": "NIRF #2 (Engineering)",
        "website": "www.iitd.ac.in",
    },
    {
        "name": "IIT Madras",
        "location": "Chennai, Tamil Nadu",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MS", "Ph.D.", "Dual Degree"],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Chemical", "Aerospace", "Ocean Engineering"],
        "fees": "2-2.5 Lakh per year",
        "total_fees": "8-10 Lakh (4 years)",
        "placements": {
            "avg_package": "19 LPA",
            "highest_package": "1.8 Crore",
            "top_recruiters": ["Google", "Microsoft", "TCS", "Infosys", "Oracle"],
            "placement_rate": "94%",
        },
        "selection": "JEE Advanced rank",
        "entrance_exam": "JEE Advanced",
        "ranking": "NIRF #1 (Overall)",
        "website": "www.iitm.ac.in",
    },
    {
        "name": "IIT Kanpur",
        "location": "Kanpur, Uttar Pradesh",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "Ph.D."],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Chemical", "Aerospace"],
        "fees": "2-2.5 Lakh per year",
        "total_fees": "8-10 Lakh (4 years)",
        "placements": {
            "avg_package": "18 LPA",
            "highest_package": "1.5 Crore",
            "top_recruiters": ["Google", "Microsoft", "Uber", "Flipkart", "Samsung"],
            "placement_rate": "90%",
        },
        "selection": "JEE Advanced rank",
        "entrance_exam": "JEE Advanced",
        "ranking": "NIRF #4 (Engineering)",
        "website": "www.iitk.ac.in",
    },
    {
        "name": "IIT Kharagpur",
        "location": "Kharagpur, West Bengal",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "Law", "Ph.D.", "Dual Degree"],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Mining", "Ocean Engineering", "Architecture"],
        "fees": "2-2.5 Lakh per year",
        "total_fees": "8-10 Lakh (4 years)",
        "placements": {
            "avg_package": "16 LPA",
            "highest_package": "1.5 Crore",
            "top_recruiters": ["Google", "Amazon", "Goldman Sachs", "Microsoft", "TCS"],
            "placement_rate": "90%",
        },
        "selection": "JEE Advanced rank",
        "entrance_exam": "JEE Advanced",
        "ranking": "NIRF #5 (Engineering)",
        "website": "www.iitkgp.ac.in",
    },

    # ---------- NITs (Engineering) ----------
    {
        "name": "NIT Trichy",
        "location": "Tiruchirappalli, Tamil Nadu",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "MCA", "Ph.D."],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Electronics", "Chemical", "Instrumentation"],
        "fees": "1.5-2 Lakh per year",
        "total_fees": "6-8 Lakh (4 years)",
        "placements": {
            "avg_package": "12 LPA",
            "highest_package": "60 LPA",
            "top_recruiters": ["Microsoft", "Amazon", "TCS", "Infosys", "Wipro"],
            "placement_rate": "92%",
        },
        "selection": "JEE Main rank + Board %",
        "entrance_exam": "JEE Main",
        "ranking": "NIRF Top 10 NIT",
        "website": "www.nitt.edu",
    },
    {
        "name": "NIT Warangal",
        "location": "Warangal, Telangana",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "MCA", "Ph.D."],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Electronics", "Chemical", "Biotech"],
        "fees": "1.5-2 Lakh per year",
        "total_fees": "6-8 Lakh (4 years)",
        "placements": {
            "avg_package": "11 LPA",
            "highest_package": "55 LPA",
            "top_recruiters": ["Amazon", "Microsoft", "Google", "TCS", "Deloitte"],
            "placement_rate": "90%",
        },
        "selection": "JEE Main rank + Board %",
        "entrance_exam": "JEE Main",
        "ranking": "NIRF Top 10 NIT",
        "website": "www.nitw.ac.in",
    },
    {
        "name": "NIT Surathkal (NITK)",
        "location": "Mangalore, Karnataka",
        "type": "Government",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MCA", "Ph.D."],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Electronics", "Chemical", "IT"],
        "fees": "1.5-2 Lakh per year",
        "total_fees": "6-8 Lakh (4 years)",
        "placements": {
            "avg_package": "11 LPA",
            "highest_package": "50 LPA",
            "top_recruiters": ["Google", "Amazon", "Cisco", "Infosys", "Oracle"],
            "placement_rate": "88%",
        },
        "selection": "JEE Main rank + Board %",
        "entrance_exam": "JEE Main",
        "ranking": "NIRF Top 10 NIT",
        "website": "www.nitk.ac.in",
    },

    # ---------- Medical Colleges ----------
    {
        "name": "AIIMS Delhi",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Medical",
        "courses": ["MBBS", "MD", "MS", "M.Ch", "Ph.D.", "B.Sc Nursing"],
        "branches": ["General Medicine", "Surgery", "Paediatrics", "Cardiology", "Neurology", "Orthopaedics"],
        "fees": "1,628 per year (MBBS)",
        "total_fees": "~8,000 (5.5 years MBBS)",
        "placements": {
            "avg_package": "Not applicable (doctors join hospitals)",
            "highest_package": "Superspecialists earn 30-80 LPA",
            "top_recruiters": ["Government Hospitals", "Apollo", "Fortis", "Max Healthcare", "AIIMS Network"],
            "placement_rate": "100% (all graduates get positions)",
        },
        "selection": "NEET UG rank (top 50-100 ranks)",
        "entrance_exam": "NEET UG",
        "ranking": "NIRF #1 (Medical)",
        "website": "www.aiims.edu",
    },
    {
        "name": "CMC Vellore",
        "location": "Vellore, Tamil Nadu",
        "type": "Private (Christian Minority)",
        "stream": "Medical",
        "courses": ["MBBS", "MD", "MS", "B.Sc Nursing", "Allied Health Sciences"],
        "branches": ["General Medicine", "Surgery", "Paediatrics", "Ophthalmology", "Dermatology"],
        "fees": "25,000 per year (MBBS)",
        "total_fees": "~1.5 Lakh (5.5 years MBBS)",
        "placements": {
            "avg_package": "Hospital residencies and positions",
            "highest_package": "Specialists earn 20-60 LPA",
            "top_recruiters": ["CMC Hospital", "Government Hospitals", "Private Hospitals"],
            "placement_rate": "100%",
        },
        "selection": "NEET UG rank + CMC counselling",
        "entrance_exam": "NEET UG",
        "ranking": "NIRF Top 5 (Medical)",
        "website": "www.cmcvellore.ac.in",
    },
    {
        "name": "JIPMER Puducherry",
        "location": "Puducherry",
        "type": "Government",
        "stream": "Medical",
        "courses": ["MBBS", "MD", "MS", "M.Ch", "Ph.D.", "B.Sc Nursing"],
        "branches": ["General Medicine", "Surgery", "Psychiatry", "Radiology", "Anaesthesia"],
        "fees": "5,950 per year (MBBS)",
        "total_fees": "~30,000 (5.5 years MBBS)",
        "placements": {
            "avg_package": "Hospital positions",
            "highest_package": "Specialists earn 20-50 LPA",
            "top_recruiters": ["Government Hospitals", "JIPMER Hospital", "Private Hospitals"],
            "placement_rate": "100%",
        },
        "selection": "NEET UG rank",
        "entrance_exam": "NEET UG",
        "ranking": "NIRF Top 5 (Medical)",
        "website": "www.jipmer.edu.in",
    },
    {
        "name": "Maulana Azad Medical College",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Medical",
        "courses": ["MBBS", "MD", "MS"],
        "branches": ["General Medicine", "Surgery", "Paediatrics", "Gynaecology", "ENT"],
        "fees": "10,000 per year (MBBS)",
        "total_fees": "~55,000 (5.5 years MBBS)",
        "placements": {
            "avg_package": "Hospital positions",
            "highest_package": "Senior doctors earn 25-60 LPA",
            "top_recruiters": ["Lok Nayak Hospital", "GB Pant Hospital", "Government Hospitals"],
            "placement_rate": "100%",
        },
        "selection": "NEET UG rank (Delhi state quota + All India)",
        "entrance_exam": "NEET UG",
        "ranking": "NIRF Top 10 (Medical)",
        "website": "www.mamc.ac.in",
    },

    # ---------- Management / MBA Colleges ----------
    {
        "name": "IIM Ahmedabad",
        "location": "Ahmedabad, Gujarat",
        "type": "Government",
        "stream": "Management",
        "courses": ["MBA (PGP)", "Ph.D. (FPM)", "Executive MBA"],
        "branches": ["Finance", "Marketing", "Operations", "HR", "Strategy", "Consulting"],
        "fees": "11 Lakh per year",
        "total_fees": "23 Lakh (2 years)",
        "placements": {
            "avg_package": "35 LPA",
            "highest_package": "1.2 Crore",
            "top_recruiters": ["McKinsey", "BCG", "Bain", "Goldman Sachs", "Amazon"],
            "placement_rate": "100%",
        },
        "selection": "CAT score + PI (Personal Interview) + WAT",
        "entrance_exam": "CAT",
        "ranking": "NIRF #1 (Management)",
        "website": "www.iima.ac.in",
    },
    {
        "name": "IIM Bangalore",
        "location": "Bangalore, Karnataka",
        "type": "Government",
        "stream": "Management",
        "courses": ["MBA (PGP)", "PGPEM", "Ph.D. (FPM)"],
        "branches": ["Finance", "Marketing", "Operations", "Entrepreneurship", "IT Management"],
        "fees": "12 Lakh per year",
        "total_fees": "24 Lakh (2 years)",
        "placements": {
            "avg_package": "34 LPA",
            "highest_package": "1.15 Crore",
            "top_recruiters": ["McKinsey", "Amazon", "Google", "Flipkart", "JP Morgan"],
            "placement_rate": "100%",
        },
        "selection": "CAT score + WAT + PI",
        "entrance_exam": "CAT",
        "ranking": "NIRF #2 (Management)",
        "website": "www.iimb.ac.in",
    },
    {
        "name": "IIM Calcutta",
        "location": "Kolkata, West Bengal",
        "type": "Government",
        "stream": "Management",
        "courses": ["MBA (PGP)", "PGDBA", "Ph.D. (FPM)", "Executive MBA"],
        "branches": ["Finance", "Marketing", "Operations", "Analytics", "Strategy"],
        "fees": "11 Lakh per year",
        "total_fees": "22 Lakh (2 years)",
        "placements": {
            "avg_package": "32 LPA",
            "highest_package": "1.1 Crore",
            "top_recruiters": ["BCG", "Goldman Sachs", "Citibank", "Amazon", "Deloitte"],
            "placement_rate": "100%",
        },
        "selection": "CAT score + PI + WAT",
        "entrance_exam": "CAT",
        "ranking": "NIRF #3 (Management)",
        "website": "www.iimcal.ac.in",
    },
    {
        "name": "XLRI Jamshedpur",
        "location": "Jamshedpur, Jharkhand",
        "type": "Private",
        "stream": "Management",
        "courses": ["MBA (BM)", "MBA (HRM)", "PGDM", "Executive MBA"],
        "branches": ["Business Management", "Human Resources", "Finance", "Marketing"],
        "fees": "13 Lakh per year",
        "total_fees": "26 Lakh (2 years)",
        "placements": {
            "avg_package": "28 LPA",
            "highest_package": "75 LPA",
            "top_recruiters": ["Aditya Birla Group", "Tata", "Deloitte", "Amazon", "Accenture"],
            "placement_rate": "100%",
        },
        "selection": "XAT score + GD + PI",
        "entrance_exam": "XAT",
        "ranking": "Top 5 B-School",
        "website": "www.xlri.ac.in",
    },

    # ---------- Commerce / CA ----------
    {
        "name": "SRCC (Shri Ram College of Commerce)",
        "location": "New Delhi, Delhi",
        "type": "Government (Delhi University)",
        "stream": "Commerce",
        "courses": ["B.Com (Hons)", "M.Com", "B.A. Economics (Hons)"],
        "branches": ["Accountancy", "Finance", "Economics", "Business Studies"],
        "fees": "20,000-30,000 per year",
        "total_fees": "60,000-90,000 (3 years)",
        "placements": {
            "avg_package": "12 LPA",
            "highest_package": "32 LPA",
            "top_recruiters": ["Deloitte", "EY", "KPMG", "PwC", "Goldman Sachs"],
            "placement_rate": "85%",
        },
        "selection": "CUET score",
        "entrance_exam": "CUET",
        "ranking": "India's #1 Commerce College",
        "website": "www.srcc.edu",
    },
    {
        "name": "LSR (Lady Shri Ram College)",
        "location": "New Delhi, Delhi",
        "type": "Government (Delhi University)",
        "stream": "Commerce",
        "courses": ["B.Com", "B.A. Economics", "B.A. English", "B.A. Psychology", "B.A. Political Science"],
        "branches": ["Commerce", "Economics", "Humanities", "Social Sciences"],
        "fees": "15,000-25,000 per year",
        "total_fees": "45,000-75,000 (3 years)",
        "placements": {
            "avg_package": "8 LPA",
            "highest_package": "25 LPA",
            "top_recruiters": ["Deloitte", "EY", "HUL", "Amazon", "Accenture"],
            "placement_rate": "80%",
        },
        "selection": "CUET score",
        "entrance_exam": "CUET",
        "ranking": "Top 3 Arts/Commerce College",
        "website": "www.lsr.edu.in",
    },
    {
        "name": "Loyola College",
        "location": "Chennai, Tamil Nadu",
        "type": "Private (Aided)",
        "stream": "Commerce",
        "courses": ["B.Com", "BBA", "B.Sc", "M.Com", "MBA"],
        "branches": ["Commerce", "Business Administration", "Economics", "Computer Science"],
        "fees": "30,000-50,000 per year",
        "total_fees": "90,000-1.5 Lakh (3 years)",
        "placements": {
            "avg_package": "5 LPA",
            "highest_package": "18 LPA",
            "top_recruiters": ["TCS", "Infosys", "Deloitte", "KPMG", "Zoho"],
            "placement_rate": "75%",
        },
        "selection": "12th marks + merit",
        "entrance_exam": "No entrance exam (merit-based)",
        "ranking": "NIRF Top 10 (College)",
        "website": "www.loyolacollege.edu",
    },

    # ---------- Arts / Humanities ----------
    {
        "name": "St. Stephen's College",
        "location": "New Delhi, Delhi",
        "type": "Government (Delhi University)",
        "stream": "Arts",
        "courses": ["B.A. English", "B.A. History", "B.A. Economics", "B.A. Philosophy", "B.Sc Physics", "B.Sc Maths"],
        "branches": ["English Literature", "History", "Economics", "Philosophy", "Mathematics"],
        "fees": "20,000-40,000 per year",
        "total_fees": "60,000-1.2 Lakh (3 years)",
        "placements": {
            "avg_package": "8 LPA",
            "highest_package": "28 LPA",
            "top_recruiters": ["Deloitte", "McKinsey", "HUL", "ITC", "Media Houses"],
            "placement_rate": "75%",
        },
        "selection": "CUET score + interview",
        "entrance_exam": "CUET",
        "ranking": "India's Top Arts College",
        "website": "www.ststephens.edu",
    },
    {
        "name": "Presidency University",
        "location": "Kolkata, West Bengal",
        "type": "Government",
        "stream": "Arts",
        "courses": ["B.A. English", "B.A. History", "B.A. Political Science", "B.Sc Physics", "B.Sc Chemistry"],
        "branches": ["Arts", "Humanities", "Sciences", "Social Sciences"],
        "fees": "5,000-15,000 per year",
        "total_fees": "15,000-45,000 (3 years)",
        "placements": {
            "avg_package": "5 LPA",
            "highest_package": "15 LPA",
            "top_recruiters": ["TCS", "Infosys", "Government Jobs", "Media Houses"],
            "placement_rate": "65%",
        },
        "selection": "Merit-based + entrance exam",
        "entrance_exam": "Presidency University Entrance Test",
        "ranking": "Historic top university",
        "website": "www.presiuniv.ac.in",
    },

    # ---------- Design Colleges ----------
    {
        "name": "NID Ahmedabad",
        "location": "Ahmedabad, Gujarat",
        "type": "Government",
        "stream": "Design",
        "courses": ["B.Des", "M.Des", "GDPD (Graduate Diploma)"],
        "branches": ["Industrial Design", "Graphic Design", "Animation", "Textile Design", "Ceramic Design"],
        "fees": "3-4 Lakh per year",
        "total_fees": "12-16 Lakh (4 years)",
        "placements": {
            "avg_package": "12 LPA",
            "highest_package": "35 LPA",
            "top_recruiters": ["Google", "Samsung", "Titan", "Asian Paints", "Design Studios"],
            "placement_rate": "90%",
        },
        "selection": "NID DAT Prelims + Mains (Studio Test + Interview)",
        "entrance_exam": "NID DAT",
        "ranking": "#1 Design Institute in India",
        "website": "www.nid.edu",
    },
    {
        "name": "NIFT Delhi",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Design",
        "courses": ["B.Des", "B.FTech", "M.Des", "M.FTech", "MFM"],
        "branches": ["Fashion Design", "Textile Design", "Accessory Design", "Knitwear Design", "Leather Design"],
        "fees": "2-3.5 Lakh per year",
        "total_fees": "8-14 Lakh (4 years)",
        "placements": {
            "avg_package": "8 LPA",
            "highest_package": "25 LPA",
            "top_recruiters": ["H&M", "Zara", "Aditya Birla Fashion", "Reliance Trends", "Titan"],
            "placement_rate": "85%",
        },
        "selection": "NIFT Entrance Exam (CAT + GAT + Situation Test)",
        "entrance_exam": "NIFT Entrance Exam",
        "ranking": "#1 Fashion Institute in India",
        "website": "www.nift.ac.in",
    },

    # ---------- Law Colleges ----------
    {
        "name": "NLSIU Bangalore",
        "location": "Bangalore, Karnataka",
        "type": "Government",
        "stream": "Law",
        "courses": ["BA LLB (5 years)", "LLM", "Ph.D."],
        "branches": ["Constitutional Law", "Corporate Law", "Criminal Law", "International Law", "IP Law"],
        "fees": "2.5-3 Lakh per year",
        "total_fees": "12-15 Lakh (5 years)",
        "placements": {
            "avg_package": "18 LPA",
            "highest_package": "45 LPA",
            "top_recruiters": ["AZB & Partners", "Cyril Amarchand", "Khaitan & Co", "Trilegal", "S&R Associates"],
            "placement_rate": "95%",
        },
        "selection": "CLAT rank (top 50-80 ranks)",
        "entrance_exam": "CLAT",
        "ranking": "NIRF #1 (Law)",
        "website": "www.nls.ac.in",
    },
    {
        "name": "NALSAR Hyderabad",
        "location": "Hyderabad, Telangana",
        "type": "Government",
        "stream": "Law",
        "courses": ["BA LLB (5 years)", "LLM", "Ph.D."],
        "branches": ["Constitutional Law", "Corporate Law", "Criminal Law", "Cyber Law"],
        "fees": "2-2.5 Lakh per year",
        "total_fees": "10-12.5 Lakh (5 years)",
        "placements": {
            "avg_package": "15 LPA",
            "highest_package": "38 LPA",
            "top_recruiters": ["AZB & Partners", "Shardul Amarchand", "L&L Partners", "Khaitan & Co"],
            "placement_rate": "92%",
        },
        "selection": "CLAT rank",
        "entrance_exam": "CLAT",
        "ranking": "NIRF Top 3 (Law)",
        "website": "www.nalsar.ac.in",
    },
    {
        "name": "NLU Delhi",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Law",
        "courses": ["BA LLB (5 years)", "LLM", "Ph.D."],
        "branches": ["Corporate Law", "Constitutional Law", "Criminal Law", "Human Rights Law"],
        "fees": "2 Lakh per year",
        "total_fees": "10 Lakh (5 years)",
        "placements": {
            "avg_package": "16 LPA",
            "highest_package": "40 LPA",
            "top_recruiters": ["AZB & Partners", "Cyril Amarchand", "Trilegal", "Luthra & Luthra"],
            "placement_rate": "93%",
        },
        "selection": "AILET rank",
        "entrance_exam": "AILET",
        "ranking": "NIRF Top 3 (Law)",
        "website": "www.nludelhi.ac.in",
    },

    # ---------- Pharmacy Colleges ----------
    {
        "name": "NIPER Mohali",
        "location": "Mohali, Punjab",
        "type": "Government",
        "stream": "Pharmacy",
        "courses": ["M.Pharm", "MBA (Pharma)", "Ph.D."],
        "branches": ["Pharmaceutical Chemistry", "Pharmacology", "Pharmaceutics", "Pharma Analysis"],
        "fees": "50,000-1 Lakh per year",
        "total_fees": "1-2 Lakh (2 years)",
        "placements": {
            "avg_package": "8 LPA",
            "highest_package": "22 LPA",
            "top_recruiters": ["Sun Pharma", "Cipla", "Dr Reddy's", "Biocon", "Lupin"],
            "placement_rate": "85%",
        },
        "selection": "NIPER JEE rank",
        "entrance_exam": "NIPER JEE",
        "ranking": "#1 Pharmacy Institute",
        "website": "www.niper.gov.in",
    },
    {
        "name": "Jamia Hamdard (Pharmacy)",
        "location": "New Delhi, Delhi",
        "type": "Private (Deemed University)",
        "stream": "Pharmacy",
        "courses": ["B.Pharm", "M.Pharm", "Pharm.D", "Ph.D."],
        "branches": ["Pharmaceutics", "Pharmacology", "Pharma Chemistry", "Clinical Pharmacy"],
        "fees": "1.5-2 Lakh per year",
        "total_fees": "6-8 Lakh (4 years B.Pharm)",
        "placements": {
            "avg_package": "5 LPA",
            "highest_package": "12 LPA",
            "top_recruiters": ["Cipla", "Sun Pharma", "Ranbaxy", "GSK", "Abbott"],
            "placement_rate": "80%",
        },
        "selection": "CUET / University entrance",
        "entrance_exam": "CUET",
        "ranking": "NIRF Top 5 (Pharmacy)",
        "website": "www.jamiahamdard.edu",
    },

    # ---------- Architecture Colleges ----------
    {
        "name": "SPA Delhi (School of Planning and Architecture)",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Architecture",
        "courses": ["B.Arch", "B.Planning", "M.Arch", "M.Planning", "Ph.D."],
        "branches": ["Architecture", "Urban Planning", "Industrial Design", "Landscape Architecture"],
        "fees": "1-1.5 Lakh per year",
        "total_fees": "5-7.5 Lakh (5 years)",
        "placements": {
            "avg_package": "8 LPA",
            "highest_package": "20 LPA",
            "top_recruiters": ["Hafeez Contractor", "CP Kukreja", "Morphogenesis", "RSP Architects"],
            "placement_rate": "80%",
        },
        "selection": "NATA / JEE Main (Paper 2) rank",
        "entrance_exam": "NATA / JEE Main Paper 2",
        "ranking": "NIRF #1 (Architecture)",
        "website": "www.spa.ac.in",
    },

    # ---------- Private Engineering ----------
    {
        "name": "BITS Pilani",
        "location": "Pilani, Rajasthan (+ Goa, Hyderabad)",
        "type": "Private",
        "stream": "Engineering",
        "courses": ["B.E.", "M.E.", "MBA", "Ph.D.", "Dual Degree"],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Chemical", "Electronics", "Pharmacy"],
        "fees": "5-6 Lakh per year",
        "total_fees": "20-24 Lakh (4 years)",
        "placements": {
            "avg_package": "15 LPA",
            "highest_package": "1 Crore",
            "top_recruiters": ["Google", "Microsoft", "Goldman Sachs", "Uber", "DE Shaw"],
            "placement_rate": "90%",
        },
        "selection": "BITSAT score",
        "entrance_exam": "BITSAT",
        "ranking": "NIRF Top 15 (Engineering)",
        "website": "www.bits-pilani.ac.in",
    },
    {
        "name": "VIT Vellore",
        "location": "Vellore, Tamil Nadu (+ Chennai, Bhopal, AP)",
        "type": "Private",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "MCA", "Ph.D."],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Civil", "Electronics", "Biotech", "IT"],
        "fees": "2-3.5 Lakh per year",
        "total_fees": "8-14 Lakh (4 years)",
        "placements": {
            "avg_package": "7 LPA",
            "highest_package": "50 LPA",
            "top_recruiters": ["Microsoft", "Amazon", "Deloitte", "TCS", "Cognizant"],
            "placement_rate": "85%",
        },
        "selection": "VITEEE rank",
        "entrance_exam": "VITEEE",
        "ranking": "NIRF Top 15 (Engineering)",
        "website": "www.vit.ac.in",
    },
    {
        "name": "SRM Chennai",
        "location": "Chennai, Tamil Nadu",
        "type": "Private",
        "stream": "Engineering",
        "courses": ["B.Tech", "M.Tech", "MBA", "MBBS", "Ph.D."],
        "branches": ["Computer Science", "Electrical", "Mechanical", "Electronics", "Biomedical", "Civil"],
        "fees": "2.5-4 Lakh per year",
        "total_fees": "10-16 Lakh (4 years)",
        "placements": {
            "avg_package": "6 LPA",
            "highest_package": "41 LPA",
            "top_recruiters": ["Amazon", "TCS", "Infosys", "Wipro", "Cognizant"],
            "placement_rate": "80%",
        },
        "selection": "SRMJEEE rank",
        "entrance_exam": "SRMJEEE",
        "ranking": "NIRF Top 30 (Engineering)",
        "website": "www.srmist.edu.in",
    },

    # ---------- Journalism / Mass Communication ----------
    {
        "name": "IIMC (Indian Institute of Mass Communication)",
        "location": "New Delhi, Delhi",
        "type": "Government",
        "stream": "Media",
        "courses": ["PG Diploma in Journalism", "PG Diploma in Advertising & PR", "PG Diploma in Radio & TV"],
        "branches": ["Print Journalism", "TV Journalism", "Digital Media", "Advertising", "Public Relations"],
        "fees": "75,000 per year",
        "total_fees": "75,000 (1 year PG Diploma)",
        "placements": {
            "avg_package": "8 LPA",
            "highest_package": "18 LPA",
            "top_recruiters": ["NDTV", "Times of India", "Indian Express", "Aaj Tak", "BBC"],
            "placement_rate": "90%",
        },
        "selection": "IIMC Entrance Exam (written + interview)",
        "entrance_exam": "IIMC Entrance Exam",
        "ranking": "#1 Media Institute in India",
        "website": "www.iimc.gov.in",
    },
]


# -------------------- ENTRANCE EXAM DATABASE --------------------

entrance_exams = [
    {
        "name": "JEE Main",
        "full_name": "Joint Entrance Examination (Main)",
        "for_courses": ["B.Tech", "B.E.", "B.Arch", "B.Planning"],
        "stream": "Engineering",
        "eligibility": "10+2 with Physics, Chemistry, Maths (75% marks or top 20 percentile)",
        "exam_month": "January & April",
        "conducting_body": "NTA (National Testing Agency)",
        "pattern": "90 questions (MCQ + Numerical), 300 marks, 3 hours",
        "subjects": "Physics, Chemistry, Mathematics",
        "colleges_accepting": ["NITs", "IIITs", "GFTIs", "State engineering colleges", "Some private colleges"],
        "preparation_tips": [
            "Start from Class 11 topics",
            "Practice NCERT thoroughly",
            "Solve previous year papers",
            "Take online mock tests regularly",
            "Focus on Physics and Maths for higher scores",
        ],
        "website": "www.jeemain.nta.nic.in",
    },
    {
        "name": "JEE Advanced",
        "full_name": "Joint Entrance Examination (Advanced)",
        "for_courses": ["B.Tech", "BS", "Dual Degree", "B.Arch (IIT Kharagpur)"],
        "stream": "Engineering",
        "eligibility": "Must clear JEE Main (top 2,50,000 ranks) + 75% in 12th board",
        "exam_month": "May / June",
        "conducting_body": "One of the IITs (rotational)",
        "pattern": "2 papers, 3 hours each, MCQ + Numerical + Matrix Match",
        "subjects": "Physics, Chemistry, Mathematics",
        "colleges_accepting": ["All 23 IITs"],
        "preparation_tips": [
            "Master JEE Main level first",
            "Focus on conceptual depth, not just formulas",
            "Practice IIT-level problems from HC Verma, Irodov",
            "Revise organic and inorganic chemistry thoroughly",
            "Time management is crucial — practice under timed conditions",
        ],
        "website": "www.jeeadv.ac.in",
    },
    {
        "name": "NEET UG",
        "full_name": "National Eligibility cum Entrance Test (Undergraduate)",
        "for_courses": ["MBBS", "BDS", "BAMS", "BHMS", "B.Sc Nursing", "BVSc"],
        "stream": "Medical",
        "eligibility": "10+2 with Physics, Chemistry, Biology (50% marks, 40% for reserved)",
        "exam_month": "May",
        "conducting_body": "NTA (National Testing Agency)",
        "pattern": "200 questions (MCQ), 720 marks, 3 hours 20 minutes",
        "subjects": "Physics, Chemistry, Biology (Botany + Zoology)",
        "colleges_accepting": ["AIIMS", "JIPMER", "All government medical colleges", "Private medical colleges"],
        "preparation_tips": [
            "NCERT is the bible — read it 3-4 times",
            "Biology has maximum marks — give it most time",
            "Practice MCQs daily (minimum 100 questions)",
            "Focus on diagrams and flowcharts in Biology",
            "Revise Physics formulas and Chemistry reactions daily",
        ],
        "website": "www.neet.nta.nic.in",
    },
    {
        "name": "CAT",
        "full_name": "Common Admission Test",
        "for_courses": ["MBA", "PGDM"],
        "stream": "Management",
        "eligibility": "Any graduation with 50% marks (45% for reserved)",
        "exam_month": "November",
        "conducting_body": "IIMs (rotational)",
        "pattern": "66 questions, 3 sections, 2 hours",
        "subjects": "Verbal Ability, Data Interpretation & Logical Reasoning, Quantitative Aptitude",
        "colleges_accepting": ["All 20+ IIMs", "FMS Delhi", "MDI Gurgaon", "SPJIMR", "IITs (MBA)"],
        "preparation_tips": [
            "Start preparation 6-8 months before exam",
            "Read newspapers daily for Reading Comprehension",
            "Practice Quantitative Aptitude from Arun Sharma",
            "Take at least 30 full-length mock tests",
            "Focus on accuracy, not just speed",
        ],
        "website": "www.iimcat.ac.in",
    },
    {
        "name": "CLAT",
        "full_name": "Common Law Admission Test",
        "for_courses": ["BA LLB (5 years)", "LLM"],
        "stream": "Law",
        "eligibility": "10+2 with 45% marks (40% for reserved)",
        "exam_month": "December",
        "conducting_body": "Consortium of NLUs",
        "pattern": "150 questions (MCQ), 150 marks, 2 hours",
        "subjects": "English, Current Affairs & GK, Legal Reasoning, Logical Reasoning, Quantitative Techniques",
        "colleges_accepting": ["NLSIU Bangalore", "NALSAR Hyderabad", "NLU Jodhpur", "NUJS Kolkata", "All 22+ NLUs"],
        "preparation_tips": [
            "Read newspapers daily (The Hindu, Indian Express)",
            "Focus on Legal Reasoning — it's the most important section",
            "Practice reading comprehension extensively",
            "Stay updated on current affairs (last 1 year)",
            "Take mock tests from CLAT Consortium",
        ],
        "website": "www.consortiumofnlus.ac.in",
    },
    {
        "name": "NATA",
        "full_name": "National Aptitude Test in Architecture",
        "for_courses": ["B.Arch"],
        "stream": "Architecture",
        "eligibility": "10+2 with Maths (50% aggregate)",
        "exam_month": "April & July",
        "conducting_body": "Council of Architecture (CoA)",
        "pattern": "Drawing + MCQ (Aptitude + Maths), 3 hours",
        "subjects": "Mathematics, General Aptitude, Drawing & Design",
        "colleges_accepting": ["SPA Delhi", "SPA Bhopal", "Government architecture colleges", "Private architecture colleges"],
        "preparation_tips": [
            "Practice freehand drawing daily",
            "Focus on 3D visualization and perspective drawing",
            "Study basic Maths (geometry, trigonometry)",
            "Practice general awareness about famous buildings",
            "Take drawing mock tests under timed conditions",
        ],
        "website": "www.nata.in",
    },
    {
        "name": "CUET",
        "full_name": "Common University Entrance Test",
        "for_courses": ["B.A.", "B.Com", "B.Sc", "BBA", "BCA", "Integrated courses"],
        "stream": "General (Arts, Commerce, Science)",
        "eligibility": "10+2 pass",
        "exam_month": "May / June",
        "conducting_body": "NTA (National Testing Agency)",
        "pattern": "MCQ-based, subject-specific papers + General Test + Language",
        "subjects": "Chosen subjects from 10+2 + General Test + Language",
        "colleges_accepting": ["All Central Universities", "Delhi University", "JNU", "BHU", "Jamia Millia", "AMU"],
        "preparation_tips": [
            "Focus on NCERT textbooks for subject papers",
            "Practice general awareness and current affairs",
            "Read English newspapers for language section",
            "Take section-wise mock tests",
            "Time management is key — don't spend too long on one question",
        ],
        "website": "www.cuet.samarth.ac.in",
    },
    {
        "name": "BITSAT",
        "full_name": "BITS Admission Test",
        "for_courses": ["B.E.", "B.Pharm", "M.Sc"],
        "stream": "Engineering",
        "eligibility": "10+2 with PCM (75% aggregate, 60% in each subject)",
        "exam_month": "May / June",
        "conducting_body": "BITS Pilani",
        "pattern": "150 questions (MCQ), 3 hours, computer-based",
        "subjects": "Physics, Chemistry, Mathematics, English, Logical Reasoning",
        "colleges_accepting": ["BITS Pilani", "BITS Goa", "BITS Hyderabad"],
        "preparation_tips": [
            "NCERT + HC Verma for Physics",
            "Speed is crucial — practice finishing in time",
            "Don't ignore English and Logical Reasoning (easy marks)",
            "Focus on NCERT Chemistry (especially inorganic)",
            "Take full-length mock tests weekly",
        ],
        "website": "www.bitsadmission.com",
    },
    {
        "name": "VITEEE",
        "full_name": "VIT Engineering Entrance Examination",
        "for_courses": ["B.Tech"],
        "stream": "Engineering",
        "eligibility": "10+2 with PCM or PCB (60% aggregate)",
        "exam_month": "April / May",
        "conducting_body": "VIT University",
        "pattern": "125 questions (MCQ), 2.5 hours, computer-based",
        "subjects": "Maths/Biology, Physics, Chemistry, English, Aptitude",
        "colleges_accepting": ["VIT Vellore", "VIT Chennai", "VIT Bhopal", "VIT AP"],
        "preparation_tips": [
            "NCERT is sufficient for most questions",
            "Practice previous year VITEEE papers",
            "Focus on application-based questions",
            "Don't skip English and Aptitude",
            "Register early — slots fill up fast",
        ],
        "website": "www.vit.ac.in",
    },
    {
        "name": "XAT",
        "full_name": "Xavier Aptitude Test",
        "for_courses": ["MBA", "PGDM"],
        "stream": "Management",
        "eligibility": "Any graduation (final year students can apply)",
        "exam_month": "January",
        "conducting_body": "XLRI Jamshedpur",
        "pattern": "100 questions + Essay, 3 hours 10 minutes",
        "subjects": "Verbal & Logical Ability, Decision Making, Quantitative Ability & Data Interpretation, GK, Essay",
        "colleges_accepting": ["XLRI Jamshedpur", "IMT Ghaziabad", "XIMB", "GIM Goa", "TAPMI", "LIBA"],
        "preparation_tips": [
            "Decision Making is unique to XAT — practice ethical dilemmas",
            "Verbal section is tougher than CAT — read extensively",
            "Practice essay writing on current topics",
            "GK section needs dedicated preparation",
            "Solve XAT previous papers for pattern familiarity",
        ],
        "website": "www.xatonline.in",
    },
    {
        "name": "NIPER JEE",
        "full_name": "National Institute of Pharmaceutical Education and Research JEE",
        "for_courses": ["M.Pharm", "MBA (Pharma)", "M.Tech (Pharma)"],
        "stream": "Pharmacy",
        "eligibility": "B.Pharm with 60% marks",
        "exam_month": "June / July",
        "conducting_body": "NIPER (rotational)",
        "pattern": "200 questions (MCQ), 2 hours",
        "subjects": "Pharmacy subjects (Pharmaceutics, Pharmacology, Pharma Chemistry, Pharma Analysis)",
        "colleges_accepting": ["NIPER Mohali", "NIPER Hyderabad", "NIPER Ahmedabad", "All 7 NIPERs"],
        "preparation_tips": [
            "Focus on GPAT-level preparation",
            "Revise core pharmacy subjects thoroughly",
            "Practice MCQs from standard textbooks",
            "Previous year NIPER JEE papers are very helpful",
            "Focus on Pharmacology and Pharmaceutics",
        ],
        "website": "www.niper.gov.in",
    },
    {
        "name": "NID DAT",
        "full_name": "National Institute of Design - Design Aptitude Test",
        "for_courses": ["B.Des", "M.Des", "GDPD"],
        "stream": "Design",
        "eligibility": "10+2 pass for B.Des",
        "exam_month": "January (Prelims) + March/April (Mains)",
        "conducting_body": "NID Ahmedabad",
        "pattern": "Prelims: MCQ (design awareness) | Mains: Studio test + Interview",
        "subjects": "Design Aptitude, General Awareness, Drawing, Creativity",
        "colleges_accepting": ["NID Ahmedabad", "NID Gandhinagar", "NID Kurukshetra", "NID MP", "NID Assam"],
        "preparation_tips": [
            "Observe everyday objects for design thinking",
            "Practice sketching and drawing daily",
            "Stay updated on design trends worldwide",
            "Build a basic portfolio of your creative work",
            "Practice storytelling through visuals",
        ],
        "website": "www.nid.edu",
    },
    {
        "name": "NIFT Entrance Exam",
        "full_name": "National Institute of Fashion Technology Entrance Exam",
        "for_courses": ["B.Des", "B.FTech", "M.Des", "M.FTech"],
        "stream": "Design",
        "eligibility": "10+2 pass for B.Des/B.FTech",
        "exam_month": "February",
        "conducting_body": "NIFT",
        "pattern": "CAT (Creative Ability Test) + GAT (General Ability Test) + Situation Test",
        "subjects": "Creative Ability, General Awareness, English, Quantitative Ability",
        "colleges_accepting": ["NIFT Delhi", "NIFT Mumbai", "NIFT Bangalore", "NIFT Hyderabad", "All 18 NIFT campuses"],
        "preparation_tips": [
            "Practice fashion illustration and sketching",
            "Stay updated on fashion trends and designers",
            "Prepare for situation test with material handling",
            "Focus on general awareness of art and culture",
            "Practice previous year NIFT papers",
        ],
        "website": "www.nift.ac.in",
    },
    {
        "name": "AILET",
        "full_name": "All India Law Entrance Test",
        "for_courses": ["BA LLB (5 years)", "LLM"],
        "stream": "Law",
        "eligibility": "10+2 with 50% marks",
        "exam_month": "December",
        "conducting_body": "NLU Delhi",
        "pattern": "150 questions (MCQ), 150 marks, 1.5 hours",
        "subjects": "English, General Knowledge, Legal Aptitude, Reasoning, Mathematics",
        "colleges_accepting": ["NLU Delhi"],
        "preparation_tips": [
            "Focus on legal aptitude and reasoning",
            "GK section covers more factual questions than CLAT",
            "Speed is crucial — 1.5 hours for 150 questions",
            "Practice previous year AILET papers",
            "Mathematics section is basic — don't ignore it",
        ],
        "website": "www.nludelhi.ac.in",
    },
    {
        "name": "UPSC CSE",
        "full_name": "Union Public Service Commission - Civil Services Examination",
        "for_courses": ["IAS", "IPS", "IFS", "IRS"],
        "stream": "Government Services",
        "eligibility": "Any graduation (21-32 years age)",
        "exam_month": "Prelims: June | Mains: September | Interview: Feb-April",
        "conducting_body": "UPSC",
        "pattern": "3 stages: Prelims (MCQ) → Mains (Descriptive) → Interview",
        "subjects": "General Studies, CSAT (Aptitude), Optional Subject, Essay",
        "colleges_accepting": ["Not college-based — leads to Government Officer positions"],
        "preparation_tips": [
            "Start with NCERT books (Class 6-12) for all subjects",
            "Read The Hindu newspaper daily for current affairs",
            "Choose optional subject wisely based on interest",
            "Practice answer writing for Mains — quality matters",
            "Join a test series for Prelims and Mains",
        ],
        "website": "www.upsc.gov.in",
    },
]


# -------------------- COLLEGE SEARCH FUNCTIONS --------------------

def search_colleges_by_stream(stream_keyword):
    """Search colleges by stream (Engineering, Medical, etc.)."""
    results = []
    for college in colleges:
        if stream_keyword.lower() in college["stream"].lower():
            results.append(college)
    return results


def search_colleges_by_name(name_keyword):
    """Search colleges by name keyword."""
    results = []
    for college in colleges:
        if name_keyword.lower() in college["name"].lower():
            results.append(college)
    return results


def search_colleges_by_location(location_keyword):
    """Search colleges by location keyword."""
    results = []
    for college in colleges:
        if location_keyword.lower() in college["location"].lower():
            results.append(college)
    return results


def search_colleges_by_course(course_keyword):
    """Search colleges that offer a specific course."""
    results = []
    for college in colleges:
        for course in college["courses"]:
            if course_keyword.lower() in course.lower():
                if college not in results:
                    results.append(college)
                break
        # Also check branches
        for branch in college["branches"]:
            if course_keyword.lower() in branch.lower():
                if college not in results:
                    results.append(college)
                break
    return results


def search_exam_by_name(exam_keyword):
    """Search entrance exams by name keyword."""
    results = []
    for exam in entrance_exams:
        if exam_keyword.lower() in exam["name"].lower() or exam_keyword.lower() in exam["full_name"].lower():
            results.append(exam)
    return results


def search_exam_by_stream(stream_keyword):
    """Search entrance exams by stream."""
    results = []
    for exam in entrance_exams:
        if stream_keyword.lower() in exam["stream"].lower():
            results.append(exam)
    return results


def show_college_detail(college):
    """Display full details of a college."""
    print("\n" + "=" * 60)
    print("  🏛️  " + college["name"])
    print("=" * 60)
    print("  📍 Location     : " + college["location"])
    print("  🏷️  Type         : " + college["type"])
    print("  📚 Stream       : " + college["stream"])
    print("  🏆 Ranking      : " + college["ranking"])
    print("  🌐 Website      : " + college["website"])

    print("\n  📋 Courses Offered:")
    for course in college["courses"]:
        print("     • " + course)

    print("\n  🔬 Branches / Specialisations:")
    for branch in college["branches"]:
        print("     • " + branch)

    print("\n  💰 Fees:")
    print("     Per Year  : " + college["fees"])
    print("     Total     : " + college["total_fees"])

    print("\n  📊 Placements:")
    print("     Avg Package     : " + college["placements"]["avg_package"])
    print("     Highest Package : " + college["placements"]["highest_package"])
    print("     Placement Rate  : " + college["placements"]["placement_rate"])
    print("     Top Recruiters  : " + ", ".join(college["placements"]["top_recruiters"]))

    print("\n  🎯 Selection Process:")
    print("     Method         : " + college["selection"])
    print("     Entrance Exam  : " + college["entrance_exam"])

    print("=" * 60)


def show_exam_detail(exam):
    """Display full details of an entrance exam."""
    print("\n" + "=" * 60)
    print("  📝  " + exam["name"] + " — " + exam["full_name"])
    print("=" * 60)
    print("  📚 Stream          : " + exam["stream"])
    print("  🎓 For Courses     : " + ", ".join(exam["for_courses"]))
    print("  📅 Exam Month      : " + exam["exam_month"])
    print("  🏢 Conducting Body : " + exam["conducting_body"])
    print("  🌐 Website         : " + exam["website"])

    print("\n  ✅ Eligibility:")
    print("     " + exam["eligibility"])

    print("\n  📋 Exam Pattern:")
    print("     " + exam["pattern"])

    print("\n  📖 Subjects:")
    print("     " + exam["subjects"])

    print("\n  🏛️  Colleges Accepting:")
    for c in exam["colleges_accepting"]:
        print("     • " + c)

    print("\n  💡 Preparation Tips:")
    for i in range(len(exam["preparation_tips"])):
        print("     " + str(i + 1) + ". " + exam["preparation_tips"][i])

    print("=" * 60)


def show_college_list(college_list, title):
    """Display a short list of colleges."""
    if len(college_list) == 0:
        print("\n  No colleges found matching your search.")
        return

    print("\n" + "-" * 60)
    print("  " + title)
    print("-" * 60)

    for i in range(len(college_list)):
        c = college_list[i]
        print("  " + str(i + 1) + ". " + c["name"])
        print("     📍 " + c["location"] + "  |  💰 " + c["fees"] + "  |  📊 Avg: " + c["placements"]["avg_package"])
    print()


def show_exam_list(exam_list, title):
    """Display a short list of exams."""
    if len(exam_list) == 0:
        print("\n  No entrance exams found matching your search.")
        return

    print("\n" + "-" * 60)
    print("  " + title)
    print("-" * 60)

    for i in range(len(exam_list)):
        e = exam_list[i]
        print("  " + str(i + 1) + ". " + e["name"] + " (" + e["full_name"] + ")")
        print("     📚 " + e["stream"] + "  |  📅 " + e["exam_month"] + "  |  🎓 " + ", ".join(e["for_courses"]))
    print()


def college_explorer_menu():
    """Interactive menu for exploring colleges and entrance exams."""

    print("\n" + "=" * 60)
    print("     🏛️  COLLEGE & EXAM EXPLORER")
    print("=" * 60)

    while True:
        print("\n  What would you like to explore?")
        print("  1. Search colleges by stream (Engineering, Medical, etc.)")
        print("  2. Search colleges by location (city/state)")
        print("  3. Search colleges by course (B.Tech, MBA, MBBS, etc.)")
        print("  4. Search colleges by name")
        print("  5. View all entrance exams for a stream")
        print("  6. Search a specific entrance exam")
        print("  7. View all colleges (full list)")
        print("  8. View all entrance exams (full list)")
        print("  0. Back to main menu")

        choice = input("\n  Enter your choice (0-8): ").strip()

        if choice == "0":
            break

        elif choice == "1":
            print("\n  Available streams: Engineering, Medical, Management,")
            print("  Commerce, Arts, Design, Law, Pharmacy, Architecture, Media")
            keyword = input("  Enter stream: ").strip()
            if keyword != "":
                results = search_colleges_by_stream(keyword)
                show_college_list(results, "Colleges in " + keyword.title())
                if len(results) > 0:
                    detail = input("  Enter number to see full details (or 0 to skip): ").strip()
                    if detail.isdigit() and 1 <= int(detail) <= len(results):
                        show_college_detail(results[int(detail) - 1])

        elif choice == "2":
            keyword = input("  Enter city or state name: ").strip()
            if keyword != "":
                results = search_colleges_by_location(keyword)
                show_college_list(results, "Colleges in " + keyword.title())
                if len(results) > 0:
                    detail = input("  Enter number to see full details (or 0 to skip): ").strip()
                    if detail.isdigit() and 1 <= int(detail) <= len(results):
                        show_college_detail(results[int(detail) - 1])

        elif choice == "3":
            keyword = input("  Enter course name (e.g. B.Tech, MBA, MBBS): ").strip()
            if keyword != "":
                results = search_colleges_by_course(keyword)
                show_college_list(results, "Colleges offering " + keyword)
                if len(results) > 0:
                    detail = input("  Enter number to see full details (or 0 to skip): ").strip()
                    if detail.isdigit() and 1 <= int(detail) <= len(results):
                        show_college_detail(results[int(detail) - 1])

        elif choice == "4":
            keyword = input("  Enter college name: ").strip()
            if keyword != "":
                results = search_colleges_by_name(keyword)
                if len(results) > 0:
                    for r in results:
                        show_college_detail(r)
                else:
                    print("  No colleges found with that name.")

        elif choice == "5":
            print("\n  Available streams: Engineering, Medical, Management,")
            print("  Law, Design, Pharmacy, Architecture, Government Services")
            keyword = input("  Enter stream: ").strip()
            if keyword != "":
                results = search_exam_by_stream(keyword)
                show_exam_list(results, "Entrance Exams for " + keyword.title())
                if len(results) > 0:
                    detail = input("  Enter number to see full details (or 0 to skip): ").strip()
                    if detail.isdigit() and 1 <= int(detail) <= len(results):
                        show_exam_detail(results[int(detail) - 1])

        elif choice == "6":
            keyword = input("  Enter exam name (e.g. JEE, NEET, CAT): ").strip()
            if keyword != "":
                results = search_exam_by_name(keyword)
                if len(results) > 0:
                    for r in results:
                        show_exam_detail(r)
                else:
                    print("  No entrance exam found with that name.")

        elif choice == "7":
            show_college_list(colleges, "ALL COLLEGES (" + str(len(colleges)) + " colleges)")
            detail = input("  Enter number to see full details (or 0 to skip): ").strip()
            if detail.isdigit() and 1 <= int(detail) <= len(colleges):
                show_college_detail(colleges[int(detail) - 1])

        elif choice == "8":
            show_exam_list(entrance_exams, "ALL ENTRANCE EXAMS (" + str(len(entrance_exams)) + " exams)")
            detail = input("  Enter number to see full details (or 0 to skip): ").strip()
            if detail.isdigit() and 1 <= int(detail) <= len(entrance_exams):
                show_exam_detail(entrance_exams[int(detail) - 1])

        else:
            print("  ⚠ Invalid choice. Enter a number from 0 to 8.")
