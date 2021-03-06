def processLogs(logs, threshold):
    map = {}
    for log in logs:
        log = log.split()
        if log[0] not in map:
            map[log[0]] = int(log[1])
        else:
            map[log[0]] += int(log[1])
        if log[0] != log[1]:
            if log[1] not in map:
                map[log[1]] = int(log[1])
            else:
                map[log[1]] += int(log[1])
    userIds = []
    for key, value in map.items():
        if value >= threshold:
            userIds.append(key)
    userIds.sort()
    return userIds

print(processLogs(["88 99 200", "88 99 300", "99 32 100", "12 12 15"], 2))