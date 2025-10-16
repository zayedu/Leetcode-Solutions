class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        nameMap = defaultdict(list)

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)
            parsed.append((name, time, amount, city, t))
            nameMap[name].append((time, city, i))


        invalid = []

        for name, time, amount, city, orig in parsed:
            if amount > 1000:
                invalid.append(orig)
            else:
                for time2, city2, j in nameMap[name]:
                    if city2 != city and abs(time - time2) <= 60:
                        invalid.append(orig)
                        break

        return invalid