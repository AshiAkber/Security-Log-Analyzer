
# Security Log Analyzer

## Aim
To investigate security logs and detect repeated failed login attempts using Python.

## Description
This project analyzes sample authentication logs,
counts failed login attempts, and flags users with
three or more failed attempts.

## Technologies Used
- Python 3
- Regular expressions
- Collections Counter

## How to Run
1. Install Python 3.
2. Place log_analyzer.py and security.log in the same folder.
3. Open Command Prompt in that folder.
4. Run: python log_analyzer.py

## Expected Result
The program displays the total failed login attempts,
counts failures by username, and alerts when a user
has three or more failed attempts.

## Security Note
This is an educational demonstration. An alert is an
investigation lead, not proof of malicious activity.

## Result
The program successfully analyzes sample logs and
identifies repeated failed login attempts.
