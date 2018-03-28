# Ian McLoughlin
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 21

ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Murtagh"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

"52167ian.mcloughlin@gmit.ie -> Discussions -> Fibonacci exercise responses -> Re: Fibonacci exercise responses
by THEA MURTAGH - Tuesday, 23 January 2018, 10:28 PM
 
My name is Thea so the first and last letter of my name (T + A = 20 + 1) give the number  21. The 21st Fibonacci number is 10946"

"52167ian.mcloughlin@gmit.ie -> Discussions -> Week 2 task -> Re: Week 2 task
by THEA MURTAGH - Thursday, 1 February 2018, 12:12 AM
 
My surname is Murtagh

The first letter M is number 77

The last letter h is number 104

Fibonacci number 181 is 30010821454963453907530667147829489881

 

Ord () returns a number defining the position of something in a series, "
