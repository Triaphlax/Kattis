import sys
import queue


class Person:
    def __init__(self, PositionX, PositionY, PossiblePartners):
        self.PositionX = PositionX
        self.PositionY = PositionY
        self.PossiblePartners = PossiblePartners

    def OneFewer(self):
        self.PossiblePartners -= 1


class Edge:
    def __init__(self, Distance, Student, Tutor):
        self.Distance = Distance
        self.Student = Student
        self.Tutor = Tutor

    def __lt__(self, _):
        return True


nofStudentsTutors = int(sys.stdin.readline())

students = {}
for student in range(nofStudentsTutors):
    position = list(map(int, sys.stdin.readline().split(' ')))
    studentObject = Person(position[0], position[1], nofStudentsTutors)
    students[student] = studentObject

tutors = {}
for tutor in range(nofStudentsTutors):
    position = tuple(map(int, sys.stdin.readline().split(' ')))
    tutorObject = Person(position[0], position[1], nofStudentsTutors)
    tutors[tutor] = tutorObject

edges = queue.PriorityQueue()
for student in students:
    studentObject = students[student]
    for tutor in tutors:
        tutorObject = tutors[tutor]
        distance = abs(studentObject.PositionX - tutorObject.PositionX) + \
            abs(studentObject.PositionY - tutorObject.PositionY)
        edgeObject = Edge(distance, student, tutor)
        edges.put((-distance, edgeObject))

highestEdge = 0
while not edges.empty():
    edge = edges.get()[1]
    if students[edge.Student].PossiblePartners == 1 or + \
            tutors[edge.Tutor].PossiblePartners == 1:
        if edge.Distance > highestEdge:
            highestEdge = edge.Distance
    students[edge.Student].OneFewer()
    tutors[edge.Tutor].OneFewer()

print(highestEdge)
