# # class Graph:
# #     def __init__(self):
# #         self.graph = {}

# #     # Add Vertex
# #     def addVertex(self, vertex):
# #         if vertex not in self.graph:
# #             self.graph[vertex] = []
# #             print(vertex, "added successfully")
# #         else:
# #             print(vertex, "already exists")

# #     # Add Edge
# #     def addEdge(self, vertex1, vertex2):
# #         if vertex1 in self.graph and vertex2 in self.graph:
# #             self.graph[vertex1].append(vertex2)
# #             self.graph[vertex2].append(vertex1)
# #             print("Edge added between", vertex1, "and", vertex2)
# #         else:
# #             print("One or both vertices not found")

# #     # Remove Edge
# #     def removeEdge(self, vertex1, vertex2):
# #         if vertex1 in self.graph and vertex2 in self.graph:

# #             if vertex2 in self.graph[vertex1]:
# #                 self.graph[vertex1].remove(vertex2)

# #             if vertex1 in self.graph[vertex2]:
# #                 self.graph[vertex2].remove(vertex1)

# #             print("Edge removed between", vertex1, "and", vertex2)
# #         else:
# #             print("One or both vertices not found")

# #     # Remove Vertex
# #     def removeVertex(self, vertex):
# #         if vertex in self.graph:

# #             # Remove connections from other vertices
# #             for otherVertex in self.graph[vertex]:
# #                 self.graph[otherVertex].remove(vertex)

# #             # Delete the vertex
# #             del self.graph[vertex]

# #             print(vertex, "removed successfully")
# #         else:
# #             print(vertex, "not found")

# #     # Display Graph
# #     def displayGraph(self):
# #         print("\nGraph:")
# #         for vertex in self.graph:
# #             print(vertex, "->", self.graph[vertex])


# # # ---------------- TESTING ----------------

# # customGraph = Graph()

# # # Add Vertices
# # customGraph.addVertex("A")
# # customGraph.addVertex("B")
# # customGraph.addVertex("C")
# # customGraph.addVertex("D")

# # # Add Edges
# # customGraph.addEdge("A", "B")
# # customGraph.addEdge("A", "C")
# # customGraph.addEdge("B", "D")

# # # Display Graph
# # customGraph.displayGraph()

# # # Remove Edge
# # customGraph.removeEdge("A", "B")

# # # Display Graph Again
# # customGraph.displayGraph()

# # # Remove Vertex
# # customGraph.removeVertex("C")

# # # Display Final Graph
# # customGraph.displayGraph()

# class Student:

#     # Instance Method
#     def get_personal_detail(self, firstname, lastname):
#         print("Your personal detail :", firstname, lastname)

#     # Static Method
#     @staticmethod
#     def contact_detail(mobile_no, rollno):
#         print("Your contact detail :", mobile_no, rollno)


# # Create Object
# s1 = Student()

# # Call Instance Method
# s1.get_personal_detail("Manohar", "Sharnagat")

# # Call Static Method
# Student.contact_detail(9876543210, 101)
# Multilevel Inheritance

# class college:

#     def college_name(self):
#         print("Modern College")


# class Student(college):

#     def student_info(self):
#         print("Student Name: Manohar")
#         print("Course: mca")


# class exam(Student):

#     def exam_detail(self):
#         print("Exam: Software Testing")
#         print("Marks: 85")


# # Create Object
# obj = exam()

# # Access Methods
# obj.college_name()
# obj.student_info()
# obj.exam_detail()

# class SubjMarks:

#     math = int(input("Enter your Maths paper marks: "))
#     de = int(input("Enter your Digital Electronics marks: "))
#     c = int(input("Enter your C Language marks: "))
#     english = int(input("Enter your English marks: "))


# class PractMarks:

#     cpract = int(input("Enter Practical marks of C Language: "))


# class Result(SubjMarks, PractMarks):

#     def total_marks(self):
#         total = (
#             self.math +self.de +self.c +self.english +self.cpract
#         )

#         print("\n------ RESULT ------")
#         print("Maths Marks:", self.math)
#         print("DE Marks:", self.de)
#         print("C Language Marks:", self.c)
#         print("English Marks:", self.english)
#         print("C Practical Marks:", self.cpract)

#         print("Total Marks:", total)

#         percentage = total / 5
#         print("Percentage:", percentage, "%")


# # Create Object
# r1 = Result()

# # Call Method
# r1.total_marks()


class Rbi:

    def home_loan(self):
        print("Home loan ROI = 8%")

    def education_loan(self):
        print("Education loan ROI = 9%")


class Sbi(Rbi):

    def education_loan(self):
        print("Education loan ROI = 10%")
        super().education_loan()


# Create Object
obj = Sbi()

# Call Methods
obj.home_loan()
obj.education_loan()

class RBI:
    def __init__(self):
        print("parent class constructor")
class SBI(RBI):
    def __init__(self):
            print("child class construcot")

obj = SBI()
