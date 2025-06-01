# طلب تفاصيل المهمة من المستخدم
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# معالجة المهمة باستخدام match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# التحقق إذا كانت المهمة مرتبطة بالوقت
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have free time."

# طباعة النتيجة
print(message)
