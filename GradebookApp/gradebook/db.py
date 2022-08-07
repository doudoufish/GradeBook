import csv
from pathlib import Path
from school import Student
import os,sys
from typing import List


class StudentRepository:
	def __init__(self):
		self.__FILENAME = "grades.csv"
	
	
	def getNumberOfWork(self):
		self.__numberOfWork = [0,0,0]
		return self.__numberOfWork
	def getPolicy(self):
		self.__policy = [0,0,0]
		return self.__policy
		
   

	def getStudent(self):
		students:List[Student] = []
		with open(Path(__file__).with_name(self.__FILENAME), newline = "") as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0] == "student":
					student = Student(row[1],row[2])
					students.append(student)
		return students
	def getAssiScores(self):
		assiScores = {}
		with open(Path(__file__).with_name(self.__FILENAME), newline = "") as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0] == "assiScores":
					assiScores[row[1]] = row[2]
		return assiScores
	def getTestScores(self):
		testScores = {}
		with open(Path(__file__).with_name(self.__FILENAME), newline = "") as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0] == "testScores":
					testScores[row[1]] = row[2]
		return testScores

	def getExamScores(self):
		examScores = {}
		with open(Path(__file__).with_name(self.__FILENAME), newline = "") as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0] == "examScores":
					examScores[row[1]] = row[2]
		return examScores

	def getFinalScores(self):
		finalScores = {}
		with open(Path(__file__).with_name(self.__FILENAME), newline = "") as file:
			reader = csv.reader(file)
			for row in reader:
				if row[0] == "finalScores":
					finalScores[row[1]] = row[2]
		return finalScores
