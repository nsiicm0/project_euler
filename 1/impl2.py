'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Solution: Inclusion-Exclusion Principle using the sum of all numbers from 1 to n is equal to n*(n+1)/2
n = 1000
t = n - 1

div_3 = 3 * (t // 3) * ((t // 3) + 1) // 2
div_5 = 5 * (t // 5) * ((t // 5) + 1) // 2
div_15 = 15 * (t // 15) * ((t // 15) + 1) // 2

print(f'{div_3} + {div_5} - {div_15} = {div_3 + div_5 - div_15}')