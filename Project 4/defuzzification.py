class Defuzzify:
    def defuzzyfication(self, input):
        result = float(0)

        x1_short = 0
        x2_short = 28
        coefisien_short = float(0)

        x1_medium = 20
        x2_medium = 48
        coefisien_medium = float(0)

        x1_long = 40
        x2_long = 90
        coefisien_long = float(0)

        _short_numerator = float(0)  # pembilang
        _medium_numerator = float(0)  # pembilang
        _long_numerator = float(0)  # pembilang

        _short_denominator = float(0)  # penyebut
        _medium_denominator = float(0)  # penyebut
        _long_denominator = float(0)  # penyebut

        for data in input:
            if data[0] == 'Short':
                coefisien_short = data[1]
            if data[0] == 'Medium':
                coefisien_medium = data[1]
            if data[0] == 'Long':
                coefisien_long = data[1]

        if coefisien_short != float(0) and coefisien_medium != float(0) and coefisien_long == float(0):
            x_start_short = x1_short
            x_end_short = x1_medium + 1

            x_start_medium = x2_short
            x_end_medium = x1_long + 1

            for i in range(x_start_short, x_end_short):
                _short_numerator += i * coefisien_short
                _short_denominator += coefisien_short

            for i in range(x_start_medium, x_end_medium):
                _medium_numerator += i * coefisien_medium
                _medium_denominator += coefisien_medium

            result = (_medium_numerator + _short_numerator) / (_medium_denominator + _short_denominator)

        if coefisien_short == float(0) and coefisien_medium != float(0) and coefisien_long != float(0):

            x_start_medium = x2_short
            x_end_medium = x1_long + 1

            x_start_long = x2_medium
            x_end_long = x2_long + 1

            for i in range(x_start_medium, x_end_medium):
                _medium_numerator += i * coefisien_medium
                _medium_denominator += coefisien_medium

            for i in range(x_start_long, x_end_long):
                _long_numerator += i * coefisien_long
                _long_denominator += coefisien_long

            result = (_medium_numerator + _long_numerator) / (_medium_denominator + _long_denominator)

        if coefisien_short != float(0) and coefisien_medium != float(0) and coefisien_long != float(0):

            x_start_short = x1_short
            x_end_short = x1_medium + 1

            x_start_medium = x2_short
            x_end_medium = x1_long + 1

            x_start_long = x2_medium
            x_end_long = x2_long + 1

            for i in range(x_start_short, x_end_short):
                _short_numerator += i * coefisien_short
                _short_denominator += coefisien_short

            for i in range(x_start_medium, x_end_medium):
                _medium_numerator += i * coefisien_medium
                _medium_denominator += coefisien_medium

            for i in range(x_start_long, x_end_long):
                _long_numerator += i * coefisien_long
                _long_denominator += coefisien_long

            result = (_short_numerator + _medium_numerator + _long_numerator) / (
                    _short_numerator + _medium_denominator + _long_denominator)

        if coefisien_short != float(0) and coefisien_medium == float(0) and coefisien_long == float(0):
            x_start_short = x1_short
            x_end_short = x1_medium + 1

            for i in range(x_start_short, x_end_short):
                _short_numerator += i * coefisien_short
                _short_denominator += coefisien_short

            result = _short_numerator / _short_denominator

        if coefisien_short == float(0) and coefisien_medium != float(0) and coefisien_long == float(0):
            x_start_medium = x2_short
            x_end_medium = x1_long + 1

            for i in range(x_start_medium, x_end_medium):
                _medium_numerator += i * coefisien_medium
                _medium_denominator += coefisien_medium

            result = _medium_numerator / _medium_denominator

        if coefisien_short == float(0) and coefisien_medium == float(0) and coefisien_long != float(0):
            x_start_long = x2_medium
            x_end_long = x2_long + 1

            for i in range(x_start_long, x_end_long):
                _long_numerator += i * coefisien_long
                _long_denominator += coefisien_long

            result = _long_numerator / _long_denominator

        return result