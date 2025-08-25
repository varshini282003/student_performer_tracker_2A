
# Student Performer Tracker

## Project Overview

Student Performer Tracker is a CLI-based Python application for managing and tracking student performance.  
It supports regular and graduate students, allows adding/removing students, recording subject scores, searching by name, listing all students, finding top scorers in subjects, and calculating department-wise averages.

## Features

- Add regular or graduate students (with thesis title)
- Remove students by ID
- Search students by name
- Add subject scores (case-insensitive)
- List all students with details
- Find top scorer in a subject
- Calculate department average scores

## Folder Structure

```
Student_performer_tracker/
│
├── main.py
├── managers/
│   └── StudentManager.py
├── models/
│   ├── student.py
│   └── Graduate.py
├── utils/
│   └── validation.py
```

## How to Run

1. **Install Python 3.7+**  
   Make sure Python is installed on your system.

2. **Navigate to the project folder in terminal:**
   ```
   cd "c:\Training\First project\Student_performer_tracker"
   ```

3. **Run the application:**
   ```
   python main.py
   ```

4. **Follow the on-screen menu to interact with the tracker.**

## Notes

- All subject names are handled case-insensitively.
- Graduate students require a thesis title.
- Student IDs are auto-generated.
- Data is stored in memory (not persistent).

---
>>>>>>> 1357aa9 (First commit)
