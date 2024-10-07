# Final-keylogger-



KeyLogger with Email Reporting

This Python-based keylogger tracks and records keystrokes, mouse movements, clicks, and other system events. It also captures screenshots and records audio using the microphone at regular intervals. All data is periodically sent to a specified email address. This keylogger is designed for educational purposes, helping users understand how keyloggers work and how data can be tracked and recorded in a local environment.

Disclaimer: This software is intended for educational and lawful usage in environments where you have permission. Do not use this tool for unauthorized monitoring or malicious purposes.

Features

Keystroke Logging: Records every keystroke and appends it to a log file.

Mouse Tracking: Captures mouse movements, clicks, and scrolls.

Screenshots: Takes screenshots of the current screen at regular intervals.

Microphone Recording: Records audio from the microphone at set intervals.

Email Reporting: Sends the collected log, screenshots, and audio recordings to a specified email address.

System Information: Logs detailed system information including hostname, IP address, processor, and operating system details.


Installation

Prerequisites

Ensure you have Python installed on your system. You’ll also need the following Python modules:

pyscreenshot

sounddevice

pynput

logging

smtplib


To install the necessary modules, run:

pip install pyscreenshot sounddevice pynput

Setup

1. Clone the repository:

git clone https://github.com/yourusername/keylogger.git
cd keylogger


2. Open the script and configure your email credentials by setting the EMAIL_ADDRESS and EMAIL_PASSWORD variables to your email account information.


3. Set the interval for reports by adjusting the SEND_REPORT_EVERY variable (in seconds).



Running the Keylogger

Once the setup is complete, you can run the script:

python keylogger.py

The keylogger will begin tracking system events and will periodically send logs and captured data to your specified email.

Usage

Educational Purpose: Use this keylogger to understand how keylogging works in local environments.

Security Auditing: Perform security audits on systems that you have authorization to monitor.


Note: This tool should only be used in environments where you have explicit permission to record and monitor data.

License

This project is licensed under the MIT License - see the LICENSE file for details.


---

