# Matrix Code Emulator for VSCode

Do you want to feel like a hacker from the Matrix movie? Do you want to impress your friends with your cool terminal skills? Do you want to have some fun while coding in vscode?

If you answered yes to any of these questions, then this extension is for you!

This extension allows you to run a matrix code emulator in your vscode terminal. It will fill your screen with green characters that look like they are falling from the top. 

## How to use it

To use this extension, you need to have **Python** and **curses** installed on your system. You can install curses by running `pip install windows-curses` on Windows or `pip install curses` on Linux or Mac and a python environment, anaconda has the couple other dependencies.

Then, you need to open a new terminal in vscode and run the following command:

`python matrix.py`

This will start the matrix code emulator. You can stop it by pressing `Ctrl+C`.

## How it works

This extension is based on a simple Python script that uses the curses library to manipulate the terminal output. The script does the following:

- It sets up the color of the text to green and black, and hides the cursor.
- It gets the size of the terminal and creates a list of 'streamers', which are columns of characters that fall from the top.
- It randomly resets a streamer to the top and draws each streamer with a random character.
- It moves each streamer down by one row and clears the character that is no longer part of the streamer.
- It refreshes the screen and waits for a bit before repeating the process.

## Disclaimer

This extension is for entertainment purposes only. It does not actually hack anything or do anything useful. It may also consume some CPU resources and slow down your system. Use it at your own risk.

## Feedback

If you like this extension, please leave a star on GitHub and share it with your friends. If you have any suggestions or issues, please open an issue on GitHub or contact me at [your email address]. Thank you for using this extension and have fun!
