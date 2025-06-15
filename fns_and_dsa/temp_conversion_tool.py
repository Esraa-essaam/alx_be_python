# temp_conversion_tool.py
# أداة لتحويل درجات الحرارة بين فهرنهايت وسلسيوس باستخدام متغيرات عامة

# المتغيرات العامة للتحويل
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

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
        # أخذ درجة الحرارة من المستخدم
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # تحويل الإدخال إلى رقم عشري

        # تحديد الوحدة
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # التحويل حسب الوحدة
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
