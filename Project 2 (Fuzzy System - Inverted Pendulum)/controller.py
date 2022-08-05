# -*- coding: utf-8 -*-

# python imports
from math import degrees

# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader


class FuzzyController:

    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)

    def _make_input(self, world):
        return dict(
            cp=world.x,
            cv=world.v,
            pa=degrees(world.theta),
            pv=degrees(world.omega)
        )

    def _make_output(self):
        return dict(
            force=0.
        )

    def integral(self, a, b, start, end):
        return pow(end, 3) * (float(a) / 3) + pow(end, 2) * (float(b) / 2) - (
                    pow(start, 3) * (float(a) / 3) + pow(start, 2) * (float(b) / 2))

    def second_integral(self, a, b, start, end):
        return pow(end, 2) * (float(a) / 2) + pow(end, 1) * (b) - (pow(start, 2) * (float(a) / 2) + pow(start, 1) * (b))

    def cp_left_far(self, x):
        if -10 <= x <= -5:
            return -x / 5 - 1
        else:
            return 0

    def cp_left_near(self, x):
        if -10 <= x <= -2.5:
            return 2*x / 15 + 4 / 3
        elif -2.5 <= x <= 0:
            return (-2*x / 5)
        else:
            return 0

    def cp_stop(self, x):
        if -2.5 <= x <= -0:
            return 2*x / 5 + 1
        elif 0 <= x <= 2.5:
            return (-2*x / 5) + 1
        else:
            return 0

    def cp_right_near(self, x):
        if 0 <= x <= 2.5:
            return 2*x / 5
        elif 2.5 <= x <= 10:
            return (-2*x / 15) + 4 / 3
        else:
            return 0

    def cp_right_far(self, x):
        if 5 <= x <= 10:
            return x / 5 - 1
        else:
            return 0

    def cv_left_fast(self, x):
        if -5 <= x <= -2.5:
            return -2*x / 5 - 1
        else:
            return 0

    def cv_left_slow(self, x):
        if -5 <= x <= -1:
            return x / 4 + 5 / 4
        elif -1 <= x <= 0:
            return -x
        else:
            return 0

    def cv_stop(self, x):
        if -1 <= x <= 0:
            return x + 1
        elif 0 <= x <= 1:
            return -x + 1
        else:
            return 0

    def cv_right_slow(self, x):
        if 0 <= x <= 1:
            return x
        elif 1 <= x <= 5:
            return (-x / 4) + 5 / 4
        else:
            return 0

    def cv_right_fast(self, x):
        if 2.5 <= x <= 5:
            return 2*x / 5 - 1
        else:
            return 0

    def pa_up_more_right(self, x):
        if 0 <= x <= 30:
            return x / 30
        elif 30 <= x <= 60:
            return (-x / 30) + 2
        else:
            return 0

    def pa_up_right(self, x):
        if 30 <= x <= 60:
            return x / 30 - 1
        elif 60 <= x <= 90:
            return (-x / 30) + 3
        else:
            return 0

    def pa_up(self, x):
        if 60 <= x <= 90:
            return x / 30 - 2
        elif 90 <= x <= 120:
            return (-x / 30) + 4
        else:
            return 0

    def pa_up_left(self, x):
        if 90 <= x <= 120:
            return x / 30 - 3
        elif 120 <= x <= 150:
            return (-x / 30) + 5
        else:
            return 0

    def pa_up_more_left(self, x):
        if 120 <= x <= 150:
            return x / 30 - 4
        elif 150 <= x <= 180:
            return (-x / 30) + 6
        else:
            return 0

    def pa_down_more_left(self, x):
        if 180 <= x <= 210:
            return x / 30 - 6
        elif 210 <= x <= 240:
            return (-x / 30) + 8
        else:
            return 0

    def pa_down_left(self, x):
        if 210 <= x <= 240:
            return x / 30 - 7
        elif 240 <= x <= 270:
            return (-x / 30) + 9
        else:
            return 0

    def pa_down(self, x):
        if 240 <= x <= 270:
            return x / 30 - 8
        elif 270 <= x <= 300:
            return (-x / 30) + 10
        else:
            return 0

    def pa_down_right(self, x):
        if 270 <= x <= 300:
            return x / 30 - 9
        elif 300 <= x <= 330:
            return (-x / 30) + 11
        else:
            return 0

    def pa_down_more_right(self, x):
        if 300 <= x <= 330:
            return x / 30 - 10
        elif 330 <= x <= 360:
            return (-x / 30) + 12
        else:
            return 0

    def pv_cw_fast(self, x):
        if -200 <= x <= -100:
            return (-x / 100) - 1
        else:
            return 0

    def pv_cw_slow(self, x):
        if -200 <= x <= -100:
            return (x / 100) + 2
        elif -100 <= x <= 0:
            return (-x / 100)
        else:
            return 0

    def pv_stop(self, x):
        if -100 <= x <= 0:
            return (x / 100) + 1
        elif 0 <= x <= 100:
            return (-x / 100) + 1
        else:
            return 0

    def pv_ccw_slow(self, x):
        if 0 <= x <= 100:
            return (x / 100)
        elif 100 <= x <= 200:
            return (-x / 100) + 2
        else:
            return 0

    def pv_ccw_fast(self, x):
        if 100 <= x <= 200:
            return (x / 100) - 1
        else:
            return 0

    def force_left_fast(self, x):
        if -100 <= x <= -80:
            return (x / 20) + 5
        elif -80 <= x <= -60:
            return (-x / 20) - 3
        else:
            return 0

    def force_left_slow(self, x):
        if -80 <= x <= -60:
            return (x / 20) + 4
        elif -60 <= x <= 0:
            return (-x / 60)
        else:
            return 0

    def force_stop(self, x):
        if -60 <= x <= 0:
            return (x / 60) + 1
        elif 0 <= x <= 60:
            return (-x / 60) + 1
        else:
            return 0

    def force_right_slow(self, x):
        if 0 <= x <= 60:
            return (x / 60)
        elif 60 <= x <= 80:
            return (-x / 20) + 4
        else:
            return 0

    def force_right_fast(self, x):
        if 60 <= x <= 80:
            return (x / 20) - 3
        elif 80 <= x <= 100:
            return (-x / 20) + 5
        else:
            return 0

    def cal_force(self, pa, pv, cp, cv):
        left_fast = []
        left_slow = []
        stop = []
        right_slow = []
        right_fast = []

        if pv > 200:
            pv = 200
        if pv < -200:
            pv = -200

        stop.append(max(min(self.pa_up(x=pa), self.pv_stop(x=pv)), min(self.pa_up_right(x=pa), self.pv_ccw_slow(x=pv)),
                        min(self.pa_up_left(x=pa), self.pv_cw_slow(x=pv))))

        with open('./rules.txt', 'r') as file:
            for line in file:
                pa_name = line.split(" ")[5][:-1]
                pv_name = line.split(" ")[9][:-1]
                force_name = line.split(" ")[13].strip()

                pa_value = 0
                pv_value = 0

                if pa_name == "up_more_right":
                    pa_value = self.pa_up_more_right(x=pa)
                if pa_name == "up_right":
                    pa_value = self.pa_up_right(x=pa)
                if pa_name == "up":
                    pa_value = self.pa_up(x=pa)
                if pa_name == "up_left":
                    pa_value = self.pa_up_left(x=pa)
                if pa_name == "up_more_left":
                    pa_value = self.pa_up_more_left(x=pa)
                if pa_name == "down_more_left":
                    pa_value = self.pa_down_more_left(x=pa)
                if pa_name == "down_left":
                    pa_value = self.pa_down_left(x=pa)
                if pa_name == "down":
                    pa_value = self.pa_down(x=pa)
                if pa_name == "down_right":
                    pa_value = self.pa_down_right(x=pa)
                if pa_name == "down_more_right":
                    pa_value = self.pa_down_more_right(x=pa)

                if pv_name == "cw_fast":
                    pv_value = self.pv_cw_fast(x=pv)
                if pv_name == "cw_slow":
                    pv_value = self.pv_cw_slow(x=pv)
                if pv_name == "stop":
                    pv_value = self.pv_stop(x=pv)
                if pv_name == "ccw_slow":
                    pv_value = self.pv_ccw_slow(x=pv)
                if pv_name == "ccw_fast":
                    pv_value = self.pv_ccw_fast(x=pv)

                min_value = min(pa_value, pv_value)

                if min_value != 0:
                    if force_name == "left_fast":
                        left_fast.append(min_value)
                    if force_name == "left_slow":
                        left_slow.append(min_value)
                    if force_name == "stop":
                        stop.append(min_value)
                    if force_name == "right_slow":
                        right_slow.append(min_value)
                    if force_name == "right_fast":
                        right_fast.append(min_value)

        with open('./rules2.txt', 'r') as file:
            for line in file:
                cp_name = line.split(" ")[5][:-1]
                cv_name = line.split(" ")[9][:-1]
                force_name = line.split(" ")[13].strip()

                cp_value = 0
                cv_value = 0

                if cp_name == "left_far":
                    cp_value = self.cp_left_far(x=cp)
                if cp_name == "left_near":
                    cp_value = self.cp_left_near(x=cp)
                if cp_name == "stop":
                    cp_value = self.cp_stop(x=cp)
                if cp_name == "right_near":
                    cp_value = self.cp_right_near(x=cp)
                if cp_name == "right_far":
                    cp_value = self.cp_right_far(x=cp)

                if cv_name == "left_fast":
                    cv_value = self.cv_left_fast(x=cv)
                if cv_name == "left_slow":
                    cv_value = self.cv_left_slow(x=cv)
                if cv_name == "stop":
                    cv_value = self.cv_stop(x=cv)
                if cv_name == "right_slow":
                    cv_value = self.cv_right_slow(x=cv)
                if cv_name == "right_fast":
                    cv_value = self.cv_right_fast(x=cv)

                min_value = min(cp_value, cv_value)

                if min_value != 0:
                    if force_name == "left_fast":
                        left_fast.append(min_value)
                    if force_name == "left_slow":
                        left_slow.append(min_value)
                    if force_name == "stop":
                        stop.append(min_value)
                    if force_name == "right_slow":
                        right_slow.append(min_value)
                    if force_name == "right_fast":
                        right_fast.append(min_value)

        if left_fast:
            left_fast = max(left_fast)
        else:
            left_fast = 0

        if left_slow:
            left_slow = max(left_slow)
        else:
            left_slow = 0

        if stop:
            stop = max(stop)
        else:
            stop = 0

        if right_slow:
            right_slow = max(right_slow)
        else:
            right_slow = 0

        if right_fast:
            right_fast = max(right_fast)
        else:
            right_fast = 0

        if right_fast > 0.99:
            right_fast = 1

        # left_fast = 0.8
        # left_slow = 0.1
        # stop = 0
        # right_slow = 0
        # right_fast = 0

        sum1 = 0
        sum2 = 0

        left_slow_smaller_than_left_fast = True
        stop_smaller_than_left_slow = True
        right_slow_smaller_than_stop = True
        right_fast_smaller_than_right_slow = True

        if left_fast > 0:
            middle = True
            if left_fast == 1:
                sum1 += self.integral(a=0.05, b=5, start=-100, end=-80)
                sum2 += self.second_integral(a=0.05, b=5, start=-100, end=-80)
                middle = False
            else:
                end = (left_fast - 5) * 20
                sum1 += self.integral(a=0.05, b=5, start=-100, end=end)
                sum2 += self.second_integral(a=0.05, b=5, start=-100, end=end)

            if middle:
                start = (left_fast - 5) * 20
                if left_fast >= left_slow:
                    end = -20 * (left_fast + 3)
                else:
                    left_slow_smaller_than_left_fast = False
                    if left_fast >= 0.5:
                        end = -20 * (left_fast + 3)
                    else:
                        end = 20 * (left_fast - 4)
                sum1 += self.integral(a=0, b=left_fast, start=start, end=end)
                sum2 += self.second_integral(a=0, b=left_fast, start=start, end=end)

            if not middle:
                if left_slow == 0:
                    sum1 += self.integral(a=-0.05, b=-3, start=-80, end=-60)
                    sum2 += self.second_integral(a=-0.05, b=-3, start=-80, end=-60)
                elif left_slow >= 0.5:
                    sum1 += self.integral(a=-0.05, b=-3, start=-80, end=-70)
                    sum2 += self.second_integral(a=-0.05, b=-3, start=-80, end=-70)
                else:
                    end = -20 * (left_slow + 3)
                    sum1 += self.integral(a=-0.05, b=-3, start=-80, end=end)
                    sum2 += self.second_integral(a=-0.05, b=-3, start=-80, end=end)

            if middle:
                if left_slow == 0:
                    start = -20 * (left_fast + 3)
                    sum1 += self.integral(a=-0.05, b=-3, start=start, end=-60)
                    sum2 += self.second_integral(a=-0.05, b=-3, start=start, end=-60)
                elif left_fast >= 0.5 and left_slow >= 0.5:
                    left_slow_smaller_than_left_fast = False
                    start = -20 * (left_fast + 3)
                    sum1 += self.integral(a=-0.05, b=-3, start=start, end=-70)
                    sum2 += self.second_integral(a=-0.05, b=-3, start=start, end=-70)
                elif left_fast >= left_slow:
                    start = -20 * (left_fast + 3)
                    end = -20 * (left_slow + 3)
                    sum1 += self.integral(a=-0.05, b=-3, start=start, end=end)
                    sum2 += self.second_integral(a=-0.05, b=-3, start=start, end=end)

        if left_slow > 0:
            middle = True
            if not left_slow_smaller_than_left_fast or left_fast == 0:
                if left_slow == 1 and left_fast >= 0.5:
                    sum1 += self.integral(a=0.05, b=4, start=-70, end=-60)
                    sum2 += self.second_integral(a=0.05, b=4, start=-70, end=-60)
                    middle = False
                elif left_slow == 1 and left_fast < 0.5:
                    start = 20 * (left_fast - 4)
                    sum1 += self.integral(a=0.05, b=4, start=start, end=-60)
                    sum2 += self.second_integral(a=0.05, b=4, start=start, end=-60)
                    middle = False
                else:
                    start = 20 * (left_fast - 4)
                    end = 20 * (left_slow - 4)
                    sum1 += self.integral(a=0.05, b=4, start=start, end=end)
                    sum2 += self.second_integral(a=0.05, b=4, start=start, end=end)
            else:
                if left_slow == 1 and left_fast >= 0.5:
                    sum1 += self.integral(a=0.05, b=4, start=-70, end=-60)
                    sum2 += self.second_integral(a=0.05, b=4, start=-70, end=-60)
                    middle = False
                elif left_slow == 1 and left_fast < 0.5:
                    start = -70
                    sum1 += self.integral(a=0.05, b=4, start=start, end=-60)
                    sum2 += self.second_integral(a=0.05, b=4, start=start, end=-60)
                    middle = False
                elif left_slow >= 0.5:
                    start = -70
                    end = 20 * (left_slow - 4)
                    sum1 += self.integral(a=0.05, b=4, start=start, end=end)
                    sum2 += self.second_integral(a=0.05, b=4, start=start, end=end)

            if middle:
                start = (left_slow - 4) * 20
                if left_slow <= 0.5 and left_slow_smaller_than_left_fast and left_slow <= left_fast:
                    start = (left_slow + 3) * -20
                if left_slow >= stop:
                    end = -60 * left_slow
                else:
                    stop_smaller_than_left_slow = False
                    if left_slow >= 0.5:
                        end = -60 * left_slow
                    else:
                        end = 60 * (left_slow - 1)
                sum1 += self.integral(a=0, b=left_slow, start=start, end=end)
                sum2 += self.second_integral(a=0, b=left_slow, start=start, end=end)

            if not middle:
                if stop == 0:
                    sum1 += self.integral(a=-0.016, b=0, start=-60, end=0)
                    sum2 += self.second_integral(a=-0.016, b=0, start=-60, end=0)
                elif stop >= 0.5:
                    sum1 += self.integral(a=-0.016, b=0, start=-60, end=-30)
                    sum2 += self.second_integral(a=-0.016, b=0, start=-60, end=-30)
                else:
                    end = -60 * stop
                    sum1 += self.integral(a=-0.016, b=0, start=-60, end=end)
                    sum2 += self.second_integral(a=-0.016, b=0, start=-60, end=end)

            if middle:
                if stop == 0:
                    start = -60 * left_slow
                    sum1 += self.integral(a=-0.016, b=0, start=start, end=0)
                    sum2 += self.second_integral(a=-0.016, b=0, start=start, end=0)
                elif left_slow >= 0.5 and stop >= 0.5:
                    stop_smaller_than_left_slow = False
                    start = -60 * left_slow
                    sum1 += self.integral(a=-0.016, b=0, start=start, end=-30)
                    sum2 += self.second_integral(a=-0.016, b=0, start=start, end=-30)
                elif left_slow >= stop:
                    start = -60 * left_slow
                    end = -60 * stop
                    sum1 += self.integral(a=-0.016, b=0, start=start, end=end)
                    sum2 += self.second_integral(a=-0.016, b=0, start=start, end=end)

        if stop > 0:
            middle = True
            if not stop_smaller_than_left_slow or left_slow == 0:
                if stop == 1 and left_slow >= 0.5:
                    sum1 += self.integral(a=0.016, b=1, start=-30, end=0)
                    sum2 += self.second_integral(a=0.016, b=1, start=-30, end=0)
                    middle = False
                elif stop == 1 and left_slow < 0.5:
                    start = 60 * (left_slow - 1)
                    sum1 += self.integral(a=0.016, b=1, start=start, end=0)
                    sum2 += self.second_integral(a=0.016, b=1, start=start, end=0)
                    middle = False
                else:
                    start = 60 * (left_slow - 1)
                    end = 60 * (stop - 1)
                    sum1 += self.integral(a=0.016, b=1, start=start, end=end)
                    sum2 += self.second_integral(a=0.016, b=1, start=start, end=end)
            else:
                if stop == 1 and left_slow >= 0.5:
                    sum1 += self.integral(a=0.016, b=1, start=-30, end=0)
                    sum2 += self.second_integral(a=0.016, b=1, start=-30, end=0)
                    middle = False
                elif stop == 1 and left_slow < 0.5:
                    start = -30
                    sum1 += self.integral(a=0.016, b=1, start=start, end=0)
                    sum2 += self.second_integral(a=0.016, b=1, start=start, end=0)
                    middle = False
                elif stop >= 0.5:
                    start = -30
                    end = 60 * (stop - 1)
                    sum1 += self.integral(a=0.016, b=1, start=start, end=end)
                    sum2 += self.second_integral(a=0.016, b=1, start=start, end=end)

            if middle:
                start = (stop - 1) * 60
                if stop <= 0.5 and stop_smaller_than_left_slow and stop <= left_slow:
                    start = (stop + 0) * -60
                if stop >= right_slow:
                    end = -60 * (stop - 1)
                else:
                    right_slow_smaller_than_stop = False
                    if stop >= 0.5:
                        end = -60 * (stop - 1)
                    else:
                        end = 60 * stop
                sum1 += self.integral(a=0, b=stop, start=start, end=end)
                sum2 += self.second_integral(a=0, b=stop, start=start, end=end)

            if not middle:
                if right_slow == 0:
                    sum1 += self.integral(a=-0.016, b=1, start=0, end=60)
                    sum2 += self.second_integral(a=-0.016, b=1, start=0, end=60)
                elif right_slow >= 0.5:
                    sum1 += self.integral(a=-0.016, b=1, start=0, end=30)
                    sum2 += self.second_integral(a=-0.016, b=1, start=0, end=30)
                else:
                    end = -60 * (right_slow - 1)
                    sum1 += self.integral(a=-0.016, b=1, start=0, end=end)
                    sum2 += self.second_integral(a=-0.016, b=1, start=0, end=end)

            if middle:
                if right_slow == 0:
                    start = -60 * (stop - 1)
                    sum1 += self.integral(a=-0.016, b=1, start=start, end=60)
                    sum2 += self.second_integral(a=-0.016, b=1, start=start, end=60)
                elif stop >= 0.5 and right_slow >= 0.5:
                    right_slow_smaller_than_stop = False
                    start = -60 * (stop - 1)
                    sum1 += self.integral(a=-0.016, b=1, start=start, end=30)
                    sum2 += self.second_integral(a=-0.016, b=1, start=start, end=30)
                elif stop >= right_slow:
                    start = -60 * (stop - 1)
                    end = -60 * (right_slow - 1)
                    sum1 += self.integral(a=-0.016, b=1, start=start, end=end)
                    sum2 += self.second_integral(a=-0.016, b=1, start=start, end=end)

        if right_slow > 0:
            middle = True
            if not right_slow_smaller_than_stop or stop == 0:
                if right_slow == 1 and stop >= 0.5:
                    sum1 += self.integral(a=0.016, b=0, start=30, end=60)
                    sum2 += self.second_integral(a=0.016, b=0, start=30, end=60)
                    middle = False
                elif right_slow == 1 and stop < 0.5:
                    start = 60 * stop
                    sum1 += self.integral(a=0.016, b=0, start=start, end=60)
                    sum2 += self.second_integral(a=0.016, b=0, start=start, end=60)
                    middle = False
                else:
                    start = 60 * stop
                    end = 60 * right_slow
                    sum1 += self.integral(a=0.016, b=0, start=start, end=end)
                    sum2 += self.second_integral(a=0.016, b=0, start=start, end=end)
            else:
                if right_slow == 1 and stop >= 0.5:
                    sum1 += self.integral(a=0.016, b=0, start=30, end=60)
                    sum2 += self.second_integral(a=0.016, b=0, start=30, end=60)
                    middle = False
                elif right_slow == 1 and stop < 0.5:
                    start = 30
                    sum1 += self.integral(a=0.016, b=0, start=start, end=60)
                    sum2 += self.second_integral(a=0.016, b=0, start=start, end=60)
                    middle = False
                elif right_slow >= 0.5:
                    start = 30
                    end = 60 * right_slow
                    sum1 += self.integral(a=0.016, b=0, start=start, end=end)
                    sum2 += self.second_integral(a=0.016, b=0, start=start, end=end)

            if middle:
                start = (right_slow - 0) * 60
                if right_slow <= 0.5 and right_slow_smaller_than_stop and right_slow <= stop:
                    start = (right_slow - 1) * -60
                if right_slow >= right_fast:
                    end = -20 * (right_slow - 4)
                else:
                    right_fast_smaller_than_right_slow = False
                    if right_slow >= 0.5:
                        end = -20 * (right_slow - 4)
                    else:
                        end = 20 * (right_slow + 3)
                sum1 += self.integral(a=0, b=right_slow, start=start, end=end)
                sum2 += self.second_integral(a=0, b=right_slow, start=start, end=end)

            if not middle:
                if right_fast == 0:
                    sum1 += self.integral(a=-0.05, b=4, start=60, end=80)
                    sum2 += self.second_integral(a=-0.05, b=4, start=60, end=80)
                elif right_fast >= 0.5:
                    sum1 += self.integral(a=-0.05, b=4, start=60, end=70)
                    sum2 += self.second_integral(a=-0.05, b=4, start=60, end=70)
                else:
                    end = -20 * (right_fast - 4)
                    sum1 += self.integral(a=-0.05, b=4, start=60, end=end)
                    sum2 += self.second_integral(a=-0.05, b=4, start=60, end=end)

            if middle:
                if right_fast == 0:
                    start = -20 * (right_slow - 4)
                    sum1 += self.integral(a=-0.05, b=4, start=start, end=80)
                    sum2 += self.second_integral(a=-0.05, b=4, start=start, end=80)
                elif right_slow >= 0.5 and right_fast >= 0.5:
                    right_fast_smaller_than_right_slow = False
                    start = -20 * (right_slow - 4)
                    sum1 += self.integral(a=-0.05, b=4, start=start, end=70)
                    sum2 += self.second_integral(a=-0.05, b=4, start=start, end=70)
                elif right_slow >= right_fast:
                    start = -20 * (right_slow - 4)
                    end = -20 * (right_fast - 4)
                    sum1 += self.integral(a=-0.05, b=4, start=start, end=end)
                    sum2 += self.second_integral(a=-0.05, b=4, start=start, end=end)

        if right_fast > 0:
            middle = True
            if not right_fast_smaller_than_right_slow or right_slow == 0:
                if right_fast == float(1) and right_slow >= 0.5:
                    sum1 += self.integral(a=0.05, b=-3, start=70, end=80)
                    sum2 += self.second_integral(a=0.05, b=-3, start=70, end=80)
                    middle = False
                elif right_fast == 1.0 and right_slow < 0.5:
                    start = 20 * (right_slow + 3)
                    sum1 += self.integral(a=0.05, b=-3, start=start, end=80)
                    sum2 += self.second_integral(a=0.05, b=-3, start=start, end=80)
                    middle = False
                else:
                    start = 20 * (right_slow + 3)
                    end = 20 * (right_fast + 3)
                    sum1 += self.integral(a=0.05, b=-3, start=start, end=end)
                    sum2 += self.second_integral(a=0.05, b=-3, start=start, end=end)
            else:
                if right_fast == 1 and right_slow >= 0.5:
                    sum1 += self.integral(a=0.05, b=-3, start=70, end=80)
                    sum2 += self.second_integral(a=0.05, b=-3, start=70, end=80)
                    middle = False
                elif right_fast == 1 and right_slow < 0.5:
                    start = 70
                    sum1 += self.integral(a=0.05, b=-3, start=start, end=80)
                    sum2 += self.second_integral(a=0.05, b=-3, start=start, end=80)
                    middle = False
                elif right_fast >= 0.5:
                    start = 70
                    end = 20 * (right_fast + 3)
                    sum1 += self.integral(a=0.05, b=-3, start=start, end=end)
                    sum2 += self.second_integral(a=0.05, b=-3, start=start, end=end)

            if middle:
                end = -20 * (right_fast - 5)
                start = (right_fast + 3) * 20
                if right_fast <= 0.5 and right_fast_smaller_than_right_slow and right_fast <= right_slow:
                    start = (right_fast - 4) * -20
                sum1 += self.integral(a=0, b=right_fast, start=start, end=end)
                sum2 += self.second_integral(a=0, b=right_fast, start=start, end=end)

            if not middle:
                sum1 += self.integral(a=-0.05, b=5, start=80, end=100)
                sum2 += self.second_integral(a=-0.05, b=5, start=80, end=100)

            if middle:
                start = -20 * (right_slow - 5)
                sum1 += self.integral(a=-0.05, b=5, start=start, end=100)
                sum2 += self.second_integral(a=-0.05, b=5, start=start, end=100)

        if sum2 != 0:
            return float(sum1 / sum2)
        else:
            return 0

        # sum1 = 0
        # sum2 = 0
        # sum2 += left_fast + left_slow + stop + right_slow + right_fast
        # sum1 += left_fast * -80 + left_slow * -40 + right_slow * 40 + right_fast * 80
        #
        # if sum2 != 0:
        #     return sum1 / sum2
        # else:
        #     return 80

    def decide(self, world):
        # output = self._make_output()
        # self.system.calculate(self._make_input(world), output)
        # return output['force']
        input = self._make_input(world)
        force = self.cal_force(pa=input['pa'], pv=input['pv'], cp=input['cp'] , cv=input['cv'])
        return force
