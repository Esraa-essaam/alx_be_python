# explore_datetime.py
# برنامج لاستكشاف وحدة datetime في بايثون

from datetime import datetime, timedelta  # استيراد الوحدات المطلوبة

def display_current_datetime():
    """
    دالة لعرض التاريخ والوقت الحالي
    """
    current_date = datetime.now()  # الحصول على التاريخ والوقت الحالي
    print("التاريخ والوقت الحالي:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """
    دالة لحساب التاريخ المستقبلي بعد عدد معين من الأيام
    """
    current_date = datetime.now()  # التاريخ الحالي
    future_date = current_date + timedelta(days=days)  # حساب التاريخ المستقبلي
    print("التاريخ المستقبلي:", future_date.strftime("%Y-%m-%d"))

# تنفيذ البرنامج الرئيسي
if __name__ == "__main__":
    display_current_datetime()
    try:
        # طلب عدد الأيام من المستخدم
        days_input = int(input("أدخل عدد الأيام التي تريد إضافتها للتاريخ الحالي: "))
        calculate_future_date(days_input)
    except ValueError:
        print("يرجى إدخال رقم صحيح.")
