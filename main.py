import os # for TTS
import platform # for TTS

import tkinter as tk # for GUI
import tkinter.messagebox as mbox # for GUI


def main():
    """
    Create and run a GUI window with a text entry, a label, and a button.
    When the button is pressed, the text from the entry is spoken using the
    speak function.
    """
    # Create the main window
    window = tk.Tk()
    window.title("Text-to-Speech")

    # Define the function to be called when the button is pressed
    def speak_func():
        """
        Get the text from the entry, and call the speak function to speak it.
        """
        text = entry.get()
        speak(text)

    # Create a label to display the text
    label = tk.Label(window, text="What would you like to say? ")
    label.pack()

    # Create an entry to get the text from the user
    entry = tk.Entry(window, width=100, borderwidth=20)
    entry.pack()

    # Create a button to start the speech
    button = tk.Button(window, text="Speak", command=speak_func)
    button.pack()

    # Start the event loop
    window.mainloop()


def speak(text):
    """
    Speak the given text using the system's text-to-speech engine.

    Args:
        text (str): The text to speak.
    """
    system = platform.system()

    # Check the system and use the appropriate text-to-speech engine
    if system == 'Windows':
        # Windows has a built-in TTS engine accessible via win32com.client
        import win32com.client  # pylint: disable=import-outside-toplevel
        # Create a COM object for the speech engine
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # Speak the given text
        speaker.Speak(text)

    elif system == 'Darwin':
        # macOS has a built-in TTS command called 'say'
        os.system(f"say '{text}'")  # pylint: disable=consider-using-with

    elif system == 'Linux':
        # Some Linux distributions have a command called 'spd-say'
        os.system(f"spd-say '{text}'")  # pylint: disable=consider-using-with

    else:
        # Print a message if the platform is not supported
        print("Platform not supported for TTS")


if __name__ == "__main__":
    main()
