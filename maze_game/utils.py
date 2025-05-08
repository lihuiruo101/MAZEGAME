def evaluate_stage(time_taken, max_time):
    ratio = time_taken / max_time
    if ratio <= 0.33:
        return 3
    elif ratio <= 0.66:
        return 2
    elif ratio <= 1.0:
        return 1
    else:
        return 0
