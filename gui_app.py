# ============================================================
#                CAREERPATH AI - GUI VERSION
#         Tkinter Frontend for Career Counselling Bot
#
#   This file creates a graphical window (GUI) for the chatbot.
#   It imports the backend data and scoring logic from main.py
#   and college_database.py, so no logic is duplicated.
#
#   Run this file to start the GUI version:
#       python gui_app.py
#
#   Widgets used: Label, Button, Entry, Text, Radiobutton,
#                 Checkbutton, Frame, Scrollbar, OptionMenu
# ============================================================

from tkinter import *

# Import backend data and functions from our existing files
from main import careers, calculate_scores, get_subject_names
from main import get_interest_name, get_skill_name, get_words
from college_database import colleges, entrance_exams
from college_database import search_colleges_by_stream, search_colleges_by_name
from college_database import search_colleges_by_location
from college_database import search_exam_by_name, search_exam_by_stream


# ==================== COLOUR AND FONT SETTINGS ====================
# We store colours and fonts in variables so they are easy to change.

BG_MAIN = "#f0f4f8"           # Light grey-blue background
HEADER_BG = "#1a237e"         # Dark navy blue for header
BTN_BG = "#1565c0"            # Blue for buttons
BTN_HOVER = "#0d47a1"         # Darker blue when mouse hovers
ACCENT = "#43a047"            # Green for positive/success
TEXT_DARK = "#333333"          # Dark text colour
WHITE = "#ffffff"              # White
CHAT_BG = "#e8eaf6"           # Light blue-grey for chat area
USER_MSG = "#c8e6c9"          # Light green for user messages
BOT_MSG = "#bbdefb"           # Light blue for bot messages
CARD_BG = "#ffffff"            # White cards
BORDER = "#bdbdbd"             # Grey border

FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_HEADING = ("Segoe UI", 14, "bold")
FONT_BODY = ("Segoe UI", 11)
FONT_SMALL = ("Segoe UI", 10)
FONT_BTN = ("Segoe UI", 11, "bold")
FONT_CHAT = ("Segoe UI", 11)


# ==================== MAIN APPLICATION CLASS ====================
# We use a class to keep all the pages and data together.
# self.root   = the main window
# self.page   = the content frame that changes on each page
# self.profile = dictionary storing the student's information

class CareerPathApp:
    """Main application class. Creates the window and manages all pages."""

    def __init__(self):
        """Set up the main window and show the Welcome page."""

        # --- Create Main Window ---
        self.root = Tk()
        self.root.title("CareerPath AI - Career Counselling Bot")
        self.root.geometry("850x620")
        self.root.configure(bg=BG_MAIN)
        self.root.resizable(True, True)

        # --- Student Profile (empty at start) ---
        self.profile = {
            "name": "",
            "grade": "",
            "group": "",
            "language": "",
            "skill_subject": "",
            "stream": "",
            "optionals": [],
            "subjects": [],
        }

        # --- Header Bar (stays on every page) ---
        self.header = Frame(self.root, bg=HEADER_BG, height=55)
        self.header.pack(fill=X)
        self.header.pack_propagate(False)   # Keep fixed height

        self.header_label = Label(
            self.header,
            text="   CAREERPATH AI  -  Career Counselling Bot",
            font=FONT_TITLE, bg=HEADER_BG, fg=WHITE, anchor="w"
        )
        self.header_label.pack(side=LEFT, padx=10, pady=8)

        # --- Page Container (content changes here) ---
        self.page = Frame(self.root, bg=BG_MAIN)
        self.page.pack(fill=BOTH, expand=True, padx=15, pady=10)

        # --- Show Welcome Page First ---
        self.show_welcome_page()

    # ==================== PAGE MANAGEMENT ====================

    def clear_page(self):
        """Remove all widgets from the page frame to load a new page."""
        for widget in self.page.winfo_children():
            widget.destroy()

    # ==================== PAGE 1: WELCOME ====================

    def show_welcome_page(self):
        """Welcome page - asks for name and class."""
        self.clear_page()

        # Title
        Label(self.page, text="Welcome! Let's set up your profile.",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(20, 15))

        # --- Name Input ---
        name_frame = Frame(self.page, bg=BG_MAIN)
        name_frame.pack(pady=5)

        Label(name_frame, text="Your Name:", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(side=LEFT, padx=(0, 10))

        self.name_entry = Entry(name_frame, font=FONT_BODY, width=25,
                                relief="solid", bd=1)
        self.name_entry.pack(side=LEFT)
        self.name_entry.focus()

        # --- Class Selection (Radiobuttons) ---
        Label(self.page, text="\nSelect your current class:",
              font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 5))

        self.class_var = StringVar(value="")   # Stores selected class

        class_options = [
            ("Class 9  (Early career exploration)", "Class 9"),
            ("Class 10 (Planning stream for Class 11)", "Class 10"),
            ("Class 11 (Exploring career pathways)", "Class 11"),
            ("Class 12 (Preparing for entrance exams)", "Class 12"),
            ("College / Other", "College / Other"),
        ]

        for text, value in class_options:
            Radiobutton(
                self.page, text=text, variable=self.class_var, value=value,
                font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK,
                activebackground=BG_MAIN, selectcolor=WHITE, anchor="w"
            ).pack(padx=60, anchor="w")

        # --- Continue Button ---
        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=(10, 0))

        Button(self.page, text="Continue  >>", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2",
               command=self.welcome_continue).pack(pady=10)

    def welcome_continue(self):
        """Validate welcome page inputs and go to subject setup."""
        name = self.name_entry.get().strip()
        grade = self.class_var.get()

        if name == "":
            name = "Student"
        if grade == "":
            self.error_label.config(text="Please select your class.")
            return

        # Save to profile
        self.profile["name"] = name
        self.profile["grade"] = grade

        if grade == "Class 9" or grade == "Class 10":
            self.profile["group"] = "junior"
            self.show_junior_setup()
        else:
            self.profile["group"] = "senior"
            self.show_senior_setup()

    # ==================== PAGE 2a: JUNIOR SETUP (Class 9/10) ====================

    def show_junior_setup(self):
        """Ask Class 9/10 students for language and skill subject."""
        self.clear_page()

        Label(self.page, text="Subject Selection (" + self.profile["grade"] + ")",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(20, 15))

        # --- 2nd Language ---
        Label(self.page, text="Your 2nd Language:", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(anchor="w", padx=60)

        self.lang_var = StringVar(value="")
        for text in ["Hindi", "Sanskrit", "Other"]:
            Radiobutton(self.page, text=text, variable=self.lang_var,
                        value=text, font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK,
                        activebackground=BG_MAIN, selectcolor=WHITE
                        ).pack(anchor="w", padx=80)

        # --- Skill Subject ---
        Label(self.page, text="\nYour Skill / Optional Subject:", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(anchor="w", padx=60, pady=(10, 0))

        self.skill_var = StringVar(value="")
        for text, value in [("Information Technology (IT)", "IT"),
                            ("Computer Science (CS)", "CS"),
                            ("Artificial Intelligence (AI)", "AI"),
                            ("None / Other", "None")]:
            Radiobutton(self.page, text=text, variable=self.skill_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK,
                        activebackground=BG_MAIN, selectcolor=WHITE
                        ).pack(anchor="w", padx=80)

        # --- Error + Continue ---
        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=(10, 0))

        Button(self.page, text="Continue  >>", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2",
               command=self.junior_continue).pack(pady=10)

    def junior_continue(self):
        """Validate junior setup and go to dashboard."""
        lang = self.lang_var.get()
        skill = self.skill_var.get()

        if lang == "" or skill == "":
            self.error_label.config(text="Please select both options.")
            return

        self.profile["language"] = lang
        self.profile["skill_subject"] = skill
        self.profile["stream"] = "Not yet chosen"
        self.profile["subjects"] = []

        self.show_dashboard()

    # ==================== PAGE 2b: SENIOR SETUP (Class 11/12/College) ====================

    def show_senior_setup(self):
        """Ask Class 11/12 students for stream and optional subjects."""
        self.clear_page()

        Label(self.page, text="Subject Selection (" + self.profile["grade"] + ")",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 10))

        # --- Stream ---
        Label(self.page, text="Your Main Stream:", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(anchor="w", padx=60)

        self.stream_var = StringVar(value="")
        stream_options = [
            ("Science (PCM - Physics, Chemistry, Maths)", "PCM"),
            ("Science (PCB - Physics, Chemistry, Biology)", "PCB"),
            ("Science (PCMB - Maths and Biology both)", "PCMB"),
            ("Commerce (Accountancy, Business Studies)", "Commerce"),
            ("Arts / Humanities", "Arts"),
        ]
        for text, value in stream_options:
            Radiobutton(self.page, text=text, variable=self.stream_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK,
                        activebackground=BG_MAIN, selectcolor=WHITE
                        ).pack(anchor="w", padx=80)

        # --- Optional Subjects (Checkbuttons - can select multiple) ---
        Label(self.page, text="\nOptional Subjects (select any):", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(anchor="w", padx=60, pady=(5, 0))

        self.opt_painting = IntVar()
        self.opt_ai = IntVar()
        self.opt_cs = IntVar()
        self.opt_pe = IntVar()
        self.opt_music = IntVar()

        opt_list = [
            ("Painting", self.opt_painting),
            ("Artificial Intelligence (AI)", self.opt_ai),
            ("Computer Science (CS)", self.opt_cs),
            ("Physical Education (PE)", self.opt_pe),
            ("Music", self.opt_music),
        ]
        for text, var in opt_list:
            Checkbutton(self.page, text=text, variable=var,
                        font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK,
                        activebackground=BG_MAIN, selectcolor=WHITE
                        ).pack(anchor="w", padx=80)

        # --- Error + Continue ---
        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=(8, 0))

        Button(self.page, text="Continue  >>", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2",
               command=self.senior_continue).pack(pady=8)

    def senior_continue(self):
        """Validate senior setup and go to dashboard."""
        stream = self.stream_var.get()
        if stream == "":
            self.error_label.config(text="Please select your stream.")
            return

        # Map stream to subject tags
        if stream == "PCM":
            self.profile["stream"] = "Science (PCM)"
            subjects = ["1", "3"]
        elif stream == "PCB":
            self.profile["stream"] = "Science (PCB)"
            subjects = ["2"]
        elif stream == "PCMB":
            self.profile["stream"] = "Science (PCMB)"
            subjects = ["1", "2"]
        elif stream == "Commerce":
            self.profile["stream"] = "Commerce"
            subjects = ["4"]
        else:
            self.profile["stream"] = "Arts / Humanities"
            subjects = ["5"]

        # Collect optional subjects
        optionals = []
        if self.opt_painting.get() == 1:
            optionals.append("Painting")
            if "5" not in subjects:
                subjects.append("5")
        if self.opt_ai.get() == 1:
            optionals.append("AI")
            if "3" not in subjects:
                subjects.append("3")
        if self.opt_cs.get() == 1:
            optionals.append("CS")
            if "3" not in subjects:
                subjects.append("3")
        if self.opt_pe.get() == 1:
            optionals.append("PE")
        if self.opt_music.get() == 1:
            optionals.append("Music")
            if "5" not in subjects:
                subjects.append("5")

        self.profile["optionals"] = optionals
        self.profile["subjects"] = subjects

        self.show_dashboard()

    # ==================== PAGE 3: DASHBOARD ====================

    def show_dashboard(self):
        """Main dashboard with navigation buttons."""
        self.clear_page()

        # Update header to show name
        self.header_label.config(
            text="   CAREERPATH AI  |  " + self.profile["name"] + " (" + self.profile["grade"] + ")"
        )

        Label(self.page, text="What would you like to do?",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(30, 20))

        # --- Menu Buttons ---
        btn_frame = Frame(self.page, bg=BG_MAIN)
        btn_frame.pack()

        # Choose button text based on group
        if self.profile["group"] == "junior":
            quiz_text = "  Take Stream Discovery Quiz  "
        else:
            quiz_text = "  Take Career Recommendation Quiz  "

        buttons = [
            (quiz_text, self.show_quiz_page),
            ("  Explore Colleges & Entrance Exams  ", self.show_college_page),
            ("  Ask CareerPath AI (Chatbot Q&A)  ", self.show_chatbot_page),
            ("  View My Profile  ", self.show_profile_page),
            ("  Exit Program  ", self.root.quit),
        ]

        for text, command in buttons:
            btn = Button(btn_frame, text=text, font=FONT_BTN,
                         bg=BTN_BG, fg=WHITE, relief="flat",
                         padx=15, pady=10, width=35, cursor="hand2",
                         command=command)
            btn.pack(pady=6)

    # ==================== PAGE 4: PROFILE ====================

    def show_profile_page(self):
        """Display the student's saved profile."""
        self.clear_page()

        Label(self.page, text="Your Student Profile",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(20, 15))

        # Profile card
        card = Frame(self.page, bg=CARD_BG, relief="solid", bd=1, padx=25, pady=20)
        card.pack(padx=40)

        info_lines = [
            ("Name", self.profile["name"]),
            ("Class", self.profile["grade"]),
        ]

        if self.profile["group"] == "junior":
            info_lines.append(("Language", self.profile["language"]))
            info_lines.append(("Skill Subject", self.profile["skill_subject"]))
            info_lines.append(("Stream", self.profile["stream"]))
        else:
            info_lines.append(("Stream", self.profile["stream"]))
            if len(self.profile["optionals"]) > 0:
                info_lines.append(("Optionals", ", ".join(self.profile["optionals"])))
            subject_names = get_subject_names(self.profile["subjects"])
            if len(subject_names) > 0:
                info_lines.append(("Mapped Subjects", ", ".join(subject_names)))

        for label_text, value_text in info_lines:
            row = Frame(card, bg=CARD_BG)
            row.pack(fill=X, pady=3)
            Label(row, text=label_text + " :", font=FONT_BTN, bg=CARD_BG,
                  fg=TEXT_DARK, width=16, anchor="e").pack(side=LEFT)
            Label(row, text="  " + value_text, font=FONT_BODY, bg=CARD_BG,
                  fg=TEXT_DARK, anchor="w").pack(side=LEFT)

        # Back button
        Button(self.page, text="<< Back to Menu", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=15, pady=8,
               cursor="hand2",
               command=self.show_dashboard).pack(pady=25)

    # ==================== PAGE 5: QUIZ ====================

    def show_quiz_page(self):
        """Start the quiz. Routes to junior or senior quiz."""
        if self.profile["group"] == "junior":
            self.start_junior_quiz()
        else:
            self.start_senior_quiz()

    # ---------- JUNIOR QUIZ (Stream Discovery) ----------

    def start_junior_quiz(self):
        """Stream Discovery Quiz for Class 9/10 - Question 1."""
        self.quiz_scores = {"pcm": 0, "pcb": 0, "commerce": 0, "arts": 0}

        # Bonus from skill subject
        skill = self.profile["skill_subject"]
        if skill == "CS" or skill == "AI" or skill == "IT":
            self.quiz_scores["pcm"] = self.quiz_scores["pcm"] + 2

        self.show_junior_q1()

    def show_junior_q1(self):
        """Junior Quiz - Question 1 of 3."""
        self.clear_page()

        Label(self.page, text="Stream Discovery Quiz",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 5))
        Label(self.page, text="Question 1 of 3",
              font=FONT_SMALL, bg=BG_MAIN, fg="grey").pack()

        Label(self.page, text="\nWhat type of problems do you enjoy solving the most?",
              font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 10))

        self.q_var = StringVar(value="")
        options = [
            ("Maths puzzles, equations, and coding challenges", "1"),
            ("Understanding how the human body and nature work", "2"),
            ("Managing money, budgets, and business ideas", "3"),
            ("Writing, debating, drawing, or social topics", "4"),
        ]
        for text, value in options:
            Radiobutton(self.page, text=text, variable=self.q_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN,
                        fg=TEXT_DARK, activebackground=BG_MAIN,
                        selectcolor=WHITE).pack(anchor="w", padx=60)

        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=5)

        Button(self.page, text="Next  >>", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2", command=self.junior_q1_next).pack()

    def junior_q1_next(self):
        """Process Q1 answer and show Q2."""
        ans = self.q_var.get()
        if ans == "":
            self.error_label.config(text="Please select an answer.")
            return
        # Score Q1 (3 points)
        if ans == "1":
            self.quiz_scores["pcm"] = self.quiz_scores["pcm"] + 3
        elif ans == "2":
            self.quiz_scores["pcb"] = self.quiz_scores["pcb"] + 3
        elif ans == "3":
            self.quiz_scores["commerce"] = self.quiz_scores["commerce"] + 3
        elif ans == "4":
            self.quiz_scores["arts"] = self.quiz_scores["arts"] + 3
        self.show_junior_q2()

    def show_junior_q2(self):
        """Junior Quiz - Question 2 of 3."""
        self.clear_page()

        Label(self.page, text="Stream Discovery Quiz",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 5))
        Label(self.page, text="Question 2 of 3",
              font=FONT_SMALL, bg=BG_MAIN, fg="grey").pack()

        Label(self.page, text="\nWhat is your dream future work environment?",
              font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 10))

        self.q_var = StringVar(value="")
        options = [
            ("Tech office, software company, or research lab", "1"),
            ("Hospital, clinic, or medical research centre", "2"),
            ("Corporate office, bank, or own business", "3"),
            ("Art studio, newsroom, courtroom, or government office", "4"),
        ]
        for text, value in options:
            Radiobutton(self.page, text=text, variable=self.q_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN,
                        fg=TEXT_DARK, activebackground=BG_MAIN,
                        selectcolor=WHITE).pack(anchor="w", padx=60)

        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=5)

        Button(self.page, text="Next  >>", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2", command=self.junior_q2_next).pack()

    def junior_q2_next(self):
        """Process Q2 answer and show Q3."""
        ans = self.q_var.get()
        if ans == "":
            self.error_label.config(text="Please select an answer.")
            return
        if ans == "1":
            self.quiz_scores["pcm"] = self.quiz_scores["pcm"] + 3
        elif ans == "2":
            self.quiz_scores["pcb"] = self.quiz_scores["pcb"] + 3
        elif ans == "3":
            self.quiz_scores["commerce"] = self.quiz_scores["commerce"] + 3
        elif ans == "4":
            self.quiz_scores["arts"] = self.quiz_scores["arts"] + 3
        self.show_junior_q3()

    def show_junior_q3(self):
        """Junior Quiz - Question 3 of 3."""
        self.clear_page()

        Label(self.page, text="Stream Discovery Quiz",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 5))
        Label(self.page, text="Question 3 of 3",
              font=FONT_SMALL, bg=BG_MAIN, fg="grey").pack()

        Label(self.page, text="\nIn a school group project, what role do you naturally take?",
              font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 10))

        self.q_var = StringVar(value="")
        options = [
            ("The coder / technical builder who handles tools and data", "1"),
            ("The researcher who collects facts and scientific info", "2"),
            ("The planner who manages budget and presentation pitch", "3"),
            ("The designer who creates visuals and speaks on stage", "4"),
        ]
        for text, value in options:
            Radiobutton(self.page, text=text, variable=self.q_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN,
                        fg=TEXT_DARK, activebackground=BG_MAIN,
                        selectcolor=WHITE).pack(anchor="w", padx=60)

        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=5)

        Button(self.page, text="See Results  >>", font=FONT_BTN,
               bg=ACCENT, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2", command=self.junior_q3_next).pack()

    def junior_q3_next(self):
        """Process Q3 and show junior results."""
        ans = self.q_var.get()
        if ans == "":
            self.error_label.config(text="Please select an answer.")
            return
        if ans == "1":
            self.quiz_scores["pcm"] = self.quiz_scores["pcm"] + 2
        elif ans == "2":
            self.quiz_scores["pcb"] = self.quiz_scores["pcb"] + 2
        elif ans == "3":
            self.quiz_scores["commerce"] = self.quiz_scores["commerce"] + 2
        elif ans == "4":
            self.quiz_scores["arts"] = self.quiz_scores["arts"] + 2
        self.show_junior_results()

    def show_junior_results(self):
        """Display stream recommendation for Class 9/10 students."""
        self.clear_page()

        s = self.quiz_scores
        # Find best stream
        best_score = s["pcm"]
        best_stream = "Science (PCM)"
        best_careers = "Software Developer, Data Scientist, AI Engineer, Architect"
        best_exams = "JEE Main, JEE Advanced, BITSAT"

        if s["pcb"] > best_score:
            best_score = s["pcb"]
            best_stream = "Science (PCB)"
            best_careers = "Doctor (MBBS), Pharmacist, Biotechnologist"
            best_exams = "NEET UG"

        if s["commerce"] > best_score:
            best_score = s["commerce"]
            best_stream = "Commerce"
            best_careers = "Chartered Accountant (CA), Investment Banker, Business Analyst"
            best_exams = "CA Foundation, CUET"

        if s["arts"] > best_score:
            best_score = s["arts"]
            best_stream = "Arts / Humanities"
            best_careers = "Lawyer, Civil Services (IAS/IPS), Journalist, Psychologist"
            best_exams = "CLAT, CUET, UPSC CSE"

        # --- Display Results ---
        Label(self.page, text="Your Stream Recommendation",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 10))

        # Result card
        card = Frame(self.page, bg=CARD_BG, relief="solid", bd=1, padx=25, pady=20)
        card.pack(padx=30, fill=X)

        Label(card, text="Recommended Stream for Class 11:",
              font=FONT_BODY, bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w")
        Label(card, text=best_stream, font=FONT_TITLE, bg=CARD_BG,
              fg=BTN_BG).pack(anchor="w", pady=(0, 10))

        Label(card, text="Top Careers this stream unlocks:",
              font=FONT_BTN, bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w")
        Label(card, text=best_careers, font=FONT_BODY, bg=CARD_BG,
              fg=TEXT_DARK, wraplength=600, justify=LEFT).pack(anchor="w", pady=(0, 10))

        Label(card, text="Key Entrance Exams:", font=FONT_BTN,
              bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w")
        Label(card, text=best_exams, font=FONT_BODY, bg=CARD_BG,
              fg=TEXT_DARK).pack(anchor="w", pady=(0, 10))

        # Score breakdown
        Label(card, text="Score Breakdown:", font=FONT_BTN,
              bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w", pady=(5, 0))
        scores_text = ("  Science PCM: " + str(s["pcm"]) + " pts" +
                       "  |  Science PCB: " + str(s["pcb"]) + " pts" +
                       "  |  Commerce: " + str(s["commerce"]) + " pts" +
                       "  |  Arts: " + str(s["arts"]) + " pts")
        Label(card, text=scores_text, font=FONT_SMALL, bg=CARD_BG,
              fg="grey").pack(anchor="w")

        Button(self.page, text="<< Back to Menu", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=15, pady=8,
               cursor="hand2", command=self.show_dashboard).pack(pady=20)

    # ---------- SENIOR QUIZ (Career Recommendation) ----------

    def start_senior_quiz(self):
        """Career Recommendation Quiz for Class 11/12 - Question 1."""
        self.show_senior_q1()

    def show_senior_q1(self):
        """Senior Quiz - Question 1 (Interest)."""
        self.clear_page()

        Label(self.page, text="Career Recommendation Quiz",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 5))
        Label(self.page, text="Question 1 of 2  |  Stream: " + self.profile["stream"],
              font=FONT_SMALL, bg=BG_MAIN, fg="grey").pack()

        Label(self.page, text="\nWhat type of work interests you the most?",
              font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 10))

        self.interest_var = StringVar(value="")
        options = [
            ("Solving technical problems and building systems", "1"),
            ("Research, experiments, and scientific discovery", "2"),
            ("Business, finance, and management", "3"),
            ("Creative work, design, and media", "4"),
            ("Helping people and serving society", "5"),
        ]
        for text, value in options:
            Radiobutton(self.page, text=text, variable=self.interest_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN,
                        fg=TEXT_DARK, activebackground=BG_MAIN,
                        selectcolor=WHITE).pack(anchor="w", padx=60)

        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=5)

        Button(self.page, text="Next  >>", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2", command=self.senior_q1_next).pack()

    def senior_q1_next(self):
        """Process Q1 and show Q2."""
        if self.interest_var.get() == "":
            self.error_label.config(text="Please select an answer.")
            return
        self.show_senior_q2()

    def show_senior_q2(self):
        """Senior Quiz - Question 2 (Skill)."""
        self.clear_page()

        Label(self.page, text="Career Recommendation Quiz",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(15, 5))
        Label(self.page, text="Question 2 of 2  |  Stream: " + self.profile["stream"],
              font=FONT_SMALL, bg=BG_MAIN, fg="grey").pack()

        Label(self.page, text="\nWhich skill describes you best?",
              font=FONT_BODY, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 10))

        self.skill_var = StringVar(value="")
        options = [
            ("Logical thinking and analysis", "1"),
            ("Communication and leadership", "2"),
            ("Creativity and artistic ability", "3"),
            ("Problem solving and critical thinking", "4"),
            ("Teamwork and collaboration", "5"),
        ]
        for text, value in options:
            Radiobutton(self.page, text=text, variable=self.skill_var,
                        value=value, font=FONT_BODY, bg=BG_MAIN,
                        fg=TEXT_DARK, activebackground=BG_MAIN,
                        selectcolor=WHITE).pack(anchor="w", padx=60)

        self.error_label = Label(self.page, text="", font=FONT_SMALL,
                                 bg=BG_MAIN, fg="red")
        self.error_label.pack(pady=5)

        Button(self.page, text="See Results  >>", font=FONT_BTN,
               bg=ACCENT, fg=WHITE, relief="flat", padx=20, pady=8,
               cursor="hand2", command=self.senior_q2_next).pack()

    def senior_q2_next(self):
        """Process Q2 and show career results."""
        if self.skill_var.get() == "":
            self.error_label.config(text="Please select an answer.")
            return
        self.show_senior_results()

    def show_senior_results(self):
        """Display career recommendations for Class 11/12 students."""
        self.clear_page()

        interest = self.interest_var.get()
        skill = self.skill_var.get()
        subjects = self.profile["subjects"]

        # Use the scoring engine from main.py
        scored = calculate_scores(subjects, interest, skill)

        Label(self.page, text="Your Career Recommendations",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 5))

        # Summary line
        summary = ("Interest: " + get_interest_name(interest) +
                   "  |  Skill: " + get_skill_name(skill))
        Label(self.page, text=summary, font=FONT_SMALL, bg=BG_MAIN,
              fg="grey").pack(pady=(0, 10))

        # --- Back button (pack at BOTTOM first so it's always visible) ---
        Button(self.page, text="<< Back to Menu", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=15, pady=6,
               cursor="hand2", command=self.show_dashboard).pack(side=BOTTOM, pady=10)

        # Scrollable results area
        result_frame = Frame(self.page, bg=BG_MAIN)
        result_frame.pack(fill=BOTH, expand=True)

        canvas = Canvas(result_frame, bg=BG_MAIN, highlightthickness=0)
        scrollbar = Scrollbar(result_frame, orient=VERTICAL, command=canvas.yview)
        scroll_frame = Frame(canvas, bg=BG_MAIN)

        scroll_frame.bind("<Configure>",
                          lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        if len(scored) == 0:
            Label(scroll_frame, text="No strong matches found. Try different combinations!",
                  font=FONT_BODY, bg=BG_MAIN, fg="red").pack(pady=20)
        else:
            # Show top 5
            count = 5
            if len(scored) < 5:
                count = len(scored)

            for i in range(count):
                career = scored[i]["career"]
                score = scored[i]["score"]

                if score >= 7:
                    match_text = "Excellent Match"
                    match_color = ACCENT
                elif score >= 5:
                    match_text = "Strong Match"
                    match_color = BTN_BG
                elif score >= 3:
                    match_text = "Good Match"
                    match_color = "#f57c00"
                else:
                    match_text = "Partial Match"
                    match_color = "grey"

                # Career card
                card = Frame(scroll_frame, bg=CARD_BG, relief="solid", bd=1,
                             padx=15, pady=10)
                card.pack(fill=X, padx=10, pady=5)

                top_row = Frame(card, bg=CARD_BG)
                top_row.pack(fill=X)

                Label(top_row,
                      text=str(i + 1) + ". " + career["name"],
                      font=FONT_BTN, bg=CARD_BG, fg=TEXT_DARK).pack(side=LEFT)
                Label(top_row, text=match_text, font=FONT_SMALL,
                      bg=CARD_BG, fg=match_color).pack(side=RIGHT)

                Label(card, text=career["description"], font=FONT_SMALL,
                      bg=CARD_BG, fg="grey", wraplength=600,
                      justify=LEFT).pack(anchor="w")

                detail_text = ("Education: " + career["education"] +
                               "   |   Salary: " + career["salary"])
                Label(card, text=detail_text, font=FONT_SMALL,
                      bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w", pady=(3, 0))

    # ==================== PAGE 6: CHATBOT ====================

    def show_chatbot_page(self):
        """Interactive chatbot page with a chat window and input field."""
        self.clear_page()

        Label(self.page, text="Ask CareerPath AI",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(5, 5))

        # --- Back button (pack at BOTTOM first so it's always visible) ---
        Button(self.page, text="<< Back to Menu", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=15, pady=6,
               cursor="hand2", command=self.show_dashboard).pack(side=BOTTOM, pady=5)

        # --- Input Area (pack at BOTTOM, above back button) ---
        input_frame = Frame(self.page, bg=BG_MAIN)
        input_frame.pack(side=BOTTOM, fill=X, padx=5, pady=(5, 0))

        self.chat_entry = Entry(input_frame, font=FONT_CHAT, relief="solid", bd=1)
        self.chat_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 5), ipady=6)
        self.chat_entry.focus()
        self.chat_entry.bind("<Return>", lambda e: self.send_chat())

        Button(input_frame, text=" Send ", font=FONT_BTN,
               bg=ACCENT, fg=WHITE, relief="flat", padx=12,
               cursor="hand2", command=self.send_chat).pack(side=LEFT)

        # --- Chat Display Area (fills remaining space) ---
        chat_frame = Frame(self.page, bg=CHAT_BG, relief="solid", bd=1)
        chat_frame.pack(fill=BOTH, expand=True, padx=5)

        self.chat_display = Text(chat_frame, font=FONT_CHAT, bg=CHAT_BG,
                                 fg=TEXT_DARK, wrap=WORD, state=DISABLED,
                                 relief="flat", padx=10, pady=10)
        chat_scroll = Scrollbar(chat_frame, command=self.chat_display.yview)
        self.chat_display.configure(yscrollcommand=chat_scroll.set)

        chat_scroll.pack(side=RIGHT, fill=Y)
        self.chat_display.pack(side=LEFT, fill=BOTH, expand=True)

        # Configure text tags for styling
        self.chat_display.tag_config("user", background=USER_MSG, foreground=TEXT_DARK,
                                     lmargin1=20, lmargin2=20, rmargin=20,
                                     spacing1=5, spacing3=5)
        self.chat_display.tag_config("bot", background=BOT_MSG, foreground=TEXT_DARK,
                                     lmargin1=20, lmargin2=20, rmargin=20,
                                     spacing1=5, spacing3=5)
        self.chat_display.tag_config("info", foreground="grey",
                                     lmargin1=20, spacing1=3, spacing3=3)

        # Welcome message
        self.add_bot_message("Hello, " + self.profile["name"] + "! I'm CareerPath AI.")
        self.add_bot_message("Ask me about careers, colleges, entrance exams, or salaries!")
        self.add_bot_message("Try: 'colleges for engineering', 'tell me about JEE', 'salary of CA'")

    def add_bot_message(self, text):
        """Add a bot message to the chat display."""
        self.chat_display.config(state=NORMAL)
        self.chat_display.insert(END, "CareerPath AI:\n", "info")
        self.chat_display.insert(END, text + "\n\n", "bot")
        self.chat_display.config(state=DISABLED)
        self.chat_display.see(END)

    def add_user_message(self, text):
        """Add a user message to the chat display."""
        self.chat_display.config(state=NORMAL)
        self.chat_display.insert(END, "You:\n", "info")
        self.chat_display.insert(END, text + "\n\n", "user")
        self.chat_display.config(state=DISABLED)
        self.chat_display.see(END)

    def send_chat(self):
        """Process the user's chat message and generate a response."""
        question = self.chat_entry.get().strip()
        if question == "":
            return

        self.chat_entry.delete(0, END)
        self.add_user_message(question)

        # Generate response
        response = self.get_response(question.lower())
        self.add_bot_message(response)

    def get_response(self, question):
        """
        Generate a chatbot response based on keyword matching.
        Uses the same logic as chatbot_followup() in main.py,
        but returns a string instead of printing.
        """
        words = get_words(question)

        # --- 1. Career Guidance Advice ---
        if "choose" in question or "confused" in question or "decide" in question or "guidance" in question or "career advice" in question:
            return ("Choosing a career can feel overwhelming. Here's my advice:\n"
                    "1. Follow your genuine interest, not peer pressure.\n"
                    "2. Talk to professionals in the fields you like.\n"
                    "3. Try internships or online courses to test the waters.\n"
                    "4. Look at long-term growth, not just starting salary.\n"
                    "5. It's okay to change paths - many successful people did!")

        # --- 2. Specific Entrance Exam ---
        exam_keywords = ["jee main", "jee advanced", "jee", "neet", "cat exam",
                         "clat", "nata", "cuet", "bitsat", "viteee", "xat",
                         "niper", "nid dat", "nid", "nift", "ailet", "upsc"]
        for ek in exam_keywords:
            if ek in question:
                results = search_exam_by_name(ek.replace(" exam", ""))
                if len(results) > 0:
                    return self.format_exam(results[0])
                break

        # --- 3. Specific College ---
        college_keywords = ["iit bombay", "iit delhi", "iit madras", "iit kanpur",
                            "iit kharagpur", "nit trichy", "nit warangal", "nitk",
                            "aiims", "cmc vellore", "jipmer", "maulana azad",
                            "iim ahmedabad", "iim bangalore", "iim calcutta",
                            "xlri", "srcc", "loyola", "st stephen", "presidency",
                            "nlsiu", "nalsar", "nlu delhi", "niper",
                            "jamia hamdard", "spa delhi", "bits pilani",
                            "vit vellore", "srm", "iimc", "nift", "nid"]
        for ck in college_keywords:
            if ck in question:
                results = search_colleges_by_name(ck)
                if len(results) > 0:
                    return self.format_college(results[0])
                break

        # --- 4. Colleges by stream or location ---
        if "college" in question or "colleges" in question or "institute" in question or "university" in question:
            streams = ["engineering", "medical", "management", "commerce",
                       "arts", "design", "law", "pharmacy", "architecture", "media"]
            for stream in streams:
                if stream in question:
                    results = search_colleges_by_stream(stream)
                    return self.format_college_list(results, "Colleges for " + stream.title())

            cities = ["delhi", "mumbai", "bangalore", "chennai", "kolkata",
                      "hyderabad", "ahmedabad", "vellore", "kanpur", "kharagpur"]
            for city in cities:
                if city in question:
                    results = search_colleges_by_location(city)
                    return self.format_college_list(results, "Colleges in " + city.title())

            return "I can help you find colleges!\nTry: 'colleges for engineering' or 'colleges in Delhi'."

        # --- 5. Entrance exams by stream ---
        if "entrance" in question or "exam" in words:
            streams = ["engineering", "medical", "management", "law",
                       "design", "pharmacy", "architecture", "government"]
            for stream in streams:
                if stream in question:
                    results = search_exam_by_stream(stream)
                    return self.format_exam_list(results, "Exams for " + stream.title())
            return "Try: 'entrance exams for engineering' or 'exams for medical'."

        # --- 6. Specific Career Search ---
        for career in careers:
            if career["name"].lower() in question:
                return self.format_career(career)

        # Common career keywords
        if "software" in words or "developer" in words or "programmer" in words or "coding" in words:
            for c in careers:
                if c["name"] == "Software Developer":
                    return self.format_career(c)
        elif "data science" in question or "data scientist" in question:
            for c in careers:
                if c["name"] == "Data Scientist":
                    return self.format_career(c)
        elif "doctor" in words or "mbbs" in words:
            for c in careers:
                if c["name"] == "Doctor (MBBS)":
                    return self.format_career(c)
        elif "ca" in words or "chartered accountant" in question:
            for c in careers:
                if c["name"] == "Chartered Accountant (CA)":
                    return self.format_career(c)
        elif "lawyer" in words or "law" in words or "advocate" in words:
            for c in careers:
                if c["name"] == "Lawyer / Advocate":
                    return self.format_career(c)
        elif "mba" in words or "business" in words or "management" in words:
            for c in careers:
                if c["name"] == "Business Analyst":
                    return self.format_career(c)
        elif "engineer" in words or "engineering" in words:
            return ("Engineering is a broad field!\n"
                    "Popular branches: Computer Science, Mechanical, Electrical, Civil.\n"
                    "Path: 10+2 (PCM) -> JEE/State CET -> B.Tech (4 years)\n"
                    "Salary: 4-25+ LPA depending on branch and company.")
        elif "teacher" in words or "teaching" in words or "professor" in words:
            for c in careers:
                if c["name"] == "Teacher / Professor":
                    return self.format_career(c)
        elif "designer" in words or "design" in words:
            for c in careers:
                if c["name"] == "Graphic Designer":
                    return self.format_career(c)

        # --- 7. Salary ---
        if "salary" in words or "pay" in words or "earn" in words:
            return ("Salaries vary by field, experience and location.\n"
                    "High-paying fields: AI/ML, Investment Banking, Medicine, CA.\n"
                    "Ask me about a specific career for salary details!")

        # --- 8. Help ---
        if "help" in words:
            return ("I can help you with:\n"
                    "- Career advice (e.g. 'how to choose a career')\n"
                    "- Career details (e.g. 'tell me about doctor')\n"
                    "- Colleges (e.g. 'colleges for engineering')\n"
                    "- Entrance exams (e.g. 'tell me about JEE')\n"
                    "- Salary info (e.g. 'salary of CA')")

        # --- 9. Greetings ---
        if "thank" in words or "thanks" in words:
            return "You're welcome! Happy to help!"
        if "hi" in words or "hello" in words or "hey" in words:
            return "Hello! Ask me anything about careers, colleges, or exams!"

        # --- 10. Fallback ---
        return ("I'm not sure about that.\n"
                "Try asking about a specific career, college, or entrance exam.\n"
                "Type 'help' for examples!")

    # ---------- Formatting helpers for chatbot responses ----------

    def format_career(self, career):
        """Format a career dictionary into a readable string."""
        text = "Career: " + career["name"] + "\n"
        text = text + "Description: " + career["description"] + "\n"
        text = text + "Education: " + career["education"] + "\n"
        text = text + "Salary Range: " + career["salary"]
        return text

    def format_college(self, college):
        """Format a college dictionary into a readable string."""
        text = "College: " + college["name"] + "\n"
        text = text + "Location: " + college["location"] + "\n"
        text = text + "Type: " + college["type"] + " | Stream: " + college["stream"] + "\n"
        text = text + "Courses: " + ", ".join(college["courses"]) + "\n"
        text = text + "Fees: " + college["fees"] + " (" + college["total_fees"] + ")\n"
        text = text + "Selection: " + college["selection"] + "\n"
        p = college["placements"]
        text = text + "Avg Package: " + p["avg_package"]
        text = text + " | Highest: " + p["highest_package"]
        text = text + " | Rate: " + p["placement_rate"]
        return text

    def format_exam(self, exam):
        """Format an entrance exam dictionary into a readable string."""
        text = exam["full_name"] + " (" + exam["name"] + ")\n"
        text = text + "Stream: " + exam["stream"] + "\n"
        text = text + "Eligibility: " + exam["eligibility"] + "\n"
        text = text + "Pattern: " + exam["pattern"] + "\n"
        text = text + "Exam Month: " + exam["exam_month"] + "\n"
        text = text + "Subjects: " + exam["subjects"] + "\n"
        text = text + "Colleges: " + ", ".join(exam["colleges_accepting"])
        return text

    def format_college_list(self, results, title):
        """Format a list of colleges into a readable string."""
        if len(results) == 0:
            return "No colleges found for that search."
        text = title + ":\n"
        for i in range(len(results)):
            c = results[i]
            text = text + str(i + 1) + ". " + c["name"]
            text = text + " (" + c["location"] + ")\n"
        return text

    def format_exam_list(self, results, title):
        """Format a list of exams into a readable string."""
        if len(results) == 0:
            return "No exams found for that search."
        text = title + ":\n"
        for i in range(len(results)):
            e = results[i]
            text = text + str(i + 1) + ". " + e["name"]
            text = text + " - " + e["full_name"] + "\n"
        return text

    # ==================== PAGE 7: COLLEGE EXPLORER ====================

    def show_college_page(self):
        """College and Entrance Exam Explorer page."""
        self.clear_page()

        Label(self.page, text="College & Exam Explorer",
              font=FONT_HEADING, bg=BG_MAIN, fg=TEXT_DARK).pack(pady=(10, 5))

        # --- Search Bar ---
        search_frame = Frame(self.page, bg=BG_MAIN)
        search_frame.pack(fill=X, padx=10, pady=5)

        Label(search_frame, text="Search:", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(side=LEFT, padx=(0, 5))

        self.college_search = Entry(search_frame, font=FONT_BODY, width=25,
                                    relief="solid", bd=1)
        self.college_search.pack(side=LEFT, padx=(0, 5), ipady=3)
        self.college_search.bind("<Return>", lambda e: self.do_college_search())

        Button(search_frame, text="Search", font=FONT_SMALL,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=10,
               cursor="hand2", command=self.do_college_search).pack(side=LEFT, padx=3)

        # --- Filter by Stream ---
        Label(search_frame, text="  Filter:", font=FONT_BODY,
              bg=BG_MAIN, fg=TEXT_DARK).pack(side=LEFT, padx=(10, 5))

        self.stream_filter = StringVar(value="All")
        stream_options = ["All", "Engineering", "Medical", "Management",
                          "Commerce", "Arts", "Law", "Design", "Pharmacy",
                          "Architecture", "Media"]
        OptionMenu(search_frame, self.stream_filter, *stream_options).pack(side=LEFT)

        Button(search_frame, text="Filter", font=FONT_SMALL,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=10,
               cursor="hand2", command=self.do_stream_filter).pack(side=LEFT, padx=3)

        # --- Toggle: Colleges / Exams ---
        toggle_frame = Frame(self.page, bg=BG_MAIN)
        toggle_frame.pack(pady=5)

        Button(toggle_frame, text="  Show All Colleges  ", font=FONT_SMALL,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=8, pady=3,
               cursor="hand2", command=self.show_all_colleges).pack(side=LEFT, padx=5)

        Button(toggle_frame, text="  Show All Exams  ", font=FONT_SMALL,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=8, pady=3,
               cursor="hand2", command=self.show_all_exams).pack(side=LEFT, padx=5)

        # --- Back Button (pack at BOTTOM first so it's always visible) ---
        Button(self.page, text="<< Back to Menu", font=FONT_BTN,
               bg=BTN_BG, fg=WHITE, relief="flat", padx=15, pady=6,
               cursor="hand2", command=self.show_dashboard).pack(side=BOTTOM, pady=5)

        # --- Results Display Area (fills remaining space) ---
        result_frame = Frame(self.page, bg=BG_MAIN)
        result_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.college_display = Text(result_frame, font=FONT_BODY, bg=CARD_BG,
                                    fg=TEXT_DARK, wrap=WORD, state=DISABLED,
                                    relief="solid", bd=1, padx=10, pady=10)
        col_scroll = Scrollbar(result_frame, command=self.college_display.yview)
        self.college_display.configure(yscrollcommand=col_scroll.set)

        col_scroll.pack(side=RIGHT, fill=Y)
        self.college_display.pack(side=LEFT, fill=BOTH, expand=True)

        # Show all colleges by default
        self.show_all_colleges()

    def update_college_display(self, text):
        """Update the college explorer text area."""
        self.college_display.config(state=NORMAL)
        self.college_display.delete("1.0", END)
        self.college_display.insert(END, text)
        self.college_display.config(state=DISABLED)
        self.college_display.see("1.0")

    def show_all_colleges(self):
        """Show all colleges in the display area."""
        text = "ALL COLLEGES (" + str(len(colleges)) + " total)\n"
        text = text + "=" * 50 + "\n\n"
        for i in range(len(colleges)):
            c = colleges[i]
            text = text + str(i + 1) + ". " + c["name"] + "\n"
            text = text + "   Location: " + c["location"] + "\n"
            text = text + "   Stream: " + c["stream"]
            text = text + "  |  Fees: " + c["fees"] + "\n"
            p = c["placements"]
            text = text + "   Avg Package: " + p["avg_package"]
            text = text + "  |  Placement Rate: " + p["placement_rate"] + "\n\n"
        self.update_college_display(text)

    def show_all_exams(self):
        """Show all entrance exams in the display area."""
        text = "ALL ENTRANCE EXAMS (" + str(len(entrance_exams)) + " total)\n"
        text = text + "=" * 50 + "\n\n"
        for i in range(len(entrance_exams)):
            e = entrance_exams[i]
            text = text + str(i + 1) + ". " + e["name"] + " - " + e["full_name"] + "\n"
            text = text + "   Stream: " + e["stream"]
            text = text + "  |  Month: " + e["exam_month"] + "\n"
            text = text + "   Eligibility: " + e["eligibility"] + "\n"
            text = text + "   Pattern: " + e["pattern"] + "\n\n"
        self.update_college_display(text)

    def do_college_search(self):
        """Search colleges/exams by name."""
        query = self.college_search.get().strip().lower()
        if query == "":
            return

        # Search colleges
        col_results = search_colleges_by_name(query)
        # Search exams
        exam_results = search_exam_by_name(query)

        text = "Search Results for: '" + query + "'\n"
        text = text + "=" * 50 + "\n\n"

        if len(col_results) > 0:
            text = text + "COLLEGES FOUND:\n\n"
            for c in col_results:
                text = text + self.format_college(c) + "\n\n"

        if len(exam_results) > 0:
            text = text + "EXAMS FOUND:\n\n"
            for e in exam_results:
                text = text + self.format_exam(e) + "\n\n"

        if len(col_results) == 0 and len(exam_results) == 0:
            text = text + "No results found. Try a different search term."

        self.update_college_display(text)

    def do_stream_filter(self):
        """Filter colleges by stream."""
        stream = self.stream_filter.get()
        if stream == "All":
            self.show_all_colleges()
            return

        results = search_colleges_by_stream(stream.lower())
        text = "Colleges for " + stream + " (" + str(len(results)) + " found)\n"
        text = text + "=" * 50 + "\n\n"

        if len(results) == 0:
            text = text + "No colleges found for " + stream + "."
        else:
            for i in range(len(results)):
                c = results[i]
                text = text + str(i + 1) + ". " + c["name"] + "\n"
                text = text + "   Location: " + c["location"] + "\n"
                text = text + "   Fees: " + c["fees"] + "\n"
                p = c["placements"]
                text = text + "   Avg Package: " + p["avg_package"]
                text = text + "  |  Rate: " + p["placement_rate"] + "\n\n"

        self.update_college_display(text)

    # ==================== RUN ====================

    def run(self):
        """Start the application main loop."""
        self.root.mainloop()


# ==================== START THE APPLICATION ====================

if __name__ == "__main__":
    app = CareerPathApp()
    app.run()
