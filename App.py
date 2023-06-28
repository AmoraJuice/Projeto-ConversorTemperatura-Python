# formula
def celsius_to_fahrenheit (temp_celsius):
    return (temp_celsius * 9/5) + 32

def celsius_to_kelvin(temp_celsius):
    return temp_celsius + 273.15

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def kelvin_to_fahrenheit(temp_kelvin):
    return (temp_kelvin * 9/5) - 459.67

def fahrenheit_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

def fahrenheit_to_kevin(temp_fahrenheit):
    return (temp_fahrenheit - 273.15)

entry_scale = input("Escolha a escala de temperatura de entrada (C, F, K): ")
outgoing_scale = input("Escolha a escala de temperatura de saída (C, F, K): ")
entry_temp = float(input("Digite o valor da temperatura de entrada: "))

# escalas
def converter_temperature(temp, entry_scale, outgoing_scale):
    if entry_scale == 'C' and outgoing_scale == 'F':
        temp_fahrenheit = celsius_to_fahrenheit(temp)
        print("A temperatura em Fahrenheit e: {:.2f}".format(temp_fahrenheit))
    elif entry_scale  == 'C' and outgoing_scale == 'K':
        temp_kelvin = celsius_to_kelvin(temp)
        print("A temperatura em Kelvin e: {:.2f}".format(temp_kelvin))
    elif  entry_scale == 'F' and outgoing_scale == 'C':
        print("A temperatura em Celsius e: {:.2f}".format(temp_celsius))
    elif entry_scale == 'F' and outgoing_scale == 'K':
        print("A temperatura em Kelvin e: {:.2f}".format(temp_kelvin))
    elif entry_scale == 'K' and outgoing_scale == 'F':
        print("A temperatura em Fahrenheit e: {:.2f}".format(temp_fahrenheit))
    elif entry_scale == 'K' and outgoing_scale == 'C':
        print("A temperatura em Celsius e: {:.2f}".format(temp_celsius))
    else:
        print("A temperatura nao pode ser convertida.")

converter_temperature(entry_temp, entry_scale,outgoing_scale)
