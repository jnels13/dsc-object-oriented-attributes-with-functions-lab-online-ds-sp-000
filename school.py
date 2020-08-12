class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, full_name, grade_level):
        self.full_name = full_name
        self.grade_level = grade_level
        if grade_level in self.roster:
            self.roster[grade_level].append(full_name)
        else:
            self.roster[grade_level] = [full_name]

    def grade(self, grade):
        self.grade = grade
        print(self.roster[grade])

    def sort_roster(self):
        for i in self.roster:
            self.roster[i].sort()
        return self.roster


