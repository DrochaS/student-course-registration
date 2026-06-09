# Project Reflection: Student Course Registration System

## 1. What was the hardest part of this project?
The hardest part was managing data persistence using flat text files (`.txt`) instead of a structured format like JSON. Because raw text is just a flat string, I had to build a custom parsing system using split delimiters (`|`). Handling hidden trailing newlines (`\n`), stripping accidental whitespace, and converting string digits into integers for course capacities required extreme precision. A single misplaced character in a data file would crash the entire data-loading logic.

## 2. Which classes did you create and why?
I created four classes to implement proper Object-Oriented Programming principles:
* **`Person` (Base Class):** Bundles common traits (`name`, `email`, `phone_number`) so code isn't duplicated.
* **`Student` (Child Class):** Inherits from `Person`, adds a unique `student_id`, and overrides `__str__` for neat terminal printing.
* **`Course` (Model Class):** Encapsulates course details like IDs, instructors, and maximum caps.
* **`SchoolSystem` (Service Class):** Acts as the core engine. It manages runtime lists, runs validation checks, and handles file reading/writing.

## 3. How does your registration logic prevent duplicate registrations?
The system captures the enrollment request as a direct list pair: `[student_id, course_id]`. Before appending anything to our records, an `if` conditional runs a membership check against the main registrations list. If that exact ID combination already exists in memory, the system blocks the operation and alerts the admin with an error message instead of saving a double entry.

## 4. How does your system check if a course is full?
Every time an enrollment request is made, a helper function loops through the active registrations list and counts how many times the target `course_id` appears. The system then pulls the maximum capacity from that specific `Course` object and runs a direct math comparison. If the current registration count is equal to or greater than the course capacity, the process is blocked and a "class is full" error is shown.

## 5. What bugs did you face and how did you fix them?
* **The Empty Line Crash (`ValueError`):** * *Bug:* A blank trailing line at the bottom of a text file caused `.split('|')` to fail because it couldn't find enough columns, crashing the app on startup.
  * *Fix:* Applied `.strip()` to remove whitespace and wrapped the parsing logic in an `if line:` check to skip empty rows.
* **The Data Duplication Bug:** * *Bug:* If the admin manually chose "Load Data" multiple times in a single session, the system repeatedly appended the file contents, doubling or tripling runtime memory entries.
  * *Fix:* Updated `load_data()` to explicitly clear the list arrays (`self.students.clear()`, etc.) before running the file-reading loops.

## 6. Which part of the code would you improve if you had more time?
I would refactor how registrations are represented. Right now, they are just a loose array of raw ID strings (`[student_id, course_id]`). While this works for simple text storage, it is less cohesive than our other structures. I would create a dedicated `Registration` class where each instance holds direct references to actual `Student` and `Course` objects, making the design fully object-oriented.