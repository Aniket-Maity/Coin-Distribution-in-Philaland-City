def countTotalWaysRepNotAllowed(arr,m,n):
    if(n==0):
        return 1
    if(n<0):
        return 0
    if(m<=0 and n>=1):
        return 0
    return countTotalWaysRepNotAllowed(arr,m-1,n) + countTotalWaysRepNotAllowed(arr,m,n-arr[m-1])
def main():
   N,NumberOfCoin = map(int,input().split())
   coinArr = list(map(int,input().split()))
   print(countTotalWaysRepNotAllowed(coinArr,NumberOfCoin,N))

if __name__ == '__main__':
   main()