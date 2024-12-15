from Car import Car
try:
    model=input("Enter a model : ")
    year=int(input("Enter a year : "))
    plate=input("Enter a plate : ")
    color=input("Enter a color : ")
    Car1=Car(model,year,plate,color)
    print(Car1)
except Exception as e:
    print(f"ERROR:{e}")


