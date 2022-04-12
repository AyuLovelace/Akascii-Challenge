
import curses

from curses import wrapper

def main(stdscr):
    # Clear screen
    curses.initscr()
    curses.start_color()
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.refresh()
    stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
    
    for i in range(1,3):
        stdscr.addstr(i, 0, "Current mode: Typing mode", curses.color_pair(1))
        stdscr.refresh()

    stdscr.getch()


wrapper(main)