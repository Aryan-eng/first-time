
def prime(n):
  for i in range(2,n):
    if n%i == 0:
      print("This number is not prime")
      break
    else:
      print("This number is prime")
      break
prime(29)