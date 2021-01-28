#!/usr/bin/python3

class Solver:
    def __init__(self, data):
        self.base_data = data
        self.rules = list()

        self.data_types = list(self.base_data.keys())
        n = len(self.data_types[0])
        self.permut = self.getPermutation(n)
        self.permut_idx = [0] * n

    def addRule(self, rule):
        new_rule = list()
        for subrule in rule:
            new_subrule = (subrule[0],
                           self.base_data[subrule[0]].index(subrule[1]),
                           subrule[2],
                           self.base_data[subrule[2]].index(subrule[3]))
            new_rule.append(new_subrule)
        self.rules.append(rule)

    def solve(self):
        res = False

        return res

    def _get_variant(self, indexes):
        variant = list()

        for idx in indexes:
            variant.append(self.permut[idx])

        return variant

    def _check_variant(self, variant):

        return False

    def getPermutation(n):

        def NextSet(a):
            j = n - 2
            while j != -1 and a[j] >= a[j + 1]:
                j -= 1
            if j == -1:
                return False #больше перестаново нет
            k = n - 1
            while a[j] >= a[k]:
                k -= 1
            a[k], a[j] = a[j], a[k]
            l = j + 1
            r = n - 1 # сортируем  оставшуюся часть последовательности
            while l < r:
                a[l], a[r] = a[r], a[l]#swap(a, l + +, r - -);
            return True

        a = list(range(0, n))
        res = list()
        while NextSet(a):
            res.append(a.copy())

        return res



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    base_data = {"gangs": ["Rocks", "Shelby", "Fix", "Yao", "Carleone"],
                 "areas": ["downtown", "busyness", "central park", "west getto", "east docks"],
                 "crimes": ["kidnapping", "smuggling", "guns", "fighting", "hijack"]}

    solver = Solver(base_data)

    # rule 2
    solver.addRule([["areas", "downtown", "crimes", "hijack"],
                     ["areas", "downtown", "crimes", "fighting"],
                     ["areas", "downtown", "crimes", "guns"]])

    print(solver.permut)

    """
    # rule 3
    solver.addRule(Rule([SubRule("areas", "busyness", "crimes", "smuggling"),
                       SubRule("areas", "busyness", "crimes", "guns")]))

    # rule 4
    solver.addRule(Rule([SubRule("gangs", "Rocks", "areas", "downtown"),
                       SubRule("gangs", "Rocks", "areas", "central park")]))

    # rule 5
    solver.addRule(Rule([SubRule("gangs", "Shelby", "areas", "fighting")]))

    # rule 6
    solver.addRule(Rule([SubRule("gangs", "Carleone", "areas", "west getto"),
                       SubRule("gangs", "Carleone", "areas", "busyness")]))

    # rule 7
    solver.addRule(Rule([SubRule("gangs", "Fix", "crimes", "guns"),
                       SubRule("gangs", "Fix", "crimes", "fighting")]))

    # rule 8
    solver.addRule(Rule([SubRule("areas", "central park", "crimes", "kidnapping"),
                       SubRule("areas", "central park", "crimes", "smuggling")]))

    # rule 9
    solver.addRule(Rule([SubRule("gangs", "Yao", "areas", "west getto")]))

    # rule 10
    solver.addRule(Rule([SubRule("gangs", "Shelby", "areas", "east docks"),
                       SubRule("gangs", "Shelby", "areas", "central park")]))

    # rule 11
    solver.addRule(Rule([SubRule("gangs", "Yao", "crimes", "smuggling"),
                       SubRule("gangs", "Yao", "crimes", "hijack")]))

    """

    #solver.solve()


