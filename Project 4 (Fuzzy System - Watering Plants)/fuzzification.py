from config import temperature_fuzzy_set, humidity_fuzzy_set, sprinkler_duration_fuzzy_set


class Fuzzification:
    def temperatureFunction(self, input):
        linguistik_temperature = []
        if -10 <= input <= 3:
            linguistik_temperature.append(temperature_fuzzy_set[0])  # Cold
        if 0 <= input <= 15:
            linguistik_temperature.append(temperature_fuzzy_set[1])  # Cool
        if 12 <= input <= 27:
            linguistik_temperature.append(temperature_fuzzy_set[2])  # Normal
        if 24 <= input <= 39:
            linguistik_temperature.append(temperature_fuzzy_set[3])  # Warm
        if 36 <= input <= 50:
            linguistik_temperature.append(temperature_fuzzy_set[4])  # Hot

        value_temp = []

        if len(linguistik_temperature) > 1:
            if linguistik_temperature[0] == temperature_fuzzy_set[0] and linguistik_temperature[1] == \
                    temperature_fuzzy_set[
                        1]:  # Between Cold and Cool
                # Cold
                cold = -(input - 3) / (3 - 0)
                value_temp.append([linguistik_temperature[0], cold])
                # Cool
                cool = (input - 0) / (3 - 0)
                value_temp.append([linguistik_temperature[1], cool])
            elif linguistik_temperature[0] == temperature_fuzzy_set[1] and linguistik_temperature[1] == \
                    temperature_fuzzy_set[2]:  # Between Cool and Normal
                # Cool
                cool = -(input - 15) / (15 - 12)
                value_temp.append([linguistik_temperature[0], cool])
                # Normal
                normal = (input - 12) / (15 - 12)
                value_temp.append([linguistik_temperature[1], normal])
            elif linguistik_temperature[0] == temperature_fuzzy_set[2] and linguistik_temperature[1] == \
                    temperature_fuzzy_set[3]:  # Between Normal and Warm
                # Normal
                normal = -(input - 27) / (27 - 24)
                value_temp.append([linguistik_temperature[0], normal])
                # Warm
                warm = (input - 24) / (27 - 24)
                value_temp.append([linguistik_temperature[1], warm])
            elif linguistik_temperature[0] == temperature_fuzzy_set[3] and linguistik_temperature[1] == \
                    temperature_fuzzy_set[4]:  # Between Warm and Hot
                # Warm
                warm = -(input - 39) / (39 - 36)
                value_temp.append([linguistik_temperature[0], warm])
                # Hot
                hot = (input - 36) / (39 - 36)
                value_temp.append([linguistik_temperature[1], hot])
        else:
            value_temp.append([linguistik_temperature[0], 1])

        return value_temp

    def humidityFunction(self, input):
        linguistik_humidity = []
        if 0 <= input <= 20:
            linguistik_humidity.append(humidity_fuzzy_set[0])  # Dry
        if 10 <= input <= 50:
            linguistik_humidity.append(humidity_fuzzy_set[1])  # Moist
        if 40 <= input <= 70:
            linguistik_humidity.append(humidity_fuzzy_set[2])  # Wet

        value_hum = []
        if len(linguistik_humidity) > 1:
            if linguistik_humidity[0] == humidity_fuzzy_set[0] and linguistik_humidity[1] == humidity_fuzzy_set[
                1]:  # Between Dry and Moist
                # Dry
                dry = -(input - 20) / (20 - 10)
                value_hum.append([linguistik_humidity[0], dry])
                # Moist
                moist = (input - 10) / (20 - 10)
                value_hum.append([linguistik_humidity[1], moist])
            elif linguistik_humidity[0] == humidity_fuzzy_set[1] and linguistik_humidity[1] == humidity_fuzzy_set[
                2]:  # Between Moist and Wet
                # Moist
                moist = -(input - 50) / (50 - 40)
                value_hum.append([linguistik_humidity[0], moist])
                # Wet
                wet = (input - 40) / (50 - 40)
                value_hum.append([linguistik_humidity[1], wet])
        else:
            value_hum.append([linguistik_humidity[0], 1])

        return value_hum
