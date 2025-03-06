class ClassRoom:
  def __init__(self,name):
    self.students = []
    self.subjects = []
    self.name = name
  def add_student(self,student):
    roll_no = f"{self.name}-{len(self.students)+1}"
    student.id = roll_no
    self.students.append(student)
  def add_subject(self, subject):
    self.subjects.append(subject)
  def take_semester_final_exam(self):
    for subject in self.subjects:
      subject.exam(self.students)
    for student in self.students:
      student.calculate_final_grade()