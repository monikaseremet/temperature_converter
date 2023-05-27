temperature_scales = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K',
    }

def convert_temperature(value, input_scale, output_scale):

    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value

    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return value  * 5 / 9 + 459.67
        else:
            return value

    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459,67
        else:
            return value
    else:
        return value

while True:
    value = float(input("Please enter the input temperature value: "))
    input_scale = input("Please enter the input temperature scale (C - Celsius, F - Fahrenheit or K - Kelvin): ").upper()
    output_scale = input("Please enter the output temperature scale (C - Celsius, F - Fahrenheit or K - Kelvin): ").upper()

    result = convert_temperature(value, input_scale, output_scale)

    print(f"{value} °{input_scale} equals to {result} °{output_scale}")

    quit = input("Please enter q to quit, or any other key to continue: ")
    if quit.lower() == 'q':
        break
