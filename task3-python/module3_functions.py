# =====================================================================
# Упражнение 2. Расчет НДС (calculate_vat)
# =====================================================================
# Демонстрация аргументов функции по умолчанию (vat_rate=20)

def calculate_vat(price, vat_rate=20):
    """Вычисляет сумму НДС от стоимости товара."""
    vat_amount = price * (vat_rate / 100)
    return round(vat_amount, 2)

print("--- Упражнение 2: Расчет НДС ---")
# Вызов со стандартной ставкой (аргумент не передается)
price_1 = 15000
print(f"Цена: {price_1} руб. НДС (по умолчанию 20%): {calculate_vat(price_1)} руб.")

# Вызов с явной (льготной) ставкой НДС
price_2 = 8000
custom_rate = 10
print(f"Цена: {price_2} руб. НДС (явный {custom_rate}%): {calculate_vat(price_2, custom_rate)} руб.")
print()


# =====================================================================
# Упражнение 3. Категория бизнеса (get_category)
# =====================================================================
# Использование инструкций if-elif-else внутри функции для возврата категорий

def get_category(annual_revenue):
    """Определяет категорию предприятия на основе его годовой выручки."""
    if annual_revenue <= 1000000:
        return "Микробизнес"
    elif annual_revenue <= 10000000:
        return "Малый бизнес"
    elif annual_revenue <= 100000000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

print("--- Упражнение 3: Категория бизнеса ---")
# Тестируем функцию на 4 различных значениях выручки
test_revenues = [450000, 4200000, 55000000, 250000000]
for rev in test_revenues:
    category = get_category(rev)
    print(f"Выручка: {rev} руб. -> Категория: {category}")
print()


# =====================================================================
# Упражнение 5. Применение скидки (apply_discount)
# =====================================================================
# Функция принимает параметры и применяется в цикле к списку элементов

def apply_discount(product_price, discount_percent):
    """Возвращает новую цену товара с учетом скидки."""
    new_price = product_price * (1 - discount_percent / 100)
    return round(new_price, 2)

print("--- Упражнение 5: Применение скидки ---")
initial_prices = [100.0, 250.5, 1200.0, 850.0, 3000.0]
discount = 15  # Скидка 15%

print(f"Применяем скидку {discount}% к каталогу товаров:")
for old_price in initial_prices:
    discounted_price = apply_discount(old_price, discount)
    print(f"Старая цена: {old_price} руб. -> Новая цена: {discounted_price} руб.")
print()


# =====================================================================
# Упражнение 6. Конвертер валюты (currency_convert)
# =====================================================================
# Передача управляющего текстового параметра для выбора логики расчета

def currency_convert(amount, exchange_rate, direction):
    """Конвертирует валюту в зависимости от указанного направления."""
    if direction == 'to_usd':
        return round(amount / exchange_rate, 2)
    elif direction == 'to_rub':
        return round(amount * exchange_rate, 2)
    else:
        return "Ошибка: неверное направление"

print("--- Упражнение 6: Конвертер валюты ---")
current_rate = 92.5

# Тест в сторону USD
rub_to_convert = 50000
usd_result = currency_convert(rub_to_convert, current_rate, 'to_usd')
print(f"Конвертация {rub_to_convert} руб. в доллары по курсу {current_rate}: ${usd_result}")

# Тест в сторону RUB
usd_to_convert = 350
rub_result = currency_convert(usd_to_convert, current_rate, 'to_rub')
print(f"Конвертация ${usd_to_convert} в рубли по курсу {current_rate}: {rub_result} руб.")
print()


# =====================================================================
# Упражнение 10. Генерация отчета (generate_report)
# =====================================================================
# Функция производит расчеты и выводит структурированный многострочный текст

def generate_report(company_name, total_revenue, total_expenses):
    """Формирует и выводит краткий финансовый отчет организации."""
    profit = total_revenue - total_expenses
    
    # Защита от деления на ноль при расчете рентабельности
    if total_revenue > 0:
        profitability = round((profit / total_revenue) * 100, 2)
    else:
        profitability = 0.0
        
    status = "Прибыльна" if profit > 0 else "Убыточна или работает в безубыточность"
    
    # Выводим оформленный текст
    print(f"=== ФИНАНСОВЫЙ ОТЧЕТ: {company_name.upper()} ===")
    print(f"Выручка компании: {total_revenue} руб.")
    print(f"Затраты компании: {total_expenses} руб.")
    print(f"Чистая прибыль: {profit} руб.")
    print(f"Рентабельность: {profitability}%")
    print(f"Эффективность деятельности: {status}")
    print("========================================")

print("--- Упражнение 10: Генерация отчета ---")
# Запускаем генерацию отчета для тестовой фирмы
generate_report("ООО Вектор Финанс", 4500000, 3200000)
print()