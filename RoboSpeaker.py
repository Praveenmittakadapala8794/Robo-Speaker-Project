import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
time.sleep(3)
text = '''Python was designed for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. '''
speak.Speak(text)

