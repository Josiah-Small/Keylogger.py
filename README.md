# Keylogger and Website Tracker

## Description

This project is a Python-based keylogger and website tracker. It logs keystrokes, detects login-related information, and tracks the active window (website) being visited. The keylogger captures keystrokes and stores them in a file, while the website tracker logs the active windows along with the timestamps.

## Features

- **Keylogging**: Records all key presses.
- **Login Information Detection**: Detects and saves login-related keywords such as 'login', 'password', 'email', and 'username'.
- **Active Window Tracking**: Tracks and logs the title of active windows (websites) along with the timestamps.

## Requirements

- Python 3.6
- `keyboard` library
- `pygetwindow` library
- `datetime` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install the required libraries:
    ```sh
    pip install keyboard pygetwindow
    ```

## Usage

1. Run the script:
    ```sh
    python keylogger.py
    ```

2. The keylogger will start capturing keystrokes and saving them in `KeyTracker.txt`. 

3. The website tracker will log active windows in `Visited_Sites.txt`.

## File Structure

- `keylogger.py`: The main script for the keylogger and website tracker.
- `KeyTracker.txt`: The file where all captured keystrokes and login information are stored.
- `Visited_Sites.txt`: The file where the titles of visited websites and their timestamps are stored.

## Code Explanation

### `get_active_window()`
- Retrieves the title of the currently active window.

### `save_info(website, login_info, DateTime)`
- Saves the detected login information along with the website title and timestamp to `KeyTracker.txt`.

### `Keylogger()`
- Captures keystrokes and detects login-related keywords. 
- Calls `save_info()` when login-related keywords are detected.

### Main Script
- Starts the keylogger and continuously tracks the active window, logging each new window visited in `Visited_Sites.txt`.

## License

This project is licensed under the MIT License. 
