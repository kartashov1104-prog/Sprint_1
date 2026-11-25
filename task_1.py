line = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for value in line.split(','):
    for unit in value.strip().split():
        if 'h' in unit:
            total_minutes += int(unit.replace('h', '')) * 60
        elif 'm' in unit:
            total_minutes += int(unit.replace('m', ''))
        elif 's' in unit:
            total_minutes += int(unit.replace('s', '')) // 60

print(total_minutes)