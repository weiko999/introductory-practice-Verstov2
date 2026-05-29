# =====================================================================
# Итоговая мини-программа. Вариант 1: Калькулятор рентабельности
# =====================================================================

def analyze_profitability(revenue, expenses):
    """Функция вычисляет чистую прибыль и процент рентабельности."""
    financial_profit = revenue - expenses
    # Защита от деления на ноль, если выручка не была указана
    profitability_index = (financial_profit / revenue) * 100 if revenue > 0 else 0.0
    return financial_profit, round(profitability_index, 2)

print("--- АНАЛИЗ ЭФФЕКТИВНОСТИ ДЕЯТЕЛЬНОСТИ ФИЛИАЛОВ ---")
company_title = input("Введите общее название компании/холдинга: ") # Тип str

# Запускаем цикл for для последовательного анализа 3 филиалов (требование ТЗ)
for branch_step in range(1, 4):
    print(f"\n--- Ввод данных по филиалу №{branch_step} ---")
    branch_name = input("Введите название филиала или отдела: ")
    branch_revenue = float(input("Введите ежемесячную выручку (руб.): ")) # Тип float
    branch_expenses = float(input("Введите ежемесячные затраты (руб.): "))
    
    # Вызов функции для математических расчетов
    profit, profitability = analyze_profitability(branch_revenue, branch_expenses)
    
    # Многоуровневое условие if-elif-else для оценки уровня рентабельности
    if profitability > 20:
        efficiency_level = "ВЫСОКАЯ"
    elif 10 <= profitability <= 20:
        efficiency_level = "СРЕДНЯЯ"
    else:
        efficiency_level = "НИЗКАЯ"
    
    # Вывод структурированного мини-отчета на экран
    print(f"\n>> МИНИ-ОТЧЕТ ПО ФИЛИАЛУ: {branch_name.upper()} (Холдинг: {company_title})")
    print(f"Чистая прибыль филиала: {profit} руб.")
    print(f"Рентабельность продаж: {profitability}%")
    print(f"Оценка эффективности данного направления: {efficiency_level}")

print("\n--- Экспресс-анализ всех трех направлений успешно завершен! ---")