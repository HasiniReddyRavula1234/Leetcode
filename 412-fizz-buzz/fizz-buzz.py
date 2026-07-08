class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s = []
        for i in range(1, n + 1):
            if int(i) % 15 == 0:
                s.append('FizzBuzz')
            elif int(i) % 3 == 0:
                s.append('Fizz')
            elif int(i) % 5 == 0:
                s.append('Buzz')
            else:
                s.append(str(i))
        return s
