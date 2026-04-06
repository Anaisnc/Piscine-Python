def ft_count_harvest_iterative():
    harvest_time = int(input("Days until harvest: "))
    count = 1
    while count <= harvest_time:
        print("Day", count)
        count += 1
    print("Harvest time!")
