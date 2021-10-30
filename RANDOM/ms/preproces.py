import re


def preprocessDate(Date):
    dates = []
    for i in range(0, len(Date)):
        date = Date[i].split()
        numbers = re.findall('[0-9]+', date[0])
        day = numbers[0]
        if int(numbers[0]) < 10:
            day = "0" + numbers[0]
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                 "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        key_list = list(month.keys())
        val_list = list(month.values())

        mot = val_list[key_list.index(date[1])]

        dates.append(date[2] + "-" + mot + "-" + day)
    return dates


dates = preprocessDate(Date)
for i in range(0, len(dates)):
    print(dates[i])