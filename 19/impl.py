from math import floor
import datetime

def split_date_string(date_string):
    parts = date_string.split(' ')
    year, month, day = parts[0], parts[1], parts[2]
    return int(year), int(month), int(day)

def convert_to_epoch(year, month, day):
    return datetime.date(year,month,day)

class Solution_Math:
    DAY_IN_SECONDS = 86400
    def __init__(self, date_one, date_two):
        self.y1, self.m1, self.d1 = split_date_string(date_one)
        self.y2, self.m2, self.d2 = split_date_string(date_two)
        self.epoch1 = int((convert_to_epoch(self.y1, self.m1, self.d1)).strftime('%s'))
        self.epoch2 = int((convert_to_epoch(self.y2, self.m2, self.d2)).strftime('%s'))
        self.wd1N, self.wd1 = self.calculate_week_day(self.y1, self.m1, self.d1)
        self.wd2N, self.wd2 = self.calculate_week_day(self.y2, self.m2, self.d2)
        self.days_diff = abs(self.epoch1 - self.epoch2) // Solution_Math.DAY_IN_SECONDS
        self.sundays_on_the_first = list(self.calculate_sundays())

    def get_sundays_on_the_first_count(self):
        return len(self.sundays_on_the_first)

    def calculate_sundays(self):
        # get base sunday of starting week
        base_sunday_starting_week_epoch = self.epoch1 - (self.wd1N * Solution_Math.DAY_IN_SECONDS)
        if base_sunday_starting_week_epoch == self.epoch1 and datetime.datetime.fromtimestamp(self.epoch1).day == 1:
            yield self.epoch1
        else:
            next_sunday = base_sunday_starting_week_epoch + (Solution_Math.DAY_IN_SECONDS * 7)
            while next_sunday <= self.epoch2:
                if datetime.datetime.fromtimestamp(next_sunday).day == 1:
                    yield next_sunday
                next_sunday += Solution_Math.DAY_IN_SECONDS * 7

    def calculate_week_day(self, year, month, day):
        # Zeller's congruence
        q = day
        m = [-1,13,14,3,4,5,6,7,8,9,10,11,12][month]
        K = year % 100
        J = year // 100
        h = (q + floor((13 * (m+1))/5) + K + floor(K/4) + floor(J/4) - (5 * J)) % 7
        return h, ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][h]

    def __str__(self):
        return 'Start Date: YYYY={0},MM={1},DD={2},WD={3}-{4},Epoch={10}\nEnd Date: YYYY={5},MM={6},DD={7},WD={8}-{9},Epoch={11}\nDays Difference={12}\nSundays Count={13}'.format(self.y1, self.m1, self.d1, self.wd1N, self.wd1, self.y2, self.m2, self.d2, self.wd2N, self.wd2, self.epoch1, self.epoch2, self.days_diff, self.get_sundays_on_the_first_count())

t = int(input().strip())
for _ in range(t):
    date_one = input().strip()
    date_two = input().strip()
    
    solution_math = Solution_Math(date_one, date_two)
    print(solution_math.get_sundays_on_the_first_count())
