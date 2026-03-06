def ft_count_harvest_recursive(harvest_time = 0, count = 1):
	if harvest_time == 0:
		harvest_time = int(input("Days until harvest: "))
	if count <= harvest_time:
		print("Day", count)
		ft_count_harvest_recursive(harvest_time, count + 1)
	else:
		print("Harvest time!")

#ft_count_harvest_recursive()
	