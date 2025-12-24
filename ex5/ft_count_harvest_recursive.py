def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_days(current_day, total_days):
        if current_day > total_days:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        count_days(current_day + 1, total_days)

    count_days(1, days)
