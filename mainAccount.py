from Account import Account
try:
    title=input("Enter a title: ")
    account_id=int(input("Enter an account ID: "))
    ammount=int(input("Enter ammount: "))
    account1=Account(title,account_id,ammount)
    print(account1)
except ValueError as Va:
    print(f"ERROR:{Va}")
except Exception as ex:
    print(f"ERROR:{ex}")