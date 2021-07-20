integer = (input("enter any number:"))
n = int(integer)
if n%2 != 0:
    print( "weired")
elif n%2 == 0 and 1<n<6:
    print("not weired")
elif n%2 == 0 and 6<n<21:
    print("weired")
else:
  print("not weired")