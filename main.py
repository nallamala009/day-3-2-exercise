# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bmi = round(weight / height ** 2, 2)
print(bmi)
if bmi < 18.5:
  print(f"your BMI is {bmi}, you are under weight")
elif bmi < 25:
  print(f"your BMI is {bmi}, you are normal weight")
elif bmi < 30:
  print(f"your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
  print(f"your BMI is {bmi}, you are obese")
else:
  print(f"your BMI is > 35, you are clinically obese")

#Write your code below this line 👇




