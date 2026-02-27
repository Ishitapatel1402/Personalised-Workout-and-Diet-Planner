"""
Diet Planner Module
Generates personalized Indian diet plans based on calorie goals, food preferences, and budget
"""

def get_diet_plan(target_calories, food_preference, budget, goal):
    """
    Generate personalized Indian diet plan
    
    Args:
        target_calories: Daily calorie target
        food_preference: 'Vegetarian' or 'Non-Vegetarian'
        budget: 'Low' or 'Medium' or 'High'
        goal: Fitness goal
    
    Returns:
        Dictionary containing meal plan
    """
    if food_preference == 'Vegetarian':
        return get_vegetarian_plan(target_calories, budget, goal)
    else:
        return get_non_vegetarian_plan(target_calories, budget, goal)


def get_vegetarian_plan(calories, budget, goal):
    """
    Vegetarian Indian meal plan
    """
    # Calculate macro distribution based on goal
    if goal == 'Weight Loss':
        protein_ratio = 0.30
        carbs_ratio = 0.40
        fat_ratio = 0.30
    elif goal == 'Muscle Gain':
        protein_ratio = 0.35
        carbs_ratio = 0.45
        fat_ratio = 0.20
    else:  # Maintenance
        protein_ratio = 0.25
        carbs_ratio = 0.50
        fat_ratio = 0.25
    
    protein_cals = calories * protein_ratio
    carbs_cals = calories * carbs_ratio
    fat_cals = calories * fat_ratio
    
    # Macros in grams (Protein & Carbs = 4 cal/g, Fat = 9 cal/g)
    protein_g = round(protein_cals / 4)
    carbs_g = round(carbs_cals / 4)
    fat_g = round(fat_cals / 9)
    
    if budget == 'Low':
        plan = {
            'breakfast': {
                'meal': '🥣 Poha with Vegetables + Tea',
                'items': [
                    '150g Poha (beaten rice) with onions, tomatoes, peas',
                    '1 tsp peanuts',
                    '1 cup tea with milk'
                ],
                'calories': '~350 cal',
                'cost': '₹20-30'
            },
            'mid_morning': {
                'meal': '🍌 Banana + Roasted Chana',
                'items': [
                    '1 banana',
                    '30g roasted chickpeas'
                ],
                'calories': '~200 cal',
                'cost': '₹15-20'
            },
            'lunch': {
                'meal': '🍛 Dal Rice + Sabzi + Curd',
                'items': [
                    '2 chapati or 1 cup rice',
                    '1 bowl dal (moong/toor)',
                    '1 bowl seasonal vegetable curry',
                    '1 bowl curd',
                    'Salad'
                ],
                'calories': '~500 cal',
                'cost': '₹40-60'
            },
            'evening': {
                'meal': '☕ Tea + Snack',
                'items': [
                    '1 cup tea',
                    '2 Marie biscuits or chana chaat'
                ],
                'calories': '~150 cal',
                'cost': '₹15-20'
            },
            'dinner': {
                'meal': '🥘 Roti + Sabzi + Dal',
                'items': [
                    '3 chapati',
                    '1 bowl mixed vegetable curry',
                    '1 bowl dal',
                    'Salad'
                ],
                'calories': '~450 cal',
                'cost': '₹40-50'
            },
            'before_bed': {
                'meal': '🥛 Milk',
                'items': [
                    '1 glass warm milk (optional: turmeric)'
                ],
                'calories': '~150 cal',
                'cost': '₹10-15'
            }
        }
    
    elif budget == 'Medium':
        plan = {
            'breakfast': {
                'meal': '🍳 Vegetable Upma + Milk',
                'items': [
                    'Upma with vegetables (rava, carrots, beans, peas)',
                    '1 glass milk or protein shake',
                    'Handful of almonds (5-6)'
                ],
                'calories': '~400 cal',
                'cost': '₹40-60'
            },
            'mid_morning': {
                'meal': '🍎 Fruit + Nuts',
                'items': [
                    '1 apple or orange',
                    '10 almonds + 5 cashews',
                    'Green tea'
                ],
                'calories': '~220 cal',
                'cost': '₹30-40'
            },
            'lunch': {
                'meal': '🍛 Paneer Curry + Roti + Rice + Curd',
                'items': [
                    '2 chapati + 1/2 cup brown rice',
                    '100g paneer curry',
                    '1 bowl dal',
                    '1 bowl vegetable sabzi',
                    '1 bowl curd',
                    'Salad with cucumber, tomato, onion'
                ],
                'calories': '~600 cal',
                'cost': '₹80-120'
            },
            'evening': {
                'meal': '🥤 Smoothie + Sprouts',
                'items': [
                    'Banana smoothie with oats',
                    'Boiled sprouts chaat (moong)'
                ],
                'calories': '~250 cal',
                'cost': '₹40-50'
            },
            'dinner': {
                'meal': '🥗 Roti + Rajma + Sabzi',
                'items': [
                    '3 chapati (whole wheat)',
                    '1 bowl rajma or chole',
                    '1 bowl green vegetable',
                    'Cucumber salad'
                ],
                'calories': '~500 cal',
                'cost': '₹60-80'
            },
            'before_bed': {
                'meal': '🥛 Protein Milk',
                'items': [
                    '1 glass milk with protein powder or',
                    'Turmeric milk with honey'
                ],
                'calories': '~180 cal',
                'cost': '₹30-40'
            }
        }
    
    else:  # High Budget
        plan = {
            'breakfast': {
                'meal': '🍳 Oats + Smoothie Bowl',
                'items': [
                    'Masala oats with vegetables',
                    'Smoothie bowl with berries, banana, chia seeds',
                    'Protein shake with whey',
                    '10 almonds + 5 walnuts'
                ],
                'calories': '~500 cal',
                'cost': '₹100-150'
            },
            'mid_morning': {
                'meal': '🥗 Greek Yogurt + Fruits',
                'items': [
                    'Greek yogurt with honey',
                    'Mixed fruits (apple, orange, berries)',
                    'Mixed nuts (15-20)',
                    'Green tea'
                ],
                'calories': '~280 cal',
                'cost': '₹60-80'
            },
            'lunch': {
                'meal': '🍛 Premium Thali',
                'items': [
                    '2 multigrain roti + 1/2 cup quinoa or brown rice',
                    '150g paneer tikka or tofu curry',
                    '1 bowl dal makhani',
                    'Mixed vegetable sabzi (broccoli, bell peppers)',
                    'Greek curd with cucumber',
                    'Large mixed salad with olive oil'
                ],
                'calories': '~700 cal',
                'cost': '₹150-200'
            },
            'evening': {
                'meal': '🥤 Protein Smoothie + Dry Fruits',
                'items': [
                    'Whey protein shake with banana and peanut butter',
                    'Mixed dry fruits (almonds, cashews, dates)',
                    'Boiled sprouts salad'
                ],
                'calories': '~350 cal',
                'cost': '₹80-100'
            },
            'dinner': {
                'meal': '🥘 Multi-Course Dinner',
                'items': [
                    '3 multigrain chapati',
                    '1 bowl paneer/tofu preparation',
                    '1 bowl rajma or chickpea curry',
                    'Grilled vegetables',
                    'Large salad with avocado',
                    'Buttermilk'
                ],
                'calories': '~600 cal',
                'cost': '₹120-150'
            },
            'before_bed': {
                'meal': '🥛 Casein Shake',
                'items': [
                    'Casein protein shake or',
                    'Warm turmeric milk with almonds',
                    '5 soaked almonds'
                ],
                'calories': '~200 cal',
                'cost': '₹50-70'
            }
        }
    
    # Add macro breakdown
    plan['macros'] = {
        'total_calories': calories,
        'protein': f'{protein_g}g',
        'carbohydrates': f'{carbs_g}g',
        'fats': f'{fat_g}g'
    }
    
    plan['tips'] = [
        '💧 Drink 3-4 liters of water daily',
        '🥗 Include salads with every major meal',
        '🍵 Replace regular tea with green tea when possible',
        '🥜 Soak almonds overnight for better absorption',
        '⏰ Maintain consistent meal timings'
    ]
    
    return plan


def get_non_vegetarian_plan(calories, budget, goal):
    """
    Non-Vegetarian Indian meal plan
    """
    # Calculate macro distribution based on goal
    if goal == 'Weight Loss':
        protein_ratio = 0.35
        carbs_ratio = 0.35
        fat_ratio = 0.30
    elif goal == 'Muscle Gain':
        protein_ratio = 0.40
        carbs_ratio = 0.40
        fat_ratio = 0.20
    else:  # Maintenance
        protein_ratio = 0.30
        carbs_ratio = 0.45
        fat_ratio = 0.25
    
    protein_cals = calories * protein_ratio
    carbs_cals = calories * carbs_ratio
    fat_cals = calories * fat_ratio
    
    protein_g = round(protein_cals / 4)
    carbs_g = round(carbs_cals / 4)
    fat_g = round(fat_cals / 9)
    
    if budget == 'Low':
        plan = {
            'breakfast': {
                'meal': '🥚 Egg Bhurji + Paratha',
                'items': [
                    '2 egg bhurji (scrambled eggs with onions, tomatoes)',
                    '2 parathas',
                    '1 cup tea'
                ],
                'calories': '~400 cal',
                'cost': '₹30-40'
            },
            'mid_morning': {
                'meal': '🍌 Boiled Eggs + Banana',
                'items': [
                    '2 boiled eggs',
                    '1 banana'
                ],
                'calories': '~250 cal',
                'cost': '₹20-25'
            },
            'lunch': {
                'meal': '🍛 Chicken Curry + Rice + Dal',
                'items': [
                    '1 cup rice or 2 chapati',
                    '100g chicken curry (home-cooked)',
                    '1 bowl dal',
                    'Salad'
                ],
                'calories': '~550 cal',
                'cost': '₹60-80'
            },
            'evening': {
                'meal': '☕ Tea + Boiled Egg',
                'items': [
                    '1 cup tea',
                    '1 boiled egg or chana chaat'
                ],
                'calories': '~150 cal',
                'cost': '₹15-20'
            },
            'dinner': {
                'meal': '🥘 Egg Curry + Roti',
                'items': [
                    '3 chapati',
                    '2 egg curry',
                    '1 bowl vegetable sabzi',
                    'Salad'
                ],
                'calories': '~500 cal',
                'cost': '₹40-60'
            },
            'before_bed': {
                'meal': '🥛 Milk',
                'items': [
                    '1 glass warm milk'
                ],
                'calories': '~150 cal',
                'cost': '₹10-15'
            }
        }
    
    elif budget == 'Medium':
        plan = {
            'breakfast': {
                'meal': '🍳 Omelette + Toast + Milk',
                'items': [
                    '3 egg omelette with veggies',
                    '2 whole wheat toast',
                    '1 glass milk',
                    'Handful of almonds'
                ],
                'calories': '~450 cal',
                'cost': '₹50-70'
            },
            'mid_morning': {
                'meal': '🥚 Boiled Eggs + Fruit',
                'items': [
                    '3 boiled eggs (2 whole + 1 white)',
                    '1 apple or banana',
                    'Green tea'
                ],
                'calories': '~270 cal',
                'cost': '₹30-40'
            },
            'lunch': {
                'meal': '🍛 Chicken/Fish + Rice + Dal',
                'items': [
                    '150g grilled chicken or fish curry',
                    '1 cup brown rice + 1 chapati',
                    '1 bowl dal',
                    '1 bowl vegetable sabzi',
                    'Large salad'
                ],
                'calories': '~650 cal',
                'cost': '₹100-140'
            },
            'evening': {
                'meal': '🥤 Protein Shake + Snack',
                'items': [
                    'Banana protein shake',
                    'Boiled eggs (2) or chicken tikka (2-3 pieces)'
                ],
                'calories': '~300 cal',
                'cost': '₹50-70'
            },
            'dinner': {
                'meal': '🥗 Fish/Chicken + Roti',
                'items': [
                    '3 chapati',
                    '120g fish curry or chicken curry',
                    '1 bowl dal or sabzi',
                    'Salad'
                ],
                'calories': '~550 cal',
                'cost': '₹80-100'
            },
            'before_bed': {
                'meal': '🥛 Protein Milk',
                'items': [
                    '1 glass milk with protein powder'
                ],
                'calories': '~180 cal',
                'cost': '₹30-40'
            }
        }
    
    else:  # High Budget
        plan = {
            'breakfast': {
                'meal': '🍳 Premium Breakfast',
                'items': [
                    '4 egg white omelette + 1 whole egg',
                    'Multigrain toast with peanut butter',
                    'Whey protein shake',
                    'Mixed nuts (almonds, walnuts)',
                    'Fresh juice'
                ],
                'calories': '~550 cal',
                'cost': '₹120-150'
            },
            'mid_morning': {
                'meal': '🥚 Eggs + Fruits + Nuts',
                'items': [
                    '3 boiled eggs (2 whole + 1 white)',
                    'Mixed fruits with Greek yogurt',
                    'Mixed nuts (15-20)',
                    'Green tea'
                ],
                'calories': '~350 cal',
                'cost': '₹70-90'
            },
            'lunch': {
                'meal': '🍛 Premium Non-Veg Thali',
                'items': [
                    '200g grilled chicken/salmon/prawns',
                    '1 cup quinoa + 1 multigrain roti',
                    '1 bowl dal',
                    'Grilled vegetables (broccoli, bell peppers)',
                    'Large mixed salad with olive oil',
                    'Buttermilk'
                ],
                'calories': '~750 cal',
                'cost': '₹200-250'
            },
            'evening': {
                'meal': '🥤 Premium Protein Snack',
                'items': [
                    'Whey isolate protein shake with banana and peanut butter',
                    'Grilled chicken breast (100g) or tuna sandwich',
                    'Mixed dry fruits'
                ],
                'calories': '~400 cal',
                'cost': '₹100-120'
            },
            'dinner': {
                'meal': '🥘 Premium Dinner',
                'items': [
                    '150g grilled fish or chicken tikka',
                    '3 multigrain roti',
                    '1 bowl dal or chickpea curry',
                    'Stir-fried vegetables',
                    'Large salad with avocado',
                    'Greek yogurt'
                ],
                'calories': '~650 cal',
                'cost': '₹150-200'
            },
            'before_bed': {
                'meal': '🥛 Casein Shake',
                'items': [
                    'Casein protein shake',
                    'Soaked almonds (5-6)'
                ],
                'calories': '~200 cal',
                'cost': '₹60-80'
            }
        }
    
    # Add macro breakdown
    plan['macros'] = {
        'total_calories': calories,
        'protein': f'{protein_g}g',
        'carbohydrates': f'{carbs_g}g',
        'fats': f'{fat_g}g'
    }
    
    plan['tips'] = [
        '💧 Drink 3-4 liters of water daily',
        '🍗 Prefer grilled/boiled over fried preparations',
        '🥗 Include salads with every major meal',
        '🐟 Include fish 2-3 times a week for omega-3',
        '⏰ Maintain consistent meal timings',
        '🥚 Egg whites are great low-calorie protein source'
    ]
    
    return plan


def format_meal_time(meal_name):
    """
    Return appropriate meal timing
    """
    timings = {
        'breakfast': '7:00 AM - 8:00 AM',
        'mid_morning': '10:30 AM - 11:00 AM',
        'lunch': '1:00 PM - 2:00 PM',
        'evening': '4:30 PM - 5:30 PM',
        'dinner': '7:30 PM - 8:30 PM',
        'before_bed': '10:00 PM - 10:30 PM'
    }
    return timings.get(meal_name, '')


if __name__ == "__main__":
    # Test the module
    plan = get_diet_plan(2200, 'Vegetarian', 'Medium', 'Muscle Gain')
    print("Diet Plan for Vegetarian (Medium Budget, Muscle Gain):")
    print(f"\nMacros: {plan['macros']}")
    print("\nMeals:")
    for meal_type, details in plan.items():
        if meal_type not in ['macros', 'tips']:
            print(f"\n{meal_type.upper().replace('_', ' ')}:")
            print(f"  {details['meal']}")
            print(f"  Timing: {format_meal_time(meal_type)}")
            print(f"  Calories: {details['calories']}")
            print(f"  Cost: {details['cost']}")
