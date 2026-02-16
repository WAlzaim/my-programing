def hollow_square(n):
    if n <= 0:
     return ""
    if n == 1:
     return "*"
    
    result = ""

    for i in range(n):
        if i == 0 or i == n - 1:
            result += "*" * n
        else:
         result += "*" + " " * (n-2) + "*"
        result += "\n"

    return result

# Plugging in n = 9
print(hollow_square(9))

def number_pattern(n):
   result = ""
   i = 1

   while i <= n:
      j = 1
      while j <= i:
         result += str(j)
         j += 1

      if i != n:
         result += "\n"

      i += 1
   return result

# Plugging in n = 10
print(number_pattern(10))


def centered_star_pyramid(n):
   result = ""
   i = 1
   
   while i <= n:
     spaces = n - i
     stars = 2 * i - 1

     result += " " * spaces
     result += "*" * stars

     if i != n:
         result += "\n"

     i += 1
   
   return result

# Plugging in n = 7
print(centered_star_pyramid(7))