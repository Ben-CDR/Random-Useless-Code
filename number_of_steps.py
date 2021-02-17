# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to 
# subtract 1 from it.

def numberOfSteps (num):
        def count(num, counter):
            if num == 0:
                return counter
            if num % 2 == 0:
                num /= 2
                counter += 1
                counter = count(num, counter)
                return counter
            else:
                num -= 1
                counter += 1
                counter = count(num, counter)
                return counter
        return count(num, 0)
        
print(numberOfSteps(14))
print(numberOfSteps(8324967532907657489370469827047692656203905))

# As you can see, recursion is friggin' fast