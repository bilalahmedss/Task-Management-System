# Builtin Function Used
# a) Used Pandas libray , pd refers to short name
# b) The heap data structure is used in this code to efficiently prioritize tasks based on difficulty and due date
# c) "datetime.strptime()" can be used to convert a string representation of a date into a datetime object for further processing.
# d) "strftime" can be used to format a datetime object into a string representation according to a specified format.
# e) "timedelta" allows you to perform operations such as adding or subtracting durations to manipulate dates and times.
# f) "df.index" attribute is used to access the index of a DataFrame. The index represents the labels or identifiers assigned to each row of the DataFrame.
# g) "pd.notnull"  function is a method provided by the pandas library in Python. It is used to check whether each element in a pandas Series or DataFrame is not null (or missing).
# h) "df.loc" attribute is used in pandas to access rows and columns of a DataFrame using label-based indexing


import pandas as pd
from datetime import datetime, timedelta
import heapq
# Initialize a list of weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Initialize the start time (7:00 AM) and end time (11:00 PM)
start_time = datetime.strptime('07:00', '%H:%M')
end_time = datetime.strptime('23:00', '%H:%M')
# Generate timeframes with a half-hour gap
time_labels = []
current_time = start_time
while current_time <= end_time:
    time_label = current_time.strftime('%H:%M')
    time_labels.append(time_label)
    current_time += timedelta(minutes=30)
# Create an empty DataFrame with weekdays as columns and timeframes as rows
df = pd.DataFrame(columns=weekdays)
df['SCHEDULE'] = time_labels
df.set_index('SCHEDULE', inplace=True)
# Write the DataFrame to an Excel file named "Schedule.xlsx"
df.to_excel('Schedule.xlsx', engine='openpyxl')
def get_block_input():
    block_detail = input("Enter block detail: ")
    start_time = input("Enter start time in 24-hour format (HH:MM): ")
    duration = int(input("Enter duration in minutes: "))
    weekday = input("Enter weekday (Monday, Tuesday, etc.): ")
    while weekday not in weekdays:
        print("Invalid weekday! Please enter a correct weekday.")
        weekday = input("Enter weekday (Monday, Tuesday, etc.): ")
    return block_detail, start_time, duration, weekday
def add_block_to_schedule(block_detail, start_time, duration, weekday, df):
    # Convert the start time to a datetime object
    start_time_dt = datetime.strptime(start_time, '%H:%M')
    # Calculate the end time
    end_time_dt = start_time_dt + timedelta(minutes=duration)
    end_time = end_time_dt.strftime('%H:%M')
    # Find the timeframes to update
    timeframes_to_update = []
    for time in df.index:
        time_dt = datetime.strptime(time, '%H:%M')
        if start_time_dt <= time_dt < end_time_dt:
            timeframes_to_update.append(time)
    # Check if a block already exists at the same time and day
    for timeframe in timeframes_to_update:
        if pd.notnull(df.loc[timeframe, weekday]):
            print("Error: A block already exists at this time and day.")
            return False
    # Update the DataFrame with the block details
    for timeframe in timeframes_to_update:
        df.loc[timeframe, weekday] = block_detail
    return True
# Read the existing schedule from the "Schedule.xlsx" file
df = pd.read_excel('Schedule.xlsx', index_col='SCHEDULE', engine='openpyxl')
# Get user input for the number of blocks to register
num_blocks = int(input("Enter the number of blocks to register: "))
# Get user input and register the blocks
for i in range(num_blocks):
    while True:
        print("\nRegistering block", str(i+1), ":")
        block_detail, start_time, duration, weekday = get_block_input()
        if add_block_to_schedule(block_detail, start_time, duration, weekday, df) == True:
            break
        print("Please try again.")
# Write the updated schedule back to the "Schedule.xlsx" file
df.to_excel('Schedule.xlsx', engine='openpyxl')
print("\nSchedule updated successfully.")
def get_class_input():
    weekday = input("Enter weekday (Monday, Tuesday, etc.): ")
    while weekday not in weekdays:
        print("Invalid weekday! Please enter a correct weekday.")
        weekday = input("Enter weekday (Monday, Tuesday, etc.): ")
    class_detail = input("Enter class detail: ")
    start_time = input("Enter start time in 24-hour format (HH:MM): ")
    duration = int(input("Enter duration in minutes: "))
    return class_detail, start_time, duration, weekday
def add_class_to_schedule(class_detail, start_time, duration, weekday, df):
    # Convert the start time to a datetime object
    start_time_dt = datetime.strptime(start_time, '%H:%M')
    # Calculate the end time
    end_time_dt = start_time_dt + timedelta(minutes=duration)
    end_time = end_time_dt.strftime('%H:%M')
    # Find the timeframes to update
    timeframes_to_update = []
    for time in df.index:
        time_dt = datetime.strptime(time, '%H:%M')
        if start_time_dt <= time_dt < end_time_dt:
            timeframes_to_update.append(time)
    # Check if a class already exists at the same time and day
    for timeframe in timeframes_to_update:
        if pd.notnull(df.loc[timeframe, weekday]):
            print("Error: A class already exists at this time and day.")
            return False
    # Update the DataFrame with the class details
    for timeframe in timeframes_to_update:
        df.loc[timeframe, weekday] = class_detail
    return True
# Read the existing schedule from the "Schedule.xlsx" file
df = pd.read_excel('Schedule.xlsx', index_col='SCHEDULE', engine='openpyxl')
# Get user input for the number of classes to register
num_classes = int(input("Enter the number of classes to register: "))
# Get user input and register the classes
for i in range(num_classes):
    while True:
        print("\nRegistering class", str(i+1), ":")
        class_detail, start_time, duration, weekday = get_class_input()
        if add_class_to_schedule(class_detail, start_time, duration, weekday, df) == True:
            break
        print("Please try again.")
# Write the updated schedule back to the "Schedule.xlsx" file
df.to_excel('Schedule.xlsx', engine='openpyxl')
print("\nSchedule updated successfully.")

def get_task_input():
    title = input("Enter task title: ")
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assignment_weekday = input("Enter assigned weekday: ")
    while assignment_weekday not in weekdays:
        print("Invalid weekday! Please enter a correct weekday.")
        assignment_weekday = input("Enter assigned weekday: ")
    due_days = int(input("Enter the number of days from the assigned day until the task is due: "))
    due_weekday_idx = (weekdays.index(assignment_weekday) + due_days) % 7
    due_weekday = weekdays[due_weekday_idx]
    difficulty = int(input("Enter difficulty level (1-10): "))
    return {"Title": title, "Assigned on": assignment_weekday, "Due Date": due_weekday, "Difficulty": difficulty}
def register_tasks(num_tasks):
    tasks = []
    for i in range(num_tasks):
        print("\nRegistering task " + str(i+1) + ":")
        task = get_task_input()
        tasks.append(task)
    return tasks
def add_tasks_to_schedule(tasks, df):
    # Create a priority queue with tasks prioritized based on difficulty (high to low) and due date (early to late)
    tasks_queue = [(-task['Difficulty'], weekdays.index(task['Due Date']), task) for task in tasks]
    heapq.heapify(tasks_queue)
    # Try to add each task to the schedule
    while tasks_queue:
        temp = heapq.heappop(tasks_queue)
        task = temp[2]
        assigned_day_idx = weekdays.index(task['Assigned on'])
def add_tasks_to_schedule(tasks, df):
    # Create a priority queue with tasks prioritized based on difficulty (high to low) and due date (early to late)
    tasks_queue = []
    for task in tasks:
        difficulty = -task['Difficulty']
        due_date_index = weekdays.index(task['Due Date'])
        task_tuple = (difficulty, due_date_index, task)
        tasks_queue.append(task_tuple)
    heapq.heapify(tasks_queue)
    # Try to add each task to the schedule
    while tasks_queue:
        temp = heapq.heappop(tasks_queue)
        task = temp[2]
        assigned_day_idx = weekdays.index(task['Assigned on'])
        # Start looking for available time slots from the day after the assigned day
        for day_offset in range(1, 7):
            weekday = weekdays[(assigned_day_idx + day_offset) % 7]
            # Find all available time slots on the current day
            available_slots = []
            for time in df.index:
                if pd.isnull(df.loc[time, weekday]):
                    available_slots.append(time)
            if len(available_slots) == 0:
                # If no time slot was available on the current day, continuse to the next day
                continue
            # Find the largest gap in the schedule
            maxgap_start = maxgap_end = available_slots[0]
            for i in range(1, len(available_slots)):
                if (datetime.strptime(available_slots[i], '%H:%M') - datetime.strptime(available_slots[i-1], '%H:%M')) > timedelta(minutes=30):
                    # If a larger gap is found, update the start and end of the max gap
                    maxgap_start = available_slots[i-1]
                    maxgap_end = available_slots[i]
            # Schedule the task in the middle of the largest gap
            maxgap_start_dt = datetime.strptime(maxgap_start, '%H:%M')
            maxgap_end_dt = datetime.strptime(maxgap_end, '%H:%M')
            task_time = (maxgap_start_dt + (maxgap_end_dt - maxgap_start_dt) / 2).strftime('%H:%M')
            df.loc[task_time, weekday] = task['Title']
            # If the task was added to the schedule, break the outer loop
            break
        else:
            # If no time slot was available on any day, print an error message
            print("Error: No available time slot for task: " + task['Title'])

    # Write the updated schedule back to the "Schedule.xlsx" file
    df.to_excel('Schedule.xlsx', engine='openpyxl')
# Get user input for the number of tasks to register
num_tasks = int(input("Enter the number of tasks to register: "))
# Register tasks and store them in a list
tasks = register_tasks(num_tasks)
# Add the tasks to the schedule
add_tasks_to_schedule(tasks, df)
print("\nSchedule and tasks updated successfully.")
