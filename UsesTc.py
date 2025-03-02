from applications import Applications

# تعريف المشكلة
items = [(2, 3), (3, 4), (4, 5), (5, 8)]  # (وزن، قيمة)
capacity = 5  # سعة الحقيبة

# إنشاء كائن التطبيقات
app = Applications()

# حل المشكلة
best_combination, best_value = app.knapsack_solution(items, capacity)

print("المجموعة الأمثل:", best_combination)
print("القيمة الإجمالية الأمثل:", best_value)