from utils import Utils
from defuzzification import Defuzzify
from fuzzification import Fuzzification
from inference import Inference


def main():
    utils = Utils()
    temperature, humidity, rules = utils.get_input()

    defuzzyfy = Defuzzify()
    fuzzyfy = Fuzzification()
    inference = Inference()

    tmp = fuzzyfy.temperatureFunction(temperature)
    hum = fuzzyfy.humidityFunction(humidity)

    print('\n\nOutput Of Fuzzyfication')
    print(tmp)
    print(hum)
    print('')

    inf = inference.inferred(tmp, hum, rules)  # inference Process

    result_rule_min = []

    for dt in inf:
        print(dt[0][0][0][1], dt[0][0][0][2], dt[0][0][1][1], dt[0][0][1][2], dt[1])
        minimum = min(dt[0][0][0][2], dt[0][0][1][2])
        result_rule_min.append([dt[1], minimum])
    print('')

    print(result_rule_min)

    result_rule_max = {}
    for data in result_rule_min:
        if data[0] in result_rule_max:
            result_rule_max[data[0]].add(data[1])
        else:
            result_rule_max[data[0]] = set([data[1]])

    output_inference = []
    for key, value in result_rule_max.items():
        output_inference.append([key, max(value)])

    print('')
    print('Output Inference is', output_inference)
    print('')

    print('Deffuzzyfication')
    finalValue = defuzzyfy.defuzzyfication(output_inference)

    print('Minutes', finalValue)


if __name__ == '__main__':
    main()
