from datetime import datetime, timedelta  # استيراد الوحدات المطلوبة

def display_current_datetime():
    """
    دالة لعرض التاريخ والوقت الحالي
    """
    current_date = datetime.now()  # الحصول على التاريخ والوقت الحالي
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """
    دالة لحساب التاريخ المستقبلي بعد عدد معين من الأيام
    """
    current_date = datetime.now()  # التاريخ الحالي
    future_date = current_date + timedelta(days=days)  # حساب التاريخ المستقبلي
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# تنفيذ البرنامج الرئيسي
if __name__ == "__main__":
    display_current_datetime()
    try:
        # ✅ هذه الجملة مطلوبة حسب التعليمات
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Please enter a valid integer number of days.")
