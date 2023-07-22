from datetime import datetime, timedelta
from collections import defaultdict

users  = [{"name": "Roblen","birthday": datetime(2000,1,3)},
          {"name": "Lunio","birthday": datetime(1942,5,22)},
          {"name": "Persostrat","birthday": datetime(1988,5,22)},
          {"name": "Pores","birthday": datetime(1987,5,22)},
          {"name": "Yavliga","birthday": datetime(2002,5,22)},
          {"name": "Nikoglay","birthday": datetime(1976,5,22)},
          {"name": "Bucefal","birthday": datetime(2004,5,22)},
          {"name": "Lubomir","birthday": datetime(2004,7,23)},
          {"name": "Sigizmund","birthday": datetime(2004,7,22)},
          {"name": "Melaniya","birthday": datetime(2004,7,29)},]

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

congr_by_day = defaultdict(list)

def get_birthdays_per_week(users):
    delta_forward = timedelta(days=7)
    delta_back = timedelta(days=2)
    current_date = datetime.now().date()
    # print("111fff", current_date.weekday())
    # print("YER",current_date.year)
    finish_diapazon = current_date + delta_forward
    start_diapazon = current_date - delta_back
    # print(f"finish {finish_diapazon} start {start_diapazon}")
    # print("D",current_date)
    to_congratulate = []
    for user in users:
        u_birthday = user["birthday"].date()
        u_birthday_replaced = u_birthday.replace(year=current_date.year)
        # print("wwwwww",u_birthday_replaced)
        # print("date",u_birthday_replaced.weekday())
        if start_diapazon <= u_birthday_replaced <= finish_diapazon:
            # print("Op piimav")
            # print(user)
            get_week_day = u_birthday_replaced.weekday()
            if start_diapazon <= u_birthday_replaced < current_date and get_week_day in (5,6):
                to_congratulate.append(user)
                print(f"День рожденя было в {week[get_week_day]} нужно поздравить в понедельник")
            elif current_date == u_birthday_replaced and get_week_day in (5,6):
                to_congratulate.append(user)
                print(f"Готовьтесь поздравлять в понедельник {user}")
            elif current_date == u_birthday_replaced:
                to_congratulate.append(user)
                print(f"Бегите уже поздравлять {user}")
            elif current_date < u_birthday_replaced <= finish_diapazon and get_week_day in (5,6):
                user.update({"next": True})
                to_congratulate.append(user)
                print(f"День рожденя только будет в {week[get_week_day]} нужно поздравить в следующий понедельник")
            elif current_date < u_birthday_replaced <= finish_diapazon and get_week_day in (0,4):
                to_congratulate.append(user)
                print(f"День рожденя только будет в {week[get_week_day]} нужно поздравить")

    # print(to_congratulate)

    for birthday_boy in to_congratulate:
        if birthday_boy.get("next"):
            birth_day = week["next"]
            congr_by_day[birth_day].append(birthday_boy["name"])
            continue

        birth_day = birthday_boy["birthday"].date()
        birth_day_replaced = birth_day.replace(year=current_date.year)
        weekday_of_birth = birth_day_replaced.weekday()
        # print("было",birth_day)
        # print("стало",weekday_of_birth)
        birth_day = week[weekday_of_birth]
        congr_by_day[birth_day].append(birthday_boy["name"])

    print(congr_by_day)
    return(congr_by_day)


get_birthdays_per_week(users)
