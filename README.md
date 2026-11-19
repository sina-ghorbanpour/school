# School Management System

## Introduction

well this project is a very simple school management system developed by "slimefun" maded completely 100% with Python. Its purpose is to manage different parts of a school for example students,teachers,courses and even classrooms.

The program uses an object-oriented approach, with separate classes for each main component of the school. This makes the code more organized and easier to maintain and even other programmers can read this code easily or maybe you dont know python that much.

## Features

- Student management: Adding,editing,deleting and viewing students details.
- Teacher Management:Adding,editing, deleting and viewing teachers details.
- Course Management:Creating courses,editing,deleting and viewing courses details.
- Classroom Management: A planned feature for organizing classrooms, teachers and students.(more fetures in future) :3
- Data Storage: Savhng and loading some information using JSON files.
- Course Selection: Assign courses to individual students. (not completed yet) :(

## Technologies

- Python
- Object-Oriented Programming (OOP)
- JSON
- UML (made with "Word")

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Make sure "data.json" is in the project directory.
4. Run the Python file.

if you download the whole folder nothing bad happends :3

## Future Improvements

- Complete classroom management.
- Implement teacher course management.
- Add student grading and scoring.
- Improve data validation and error handling.
## Structure

| Courses| Properties |
|---|---|
| `id` | A unique identifier used to find and identify a course. |
| `name` | The name of the course. |
| `units` | The number of units assigned to the course. |
| `score` | Stores the student's score for the course. |

| Courses | Methods |
|---|---|
| `__init__()` | Initializes a course with an ID, name, and number of units. |
| `__eq__()` | Compares two courses using their IDs. |



| Student | Properties |
|---|---|
| `id` | A unique identifier for the student. |
| `name` | The student's first name. |
| `family` | The student's family name. |
| `courses` | A list of courses assigned to the student. |

| Student | Methods |
|---|---|
| `__init__()` | Initializes a student. |
| `__eq__()` | Compares two students using their IDs. |



| Teacher | Properties |
|---|---|
| `id` | A unique identifier for the teacher. |
| `name` | The teacher's first name. |
| `family` | The teacher's family name. |
| `grade` | The teacher's grade or qualification. |
| `courses` | A list of courses assigned to the teacher. |

| Teacher | Method |
|---|---|
| `__init__()` | Initializes a teacher. |
| `__eq__()` | Compares two teachers using their IDs. |

| Classroom | Properties |
|---|---|
| `id` | A unique identifier for the classroom. |
| `name` | The classroom's name. |
| `course` | The course taught in the classroom. |
| `teacher` | The teacher assigned to the classroom. |
| `students` | A list of students in the classroom. |

| Classroom | Methods |
|---|---|
| `__init__()` | Initializes a classroom with an ID and name. |
| `__eq__()` | Compares two classrooms using their IDs. |


| School | Properties |
|---|---|
| `name` | The name of the school. |
| `courses` | Stores all courses available in the school. |
| `teachers` | Stores all teachers registered in the school. |
| `students` | Stores all students registered in the school. |
| `selected_student` | Stores the currently selected student. |
| `selected_teacher` | Stores the currently selected teacher. |

| School | Methods |
|---|---|
| `__init__()` | Initializes the school. |
| `add_student()` | Adds a new student if their ID doesn't already exist. |
| `delete_student()` | Removes a student using their ID. |
| `add_teacher()` | Adds a new teacher if their ID doesn't already exist. |
| `delete_teacher()` | Removes a teacher using their ID. |
| `load_data()` | Loads courses, students, and teachers from a JSON file. |
| `save_data()` | Saves courses, students, and teachers into a JSON file. |