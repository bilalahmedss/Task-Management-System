# Personalized Task Management System using a Priority Queue

## Overview

The **Personalized Task Management System** is designed to help users manage their tasks efficiently by prioritizing them using a **priority queue** data structure. This system allows users to add, remove, and update tasks based on user-defined criteria, such as due date, difficulty, and importance.

## Features

- **Task Prioritization**: Tasks are organized based on user-defined priorities, such as due date and difficulty.
- **Time Management**: The system suggests the best time to work on a task based on available time slots in the user's schedule.
- **Schedule Integration**: Tasks are added directly to a weekly schedule, helping users stay organized and efficient.
- **Dynamic Updates**: Users can add new tasks, update existing ones, and remove tasks easily.
- **Data Export**: The system generates and exports the updated schedule to an Excel file (`Schedule.xlsx`).

## Installation

To run the project, you will need to install the required dependencies. Follow these steps:

1. **Install Python 3.11**

2. **Install Required Libraries**:
   - You need `pandas` and `openpyxl` to handle scheduling and Excel file export.
   - If not installed, you can use the following commands:
   
   ```bash
   pip install pandas openpyxl
   ```

## How to Use

1. **Running the Program**:
   - Run the script using the following command:
   
   ```bash
   python "Task Management - Priority Queue.py"
   ```

2. **Registering Tasks**:
   - The program will prompt you to enter tasks, specifying:
     - Task title
     - Assigned weekday
     - Due date (number of days from the assigned day)
     - Difficulty level (1-10)
   
   - The tasks are then stored in a priority queue and added to the weekly schedule based on their priority.

3. **Viewing and Updating Schedule**:
   - The program updates the `Schedule.xlsx` file with the tasks, classes, and blocks, showing the best available time for each task.

4. **Excel Output**:
   - The updated schedule is saved in an Excel file, which you can open to view your tasks and their scheduled times.

## Code Walkthrough

### Key Functions

- **`get_task_input()`**: Prompts the user to input task details, including title, assigned weekday, due date, and difficulty level.
- **`add_tasks_to_schedule()`**: Uses a priority queue (implemented with `heapq`) to prioritize tasks based on difficulty and due date, and then places them into the user's schedule at the most optimal time slots.
- **`get_block_input()` and `add_block_to_schedule()`**: Allow users to add "blocks" (periods of time) to the weekly schedule.
- **`get_class_input()` and `add_class_to_schedule()`**: Let users add classes to their weekly schedule, ensuring no overlap with existing blocks or tasks.

### Libraries Used

- **`pandas`**: Used for creating and manipulating the weekly schedule (stored in a DataFrame).
- **`openpyxl`**: Required to read/write `.xlsx` Excel files.
- **`heapq`**: Implements a priority queue for efficient task prioritization.


## Conclusion

This project aims to create a personalized task management system that efficiently organizes tasks and schedules them based on priority. It will help users manage their time and tasks effectively, ultimately improving productivity.

---
## Contribution

This project is open for contributions! If you would like to improve this task management system, feel free to fork the repository, make your changes, and submit a **pull request**. All contributions are welcome, and we appreciate your help in improving this project.

Looking forward to your contributions!