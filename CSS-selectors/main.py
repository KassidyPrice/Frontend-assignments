# Write a program that separates each character of a string by a hyphen. Each character should accumulate based on the current iteration count. The start of each accumulated value should be capitalized. 
# IE:  "abcd" => "A-Bb-Ccc-Dddd"
# "RqaEzTy" => "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

lst = []
def funky_challenge(string):
 
 for count, value in enumerate(string):
  # value = value * (count+1)
  # lst.append(value.title())
  lst.append((value * (count + 1)).title())

 joined_str = "-".join(lst)
 return joined_str

print(funky_challenge("RqaEzTy")) 