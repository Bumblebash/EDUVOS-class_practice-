
"""
NAME : SSIMBWA BASHIR 
STUDENT NUMBER: EDUV10064199
MODULE: PROGRAM DESIGN

"""
"""
Programmer:   SSIMBWA BASHIR
STUDENT NUMBER: EDUV10064199
Date:         2026-06-10
Program:      Learner Progress Tracking System (LPTS)
Purpose:      A console-based application for a community learning centre
              to manage learners, record marks, calculate averages,
              determine performance (Fail/Pass/Distinction), and display
              progress summaries. Uses tkinter.messagebox for GUI feedback.
"""

import tkinter as tk
from tkinter import messagebox

# --------------------------- BASE CLASS (INHERITANCE) ---------------------------
class Person:
    """Base class representing a generic person with name and age."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# --------------------------- DERIVED CLASS (LEARNER) ---------------------------
class Learner(Person):
    """Derived class representing a learner, inherits from Person.
       Adds learner_id, course, marks list, and encapsulates average mark.
    """
    def __init__(self, learner_id: int, name: str, age: int, course: str):
        # Call base class constructor
        super().__init__(name, age)
        self.learner_id = learner_id
        self.course = course
        self.marks = []          # list to store assessment marks (float/int)
        self.__average = 0.0     # ENCAPSULATED (protected) attribute

    # ---------------------- ENCAPSULATION METHODS ----------------------
    def get_average(self):
        """Accessor method for the protected average mark."""
        return self.__average

    def _calculate_average(self):
        """Private method to compute average from marks list.
           Updates the encapsulated __average attribute.
        """
        if not self.marks:
            self.__average = 0.0
        else:
            self.__average = sum(self.marks) / len(self.marks)
        return self.__average

    # ---------------------- HELPER METHODS ----------------------
    def add_mark(self, mark: float):
        """Adds a single mark to the learner's marks list."""
        if 0 <= mark <= 100:
            self.marks.append(mark)
            self._calculate_average()   # update encapsulated average
            return True
        return False

    def add_marks_list(self, marks_list):
        """Adds multiple marks at once and updates average."""
        for m in marks_list:
            if 0 <= m <= 100:
                self.marks.append(m)
        self._calculate_average()

    def get_performance_category(self):
        """Determines Fail/Pass/Distinction based on average."""
        avg = self.get_average()
        if avg < 50:
            return "Fail"
        elif avg <= 74:
            return "Pass"
        else:
            return "Pass with Distinction"

    def qualifies_for_certificate(self):
        """Predicate function: returns True if learner has Pass or Distinction."""
        return self.get_performance_category() != "Fail"

    def display_summary(self):
        """Returns a formatted string with all learner details."""
        perf = self.get_performance_category()
        cert = "Yes" if self.qualifies_for_certificate() else "No"
        summary = (f"Learner ID: {self.learner_id}\n"
                   f"Name: {self.name}\n"
                   f"Age: {self.age}\n"
                   f"Course: {self.course}\n"
                   f"Marks: {self.marks}\n"
                   f"Average: {self.get_average():.2f}\n"
                   f"Result: {perf}\n"
                   f"Certificate: {cert}")
        return summary


# --------------------------- RECURSIVE FUNCTION ---------------------------
def recursive_sum_marks(marks_list, index=0):
    """
    Recursively calculates the sum of marks in a list.
    Base case: when index reaches list length, return 0.
    Recursive case: marks_list[index] + sum of the rest.
    """
    if index == len(marks_list):
        return 0
    return marks_list[index] + recursive_sum_marks(marks_list, index + 1)


# --------------------------- PREDICATE FUNCTION (example) ---------------------------
def is_valid_age(age):
    """Predicate function: returns True if age is between 1 and 120."""
    return 1 <= age <= 120


# --------------------------- FUNCTION WITH DEFAULT ARGUMENT ---------------------------
def get_certificate_status(learner, custom_message="Certificate eligibility: "):
    """Function with a default argument (custom_message)."""
    status = "Yes" if learner.qualifies_for_certificate() else "No"
    return custom_message + status


# --------------------------- MAIN SYSTEM CLASS ---------------------------
class LearnerProgressSystem:
    def __init__(self):
        self.learners = []      # list to store all Learner objects
        self.next_id = 1

    # ---------------------- LEARNER MANAGEMENT ----------------------
    def add_learner(self, name, age, course):
        """Adds a new learner after validating age."""
        try:
            age = int(age)
            if not is_valid_age(age):   # using predicate function
                messagebox.showerror("Invalid Age", "Age must be between 1 and 120.")
                return False
            learner = Learner(self.next_id, name, age, course)
            self.learners.append(learner)
            self.next_id += 1
            messagebox.showinfo("Success", f"Learner '{name}' added successfully (ID: {learner.learner_id})")
            return True
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return False

    def find_learner_by_id(self, learner_id):
        """Searches the learners list by ID."""
        for l in self.learners:
            if l.learner_id == learner_id:
                return l
        return None

    def view_all_learners(self):
        """Traverses the learners list and prints summaries to console."""
        if not self.learners:
            print("\nNo learners registered yet.\n")
            return
        print("\n" + "=" * 50)
        print("ALL LEARNERS SUMMARY")
        print("=" * 50)
        for learner in self.learners:
            print(learner.display_summary())
            print("-" * 40)

    def update_learner(self, learner_id, new_name, new_age, new_course):
        """Updates learner details after validation."""
        learner = self.find_learner_by_id(learner_id)
        if not learner:
            messagebox.showerror("Error", f"No learner with ID {learner_id} found.")
            return False
        try:
            new_age = int(new_age)
            if not is_valid_age(new_age):
                messagebox.showerror("Invalid Age", "Age must be between 1 and 120.")
                return False
            learner.name = new_name
            learner.age = new_age
            learner.course = new_course
            messagebox.showinfo("Success", "Learner details updated successfully.")
            return True
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return False

    def remove_learner(self, learner_id):
        """Removes a learner from the list."""
        learner = self.find_learner_by_id(learner_id)
        if learner:
            self.learners.remove(learner)
            messagebox.showinfo("Removed", f"Learner ID {learner_id} deleted successfully.")
            return True
        else:
            messagebox.showerror("Error", f"Learner ID {learner_id} not found.")
            return False

    # ---------------------- ASSESSMENT AND MARKS ----------------------
    def capture_marks_for_learner(self, learner_id):
        """Allows staff to input multiple marks for a learner."""
        learner = self.find_learner_by_id(learner_id)
        if not learner:
            messagebox.showerror("Error", "Learner not found.")
            return

        print(f"\nEntering marks for {learner.name} (ID: {learner.learner_id})")
        print("Enter mark (0-100). Type 'done' to finish or 'stop' to cancel.")

        marks_temp = []
        while True:
            user_input = input("Mark: ")
            if user_input.lower() in ('done', 'stop'):
                break
            try:
                mark = float(user_input)
                if 0 <= mark <= 100:
                    marks_temp.append(mark)
                else:
                    messagebox.showwarning("Invalid Mark", "Mark must be between 0 and 100. Skipped.")
                    continue       # use of 'continue'
            except ValueError:
                messagebox.showerror("Error", "Please enter a numeric mark or 'done'.")
                continue

        if marks_temp:
            # Use a for loop to process and add each mark
            for m in marks_temp:
                learner.add_mark(m)
            messagebox.showinfo("Marks Saved", f"{len(marks_temp)} mark(s) added for {learner.name}.")
        else:
            messagebox.showinfo("No Marks", "No valid marks were entered.")

    def display_learner_marks(self, learner_id):
        """Shows all marks for a given learner."""
        learner = self.find_learner_by_id(learner_id)
        if not learner:
            messagebox.showerror("Error", "Learner not found.")
            return
        if not learner.marks:
            print(f"\n{learner.name} has no marks recorded yet.")
        else:
            print(f"\nMarks for {learner.name}: {learner.marks}")

    def show_learner_result(self, learner_id):
        """Displays average, performance, and certificate status using messagebox."""
        learner = self.find_learner_by_id(learner_id)
        if not learner:
            messagebox.showerror("Error", "Learner not found.")
            return

        # Use function with keyword argument
        cert_msg = get_certificate_status(learner, custom_message="Certificate: ")
        info = (f"Learner: {learner.name}\n"
                f"Average: {learner.get_average():.2f}\n"
                f"Performance: {learner.get_performance_category()}\n"
                f"{cert_msg}")
        messagebox.showinfo("Learner Result", info)

        # Also print to console for record
        print("\n" + learner.display_summary())

    # ---------------------- RECURSION DEMO ----------------------
    def demonstrate_recursion(self, learner_id):
        """Uses recursive_sum_marks to compute sum of marks for a learner."""
        learner = self.find_learner_by_id(learner_id)
        if not learner:
            messagebox.showerror("Error", "Learner not found.")
            return
        total = recursive_sum_marks(learner.marks)
        messagebox.showinfo("Recursive Sum", f"Sum of marks for {learner.name}: {total}")


# --------------------------- MENU AND MAIN PROGRAM ---------------------------
def main():
    # Hide root tkinter window
    root = tk.Tk()
    root.withdraw()

    system = LearnerProgressSystem()

    # Pre-populate with demo data (optional but helpful for testing)
    demo = Learner(1, "Lucy Manyange", 18, "Intro to Python")
    demo.add_marks_list([50, 76, 65])
    system.learners.append(demo)
    system.next_id = 2

    while True:   # condition-controlled loop for the main menu
        print("\n" + "=" * 50)
        print("     LEARNER PROGRESS TRACKING SYSTEM")
        print("=" * 50)
        print("1. Add new learner")
        print("2. Enter marks for a learner")
        print("3. View all learners")
        print("4. Search learner by ID")
        print("5. Update learner details")
        print("6. Remove learner")
        print("7. Show learner result (average & performance)")
        print("8. Demonstrate recursion (sum of marks)")
        print("9. Exit")
        print("-" * 50)

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add learner
            name = input("Enter name: ")
            age = input("Enter age: ")
            course = input("Enter course: ")
            system.add_learner(name, age, course)

        elif choice == '2':
            # Enter marks
            try:
                lid = int(input("Enter learner ID: "))
                system.capture_marks_for_learner(lid)
            except ValueError:
                messagebox.showerror("Error", "Invalid ID. Please enter a number.")
                continue

        elif choice == '3':
            # View all learners
            system.view_all_learners()

        elif choice == '4':
            # Search learner
            try:
                lid = int(input("Enter learner ID to search: "))
                learner = system.find_learner_by_id(lid)
                if learner:
                    print("\n" + learner.display_summary())
                else:
                    messagebox.showinfo("Not Found", f"No learner with ID {lid}.")
            except ValueError:
                messagebox.showerror("Error", "Invalid ID.")

        elif choice == '5':
            # Update learner
            try:
                lid = int(input("Enter learner ID to update: "))
                new_name = input("Enter new name: ")
                new_age = input("Enter new age: ")
                new_course = input("Enter new course: ")
                system.update_learner(lid, new_name, new_age, new_course)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for ID.")

        elif choice == '6':
            # Remove learner
            try:
                lid = int(input("Enter learner ID to remove: "))
                system.remove_learner(lid)
            except ValueError:
                messagebox.showerror("Error", "Invalid ID.")

        elif choice == '7':
            # Show result
            try:
                lid = int(input("Enter learner ID: "))
                system.show_learner_result(lid)
            except ValueError:
                messagebox.showerror("Error", "Invalid ID.")

        elif choice == '8':
            # Recursion demo
            try:
                lid = int(input("Enter learner ID to compute sum of marks recursively: "))
                system.demonstrate_recursion(lid)
            except ValueError:
                messagebox.showerror("Error", "Invalid ID.")

        elif choice == '9':
            # Exit confirmation with messagebox
            confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
            if confirm:
                messagebox.showinfo("Goodbye", "Thank you for using LPTS.")
                break
            else:
                continue

        else:
            messagebox.showerror("Invalid Option", "Please enter a number between 1 and 9.")
            continue

        # Use of 'break' is not needed here; loop naturally continues until exit.
        # However, to satisfy the requirement of 'break' - we can break on error but we already handle.
        # We'll demonstrate 'break' inside input validation if needed. The exit option already breaks.

    # Close the root window
    root.destroy()


if __name__ == "__main__":
    main()





    # REFERENCES #
  #https://www.geeksforgeeks.org/python/python-functions/
  #https://www.py4e.com/lessons#
  # https://realpython.com/#