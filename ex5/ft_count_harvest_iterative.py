def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    current_day = 1
    while current_day <= days:
        print(f"Day {current_day}")
        current_day += 1
    print("Harvest time!")

# def ft_count_harvest_iterative():
#     days = int(input("Days until harvest: "))
#     for i in range(1, days + 1):
#         print(f"Day {i}")
#     print("Harvest time!")
