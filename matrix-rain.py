import curses
import random
import time

def main(stdscr):
    # Set up the color of the text
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))

    # Hide the cursor
    curses.curs_set(0)

    # Get the size of the terminal
    h, w = stdscr.getmaxyx()

    # Create a list to hold the 'streamers'
    streamers = [[0]*5 for _ in range(w)]

    while True:
        # Randomly reset a streamer to the top
        i = random.randint(0, w-1)
        streamers[i] = [0]*5

        # Draw each streamer
        for i in range(w):
            for j in range(5):
                # Only draw the streamer if it's in bounds
                if 0 <= streamers[i][j] < h and 0 <= i < w:
                    # Generate a random character
                    char = chr(random.randint(33, 126))

                    try:
                        # Draw the character
                        stdscr.addch(streamers[i][j], i, char)
                    except curses.error:
                        pass

                    # Move the streamer down
                    streamers[i][j] += 1

                # Clear the character that's no longer part of the streamer
                if 0 <= streamers[i][j] - 5 < h and 0 <= i < w:
                    try:
                        stdscr.addch(streamers[i][j] - 5, i, ' ')
                    except curses.error:
                        pass

        # Refresh the screen
        stdscr.refresh()

        # Wait for a bit
        time.sleep(0.1)

if __name__ == "__main__":
    time.sleep(1)  # Add a delay to give the terminal time to initialize
    curses.wrapper(main)
