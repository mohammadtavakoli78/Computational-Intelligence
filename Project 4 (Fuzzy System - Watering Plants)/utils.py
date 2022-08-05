import sys


class Utils:
    def get_input(self):
        print('Input Of Fuzzyfication')
        print('Please input temperature value (celcius) : ', end='', flush=True)
        temperature = int(sys.stdin.readline())

        print('Please input percentage humidity (%) : ', end='', flush=True)
        humidity = int(sys.stdin.readline())

        rules = self.parse_kb_file('rules.ru')

        return temperature, humidity, rules

    def split_and_build_literals(self, line):
        rules = []
        # Split the line of literals
        literals = line.split(' ')
        hypothesis = []
        while len(literals) > 1:
            hypothesis.append(literals.pop(0))
        rules.append(hypothesis)
        rules.append(literals.pop(0))
        return rules

    def parse_kb_file(self, filename):
        kb_file = open(filename, 'r')  # 'rU' is smart about line-endings
        kb_rules = []  # to hold the list of rules

        for line in kb_file:  # read the non-commented lines
            if not line.startswith('#') and line != '\n':
                kb_rules.append(self.split_and_build_literals(line.strip()))

        kb_file.close()
        return kb_rules
