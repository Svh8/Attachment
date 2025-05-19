class Attachee:
    def __init__(self, name, division):
        
        self.name = name
        self.division = division
        self.task = None
        self.feedback = None
        self.score = None

    def assign_task(self, task):
        self.task = task
        print(f"Task '{task}' assigned to {self.name} in {self.division} division.")

    def give_feedback(self, feedback):
        self.feedback = feedback
        print(f"Feedback for {self.name}: {feedback}")

    def assign_score(self, score):
        if 0 <= score <= 100:
            self.score = score
            print(f"{self.name} scored {score}/100.")
        else:
            print("Score must be between 0 and 100.")

    def display_performance(self):
        print(f"{self.name} | Division: {self.division} | Task: {self.task} | Score: {self.score} | Feedback: {self.feedback}")

class DivisionManager:
    def __init__(self):
        self.divisions = {
            "Engineering": [],
            "Tech Programs": [],
            "Radio Support": [],
            "Hub Support": []
        }

    def add_attachee(self, attachee):
        if attachee.division in self.divisions:
            self.divisions[attachee.division].append(attachee)
        else:
            print(f"Invalid division for {attachee.name}")

    def assign_task_to_division(self, division, task):
        if division in self.divisions:
            for attachee in self.divisions[division]:
                attachee.assign_task(task)
        else:
            print("Division not found.")

    def give_feedback_to_attachee(self, name, feedback):
        for division_list in self.divisions.values():
            for attachee in division_list:
                if attachee.name == name:
                    attachee.give_feedback(feedback)
                    return
        print("Attachee not found.")

    def score_attachee(self, name, score):
        for division_list in self.divisions.values():
            for attachee in division_list:
                if attachee.name == name:
                    attachee.assign_score(score)
                    return
        print("Attachee not found.")

    def display_all_attachees(self):
        print("\n--- Attachees by Division ---")
        for division, attachees in self.divisions.items():
            print(f"\n{division}:")
            for attachee in attachees:
                attachee.display_performance()

manager = DivisionManager()
a1 = Attachee("Izzo", "Engineering")
a2 = Attachee("Steve", "Tech Programs")
a3 = Attachee("james", "Radio Support")
a4 = Attachee("Marvin", "Hub Support")
a5 = Attachee("zablon", "Engineering")
for attachee in [a1, a2, a3, a4, a5]:
    manager.add_attachee(attachee)
manager.assign_task_to_division("Engineering", "Build API")
manager.assign_task_to_division("Tech Programs", "Organize workshop")
manager.assign_task_to_division("Radio Support", "Setup broadcast")
manager.assign_task_to_division("Hub Support", "Manage events")

manager.give_feedback_to_attachee("Izzo", "Excellent coding skills")
manager.score_attachee("Izzo", 92)

manager.give_feedback_to_attachee("Steve", "Very organized")
manager.score_attachee("steve", 85)

manager.display_all_attachees()