def main(prompt):
     return f"{prompt} is also my favourite city"
user_input:str = str(input("What's your favorite city? "))
res = main(user_input)
print(res)