def calculate_revenue_generated(product_category, units_sold, price_tier):
    if product_category == 'electronics':
        if price_tier == 'low': return 45 * units_sold
        elif price_tier == 'medium': return 75 * units_sold
        else: return 120 * units_sold
    elif product_category == 'clothing':
        if price_tier == 'low': return 25 * units_sold
        elif price_tier == 'medium': return 40 * units_sold
        else: return 65 * units_sold
    else:
        if price_tier == 'low': return 15 * units_sold
        elif price_tier == 'medium': return 25 * units_sold
        else: return 35 * units_sold
def calculate_performance_ratio(experience_years, baseline_sales, actual_sales):
    expected_sales = 1000 + (experience_years * 100)
    sales_capacity = expected_sales - baseline_sales
    return round((actual_sales - baseline_sales) / sales_capacity * 100, 1)
def determine_achievement_level(performance_percent):
    if performance_percent < 50: return "Developing Level"
    elif performance_percent < 60: return "Competent Level"
    elif performance_percent < 70: return "Proficient Level"
    elif performance_percent < 85: return "Advanced Level"
    else: return "Expert Level"

def calculate_commission_earned(revenue, units, level_multiplier):
    base_commision =  revenue * 0.05 + units * 2
    if level_multiplier == "Developing Level": return round(base_commision*0.5, 1)
    elif level_multiplier == "Competent Level": return round(base_commision, 1)
    elif level_multiplier == "Proficient Level": return round(base_commision*1.2, 1)
    elif level_multiplier == "Advanced Level": return round(base_commision*1.5, 1)
    else: return round(base_commision*1.8, 1)

def needs_training_support(consecutive_months, total_units, avg_performance):
    if (consecutive_months >= 6 and avg_performance < 50) or (total_units < 100 and avg_performance < 60) or (consecutive_months >= 4 and avg_performance < 40): return True
    else: return False

def generate_sales_report(employee, product_category, units, price_tier, experience_years, baseline_sales, actual_sales, consecutive_months):
    print("========================================")
    print(f"Sales Report for: {employee}")
    print("----------------------------------------")
    print(f"Product Category: {product_category}")
    print(f"Units Sold: {units}")
    print(f"Price Tier: {price_tier}")
    revenue_generated = calculate_revenue_generated(product_category, units, price_tier)
    print(f"Revenue Generated: ${revenue_generated}")
    print("Performance Analysis:")
    print(f"  Experience: {experience_years} years, Baseline: {baseline_sales}, Actual Sales: {actual_sales}")
    performance = calculate_performance_ratio(experience_years, baseline_sales, actual_sales)
    print(f"  Performance: {performance}%")
    level_multiplyer = determine_achievement_level(performance)
    print(f"  Achievement Level: {level_multiplyer}")
    comission = calculate_commission_earned(revenue_generated, units, level_multiplyer)
    print(f"Commission Earned: ${comission}")
    c  = consecutive_months
    print(f"Consecutive Months: {c}")

    is_month = needs_training_support(consecutive_months, units, performance)
    print(f"Training Support Needed: {'Yes' if is_month else 'No'}")
    print()
n = int(input("Enter the number of records: "))
for i in range(n):
    employee = input("Enter the  name of the employee: ")
    product_category = input("Enter the category: ")
    units = int(input("Enter the number of units: "))
    price_tier = input("Enter the price tier: ")
    experience_years = int(input("Enter the years of experience: "))
    baseline_sales = int(input("Enter baseline: "))
    actual_sales = int(input("Enter the actual sales: "))
    consecutive_months = int(input("Enter the consecutive months: "))
    if i == 0: print('\nRETAIL SALES PERFORMANCE SYSTEM')
    generate_sales_report(employee, product_category, units, price_tier, experience_years, baseline_sales, actual_sales, consecutive_months)