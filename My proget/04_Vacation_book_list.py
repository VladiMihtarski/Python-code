pages_in_book = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

total_hours = (pages_in_book // pages_per_hour) / days_to_read

print(int(total_hours))
