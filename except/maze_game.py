import random
import time
import string
import os
import json
import curses

# 이어하기 코드 및 인증번호 생성
def generate_codes():
    # 이어하기 코드 (9자리, a-f, 0-9)
    code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    # 인증번호 (4자리, 0-9)
    password = ''.join(random.choices(string.digits, k=4))
    return code, password

# 미로 생성 함수
def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def carve(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy // 2][x + dx // 2] = 0
                carve(nx, ny)

    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    carve(start_x, start_y)

    maze[0][1] = 0  # entrance
    maze[height - 1][width - 2] = 0  # exit

    return maze

# 미로 출력 함수
def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell == 1 else ' ' for cell in row]))

# 세션에 대한 설명
def show_help():
    print("""
    Help - 게임 설명
    -------------------
    - ESC: Get Code (이어하기 코드와 인증번호 생성)
    - Ctrl: Save Code (저장된 코드를 통해 게임을 이어서 할 수 있음)
    - Alt: Help (게임의 기능에 대해 설명)
    """)

# 세션 저장 함수
def save_session(code, password):
    save_data = {
        "code": code,
        "password": password,
        "timestamp": time.time()
    }
    if not os.path.exists("save"):
        os.makedirs("save")
    with open(f"save/{code}.json", "w") as f:
        json.dump(save_data, f)

# 세션 로드 함수
def load_session(code):
    try:
        with open(f"save/{code}.json", "r") as f:
            save_data = json.load(f)
        return save_data
    except FileNotFoundError:
        print(f"세션 코드 {code}가 없습니다.")
        return None

# 키 입력을 처리하는 게임 루프
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    height, width = stdscr.getmaxyx()

    # 초기 변수 설정
    stage = 1
    timer = None
    maze = None
    code = None
    password = None

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Stage: {stage}")
        stdscr.addstr(1, 0, "Press ESC for Get Code, Ctrl for Save Code, Alt for Help")

        if maze:
            print_maze(maze)

        key = stdscr.getch()

        # ESC 키 (Get Code)
        if key == 27:  # ESC 키
            code, password = generate_codes()
            stdscr.addstr(3, 0, f"Generated Code: {code}")
            stdscr.addstr(4, 0, f"Generated Password: {password}")
            save_session(code, password)
            stdscr.refresh()
            time.sleep(2)

        # Ctrl 키 (Save Code)
        elif key == 3:  # Ctrl 키
            if code and password:
                session = load_session(code)
                if session:
                    stdscr.addstr(5, 0, f"Resuming Game with Code: {code}")
                    # 미로와 타이머 초기화
                    maze = generate_maze(15, 15)
                    stage += 1
                    stdscr.refresh()
                    time.sleep(2)
            else:
                stdscr.addstr(5, 0, "No code to save.")
                stdscr.refresh()
                time.sleep(2)

        # Alt 키 (Help)
        elif key == 26:  # Alt 키
            show_help()
            stdscr.refresh()
            time.sleep(5)

        # 퀴즈나 미로 진행 로직 추가 가능
        if maze is None:
            maze = generate_maze(15, 15)

        stdscr.refresh()
        time.sleep(0.1)
