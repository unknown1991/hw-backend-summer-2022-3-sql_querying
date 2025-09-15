# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """  SELECT flight_no, scheduled_arrival - scheduled_departure as duration 
                    FROM flights 
                    ORDER BY duration 
                    LIMIT 5;
"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """  SELECT flight_no, count(1) as count 
                    FROM flights 
                    GROUP BY flight_no 
                    HAVING count(1) < 50 
                    ORDER BY count DESC
                    LIMIT 3;
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """  SELECT count(1) as count 
                    FROM flights as f
                    INNER JOIN airports_data as aa ON f.arrival_airport = aa.airport_code
                    INNER JOIN airports_data as da ON f.departure_airport = da.airport_code
                    WHERE aa.timezone = da.timezone;
"""
#  count
# --------
#  16824
