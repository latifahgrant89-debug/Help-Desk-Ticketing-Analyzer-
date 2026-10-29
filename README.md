# Help-Desk-Ticketing-Analyzer-
IT Help Desk Ticket Analyzer

Project Overview
The IT Help Desk Ticket Analyzer is a Python project designed to organize and analyze IT support ticket data. It processes a collection of sample tickets to identify patterns in support requests, including ticket categories, priority levels, and statuses. I created this project to strengthen my Python programming skills while learning more about how IT support teams manage technical issues. It also helped me explore how data analysis can be used to better understand support requests and identify areas that may require additional attention.

Features
Read ticket information from a text file.
Counts the total number of support tickets.
Groups tickets by category, including Network, Software, Account, and Hardware.
Counts tickets by priority level: Low, Medium, and High.
Tracks open and closed tickets.
Identifies high-priority tickets that are still open.
Displays a summary of the analyzed ticket data.

Technologies Used
Python 3 — Used to process and analyze ticket information.
Text files — Used to store the sample help desk tickets.

Project Structure

it-helpdesk-ticket-analyzer/
├── main.py
└── helpdesk_tickets.txt

main.py contains the Python code used to analyze the tickets.
helpdesk_tickets.txt contains the sample ticket records processed by the program.

How to Run the Project
Download or clone the repository.
Make sure Python 3 is installed on your computer.
Open the project folder in VS Code or another Python editor.
Confirm that helpdesk_tickets.txt is in the same directory as main.py.
Open the terminal and run:
python3 main.py
The program will read the ticket records, calculate the statistics, and display a summary of the results.

What I Learned
Through this project, I practiced reading files, processing strings, using loops and conditional statements, and organizing information with Python.
I also developed a better understanding of how IT support teams categorize technical issues, prioritize requests, and track ticket statuses. This project helped me see how programming can be used to turn raw data into information that supports everyday IT operations.
Limitations
The current version analyzes sample ticket data stored in a text file. It does not connect to a live ticketing platform or automatically retrieve real support requests. The accuracy of the results also depends on the consistency and formatting of the ticket records.

Future Improvements
Allow users to add new tickets directly through the program.
Add search and filtering options for specific categories or priorities.
Identify recurring technical issues.
Generate reports that can be saved to a separate file.
Add error handling for missing files or incorrectly formatted ticket records.
Connect the program to a database for more efficient ticket storage and management.
Disclaimer
This project is intended for educational purposes and demonstrates basic Python programming and IT support data analysis using sample ticket records.
