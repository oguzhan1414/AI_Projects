def add(a,b):
    return a+b  #değer dönderen

result = add(5,12)
print(result)

def math_operations(a,b):
    add = a+b
    sub = a-b
    return add,sub


#SICAKLIK DÖNÜŞTÜRÜCÜ

def celsis_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celcius):
    return celcius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def show_menu():
    print("1. Celsius to Fahneheit ve Kelvin")
    print("2. Fahneheit to Celsius ve Kelvin")
    print("3. Kelvin to Fahneheit ve Celsius")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter yout choice (1-4): ")
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Fahrenheit : {celsis_to_fahrenheit(celsius):.2f}")
        print(f"Kelvin : {celsius_to_kelvin(celsius):.2f}")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        print(f"Celcius : {fahrenheit_to_celsius(fahrenheit):.2f}")
        print(f"Kelvin : {fahrenheit_to_kelvin(fahrenheit):.2f}")
    elif choice == "3":
        kelvin = float(input("Enter temperature in kelvin: "))
        print(f"Celcius : {kelvin_to_celsius(kelvin):.2f}")
        print(f"Fahrenheit : {kelvin_to_fahrenheit(kelvin):.2f}")

    else:
        print("Çıkış Yapılıyor")
        break
