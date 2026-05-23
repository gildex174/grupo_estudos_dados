class Student:
    def __init__(self, name, course):
        self.name = name 
        self.course = course
        
    def __str__(self):
        return f"{self.name} faz {self.course}"

    @property    
    def course(self):
        return self._course
    
    @course.setter
    def course(self, course):
        if course not in ["fisica", "fiscomp", "biomol", "lic"]:
            raise ValueError("Curso inválido!")
        self._course = course

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Faltou o nome!!")
        self._name = name

    @classmethod
    def get(cls):
        name = input("Name: ")
        course = input("Course: ")

        return cls(name, course)

# def get_student():

#     name = input("Name: ")
#     course = input("Course: ")

#     student = Student(name, course)

#     return student

def main():
    student = Student.get()

    # student.course = "Letras"

    print(student)

if __name__ == "__main__":
    main()
