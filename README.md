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

### 1. Courses
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

### 2. Student

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

### 3. Teacher

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

### 4. Classroom

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

### 5. School

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

# How It Works

When you run the program, the main menu appears:

    1. Students
    2. Teachers
    3. Courses
    4. Classrooms
    5. Save
    0. Exit

Each option opens a different section of the program.

## 1. Students

Selecting `Students` opens the student management menu:

    1. Show students
    2. Add student
    3. Edit student
    4. Delete student
    5. Select student
    0. Back

- **Show students:** Displays all registered students, including their ID, first name, and family name.

- **Add student:** Asks for the student's ID, first name, and family name, then creates and adds the student to the school. If a student with the same ID already exists, it displays an error message.

- **Edit student:** Asks for the student's ID and new information (first name and family name), then updates the student's information.

- **Delete student:** Asks for the student's ID and removes the corresponding student from the school.

- **Select student:** Allows you to select a student using their ID. After selecting a student, you enter the student's individual menu.

### Selected Student Menu

After selecting a student, the following options are available:

    1. Show info
    2. Add course
    3. Delete courses
    4. Set scores
    0. Back

- **Show info:** Displays the selected student's ID, first name, family name, and registered courses.

- **Add course:** Displays all available courses and asks for a course ID. If the course exists, it is added to the selected student's course list.

- **Delete courses:** Displays the student's registered courses and asks for a course ID to remove.

- **Set scores:** Reserved for assigning scores to the student's courses (not implemented yet).

## 2. Teachers

Selecting `Teachers` opens the teacher management menu:

    1. Show teachers
    2. Add teacher
    3. Edit teacher
    4. Delete teacher
    5. Select teacher
    0. Back

- **Show teachers:** Displays all registered teachers, including their ID, first name, family name, and grade.

- **Add teacher:** Asks for the teacher's ID, first name, family name, and grade, then adds the teacher to the school.

- **Edit teacher:** Asks for the teacher's ID and new information, then updates the teacher's details.

- **Delete teacher:** Removes a teacher using their ID.

- **Select teacher:** Intended to select a teacher using their ID and open the teacher's individual menu.

### Selected Teacher Menu

After selecting a teacher, the following options are intended:

    1. Show info
    2. Add course
    3. Delete courses
    0. Back

These options are not fully implemented yet.

## 3. Courses

Selecting `Courses` opens the course management menu:

    1. Show courses
    2. Add course
    3. Edit course
    4. Delete course
    0. Back

- **Show courses:** Displays all available courses, including their ID, name, and number of units.

- **Add course:** Asks for the course's ID, name, and number of units, then adds it to the school. Duplicate IDs are not allowed.

- **Edit course:** Asks for the course's ID and new information (name and number of units), then updates the course.

- **Delete course:** Removes a course using its ID.

## 4. Classrooms

Selecting `Classrooms` opens the classroom management menu:

    1. Show classrooms
    2. Add classroom
    3. Edit classroom
    4. Delete classroom
    5. Select classroom
    0. Back

Classroom management is planned but its functions have not been implemented yet.

## 5. Save

Selecting `Save` saves the school's current data into `data.json`.

The program stores:
- All courses.
- All students.
- All teachers.

The information is converted into JSON format so it can be loaded again when the program starts.

## 0. Exit

Selecting `Exit` terminates the program.

**Note:** The program currently loads data from `data.json` when it starts. Changes should be saved using the Save option before exiting.