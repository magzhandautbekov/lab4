from datetime import datetime

# будем использовать функцию strptime
# datetime.strptime(date_string, format) -> будем преобразать строковое представления даты и времени в объект datetime.
# date_string -> введенное время ,format -> формат введенных данных

input_date_time1 = input("(ГГГГ-ММ-ДД ЧЧ:ММ:СС):")
date_time1 = datetime.strptime(input_date_time1,"%Y-%m-%d %H:%M:%S")

input_date_time2 = input("(ГГГГ-ММ-ДД ЧЧ:ММ:СС):")
date_time2 = datetime.strptime(input_date_time2,"%Y-%m-%d %H:%M:%S")

difference = date_time1 - date_time2
print(difference)

