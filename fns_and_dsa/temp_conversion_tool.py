# temp_conversion_tool.py
# أداة لتحويل درجات الحرارة بين فهرنهايت وسلسيوس باستخدام متغيرات عامة

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # ✅ كما هو مطلوب

def convert_to_celsius(fahrenheit):
    """
    تحويل من فهرنهايت إلى سلسيوس
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    تحويل من سلسيوس إلى فهرنهايت
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# تنفيذ البرنامج الرئيسي
if __name__ == "__main__":
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
