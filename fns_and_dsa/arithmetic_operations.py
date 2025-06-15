def perform_operation(num1, num2, operation):
    """
    تنفيذ العمليات الحسابية الأساسية: جمع، طرح، ضرب، قسمة.

    المعاملات:
    - num1 (float): الرقم الأول
    - num2 (float): الرقم الثاني
    - operation (str): نوع العملية (add, subtract, multiply, divide)

    الناتج:
    - ناتج العملية أو رسالة خطأ في حال وجود مشكلة
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
