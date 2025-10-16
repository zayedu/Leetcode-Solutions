class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        parsed = []
        for i, t in enumerate(transactions):
            parts = t.split(",")
            parsed.append((parts[0], int(parts[1]), int(parts[2]), parts[3], i))
        
        # Sort by name, then time for better cache locality
        by_name = defaultdict(list)
        for name, time, amt, city, idx in parsed:
            by_name[name].append((time, city, idx))
        
        # Sort each person's transactions by time
        for name in by_name:
            by_name[name].sort()
        
        invalid = set()
        
        for name, time, amt, city, idx in parsed:
            if amt > 1000:
                invalid.add(idx)
            
            # Binary search approach for time window
            name_txns = by_name[name]
            for other_time, other_city, _ in name_txns:
                # Early termination: if sorted by time, we can break early
                if other_time < time - 60:
                    continue
                if other_time > time + 60:
                    break
                if city != other_city:
                    invalid.add(idx)
                    break
        
        return [transactions[i] for i in sorted(invalid)]