#Program Name
This program is a GUI application for backing up files from a source folder to a destination folder. The 
backup can be performed manually by clicking on the "Force Backup" button or automatically based on 
a period defined in a configuration file. The program uses the shutil and os modules for copying files, the 
logging module for logging backup information, the psutil module for checking if the program is running, 
and the tkinter module for creating a graphical user interface. 

#Installation
You need python 3.10 installed

Open command-line and type: pip install -r requirements.txt

To run the program simply type: python auto_backup.py

#Usage
When you execute the script a GUI pops out. the Interface includes:
- A "Force Backup" green button to manually backup files
- A label that show current backup period
- Source and Destination blue buttons to change your source of the directory with the files to be copied to the specified destination folder
- A label will appear everytime a backup is made
- A terminate red button to close the program
- For the program to run automatically just leave the window open or minimize dont close the program
- Theres a log file in the log folder for every activity of the script

Changing backup Period
- open the the period.config file in the config folder with any text editor and change day or time as you prefer


Examples
- In the period.config >> friday
                          10:30
that means program will backup every Friday at 10:30 am - uses 24hr notation

#Contributing
If you would like to contribute to this project, you can create a pull request with your suggested changes.
Report issues to xcryptocyber@gmail.com

#License
This program is licensed under the MIT License.


#Contact
Developer - Elton Fungirai
Email - eltonfungirai@gmail.com
