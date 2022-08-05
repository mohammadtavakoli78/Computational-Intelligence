class Inference:
    def inferred(self, fuzzification_temp, fuzzification_hum, fuzzyfication_rule):
        agenda = []
        possibility = []

        for dt in fuzzification_temp:
            agenda.append(dt)
        for dt in fuzzification_hum:
            agenda.append(dt)

        while agenda:
            item = agenda.pop(0)
            for rule in fuzzyfication_rule:
                for j, premise in enumerate(rule[0]):
                    if premise == item[0]:
                        rule[0][j] = [True, rule[0][j], item[1]]
                if self.check_hypothesis(rule[0]):
                    conclusion = rule[1]
                    possibility.append(rule)
                    agenda.append(conclusion)
                    rule[0] = [rule[0], 'processed']

        return possibility

    def check_hypothesis(self, hypothesis):
        for entry in hypothesis:
            if entry[0] != True:
                return False
        return True