import curses
from maze_game import main  # maze_game.py에서 main()을 호출

if __name__ == "__main__":
    curses.wrapper(main)
