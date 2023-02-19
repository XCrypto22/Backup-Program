# Import modules
import schedule
import time
import shutil
import os
import logging
import tkinter as tk # For GUI
import psutil # For checking if program is running
import tkinter.filedialog

# Define program state in order to terminate it
program_is_running = True

# Open the file for reading
with open("./config/period.config", "r") as f:
    # Read all lines into a list
    lines = f.readlines()

    # Remove newline characters from each element of lines
    lines = [line.strip() for line in lines]

    # Split each element of lines by whitespace
    lines = [line.split(" ") for line in lines]

    # Assign day and time variables from lines
    _day = lines[0][0].lower()
    _time = lines[1][0]
    _hours = lines[2][0]

# Define source and destination folders
source = "C:\\Users\\PC\\Music\\download"
destination = "C:\\Users\\PC\\Desktop\\backup"

# Define log file name and format
log_file = "./logs/backup.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

# Define backup function
def backup():
    # Initialize counter for number of files copied
    count = 0
    # Loop through files in source folder
    for file in os.listdir(source):
        # Create file name of the recently recorded file 
        recent_recorded_file = time.strftime('rec_%Y%m%d-%H0000_1.mp3')
        # Skip the most recent file being recorded in the LOGGER MACHINE
        if file != recent_recorded_file:
            # Get full path of file
            file_path = os.path.join(source, file)
            # Check if file is newer than existing backup or does not exist in backup
            if not os.path.exists(os.path.join(destination, file)) or \
            os.stat(file_path).st_mtime > os.stat(os.path.join(destination, file)).st_mtime:
                # Copy file to destination folder
                shutil.copy2(file_path, destination)
                print(f"Copied {file} to {destination}")
                # Increment counter and log file name
                count += 1 
                logging.info(f"Copied {file} to {destination}")
    # Print and log number of files copied and date of backup 
    print(f"Backup completed. Copied {count} files on {time.strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Backup completed. Copied {count} files on {time.strftime('%Y-%m-%d %H:%M:%S')}")
    # Update the GUI label with the result message 
    result_label.config(text=f"Backup completed. Copied {count} files on {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Create a root window for GUI 
root = tk.Tk()
# Set the title and geometry of the window 
root.title("Backup Program")
root.geometry("700x450")
# Set the background color to #2d2d2d 
root.config(bg="#2d2d2d")
# Create a futuristic font for the GUI elements 
font = ("Arial", 20, "bold")
# Create a label to display the program name 
title_label = tk.Label(root, text="Backup Program", font=font, fg="purple", bg="#2d2d2d",)
# Place the label at the center of the window 
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
# Create a button to start the backup function manually 
backup_button = tk.Button(root, text="Force Backup", font=("Arial", 16, "bold"), fg="white", bg="#2d2d2d", command=backup)
# Place the button below the label with some padding 
backup_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
# Create a label to display the configured backup period
if _hours == '0':
    period_status = tk.Label(root,text=f'Backup period: {_day}@{_time}',font=("Courier", 8),bg='#2d2d2d',fg='white')
    period_status.place(relx=.05, rely=.2)
else:
    period_status = tk.Label(root,text=f'Backup period: {_hours} hours',font=("Courier", 8),bg='#2d2d2d',fg='white')
    period_status.place(relx=.05, rely=.2)

def change_source():
    global source    
    new_source = tkinter.filedialog.askdirectory(title='Select Source Folder')    
    if new_source:        
        source = new_source        
        print(f"Source folder changed to: {source}")        
        logging.info(f"Source folder changed to: {source}")        
        source_label.config(text=f">> {source}")

def change_destination():
    global destination    
    new_destination = tkinter.filedialog.askdirectory(title='Select Destination Folder')    
    if new_destination:        
        destination = new_destination        
        print(f"Destination folder changed to: {destination}")        
        logging.info(f"Destination folder changed to: {destination}")        
        destination_label.config(text=f">> {destination}")
        

# Create another button to change source folder  
source_button = tk.Button(root,text='Change Source',font=("Arial", 12, "bold"),bg='blue',fg='white',command=change_source)  
source_button.place(relx=.15,rely=.40)  

# Create another button to change destination folder  
destination_button = tk.Button(root,text='Change Destination',font=("Arial", 12, "bold"),bg='blue',fg='white',command=change_destination)  
destination_button.place(relx=.60,rely=.40)  

# Create another label to display current source folder  
source_label = tk.Label(root,text=f'>> {source}',font=("Courier", 8),bg='#2d2d2d',fg='white')  
source_label.place(relx=.10,rely=.50)  

# Create another label to display current destination folder  
destination_label = tk.Label(root,text=f'>> {destination}',font=("Courier", 8),bg='#2d2d2d',fg='white')
destination_label.place(relx=.55, rely=.50)


# Create another label to display if program is running in auto mode or off  
status_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="white", bg="#2d2d2d")
# Place the label below the button with some padding 
status_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
# Create another label to display the result message after backup 
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="yellow", bg="#2d2d2d")
# Place the label below status label with some padding 
result_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


def close_program():
    global root    
    print("Closing program...")
    logging.info("Closing program...")
    pid = os.getpid()
    root.destroy() # destroy GUI window
    global program_is_running
    program_is_running = False # Change program state to terminate all processes
    

# Create another button to terminate program  
terminate_button = tk.Button(root,text='Terminate Program',font=("Arial", 14, "bold"),bg='red',fg='white',command=close_program)  
terminate_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Create a label to display details of the developer
about_label = tk.Label(root,text=f'Created by: Snr Elton \nhttps://github.com/XCrypto22',font=("Courier", 7),bg='#2d2d2d',fg='white')
about_label.place(relx=.75, rely=.92)

def update_status():
    global status_label    
    # Check if program is running by its name (change this according to your program name)    
    program_name = "python.exe"
    running_processes = [p.name() for p in psutil.process_iter()]
    if program_name in running_processes:
        status_label.config(text=f"Program is running in Auto Mode.")
    else:
        status_label.config(text=f"Program is off.")
        
update_status()        

# Schedule backup function to run once every week(this will run in background)
# Define a function for each day of the week
def monday():
    schedule.every().monday.at(_time).do(backup)

def tuesday():
    schedule.every().tuesday.at(_time).do(backup)

def wednesday():
    schedule.every().wednesday.at(_time).do(backup)

def thursday():
    schedule.every().thursday.at(_time).do(backup)

def friday():
    schedule.every().friday.at(_time).do(backup)

def saturday():
    schedule.every().saturday.at(_time).do(backup)

def sunday():
    schedule.every().sunday.at(_time).do(backup)

# Define a dictionary that maps each day to a function
switcher = {
    "monday": monday,
    "tuesday": tuesday,
    "wednesday": wednesday,
    "thursday": thursday,
    "friday": friday,
    "saturday": saturday,
    "sunday": sunday
}

# Define a function that takes user input and executes the corresponding function
def switch(day):
    # Get the function from the dictionary
    func = switcher.get(day, lambda: print("Invalid day"))
    
    # Execute the function
    func()


# Call the switch function with configured day
if _hours == '0':
    switch(_day)
else:
    schedule.every(int(_hours)).hours.do(backup)

# Run scheduled tasks in a loop (this will also run in background)
def run_scheduled_tasks():
    while program_is_running:
        schedule.run_pending()
        time.sleep(1) # Wait one second

# Start a new thread for running scheduled tasks (so that it does not block the GUI)        
from threading import Thread        
thread = Thread(target=run_scheduled_tasks)
thread.start()

root.mainloop()
