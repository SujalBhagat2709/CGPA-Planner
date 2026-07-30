"""
CGPA Planner Studio
-------------------
Main file for CGPA Planner.
"""

from cgpa_planner import CGPAPlanner


class CGPAPlannerStudio:

    def __init__(self):

        self.planner = CGPAPlanner()

    # ----------------------------------
    # Add Semester
    # ----------------------------------
    def add_semester(self):

        print("\n========== ADD SEMESTER ==========\n")

        semester = input(
            "Semester Name: "
        ).strip()

        credits = float(
            input(
                "Credits: "
            )
        )

        gpa = float(
            input(
                "Semester GPA: "
            )
        )

        record = self.planner.add_semester(
            semester,
            credits,
            gpa
        )

        print("\nSemester Added Successfully.")

        self.planner.display_record(record)

    # ----------------------------------
    # View Semesters
    # ----------------------------------
    def view_semesters(self):

        self.planner.display_records()

    # ----------------------------------
    # Current CGPA
    # ----------------------------------
    def current_cgpa(self):

        print("\n========== CURRENT CGPA ==========\n")

        print(
            f"Current CGPA : {self.planner.current_cgpa()}"
        )

    # ----------------------------------
    # Predict Future CGPA
    # ----------------------------------
    def predict_cgpa(self):

        future_credits = float(
            input(
                "\nFuture Credits: "
            )
        )

        expected_gpa = float(
            input(
                "Expected GPA: "
            )
        )

        result = self.planner.predict_cgpa(
            future_credits,
            expected_gpa
        )

        print(
            f"\nPredicted CGPA : {result}"
        )

    # ----------------------------------
    # Required GPA
    # ----------------------------------
    def required_gpa(self):

        target = float(
            input(
                "\nTarget CGPA: "
            )
        )

        future = float(
            input(
                "Future Credits: "
            )
        )

        result = self.planner.required_gpa(
            target,
            future
        )

        print(
            f"\nRequired GPA : {result}"
        )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.planner.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 55)
            print("               CGPA PLANNER")
            print("=" * 55)

            print("1. Add Semester")
            print("2. View Semesters")
            print("3. Current CGPA")
            print("4. Predict Future CGPA")
            print("5. Required GPA")
            print("6. Academic Summary")
            print("7. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_semester()

            elif choice == "2":

                self.view_semesters()

            elif choice == "3":

                self.current_cgpa()

            elif choice == "4":

                self.predict_cgpa()

            elif choice == "5":

                self.required_gpa()

            elif choice == "6":

                self.summary()

            elif choice == "7":

                print(
                    "\nThank you for using CGPA Planner."
                )

                break

            else:

                print("\nInvalid choice.")


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = CGPAPlannerStudio()

    studio.menu()