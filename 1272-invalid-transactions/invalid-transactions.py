class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transaction_mapping = { }

        '''
        transaction_mapping should look like:
            transation_name -> transaction
        '''

        possibly_invalid = set()

        for i in range(len(transactions)):
            transaction_info = transactions[i].split(',')
            transaction_info.append(i)

            if int(transaction_info[2]) > 1000:
                possibly_invalid.add(i)
                


            if transaction_info[0] not in transaction_mapping:
                transaction_mapping[transaction_info[0]] = [transaction_info]

            else:
                for tran in transaction_mapping[transaction_info[0]]:
                    if abs(int(tran[1])-int(transaction_info[1])) <= 60 and tran[3]!=transaction_info[3]:
                        possibly_invalid.add(tran[4])
                        possibly_invalid.add(i)
                transaction_mapping[transaction_info[0]].append(transaction_info)
        ans = []
        for i in possibly_invalid:
            ans.append(transactions[i])
        return ans


