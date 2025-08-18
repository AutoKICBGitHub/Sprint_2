time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

parts = time_str.split(',')
total_minutes = 0

for part in parts:
    tokens = part.split()  
    for token in tokens:
        if 'h' in token:
            total_minutes += int(token.replace('h', '')) * 60
        elif 'm' in token:
            total_minutes += int(token.replace('m', ''))
        elif 's' in token:
            total_minutes += int(token.replace('s', '')) // 60

print(total_minutes)