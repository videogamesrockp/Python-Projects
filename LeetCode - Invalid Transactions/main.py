class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid=[]
        for i in range(len(transactions)):
            temp = transactions[i].split(",")
            if int(temp[2]) >= 1000:
                invalid.append(i)
            for j in range(len(transactions)):
                temp2 = transactions[j].split(",")
                if abs(int(temp[1])-int(temp2[1])) <= 60 and temp[0]==temp2[0] and temp[3]!=temp2[3]:
                    invalid.append(i)
        final = []
        [final.append(x) for x in invalid if x not in final]
        for i in range(len(final)):
            final[i]=transactions[final[i]]
        return final
