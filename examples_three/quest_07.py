def find_time(avg_speed_per_hour, distance):
    avg_speed_per_minute = avg_speed_per_hour / 60
    minute = distance / avg_speed_per_minute
    hour = minute // 60
    minute %= 60

    return hour, minute


hour, minute = find_time(50, 120)
print(f"hour:{hour}\nminute:{minute}")
