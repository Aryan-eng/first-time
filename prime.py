
def prime():
  n = int(input("What number do you want to check prime for?:"))
  for i in range(2,n):
    if n%i == 0:
      print("This number is not prime")
      break
    else:
      print("This number is prime")
      break
prime()