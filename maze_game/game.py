def main():
    stage = 1
    while True:
        width = 15 + stage * 2
        height = 15 + stage * 2
        maze = generate_maze(width, height)
        # 게임 플레이 함수 (pygame으로 표시, timer 작동 등)
        # 시간 측정 후 별 개수 평가
        stage += 1
