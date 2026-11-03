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

careers = [
    {
        "name": "Software Developer",
        "description": "Design, build and maintain software applications and systems.",
        "education": "B.Tech/B.E. in Computer Science or BCA/MCA",
        "salary": "5-25 LPA",
        "tags_subject": ["1", "3"],       # Maths, CS
        "tags_interest": ["1"],            # Solving technical problems
        "tags_skill": ["1", "4"],          # Logical thinking, Problem solving
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
    print("\n" + "=" * 50)
    print("            ★  CAREERPATH  AI  ★")
    print("         CAREER COUNSELLING CHATBOT")
    print("=" * 50)


def show_menu(title, options):
    """Display a numbered menu and return nothing."""
    print("\n" + title)
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])


def get_single_choice(prompt, max_val):
    """Get a single valid choice from the user (1 to max_val)."""
    while True:
        choice = input(prompt).strip()
        if choice == "":
            print("  ⚠ Please enter a choice.")
        elif choice.isdigit() and 1 <= int(choice) <= max_val:
            return choice
        else:
            print("  ⚠ Invalid. Enter a number from 1 to " + str(max_val) + ".")


def get_multi_choice(prompt, max_val):
    """Get one or more valid choices separated by commas."""
    while True:
        raw = input(prompt).strip().replace(" ", "")
        if raw == "":
            print("  ⚠ Please enter at least one choice.")
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
            print("  ⚠ Invalid. Enter numbers from 1 to " + str(max_val) + " separated by commas.")


def calculate_scores(subjects, interest, skill):
    """
    Score each career based on how well it matches the user's inputs.
    Uses simple if-else counting — no ML, no libraries.
    
    Scoring rules:
      - Each matching subject tag     = +2 points
      - Matching interest tag         = +3 points  (weighted higher)
      - Matching skill tag            = +2 points
    """
    scored = []

    for career in careers:
        score = 0

        # Subject match — check each selected subject
        for s in subjects:
            if s in career["tags_subject"]:
                score = score + 2

        # Interest match
        if interest in career["tags_interest"]:
            score = score + 3

        # Skill match
        if skill in career["tags_skill"]:
            score = score + 2

        if score > 0:
            scored.append({"career": career, "score": score})

    # Sort by score (simple bubble sort — no imports needed)
    for i in range(len(scored)):
        for j in range(i + 1, len(scored)):
            if scored[j]["score"] > scored[i]["score"]:
                temp = scored[i]
                scored[i] = scored[j]
                scored[j] = temp

    return scored


def show_career_detail(career):
    """Display full details of a single career."""
    print("\n" + "-" * 50)
    print("  📌  " + career["name"])
    print("-" * 50)
    print("  Description : " + career["description"])
    print("  Education   : " + career["education"])
    print("  Salary Range: " + career["salary"])
    print("-" * 50)


def show_results(name, subjects, interest, skill):
    """Show career recommendations based on user inputs."""
    scored = calculate_scores(subjects, interest, skill)

    print("\n" + "=" * 50)
    print("     📊  YOUR CAREER RECOMMENDATIONS")
    print("=" * 50)
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

        # Star rating based on score
        if score >= 7:
            stars = "★★★★★"
            match_text = "Excellent Match"
        elif score >= 5:
            stars = "★★★★☆"
            match_text = "Strong Match"
        elif score >= 3:
            stars = "★★★☆☆"
            match_text = "Good Match"
        else:
            stars = "★★☆☆☆"
            match_text = "Partial Match"

        print("  " + str(i + 1) + ". " + career["name"])
        print("     " + stars + "  (" + match_text + ")")
        print("     " + career["description"])
        print()

    return scored[:count]


def explore_career(top_careers):
    """Let the user explore a recommended career in detail."""
    if len(top_careers) == 0:
        return

    while True:
        print("\n💬 Want to explore a career in detail?")
        print("  Enter a number (1-" + str(len(top_careers)) + ") to see details, or 0 to skip.")

        choice = input("  Your choice: ").strip()

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(top_careers):
            show_career_detail(top_careers[int(choice) - 1]["career"])
        else:
            print("  ⚠ Invalid choice.")


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


def show_profile_summary(name, subjects, interest, skill):
    """Show a summary of the user's profile."""
    print("\n" + "=" * 50)
    print("     📋  YOUR PROFILE SUMMARY")
    print("=" * 50)

    print("\n  Name     : " + name)

    subject_names = get_subject_names(subjects)
    print("  Subjects : " + ", ".join(subject_names))
    print("  Interest : " + get_interest_name(interest))
    print("  Skill    : " + get_skill_name(skill))


def chatbot_followup():
    """Simple chatbot that answers career-related follow-up questions."""
    print("\n" + "=" * 50)
    print("     🤖  ASK CAREERPATH AI")
    print("=" * 50)
    print("\n  You can ask me questions! Type 'done' to exit.\n")
    print("  Try asking about:")
    print("    - A specific career  (e.g. 'tell me about data science')")
    print("    - Education paths    (e.g. 'how to become a doctor')")
    print("    - Salary info        (e.g. 'salary of software developer')")
    print("    - Career comparisons (e.g. 'compare CA and MBA')")
    print("    - Colleges           (e.g. 'colleges for engineering')")
    print("    - Entrance exams     (e.g. 'tell me about JEE')\n")

    while True:
        question = input("  You: ").strip().lower()

        if question == "" or question == "done" or question == "exit" or question == "quit" or question == "bye":
            print("\n  CareerPath AI: Goodbye! All the best for your future! 🎉")
            break

        answered = False

        # Search career database for matching career name
        for career in careers:
            career_lower = career["name"].lower()
            if career_lower in question or career_lower.split("/")[0].strip().lower() in question:
                print("\n  CareerPath AI:")
                show_career_detail(career)
                answered = True
                break

        if answered:
            continue

        # --- College and Exam queries ---

        # Check if user is asking about a specific entrance exam
        exam_keywords = ["jee main", "jee advanced", "neet", "cat exam", "clat", "nata",
                         "cuet", "bitsat", "viteee", "xat", "niper", "nid dat",
                         "nift entrance", "ailet", "upsc"]
        exam_found = False
        for ek in exam_keywords:
            if ek in question:
                results = search_exam_by_name(ek.replace(" exam", ""))
                if len(results) > 0:
                    print("\n  CareerPath AI:")
                    for r in results:
                        show_exam_detail(r)
                    exam_found = True
                break

        if exam_found:
            continue

        # Check if user is asking about a specific college
        college_keywords = ["iit bombay", "iit delhi", "iit madras", "iit kanpur", "iit kharagpur",
                            "nit trichy", "nit warangal", "nitk", "nit surathkal",
                            "aiims", "cmc vellore", "jipmer", "maulana azad",
                            "iim ahmedabad", "iim bangalore", "iim calcutta", "xlri",
                            "srcc", "lsr", "loyola", "st stephen", "presidency",
                            "nid", "nift", "nlsiu", "nalsar", "nlu delhi",
                            "niper", "jamia hamdard", "spa delhi",
                            "bits pilani", "vit vellore", "srm", "iimc"]
        college_found = False
        for ck in college_keywords:
            if ck in question:
                results = search_colleges_by_name(ck)
                if len(results) > 0:
                    print("\n  CareerPath AI:")
                    for r in results:
                        show_college_detail(r)
                    college_found = True
                break

        if college_found:
            continue

        # Check if user is asking about colleges for a stream
        if "college" in question or "colleges" in question or "institute" in question or "university" in question:
            stream_found = False
            stream_list = ["engineering", "medical", "management", "commerce", "arts",
                           "design", "law", "pharmacy", "architecture", "media"]
            for stream in stream_list:
                if stream in question:
                    results = search_colleges_by_stream(stream)
                    print("\n  CareerPath AI:")
                    show_college_list(results, "Colleges for " + stream.title())
                    stream_found = True
                    break

            if not stream_found:
                # Check by location
                locations = ["delhi", "mumbai", "bangalore", "chennai", "kolkata",
                             "hyderabad", "pune", "ahmedabad", "jamshedpur", "vellore",
                             "kanpur", "kharagpur", "puducherry", "mohali", "mangalore",
                             "warangal", "pilani"]
                for loc in locations:
                    if loc in question:
                        results = search_colleges_by_location(loc)
                        print("\n  CareerPath AI:")
                        show_college_list(results, "Colleges in " + loc.title())
                        stream_found = True
                        break

            if not stream_found:
                print("\n  CareerPath AI: I can help you find colleges!")
                print("  Try: 'colleges for engineering', 'colleges in Delhi',")
                print("  or ask about a specific college like 'IIT Bombay'.")
            continue

        # Check if asking about entrance exam for a stream
        if "entrance" in question or "exam" in question:
            stream_found = False
            stream_list = ["engineering", "medical", "management", "law",
                           "design", "pharmacy", "architecture", "government"]
            for stream in stream_list:
                if stream in question:
                    results = search_exam_by_stream(stream)
                    print("\n  CareerPath AI:")
                    show_exam_list(results, "Entrance Exams for " + stream.title())
                    stream_found = True
                    break
            if not stream_found:
                print("\n  CareerPath AI: I can help with entrance exams!")
                print("  Try: 'entrance exams for engineering', 'tell me about JEE',")
                print("  or 'exams for medical'.")
            continue

        # Keyword-based responses using if-else

        if "engineering" in question or "engineer" in question:
            print("\n  CareerPath AI: Engineering is a broad field!")
            print("  Popular branches: Computer Science, Mechanical, Electrical, Civil, Electronics.")
            print("  Path: 10+2 (PCM) → JEE/State CET → B.Tech (4 years)")
            print("  Salary: 4-25+ LPA depending on branch and company.\n")

        elif "doctor" in question or "mbbs" in question or "medical" in question:
            print("\n  CareerPath AI: To become a doctor:")
            print("  Path: 10+2 (PCB) → NEET → MBBS (5.5 years) → MD/MS (3 years)")
            print("  It requires dedication but is very rewarding.")
            print("  Salary: 8-30+ LPA for specialists.\n")

        elif "data science" in question or "data analyst" in question:
            print("\n  CareerPath AI: Data Science is a booming field!")
            print("  Skills needed: Python, Statistics, SQL, Machine Learning")
            print("  Path: B.Tech/B.Sc. → Learn Python & ML → Build projects → Apply")
            print("  Salary: 6-30 LPA. Very high demand!\n")

        elif "ca" in question or "chartered accountant" in question:
            print("\n  CareerPath AI: Chartered Accountancy (CA):")
            print("  Path: After 10th/12th → CA Foundation → CA Inter → CA Final")
            print("  Duration: 4-5 years after 12th")
            print("  Salary: 7-25 LPA. Top CAs earn 50+ LPA.\n")

        elif "mba" in question or "business" in question or "management" in question:
            print("\n  CareerPath AI: MBA (Master of Business Administration):")
            print("  Path: Any graduation → CAT/MAT/GMAT → MBA (2 years)")
            print("  Specialisations: Finance, Marketing, HR, Operations")
            print("  Salary: 8-30 LPA from top B-schools.\n")

        elif "design" in question or "designer" in question:
            print("\n  CareerPath AI: Design careers include:")
            print("  - Graphic Design, UI/UX Design, Fashion Design, Interior Design")
            print("  Path: 10+2 → NID/NIFT/UCEED exam → B.Des (4 years)")
            print("  Key skills: Creativity, tools like Figma, Photoshop, Illustrator.\n")

        elif "salary" in question or "pay" in question or "earn" in question:
            print("\n  CareerPath AI: Salaries vary by field, experience and location.")
            print("  High-paying fields: AI/ML, Investment Banking, Medicine, CA")
            print("  Ask me about a specific career for salary details!\n")

        elif "compare" in question:
            print("\n  CareerPath AI: To compare careers, think about:")
            print("  1. Your personal interest and passion")
            print("  2. Education time and cost")
            print("  3. Job availability and growth")
            print("  4. Work-life balance")
            print("  5. Salary potential")
            print("  Ask me about specific careers to compare!\n")

        elif "help" in question:
            print("\n  CareerPath AI: I can help you with:")
            print("  - Career information (e.g. 'tell me about AI engineering')")
            print("  - Education paths (e.g. 'how to become a lawyer')")
            print("  - Salary details (e.g. 'salary of a CA')")
            print("  - College info (e.g. 'IIT Bombay', 'colleges for medical')")
            print("  - Entrance exams (e.g. 'tell me about JEE', 'exams for law')")
            print("  - General advice (e.g. 'how to choose a career')")
            print("  Type 'done' when you're finished.\n")

        elif "choose" in question or "confused" in question or "decide" in question:
            print("\n  CareerPath AI: Choosing a career can feel overwhelming. Here's my advice:")
            print("  1. Follow your genuine interest, not trends.")
            print("  2. Talk to professionals in the field.")
            print("  3. Try internships or online courses to test it out.")
            print("  4. Consider your long-term goals, not just salary.")
            print("  5. It's okay to change paths — many successful people did!\n")

        elif "thank" in question:
            print("\n  CareerPath AI: You're welcome! Happy to help! 😊\n")

        elif "hello" in question or "hi" in question or "hey" in question:
            print("\n  CareerPath AI: Hello! Ask me anything about careers! 😊\n")

        else:
            print("\n  CareerPath AI: I'm not sure about that.")
            print("  Try asking about a specific career, education path, or salary.")
            print("  Type 'help' for a list of things I can answer!\n")


# -------------------- MAIN PROGRAM --------------------

def main():
    """Main function — runs the chatbot."""
    show_banner()
    print("\nWelcome! I'm CareerPath AI, your career counselling assistant.")
    print("I'll ask you a few questions and recommend the best careers for you.\n")

    # Get user name
    name = input("What's your name? ").strip()
    if name == "":
        name = "Student"

    print("\nNice to meet you, " + name + "! Let's get started.\n")

    keep_going = True

    while keep_going:

        # ---- STEP 1: Subject Selection ----
        show_menu(
            "📚 QUESTION 1: What are your favourite subjects? (pick one or more)",
            [
                "Mathematics",
                "Biology",
                "Computer Science",
                "Commerce",
                "Arts / Humanities",
            ],
        )
        subjects = get_multi_choice("\n  Enter choices (e.g. 1,3): ", 5)

        # ---- STEP 2: Interest Selection ----
        show_menu(
            "💡 QUESTION 2: What type of work interests you most?",
            [
                "Solving technical problems",
                "Research and experiments",
                "Business and management",
                "Creative work and design",
                "Helping people and society",
            ],
        )
        interest = get_single_choice("\n  Enter your choice (1-5): ", 5)

        # ---- STEP 3: Skill Selection ----
        show_menu(
            "🛠️  QUESTION 3: Which skill describes you best?",
            [
                "Logical thinking",
                "Communication",
                "Creativity",
                "Problem solving",
                "Teamwork",
            ],
        )
        skill = get_single_choice("\n  Enter your choice (1-5): ", 5)

        # ---- STEP 4: Show Profile Summary ----
        show_profile_summary(name, subjects, interest, skill)

        # ---- STEP 5: Show Recommendations ----
        top_careers = show_results(name, subjects, interest, skill)

        # ---- STEP 6: Explore in detail ----
        explore_career(top_careers)

        # ---- STEP 7: College & Exam Explorer ----
        print("\n" + "=" * 50)
        print("  Would you like to explore colleges and entrance exams?")
        print("  1. Yes, open the College Explorer")
        print("  2. No, skip to Q&A chatbot")
        print("=" * 50)

        college_choice = get_single_choice("  Your choice (1-2): ", 2)
        if college_choice == "1":
            college_explorer_menu()

        # ---- STEP 8: Follow-up chatbot ----
        chatbot_followup()

        # ---- STEP 9: Ask to restart or exit ----
        print("\n" + "=" * 50)
        print("  What would you like to do?")
        print("  1. Start over with new answers")
        print("  2. Exit")
        print("=" * 50)

        final = get_single_choice("  Your choice (1-2): ", 2)

        if final == "2":
            keep_going = False

    # Goodbye message
    print("\n" + "=" * 50)
    print("          ★  THANK YOU, " + name.upper() + "!  ★")
    print("=" * 50)
    print("\n  Thank you for using CareerPath AI!")
    print("  Remember: These recommendations are a starting point.")
    print("  Explore your interests, get real-world experience,")
    print("  and follow your passion. Good luck! 🚀\n")


# Run the program
main()
