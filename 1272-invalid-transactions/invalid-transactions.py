class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transaction_map = defaultdict(list)

        '''
        name ->[(timei,cityi,i)]
        '''

        possibly_invalid = set()

        for index in range(len(transactions)):
            print(transactions[index])
            transaction_info = transactions[index].split(',')
            #[name,time,amount,city]
            print(transaction_info)
            if int(transaction_info[2]) > 1000:
                possibly_invalid.add(index)

            if transaction_info[0] in transaction_map:
                other_trans = transaction_map[transaction_info[0]]
                for tran in other_trans:
                    if tran[1] != transaction_info[3] and abs(int(tran[0])-int(transaction_info[1])) <= 60:
                        possibly_invalid.add(index)
                        possibly_invalid.add(tran[2])
            
            transaction_map[transaction_info[0]].append((transaction_info[1],transaction_info[3],index))
        ans = []
        for index in possibly_invalid:
            ans.append(transactions[index])

        return ans

            

