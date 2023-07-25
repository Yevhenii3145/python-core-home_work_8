from datetime import datetime, timedelta
from collections import defaultdict

users = [{"name": "Roblen", "birthday": datetime(2000, 1, 3)},
         {"name": "Lunio", "birthday": datetime(1942, 7, 23)},
         {"name": "Persostrat", "birthday": datetime(1988, 5, 22)},
         {"name": "Pores", "birthday": datetime(1987, 5, 22)},
         {"name": "Yavliga", "birthday": datetime(2002, 7, 30)},
         {"name": "Nikoglay", "birthday": datetime(1976, 7, 27)},
         {"name": "Bucefal", "birthday": datetime(2004, 5, 22)},
         {"name": "Lubomir", "birthday": datetime(1950, 7, 23)},
         {"name": "Sigizmund", "birthday": datetime(1078, 7, 22)},
         {"name": "Melaniya", "birthday": datetime(1996, 7, 27)},
         {"name": "Aslan", "birthday": datetime(2001, 8, 1)},
         {"name": "Oxana", "birthday": datetime(1995, 7, 28)}]


week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
    "next": "Next Monday"
}

celebrate_dict = defaultdict(list)


def get_birthdays_per_week(users):
    delta_forward = timedelta(days=7)
    delta_back = timedelta(days=2)

    current_date = datetime.now().date()
    finish_diapazon = current_date + delta_forward
    start_diapazon = current_date - delta_back

    celebrate_list = []

    for user in users:
        birth_day = user["birthday"].date()
        birth_day = birth_day.replace(year=current_date.year)

        if start_diapazon <= birth_day <= finish_diapazon:
            birth_day_weekday = birth_day.weekday()

            if start_diapazon <= birth_day < current_date and birth_day_weekday in (5, 6) and current_date.weekday() == 0:
                user.update({"today": True})
                celebrate_list.append(user)
                print(
                    f"День рожденя {user['name']} было в {week[ birth_day_weekday]} нужно поздравить сегодня")

            elif current_date == birth_day and birth_day_weekday in (5, 6):
                celebrate_list.append(user)
                print(f"Готовьтесь поздравлять в понедельник {user['name']}")

            elif current_date == birth_day:
                celebrate_list.append(user)
                print(f"Бегите уже поздравлять {user['name']}")

            elif current_date < birth_day <= finish_diapazon and birth_day_weekday in range(5, 6+1):
                user.update({"next": True})
                celebrate_list.append(user)
                print(
                    f"День рожденя {user['name']} только будет в {week[ birth_day_weekday]} нужно поздравить в следующий понедельник")

            elif current_date < birth_day <= finish_diapazon and (birth_day_weekday in range(0, 4+1)):
                celebrate_list.append(user)
                print(
                    f"День рожденя {user['name']} только будет в {week[ birth_day_weekday]} нужно поздравить")

    for celebrator in celebrate_list:

        if celebrator.get("next"):
            week_day = week["next"]
            celebrate_dict[week_day].append(celebrator["name"])
            continue

        elif celebrator.get("today"):
            week_day = week[0]
            celebrate_dict[week_day].append(celebrator["name"])
            continue

        birth_day = celebrator["birthday"].date()
        birth_day = birth_day.replace(year=current_date.year)
        birth_day_weekday = birth_day.weekday()
        week_day = week[birth_day_weekday]

        celebrate_dict[week_day].append(celebrator["name"])

    result = {"Monday": celebrate_dict.get("Monday", ""),
              "Tuesday": celebrate_dict.get("Tuesday", ""),
              "Wednesday": celebrate_dict.get("Wednesday", ""),
              "Thursday": celebrate_dict.get("Thursday", ""),
              "Friday": celebrate_dict.get("Friday", ""),
              "Saturday": celebrate_dict.get("Saturday", ""),
              "Sunday": celebrate_dict.get("Sunday", ""),
              "Next Monday": celebrate_dict.get("Next Monday", ""), }

    print(result)
    return (result)


get_birthdays_per_week(users)
