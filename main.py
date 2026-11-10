# ============================================================
#                    CAREERPATH AI
#            CAREER COUNSELLING CHATBOT
#         Simple if-else based recommendation system
# ============================================================

from college_database import colleges, entrance_exams
from college_database import search_colleges_by_stream, search_colleges_by_name
from college_database import search_colleges_by_location, search_colleges_by_course
from college_database import search_exam_by_name, search_exam_by_stream
from college_database import show_college_detail, show_exam_detail
from college_database import show_college_list, show_exam_list
from college_database import college_explorer_menu


# -------------------- CAREER DATABASE --------------------
# Each career is a dictionary with details.
# Tags link careers to subjects, interests, and skills.
# Subject tags: 1=Maths, 2=Biology, 3=Computer Science, 4=Commerce, 5=Arts

careers = [
    {
        "name": "Software Developer",
        "description": "Design, build and maintain software applications and systems.",
        "education": "B.Tech/B.E. in Computer Science or BCA/MCA",
        "salary": "5-25 LPA",
        "tags_subject": ["1", "3"],
        "tags_interest": ["1"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "Data Scientist",
        "description": "Analyse large datasets to find patterns and help businesses make decisions.",
        "education": "B.Tech + M.Tech / M.Sc. in Data Science or Statistics",
        "salary": "6-30 LPA",
        "tags_subject": ["1", "3"],
        "tags_interest": ["1", "2"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "AI / Machine Learning Engineer",
        "description": "Build intelligent systems that can learn and make predictions.",
        "education": "B.Tech/M.Tech in CS / AI, or related research degree",
        "salary": "8-35 LPA",
        "tags_subject": ["1", "3"],
        "tags_interest": ["1", "2"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "Cybersecurity Analyst",
        "description": "Protect computer networks and systems from cyber threats and attacks.",
        "education": "B.Tech in CS / IT + security certifications (CEH, CISSP)",
        "salary": "5-20 LPA",
        "tags_subject": ["3"],
        "tags_interest": ["1"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "Doctor (MBBS)",
        "description": "Diagnose and treat illnesses, perform surgeries and care for patients.",
        "education": "MBBS + MD/MS specialisation",
        "salary": "8-30 LPA",
        "tags_subject": ["2"],
        "tags_interest": ["2", "5"],
        "tags_skill": ["4", "5"],
    },
    {
        "name": "Biotechnologist",
        "description": "Use biological systems to develop products in medicine, agriculture and industry.",
        "education": "B.Tech/M.Tech in Biotechnology or B.Sc./M.Sc. Biotech",
        "salary": "4-15 LPA",
        "tags_subject": ["2", "3"],
        "tags_interest": ["2"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "Pharmacist",
        "description": "Prepare and dispense medicines, advise patients on medication use.",
        "education": "B.Pharm / M.Pharm",
        "salary": "3-12 LPA",
        "tags_subject": ["2"],
        "tags_interest": ["2", "5"],
        "tags_skill": ["4"],
    },
    {
        "name": "Medical Researcher",
        "description": "Conduct experiments and studies to advance medical science.",
        "education": "MBBS + MD or Ph.D. in medical sciences",
        "salary": "6-20 LPA",
        "tags_subject": ["2"],
        "tags_interest": ["2"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "Chartered Accountant (CA)",
        "description": "Handle financial accounts, auditing, taxation and business advisory.",
        "education": "B.Com + CA certification (ICAI)",
        "salary": "7-25 LPA",
        "tags_subject": ["1", "4"],
        "tags_interest": ["3"],
        "tags_skill": ["1", "4"],
    },
    {
        "name": "Business Analyst",
        "description": "Analyse business processes and recommend improvements using data.",
        "education": "BBA/MBA or B.Tech with MBA",
        "salary": "5-18 LPA",
        "tags_subject": ["1", "4"],
        "tags_interest": ["3"],
        "tags_skill": ["1", "2", "4"],
    },
    {
        "name": "Marketing Manager",
        "description": "Plan and execute marketing strategies to promote products and services.",
        "education": "BBA/MBA in Marketing",
        "salary": "5-20 LPA",
        "tags_subject": ["4", "5"],
        "tags_interest": ["3"],
        "tags_skill": ["2", "3"],
    },
    {
        "name": "Entrepreneur",
        "description": "Start and run your own business, turning ideas into products or services.",
        "education": "Any degree + business skills and experience",
        "salary": "Varies widely",
        "tags_subject": ["4"],
        "tags_interest": ["3"],
        "tags_skill": ["2", "3", "4"],
    },
    {
        "name": "Investment Banker",
        "description": "Help companies raise capital, manage mergers, and advise on financial deals.",
        "education": "B.Com/BBA + MBA in Finance or CFA",
        "salary": "10-40 LPA",
        "tags_subject": ["1", "4"],
        "tags_interest": ["3"],
        "tags_skill": ["1", "2"],
    },
    {
        "name": "Graphic Designer",
        "description": "Create visual content like logos, posters, websites and brand identities.",
        "education": "B.Des / BFA / diploma in graphic design",
        "salary": "3-15 LPA",
        "tags_subject": ["5"],
        "tags_interest": ["4"],
        "tags_skill": ["3"],
    },
    {
        "name": "UI/UX Designer",
        "description": "Design user-friendly interfaces and experiences for apps and websites.",
        "education": "B.Des / B.Tech in CS + UX courses",
        "salary": "5-20 LPA",
        "tags_subject": ["3", "5"],
        "tags_interest": ["4"],
        "tags_skill": ["3", "4"],
    },
    {
        "name": "Animator / VFX Artist",
        "description": "Create animations, visual effects for films, games and advertisements.",
        "education": "B.Sc. Animation / B.Des / diploma in VFX",
        "salary": "3-18 LPA",
        "tags_subject": ["5", "3"],
        "tags_interest": ["4"],
        "tags_skill": ["3"],
    },
    {
        "name": "Journalist",
        "description": "Investigate, write and report news stories across media platforms.",
        "education": "BA in Journalism / Mass Communication",
        "salary": "3-12 LPA",
        "tags_subject": ["5"],
        "tags_interest": ["4", "5"],
        "tags_skill": ["2", "3"],
    },
    {
        "name": "Architect",
        "description": "Design buildings and structures that are functional, safe and beautiful.",
        "education": "B.Arch (5 years)",
        "salary": "4-18 LPA",
        "tags_subject": ["1", "5"],
        "tags_interest": ["4"],
        "tags_skill": ["3", "4"],
    },
    {
        "name": "Teacher / Professor",
        "description": "Educate students, develop curricula and inspire learning.",
        "education": "B.A./B.Sc./B.Ed. + M.A./M.Sc. + NET/SET for professor",
        "salary": "3-15 LPA",
        "tags_subject": ["1", "2", "3", "4", "5"],
        "tags_interest": ["5"],
        "tags_skill": ["2", "5"],
    },
    {
        "name": "Psychologist / Counsellor",
        "description": "Help people manage mental health, emotions and personal challenges.",
        "education": "BA/MA in Psychology + RCI registration for clinical",
        "salary": "3-15 LPA",
        "tags_subject": ["2", "5"],
        "tags_interest": ["5"],
        "tags_skill": ["2", "5"],
    },
    {
        "name": "Civil Services (IAS/IPS)",
        "description": "Serve in government administration, policy-making and public welfare.",
        "education": "Any graduation + UPSC exam",
        "salary": "8-18 LPA + benefits",
        "tags_subject": ["1", "2", "3", "4", "5"],
        "tags_interest": ["5", "3"],
        "tags_skill": ["2", "4", "5"],
    },
    {
        "name": "Lawyer / Advocate",
        "description": "Represent clients in legal matters, draft legal documents and argue cases.",
        "education": "BA LLB (5 years) or LLB (3 years)",
        "salary": "4-25 LPA",
        "tags_subject": ["5", "4"],
        "tags_interest": ["5", "3"],
        "tags_skill": ["2", "4"],
    },
    {
        "name": "Web Developer",
        "description": "Build and maintain websites and web applications.",
        "education": "B.Tech/BCA in CS or self-taught with portfolio",
        "salary": "4-18 LPA",
        "tags_subject": ["3"],
        "tags_interest": ["1", "4"],
        "tags_skill": ["3", "4"],
    },
    {
        "name": "Game Developer",
        "description": "Design and program video games for computers, consoles and mobile devices.",
        "education": "B.Tech in CS / B.Sc. in Game Development",
        "salary": "4-20 LPA",
        "tags_subject": ["1", "3"],
        "tags_interest": ["1", "4"],
        "tags_skill": ["3", "4"],
    },
    {
        "name": "Environmental Scientist",
        "description": "Study and solve environmental problems like pollution and climate change.",
        "education": "B.Sc./M.Sc. in Environmental Science",
        "salary": "4-12 LPA",
        "tags_subject": ["2"],
        "tags_interest": ["2", "5"],
        "tags_skill": ["1", "5"],
    },
]


# -------------------- HELPER FUNCTIONS --------------------

def show_banner():
    """Display the welcome banner."""
    print("\n" + "=" * 55)
    print("         CAREERPATH AI - CAREER COUNSELLING BOT")
    print("=" * 55)


def show_menu(title, options):
    """Display a numbered menu."""
    print("\n" + title)
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])


def get_single_choice(prompt, max_val):
    """Get a single valid choice from the user (1 to max_val)."""
    while True:
        choice = input(prompt).strip()
        if choice == "":
            print("  Please enter a choice.")
        elif choice.isdigit() and 1 <= int(choice) <= max_val:
            return choice
        else:
            print("  Invalid. Enter a number from 1 to " + str(max_val) + ".")


def get_multi_choice(prompt, max_val):
    """Get one or more valid choices separated by commas."""
    while True:
        raw = input(prompt).strip().replace(" ", "")
        if raw == "":
            print("  Please enter at least one choice.")
            continue

        parts = raw.split(",")
        valid = True
        seen = []

        for p in parts:
            if p.isdigit() and 1 <= int(p) <= max_val:
                if p not in seen:
                    seen.append(p)
            else:
                valid = False
                break

        if valid and len(seen) > 0:
            return seen
        else:
            print("  Invalid. Enter numbers from 1 to " + str(max_val) + " separated by commas.")


def get_words(sentence):
    """Split a sentence into clean individual words (removing punctuation)."""
    # Replace common punctuation with spaces, then split
    clean = sentence.replace("?", " ").replace("!", " ")
    clean = clean.replace(".", " ").replace(",", " ")
    clean = clean.replace(":", " ").replace(";", " ")
    return clean.split()


# -------------------- STUDENT PROFILE --------------------

def setup_user_profile():
    """Ask the student for their name, class, and subjects. Returns a profile dictionary."""

    print("\nWelcome! Let's set up your Student Profile first.\n")

    # --- Ask Name ---
    name = input("Enter your name: ").strip()
    if name == "":
        name = "Student"

    # --- Ask Class ---
    show_menu("Select your current class:", [
        "Class 9  (Early career exploration)",
        "Class 10 (Planning stream for Class 11)",
        "Class 11 (Exploring career pathways)",
        "Class 12 (Preparing for entrance exams and colleges)",
        "College / Other",
    ])
    grade_choice = get_single_choice("\n  Your choice (1-5): ", 5)

    # Convert choice to grade name
    if grade_choice == "1":
        grade = "Class 9"
    elif grade_choice == "2":
        grade = "Class 10"
    elif grade_choice == "3":
        grade = "Class 11"
    elif grade_choice == "4":
        grade = "Class 12"
    else:
        grade = "College / Other"

    # --- CLASS 9 and 10: Ask 2nd Language and Skill Subject ---
    if grade_choice == "1" or grade_choice == "2":

        show_menu("Select your 2nd Language:", [
            "Hindi",
            "Sanskrit",
            "Other",
        ])
        lang_choice = get_single_choice("  Your choice (1-3): ", 3)

        if lang_choice == "1":
            language = "Hindi"
        elif lang_choice == "2":
            language = "Sanskrit"
        else:
            language = "Other"

        show_menu("Select your Skill / Optional Subject:", [
            "Information Technology (IT)",
            "Computer Science (CS)",
            "Artificial Intelligence (AI)",
            "None / Other",
        ])
        skill_sub_choice = get_single_choice("  Your choice (1-4): ", 4)

        if skill_sub_choice == "1":
            skill_subject = "IT"
        elif skill_sub_choice == "2":
            skill_subject = "CS"
        elif skill_sub_choice == "3":
            skill_subject = "AI"
        else:
            skill_subject = "None"

        # Build profile for Class 9/10
        profile = {
            "name": name,
            "grade": grade,
            "group": "junior",
            "language": language,
            "skill_subject": skill_subject,
            "stream": "Not yet chosen",
            "optionals": [],
            "subjects": [],
        }

    # --- CLASS 11, 12, COLLEGE: Ask Stream and Optional Subjects ---
    else:

        show_menu("Select your main stream:", [
            "Science (PCM - Physics, Chemistry, Maths)",
            "Science (PCB - Physics, Chemistry, Biology)",
            "Science (PCMB - Maths and Biology both)",
            "Commerce (Accountancy, Business Studies, Economics)",
            "Arts / Humanities (History, Political Science, etc.)",
        ])
        stream_choice = get_single_choice("\n  Your choice (1-5): ", 5)

        if stream_choice == "1":
            stream = "Science (PCM)"
            subjects = ["1", "3"]    # Maths + CS-related
        elif stream_choice == "2":
            stream = "Science (PCB)"
            subjects = ["2"]         # Biology
        elif stream_choice == "3":
            stream = "Science (PCMB)"
            subjects = ["1", "2"]    # Maths + Biology
        elif stream_choice == "4":
            stream = "Commerce"
            subjects = ["4"]         # Commerce
        else:
            stream = "Arts / Humanities"
            subjects = ["5"]         # Arts

        show_menu("Select your optional subject(s) (pick one or more, e.g. 1,3):", [
            "Painting",
            "Artificial Intelligence (AI)",
            "Computer Science (CS)",
            "Physical Education (PE)",
            "Music",
            "None / Other",
        ])
        opt_choices = get_multi_choice("  Enter choices: ", 6)

        optionals = []
        for o in opt_choices:
            if o == "1":
                optionals.append("Painting")
                if "5" not in subjects:
                    subjects.append("5")    # Painting boosts Arts careers
            elif o == "2":
                optionals.append("AI")
                if "3" not in subjects:
                    subjects.append("3")    # AI boosts CS careers
            elif o == "3":
                optionals.append("CS")
                if "3" not in subjects:
                    subjects.append("3")    # CS boosts CS careers
            elif o == "4":
                optionals.append("PE")
            elif o == "5":
                optionals.append("Music")
                if "5" not in subjects:
                    subjects.append("5")    # Music boosts Arts careers
            else:
                optionals.append("None")

        # Build profile for Class 11/12/College
        profile = {
            "name": name,
            "grade": grade,
            "group": "senior",
            "language": "",
            "skill_subject": "",
            "stream": stream,
            "optionals": optionals,
            "subjects": subjects,
        }

    # --- Confirmation ---
    print("\n  Profile created successfully for " + name + " (" + grade + ")!")
    return profile


# -------------------- PROFILE DISPLAY --------------------

def show_my_profile(profile):
    """Display the student's profile summary."""
    print("\n" + "=" * 55)
    print("         YOUR STUDENT PROFILE")
    print("=" * 55)
    print("  Name     : " + profile["name"])
    print("  Class    : " + profile["grade"])

    if profile["group"] == "junior":
        print("  Language : " + profile["language"])
        print("  Skill Sub: " + profile["skill_subject"])
        print("  Stream   : " + profile["stream"])
    else:
        print("  Stream   : " + profile["stream"])
        if len(profile["optionals"]) > 0:
            print("  Optionals: " + ", ".join(profile["optionals"]))
        subject_names = get_subject_names(profile["subjects"])
        if len(subject_names) > 0:
            print("  Mapped   : " + ", ".join(subject_names))
    print("=" * 55)


# -------------------- SCORING ENGINE --------------------

def calculate_scores(subjects, interest, skill):
    """
    Score each career based on how well it matches the user's inputs.
    
    Eligibility rule:
      - Career must match at least one of the student's subjects.
    
    Scoring rules:
      - Each matching subject tag     = +2 points
      - Matching interest tag         = +3 points  (weighted higher)
      - Matching skill tag            = +2 points
    """
    scored = []

    for career in careers:
        # Subject Eligibility Check
        has_prerequisite = False
        for s in subjects:
            if s in career["tags_subject"]:
                has_prerequisite = True
                break

        if not has_prerequisite:
            continue

        # Score calculation
        score = 0

        for s in subjects:
            if s in career["tags_subject"]:
                score = score + 2

        if interest in career["tags_interest"]:
            score = score + 3

        if skill in career["tags_skill"]:
            score = score + 2

        if score > 0:
            scored.append({"career": career, "score": score})

    # Bubble sort by score (descending)
    for i in range(len(scored)):
        for j in range(i + 1, len(scored)):
            if scored[j]["score"] > scored[i]["score"]:
                temp = scored[i]
                scored[i] = scored[j]
                scored[j] = temp

    return scored


# -------------------- DISPLAY FUNCTIONS --------------------

def show_career_detail(career):
    """Display full details of a single career."""
    print("\n" + "-" * 50)
    print("  Career    : " + career["name"])
    print("-" * 50)
    print("  Description : " + career["description"])
    print("  Education   : " + career["education"])
    print("  Salary Range: " + career["salary"])
    print("-" * 50)


def show_results(name, subjects, interest, skill):
    """Show career recommendations based on user inputs."""
    scored = calculate_scores(subjects, interest, skill)

    print("\n" + "=" * 55)
    print("         YOUR CAREER RECOMMENDATIONS")
    print("=" * 55)
    print("\nHello, " + name + "! Based on your answers:\n")

    if len(scored) == 0:
        print("  Sorry, no strong matches found.")
        print("  Try different combinations!\n")
        return []

    # Show top 5 (or fewer)
    count = 5
    if len(scored) < 5:
        count = len(scored)

    print("  Top " + str(count) + " career matches:\n")

    for i in range(count):
        career = scored[i]["career"]
        score = scored[i]["score"]

        if score >= 7:
            match_text = "Excellent Match"
        elif score >= 5:
            match_text = "Strong Match"
        elif score >= 3:
            match_text = "Good Match"
        else:
            match_text = "Partial Match"

        print("  " + str(i + 1) + ". " + career["name"] + "  (" + match_text + ")")
        print("     " + career["description"])
        print()

    return scored[:count]


def explore_career(top_careers):
    """Let the user explore a recommended career in detail."""
    if len(top_careers) == 0:
        return

    while True:
        print("\nWant to explore a career in detail?")
        print("  Enter a number (1-" + str(len(top_careers)) + ") to see details, or 0 to go back.")

        choice = input("  Your choice: ").strip()

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(top_careers):
            show_career_detail(top_careers[int(choice) - 1]["career"])
        else:
            print("  Invalid choice.")


def get_subject_names(subjects):
    """Convert subject numbers to names."""
    names = []
    if "1" in subjects:
        names.append("Mathematics")
    if "2" in subjects:
        names.append("Biology")
    if "3" in subjects:
        names.append("Computer Science")
    if "4" in subjects:
        names.append("Commerce")
    if "5" in subjects:
        names.append("Arts")
    return names


def get_interest_name(interest):
    """Convert interest number to name."""
    if interest == "1":
        return "Solving technical problems"
    elif interest == "2":
        return "Research and experiments"
    elif interest == "3":
        return "Business and management"
    elif interest == "4":
        return "Creative work and design"
    elif interest == "5":
        return "Helping people"
    else:
        return "Unknown"


def get_skill_name(skill):
    """Convert skill number to name."""
    if skill == "1":
        return "Logical thinking"
    elif skill == "2":
        return "Communication"
    elif skill == "3":
        return "Creativity"
    elif skill == "4":
        return "Problem solving"
    elif skill == "5":
        return "Teamwork"
    else:
        return "Unknown"


# -------------------- QUIZ FOR CLASS 9 & 10 --------------------

def run_class_9_10_quiz(profile):
    """Stream Discovery Quiz for Class 9 and 10 students."""

    print("\n" + "=" * 55)
    print("    STREAM DISCOVERY QUIZ (For Class 9 & 10)")
    print("=" * 55)
    print("\n  Let's find which stream suits you best for Class 11!\n")

    # Points for each stream: PCM, PCB, Commerce, Arts
    pcm = 0
    pcb = 0
    commerce = 0
    arts = 0

    # Bonus from their skill subject
    if profile["skill_subject"] == "CS" or profile["skill_subject"] == "AI" or profile["skill_subject"] == "IT":
        pcm = pcm + 2   # Tech-oriented students lean toward PCM

    # --- Question 1 ---
    show_menu("Q1: What type of problems do you enjoy solving the most?", [
        "Maths puzzles, equations, and coding challenges",
        "Understanding how the human body and nature work",
        "Managing money, budgets, and business ideas",
        "Writing, debating, drawing, or social topics",
    ])
    q1 = get_single_choice("  Your answer (1-4): ", 4)

    if q1 == "1":
        pcm = pcm + 3
    elif q1 == "2":
        pcb = pcb + 3
    elif q1 == "3":
        commerce = commerce + 3
    elif q1 == "4":
        arts = arts + 3

    # --- Question 2 ---
    show_menu("Q2: What is your dream future work environment?", [
        "Tech office, software company, or research lab with computers",
        "Hospital, clinic, medical research centre, or nature reserve",
        "Corporate office, bank, stock exchange, or own business",
        "Art studio, newsroom, courtroom, or government office",
    ])
    q2 = get_single_choice("  Your answer (1-4): ", 4)

    if q2 == "1":
        pcm = pcm + 3
    elif q2 == "2":
        pcb = pcb + 3
    elif q2 == "3":
        commerce = commerce + 3
    elif q2 == "4":
        arts = arts + 3

    # --- Question 3 ---
    show_menu("Q3: In a school group project, what role do you naturally take?", [
        "The coder / technical builder who handles tools and data",
        "The researcher who collects facts and scientific information",
        "The planner who manages budget, deadlines, and presentation pitch",
        "The designer who creates visuals, posters, and speaks on stage",
    ])
    q3 = get_single_choice("  Your answer (1-4): ", 4)

    if q3 == "1":
        pcm = pcm + 2
    elif q3 == "2":
        pcb = pcb + 2
    elif q3 == "3":
        commerce = commerce + 2
    elif q3 == "4":
        arts = arts + 2

    # --- Determine best stream ---
    best_score = pcm
    best_stream = "Science (PCM)"
    best_careers = "Software Developer, Data Scientist, AI Engineer, Architect"
    best_exams = "JEE Main, JEE Advanced, BITSAT"

    if pcb > best_score:
        best_score = pcb
        best_stream = "Science (PCB)"
        best_careers = "Doctor (MBBS), Pharmacist, Biotechnologist, Medical Researcher"
        best_exams = "NEET UG"

    if commerce > best_score:
        best_score = commerce
        best_stream = "Commerce"
        best_careers = "Chartered Accountant (CA), Investment Banker, Business Analyst"
        best_exams = "CA Foundation, CUET"

    if arts > best_score:
        best_score = arts
        best_stream = "Arts / Humanities"
        best_careers = "Lawyer, Civil Services (IAS/IPS), Journalist, Psychologist"
        best_exams = "CLAT, CUET, UPSC CSE"

    # --- Show Results ---
    print("\n" + "=" * 55)
    print("    YOUR STREAM RECOMMENDATION")
    print("=" * 55)

    print("\n  Hello, " + profile["name"] + "! Based on your quiz answers:\n")
    print("  Recommended Stream for Class 11:")
    print("  >> " + best_stream + " <<\n")
    print("  Top Careers this stream unlocks:")
    print("  " + best_careers + "\n")
    print("  Key Entrance Exams to prepare for:")
    print("  " + best_exams + "\n")

    print("  Score Breakdown:")
    print("    Science PCM : " + str(pcm) + " points")
    print("    Science PCB : " + str(pcb) + " points")
    print("    Commerce    : " + str(commerce) + " points")
    print("    Arts        : " + str(arts) + " points")
    print("=" * 55)


# -------------------- QUIZ FOR CLASS 11, 12 & COLLEGE --------------------

def run_class_11_12_quiz(profile):
    """Career Specialization Quiz for Class 11, 12 and College students."""

    print("\n" + "=" * 55)
    print("    CAREER RECOMMENDATION QUIZ")
    print("=" * 55)
    print("\n  Stream: " + profile["stream"])

    subjects = profile["subjects"]

    # --- Question 1: Interest ---
    show_menu("Q1: What type of work interests you the most?", [
        "Solving technical problems and building systems",
        "Research, experiments, and scientific discovery",
        "Business, finance, and management",
        "Creative work, design, and media",
        "Helping people and serving society",
    ])
    interest = get_single_choice("\n  Your answer (1-5): ", 5)

    # --- Question 2: Skill ---
    show_menu("Q2: Which skill describes you best?", [
        "Logical thinking and analysis",
        "Communication and leadership",
        "Creativity and artistic ability",
        "Problem solving and critical thinking",
        "Teamwork and collaboration",
    ])
    skill = get_single_choice("\n  Your answer (1-5): ", 5)

    # --- Show Profile Summary ---
    print("\n" + "=" * 55)
    print("         YOUR QUIZ SUMMARY")
    print("=" * 55)
    print("  Name     : " + profile["name"])
    print("  Class    : " + profile["grade"])
    print("  Stream   : " + profile["stream"])
    subject_names = get_subject_names(subjects)
    print("  Subjects : " + ", ".join(subject_names))
    print("  Interest : " + get_interest_name(interest))
    print("  Skill    : " + get_skill_name(skill))

    # --- Show Recommendations ---
    top_careers = show_results(profile["name"], subjects, interest, skill)

    # --- Explore in detail ---
    explore_career(top_careers)


# -------------------- CHATBOT --------------------

def chatbot_followup():
    """Simple chatbot that answers career-related follow-up questions."""
    print("\n" + "=" * 55)
    print("         ASK CAREERPATH AI (Chatbot)")
    print("=" * 55)
    print("\n  You can ask me questions! Type 'done' to go back.\n")
    print("  Try asking about:")
    print("    - Career advice    (e.g. 'how to choose a career')")
    print("    - A career         (e.g. 'tell me about data science')")
    print("    - Colleges         (e.g. 'colleges for engineering')")
    print("    - A college        (e.g. 'IIT Bombay', 'AIIMS')")
    print("    - Entrance exams   (e.g. 'tell me about JEE', 'NEET')")
    print("    - Salary info      (e.g. 'salary of software developer')\n")

    # Lists for keyword matching (exams, colleges)
    exam_keywords = ["jee main", "jee advanced", "jee", "neet", "cat exam",
                     "clat", "nata", "cuet", "bitsat", "viteee", "xat",
                     "niper", "nid dat", "nid", "nift", "ailet", "upsc"]

    college_keywords = ["iit bombay", "iit delhi", "iit madras", "iit kanpur",
                        "iit kharagpur", "nit trichy", "nit warangal", "nitk",
                        "aiims", "cmc vellore", "jipmer", "maulana azad",
                        "iim ahmedabad", "iim bangalore", "iim calcutta",
                        "xlri", "srcc", "loyola", "st stephen", "presidency",
                        "nlsiu", "nalsar", "nlu delhi", "niper",
                        "jamia hamdard", "spa delhi", "bits pilani",
                        "vit vellore", "srm", "iimc", "nift", "nid"]

    while True:
        question = input("  You: ").strip().lower()

        if question == "" or question == "done" or question == "exit" or question == "quit" or question == "bye":
            print("\n  CareerPath AI: Going back to the Main Menu!")
            break

        # Split question into individual words for safe matching
        words = get_words(question)

        # --- 1. Career Guidance Advice ---
        if "choose" in question or "confused" in question or "decide" in question or "guidance" in question or "career advice" in question or "career path" in question:
            print("\n  CareerPath AI: Choosing a career can feel overwhelming. Here's my advice:")
            print("  1. Follow your genuine interest, not peer pressure or trends.")
            print("  2. Talk to professionals working in the fields you like.")
            print("  3. Try internships or online courses to test the waters.")
            print("  4. Look at long-term growth, not just starting salary.")
            print("  5. It's okay to change paths - many successful people did!\n")
            continue

        # --- 2. Specific Entrance Exam ---
        exam_found = False
        for ek in exam_keywords:
            if ek in question:
                results = search_exam_by_name(ek.replace(" exam", ""))
                if len(results) > 0:
                    print("\n  CareerPath AI:")
                    show_exam_detail(results[0])
                    exam_found = True
                break
        if exam_found:
            continue

        # --- 3. Specific College ---
        college_found = False
        for ck in college_keywords:
            if ck in question:
                results = search_colleges_by_name(ck)
                if len(results) > 0:
                    print("\n  CareerPath AI:")
                    show_college_detail(results[0])
                    college_found = True
                break
        if college_found:
            continue

        # --- 4. Colleges by stream or location ---
        if "college" in question or "colleges" in question or "institute" in question or "university" in question:
            found = False
            streams = ["engineering", "medical", "management", "commerce",
                       "arts", "design", "law", "pharmacy", "architecture", "media"]
            for stream in streams:
                if stream in question:
                    results = search_colleges_by_stream(stream)
                    print("\n  CareerPath AI:")
                    show_college_list(results, "Colleges for " + stream.title())
                    found = True
                    break

            if not found:
                cities = ["delhi", "mumbai", "bangalore", "chennai", "kolkata",
                          "hyderabad", "ahmedabad", "vellore", "kanpur", "kharagpur"]
                for city in cities:
                    if city in question:
                        results = search_colleges_by_location(city)
                        print("\n  CareerPath AI:")
                        show_college_list(results, "Colleges in " + city.title())
                        found = True
                        break

            if not found:
                print("\n  CareerPath AI: I can help you find colleges!")
                print("  Try: 'colleges for engineering' or 'colleges in Delhi'.\n")
            continue

        # --- 5. Entrance exams by stream ---
        if "entrance" in question or "exam" in words:
            found = False
            streams = ["engineering", "medical", "management", "law",
                       "design", "pharmacy", "architecture", "government"]
            for stream in streams:
                if stream in question:
                    results = search_exam_by_stream(stream)
                    print("\n  CareerPath AI:")
                    show_exam_list(results, "Entrance Exams for " + stream.title())
                    found = True
                    break
            if not found:
                print("\n  CareerPath AI: Try 'entrance exams for engineering' or 'exams for medical'.\n")
            continue

        # --- 6. Specific Career Search ---
        career_found = False
        for career in careers:
            career_name = career["name"].lower()
            # Check if the full career name appears in the question
            if career_name in question:
                print("\n  CareerPath AI:")
                show_career_detail(career)
                career_found = True
                break

        if not career_found:
            # Check common career keywords using word-level matching
            if "software" in words or "developer" in words or "programmer" in words or "coding" in words:
                for c in careers:
                    if c["name"] == "Software Developer":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "data science" in question or "data scientist" in question:
                for c in careers:
                    if c["name"] == "Data Scientist":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "doctor" in words or "mbbs" in words:
                for c in careers:
                    if c["name"] == "Doctor (MBBS)":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "ca" in words or "chartered accountant" in question:
                for c in careers:
                    if c["name"] == "Chartered Accountant (CA)":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "mba" in words or "business" in words or "management" in words:
                for c in careers:
                    if c["name"] == "Business Analyst":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "lawyer" in words or "law" in words or "advocate" in words:
                for c in careers:
                    if c["name"] == "Lawyer / Advocate":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "engineer" in words or "engineering" in words:
                print("\n  CareerPath AI: Engineering is a broad field!")
                print("  Popular branches: Computer Science, Mechanical, Electrical, Civil.")
                print("  Path: 10+2 (PCM) -> JEE/State CET -> B.Tech (4 years)")
                print("  Salary: 4-25+ LPA depending on branch and company.\n")
                career_found = True
            elif "teacher" in words or "teaching" in words or "professor" in words:
                for c in careers:
                    if c["name"] == "Teacher / Professor":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break
            elif "designer" in words or "design" in words:
                for c in careers:
                    if c["name"] == "Graphic Designer":
                        print("\n  CareerPath AI:")
                        show_career_detail(c)
                        career_found = True
                        break

        if career_found:
            continue

        # --- 7. Salary query ---
        if "salary" in words or "pay" in words or "earn" in words:
            print("\n  CareerPath AI: Salaries vary by field, experience and location.")
            print("  High-paying fields: AI/ML, Investment Banking, Medicine, CA.")
            print("  Ask me about a specific career for salary details!\n")
            continue

        # --- 8. Help ---
        if "help" in words:
            print("\n  CareerPath AI: I can help you with:")
            print("  - Career advice      (e.g. 'how to choose a career')")
            print("  - Career details     (e.g. 'tell me about doctor')")
            print("  - Colleges           (e.g. 'colleges for engineering')")
            print("  - Entrance exams     (e.g. 'tell me about JEE')")
            print("  - Salary info        (e.g. 'salary of CA')")
            print("  Type 'done' when you're finished.\n")
            continue

        # --- 9. Greetings ---
        if "thank" in words or "thanks" in words:
            print("\n  CareerPath AI: You're welcome! Happy to help!\n")
            continue

        if "hi" in words or "hello" in words or "hey" in words:
            print("\n  CareerPath AI: Hello! Ask me anything about careers!\n")
            continue

        # --- 10. Fallback ---
        print("\n  CareerPath AI: I'm not sure about that.")
        print("  Try asking about a specific career, college, or entrance exam.")
        print("  Type 'help' for examples!\n")


# -------------------- MAIN PROGRAM --------------------

def main():
    """Main function - runs the chatbot with a dashboard menu."""

    show_banner()

    # STEP 1: Student Profile Onboarding
    profile = setup_user_profile()

    # STEP 2: Main Dashboard Menu Loop
    while True:
        print("\n" + "=" * 55)
        print("  MAIN MENU  |  " + profile["name"] + " (" + profile["grade"] + ")")
        print("=" * 55)

        if profile["group"] == "junior":
            print("  1. Take Stream Discovery Quiz (Which stream for Class 11?)")
        else:
            print("  1. Take Career Recommendation Quiz")

        print("  2. Explore Colleges and Entrance Exams")
        print("  3. Ask CareerPath AI (Chatbot Q&A)")
        print("  4. View My Profile")
        print("  5. Exit Program")
        print("=" * 55)

        choice = get_single_choice("\n  Enter your choice (1-5): ", 5)

        if choice == "1":
            if profile["group"] == "junior":
                run_class_9_10_quiz(profile)
            else:
                run_class_11_12_quiz(profile)

        elif choice == "2":
            college_explorer_menu()

        elif choice == "3":
            chatbot_followup()

        elif choice == "4":
            show_my_profile(profile)

        elif choice == "5":
            break

    # STEP 3: Farewell
    print("\n" + "=" * 55)
    print("  THANK YOU, " + profile["name"].upper() + "!")
    print("=" * 55)
    print("\n  Thank you for using CareerPath AI!")
    print("  Remember: Your career path is a journey, not a single decision.")
    print("  Keep exploring your interests and follow your passion.")
    print("  Best of luck for your future!\n")


# Run the program
main()
