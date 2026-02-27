"""
BMI Calculator and Calorie Requirement Module
Calculates BMI, health category, BMR, and TDEE based on user inputs
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index)
    
    Args:
        weight: Weight in kilograms
        height: Height in centimeters
    
    Returns:
        BMI value (float)
    """
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """
    Classify BMI into health categories
    
    Args:
        bmi: BMI value
    
    Returns:
        Category string and health status
    """
    if bmi < 18.5:
        return "Underweight", "⚠️ Below normal weight"
    elif 18.5 <= bmi < 25:
        return "Normal", "✅ Healthy weight range"
    elif 25 <= bmi < 30:
        return "Overweight", "⚠️ Above normal weight"
    else:
        return "Obese", "🔴 Significantly above normal weight"


def calculate_bmr(weight, height, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation
    
    Args:
        weight: Weight in kg
        height: Height in cm
        age: Age in years
        gender: 'Male' or 'Female'
    
    Returns:
        BMR value (calories per day)
    """
    if gender.lower() == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    return round(bmr, 2)


def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure (TDEE)
    
    Args:
        bmr: Basal Metabolic Rate
        activity_level: Activity level string
    
    Returns:
        TDEE value (calories per day)
    """
    activity_multipliers = {
        'Sedentary (little or no exercise)': 1.2,
        'Lightly Active (exercise 1-3 days/week)': 1.375,
        'Moderately Active (exercise 3-5 days/week)': 1.55,
        'Very Active (exercise 6-7 days/week)': 1.725,
        'Extra Active (very intense exercise daily)': 1.9
    }
    
    multiplier = activity_multipliers.get(activity_level, 1.2)
    tdee = bmr * multiplier
    
    return round(tdee, 2)


def calculate_calorie_goal(tdee, goal):
    """
    Calculate daily calorie goal based on fitness objective
    
    Args:
        tdee: Total Daily Energy Expenditure
        goal: Fitness goal ('Weight Loss', 'Muscle Gain', 'Maintenance')
    
    Returns:
        Target daily calories
    """
    if goal == 'Weight Loss':
        # Deficit of 500 calories per day (lose ~0.45 kg per week)
        return round(tdee - 500, 2)
    elif goal == 'Muscle Gain':
        # Surplus of 300-500 calories per day
        return round(tdee + 400, 2)
    else:  # Maintenance
        return tdee


def get_fitness_metrics(weight, height, age, gender, activity_level, goal):
    """
    Calculate all fitness metrics
    
    Args:
        weight: Weight in kg
        height: Height in cm
        age: Age in years
        gender: 'Male' or 'Female'
        activity_level: Activity level string
        goal: Fitness goal
    
    Returns:
        Dictionary containing all metrics
    """
    bmi = calculate_bmi(weight, height)
    category, health_status = get_bmi_category(bmi)
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    target_calories = calculate_calorie_goal(tdee, goal)
    
    return {
        'bmi': bmi,
        'category': category,
        'health_status': health_status,
        'bmr': bmr,
        'tdee': tdee,
        'target_calories': target_calories
    }


if __name__ == "__main__":
    # Test the module
    test_metrics = get_fitness_metrics(70, 175, 22, 'Male', 
                                       'Moderately Active (exercise 3-5 days/week)', 
                                       'Muscle Gain')
    print("Test Metrics:", test_metrics)
