---------------------------Happy number---------------------------
class Solution(object):
    def sqsum(self,n):
        sum=0
        while(n!=0):
            sum+=(n%10)*(n%10)   #squaring of each num function......
            n=n/10
        return sum

    def isHappy(self, n):
        s=set()
        while(n!=1 and n not in s):  #checking for n==1 and n is not repeating same sum.....
            s.add(n)
            n=self.sqsum(n)
        return n==1

eg:- 19
-------------------------------Happy num------------------------------------------



------------------------------ugly number-----------------------------------------
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.

class Solution(object):
    def isUgly(self, n):
        if n==0:
            return False
        for i in 2,3,5:          # n has only prime factors in 2,3,5 only
            while n%i==0:        
                n=n/i               # critical step
        return n==1

CPP-Solution:-
---------------------------
class Solution {
public:
bool isUgly(int n) {
    if (n<=0) return false;
    while(n!=1)
    {
        if(n%2==0)
        {
            n=n/2;
        }
        else if(n%3==0)
        {
            n=n/3;
        }
        else if(n%5==0)
        {
            n=n/5;
        }
        else 
        {
            return false;
        }
    }
               return true;

}
};
-----------------------------ugly number-----------------------------------------------



