"""
Workout Planner Module
Generates personalized workout plans based on fitness goals and equipment availability
"""

def get_workout_plan(goal, equipment, fitness_level='Beginner'):
    """
    Generate personalized workout plan
    
    Args:
        goal: Fitness goal ('Weight Loss', 'Muscle Gain', 'Maintenance')
        equipment: 'Gym' or 'Home'
        fitness_level: Fitness level (default: 'Beginner')
    
    Returns:
        Dictionary containing weekly workout plan
    """
    
    if goal == 'Weight Loss':
        return get_weight_loss_plan(equipment)
    elif goal == 'Muscle Gain':
        return get_muscle_gain_plan(equipment)
    else:  # Maintenance
        return get_maintenance_plan(equipment)


def get_weight_loss_plan(equipment):
    """
    Weight loss focused workout plan (High cardio, moderate strength)
    """
    if equipment == 'Gym':
        plan = {
            'Monday': {
                'focus': 'Cardio + Core',
                'exercises': [
                    '🏃 Treadmill Running - 30 mins (moderate pace)',
                    '🚴 Stationary Bike - 15 mins (HIIT)',
                    '💪 Planks - 3 sets x 30 seconds',
                    '💪 Crunches - 3 sets x 15 reps',
                    '💪 Russian Twists - 3 sets x 20 reps'
                ]
            },
            'Tuesday': {
                'focus': 'Upper Body Strength',
                'exercises': [
                    '💪 Bench Press - 3 sets x 12 reps',
                    '💪 Lat Pulldown - 3 sets x 12 reps',
                    '💪 Shoulder Press - 3 sets x 10 reps',
                    '💪 Bicep Curls - 3 sets x 12 reps',
                    '💪 Tricep Extensions - 3 sets x 12 reps'
                ]
            },
            'Wednesday': {
                'focus': 'Cardio + Abs',
                'exercises': [
                    '🏃 Treadmill Incline Walk - 30 mins',
                    '⚡ Elliptical - 20 mins',
                    '💪 Leg Raises - 3 sets x 15 reps',
                    '💪 Mountain Climbers - 3 sets x 20 reps',
                    '💪 Bicycle Crunches - 3 sets x 20 reps'
                ]
            },
            'Thursday': {
                'focus': 'Lower Body Strength',
                'exercises': [
                    '💪 Squats - 3 sets x 12 reps',
                    '💪 Leg Press - 3 sets x 12 reps',
                    '💪 Lunges - 3 sets x 10 reps each leg',
                    '💪 Leg Curls - 3 sets x 12 reps',
                    '💪 Calf Raises - 3 sets x 15 reps'
                ]
            },
            'Friday': {
                'focus': 'HIIT Cardio',
                'exercises': [
                    '⚡ Burpees - 4 sets x 10 reps',
                    '⚡ Jump Rope - 4 sets x 1 min',
                    '⚡ Box Jumps - 4 sets x 12 reps',
                    '⚡ Battle Ropes - 4 sets x 30 seconds',
                    '🏃 Treadmill Sprints - 5 sets x 1 min'
                ]
            },
            'Saturday': {
                'focus': 'Active Recovery',
                'exercises': [
                    '🏊 Swimming - 30 mins or',
                    '🚶 Brisk Walking - 45 mins',
                    '🧘 Stretching - 15 mins',
                    '🧘 Yoga - 20 mins'
                ]
            },
            'Sunday': {
                'focus': 'Rest Day',
                'exercises': ['😴 Complete Rest or Light Stretching']
            }
        }
    else:  # Home
        plan = {
            'Monday': {
                'focus': 'Cardio + Core',
                'exercises': [
                    '🏃 Jogging/Running - 30 mins',
                    '⚡ Jumping Jacks - 4 sets x 30 reps',
                    '⚡ High Knees - 4 sets x 30 seconds',
                    '💪 Planks - 3 sets x 45 seconds',
                    '💪 Crunches - 3 sets x 20 reps'
                ]
            },
            'Tuesday': {
                'focus': 'Upper Body',
                'exercises': [
                    '💪 Push-ups - 4 sets x 12-15 reps',
                    '💪 Pike Push-ups - 3 sets x 10 reps',
                    '💪 Tricep Dips (chair) - 3 sets x 12 reps',
                    '💪 Superman Exercise - 3 sets x 15 reps',
                    '💪 Arm Circles - 3 sets x 20 reps'
                ]
            },
            'Wednesday': {
                'focus': 'Cardio + Abs',
                'exercises': [
                    '🏃 Running/Jogging - 30 mins',
                    '⚡ Burpees - 4 sets x 10 reps',
                    '💪 Mountain Climbers - 4 sets x 20 reps',
                    '💪 Leg Raises - 3 sets x 15 reps',
                    '💪 Bicycle Crunches - 3 sets x 25 reps'
                ]
            },
            'Thursday': {
                'focus': 'Lower Body',
                'exercises': [
                    '💪 Bodyweight Squats - 4 sets x 20 reps',
                    '💪 Lunges - 4 sets x 12 reps each leg',
                    '💪 Jump Squats - 3 sets x 15 reps',
                    '💪 Wall Sit - 3 sets x 45 seconds',
                    '💪 Calf Raises - 4 sets x 20 reps'
                ]
            },
            'Friday': {
                'focus': 'HIIT Training',
                'exercises': [
                    '⚡ Burpees - 5 sets x 10 reps',
                    '⚡ Jump Rope - 5 sets x 1 min',
                    '⚡ High Knees - 4 sets x 30 seconds',
                    '⚡ Mountain Climbers - 4 sets x 20 reps',
                    '⚡ Jumping Jacks - 4 sets x 30 reps'
                ]
            },
            'Saturday': {
                'focus': 'Active Recovery',
                'exercises': [
                    '🚶 Brisk Walking - 45 mins',
                    '🧘 Yoga Flow - 30 mins',
                    '🧘 Stretching - 15 mins'
                ]
            },
            'Sunday': {
                'focus': 'Rest Day',
                'exercises': ['😴 Complete Rest or Light Stretching']
            }
        }
    
    return plan


def get_muscle_gain_plan(equipment):
    """
    Muscle gain focused workout plan (High strength training)
    """
    if equipment == 'Gym':
        plan = {
            'Monday': {
                'focus': 'Chest + Triceps',
                'exercises': [
                    '💪 Barbell Bench Press - 4 sets x 8-10 reps',
                    '💪 Incline Dumbbell Press - 4 sets x 10 reps',
                    '💪 Chest Flyes - 3 sets x 12 reps',
                    '💪 Cable Crossover - 3 sets x 12 reps',
                    '💪 Tricep Pushdowns - 4 sets x 12 reps',
                    '💪 Overhead Tricep Extension - 3 sets x 10 reps'
                ]
            },
            'Tuesday': {
                'focus': 'Back + Biceps',
                'exercises': [
                    '💪 Deadlifts - 4 sets x 8 reps',
                    '💪 Pull-ups - 4 sets x 8-10 reps',
                    '💪 Barbell Rows - 4 sets x 10 reps',
                    '💪 Lat Pulldown - 3 sets x 12 reps',
                    '💪 Barbell Curls - 4 sets x 10 reps',
                    '💪 Hammer Curls - 3 sets x 12 reps'
                ]
            },
            'Wednesday': {
                'focus': 'Legs',
                'exercises': [
                    '💪 Barbell Squats - 4 sets x 8-10 reps',
                    '💪 Leg Press - 4 sets x 12 reps',
                    '💪 Romanian Deadlifts - 4 sets x 10 reps',
                    '💪 Leg Extensions - 3 sets x 12 reps',
                    '💪 Leg Curls - 3 sets x 12 reps',
                    '💪 Calf Raises - 4 sets x 15 reps'
                ]
            },
            'Thursday': {
                'focus': 'Shoulders + Abs',
                'exercises': [
                    '💪 Military Press - 4 sets x 8-10 reps',
                    '💪 Lateral Raises - 4 sets x 12 reps',
                    '💪 Front Raises - 3 sets x 12 reps',
                    '💪 Rear Delt Flyes - 3 sets x 12 reps',
                    '💪 Shrugs - 4 sets x 15 reps',
                    '💪 Hanging Leg Raises - 3 sets x 12 reps'
                ]
            },
            'Friday': {
                'focus': 'Arms (Focused)',
                'exercises': [
                    '💪 Close-Grip Bench Press - 4 sets x 10 reps',
                    '💪 Preacher Curls - 4 sets x 10 reps',
                    '💪 Skull Crushers - 4 sets x 10 reps',
                    '💪 Concentration Curls - 3 sets x 12 reps',
                    '💪 Cable Rope Pushdown - 3 sets x 12 reps',
                    '💪 Cable Bicep Curls - 3 sets x 12 reps'
                ]
            },
            'Saturday': {
                'focus': 'Light Cardio + Core',
                'exercises': [
                    '🚴 Stationary Bike - 20 mins (light)',
                    '💪 Planks - 3 sets x 1 min',
                    '💪 Ab Wheel Rollouts - 3 sets x 10 reps',
                    '🧘 Stretching - 15 mins'
                ]
            },
            'Sunday': {
                'focus': 'Rest Day',
                'exercises': ['😴 Complete Rest for Muscle Recovery']
            }
        }
    else:  # Home
        plan = {
            'Monday': {
                'focus': 'Chest + Triceps',
                'exercises': [
                    '💪 Push-ups - 5 sets x 15-20 reps',
                    '💪 Diamond Push-ups - 4 sets x 12 reps',
                    '💪 Wide Push-ups - 4 sets x 12 reps',
                    '💪 Decline Push-ups - 3 sets x 12 reps',
                    '💪 Tricep Dips (chair) - 4 sets x 15 reps',
                    '💪 Close-Grip Push-ups - 3 sets x 12 reps'
                ]
            },
            'Tuesday': {
                'focus': 'Back + Biceps',
                'exercises': [
                    '💪 Pull-ups (if bar available) - 4 sets x max reps',
                    '💪 Superman Exercise - 4 sets x 15 reps',
                    '💪 Reverse Snow Angels - 3 sets x 12 reps',
                    '💪 Chin-ups (if bar) - 4 sets x max reps',
                    '💪 Towel Curls - 4 sets x 15 reps',
                    '💪 Isometric Bicep Hold - 3 sets x 30 sec'
                ]
            },
            'Wednesday': {
                'focus': 'Legs',
                'exercises': [
                    '💪 Pistol Squats - 4 sets x 8 reps each leg',
                    '💪 Bulgarian Split Squats - 4 sets x 12 reps',
                    '💪 Jump Squats - 4 sets x 15 reps',
                    '💪 Single Leg Deadlifts - 4 sets x 10 reps',
                    '💪 Walking Lunges - 4 sets x 12 reps each',
                    '💪 Calf Raises - 4 sets x 20 reps'
                ]
            },
            'Thursday': {
                'focus': 'Shoulders + Abs',
                'exercises': [
                    '💪 Pike Push-ups - 4 sets x 12 reps',
                    '💪 Handstand Hold (wall) - 3 sets x 30 sec',
                    '💪 Lateral Arm Raises (bottles) - 4 sets x 15 reps',
                    '💪 Front Raises (bottles) - 3 sets x 15 reps',
                    '💪 Planks - 4 sets x 1 min',
                    '💪 Russian Twists - 4 sets x 25 reps'
                ]
            },
            'Friday': {
                'focus': 'Full Body',
                'exercises': [
                    '💪 Burpees - 5 sets x 15 reps',
                    '💪 Mountain Climbers - 4 sets x 25 reps',
                    '💪 Push-ups - 4 sets x 15 reps',
                    '💪 Squats - 4 sets x 20 reps',
                    '💪 Plank to Push-up - 3 sets x 10 reps',
                    '💪 Bicycle Crunches - 3 sets x 25 reps'
                ]
            },
            'Saturday': {
                'focus': 'Core + Flexibility',
                'exercises': [
                    '💪 Planks - 4 sets x 1 min',
                    '💪 Side Planks - 3 sets x 45 sec each',
                    '💪 Leg Raises - 4 sets x 15 reps',
                    '🧘 Yoga Flow - 30 mins',
                    '🧘 Stretching - 15 mins'
                ]
            },
            'Sunday': {
                'focus': 'Rest Day',
                'exercises': ['😴 Complete Rest for Muscle Recovery']
            }
        }
    
    return plan


def get_maintenance_plan(equipment):
    """
    Maintenance focused workout plan (Balanced approach)
    """
    if equipment == 'Gym':
        plan = {
            'Monday': {
                'focus': 'Upper Body',
                'exercises': [
                    '💪 Bench Press - 3 sets x 10 reps',
                    '💪 Lat Pulldown - 3 sets x 10 reps',
                    '💪 Shoulder Press - 3 sets x 10 reps',
                    '💪 Bicep Curls - 3 sets x 12 reps',
                    '💪 Tricep Extensions - 3 sets x 12 reps'
                ]
            },
            'Tuesday': {
                'focus': 'Cardio',
                'exercises': [
                    '🏃 Treadmill - 25 mins (moderate)',
                    '🚴 Stationary Bike - 15 mins',
                    '💪 Core Circuit - 15 mins'
                ]
            },
            'Wednesday': {
                'focus': 'Lower Body',
                'exercises': [
                    '💪 Squats - 3 sets x 12 reps',
                    '💪 Leg Press - 3 sets x 12 reps',
                    '💪 Lunges - 3 sets x 10 reps each',
                    '💪 Leg Curls - 3 sets x 12 reps',
                    '💪 Calf Raises - 3 sets x 15 reps'
                ]
            },
            'Thursday': {
                'focus': 'Cardio + Core',
                'exercises': [
                    '🏃 Running - 20 mins',
                    '⚡ Elliptical - 15 mins',
                    '💪 Planks - 3 sets x 45 sec',
                    '💪 Crunches - 3 sets x 15 reps'
                ]
            },
            'Friday': {
                'focus': 'Full Body',
                'exercises': [
                    '💪 Deadlifts - 3 sets x 10 reps',
                    '💪 Pull-ups - 3 sets x 8 reps',
                    '💪 Push-ups - 3 sets x 15 reps',
                    '💪 Squats - 3 sets x 12 reps',
                    '🏃 Light Cardio - 15 mins'
                ]
            },
            'Saturday': {
                'focus': 'Active Recovery',
                'exercises': [
                    '🏊 Swimming - 30 mins or',
                    '🚶 Walking - 45 mins',
                    '🧘 Yoga - 20 mins'
                ]
            },
            'Sunday': {
                'focus': 'Rest Day',
                'exercises': ['😴 Complete Rest']
            }
        }
    else:  # Home
        plan = {
            'Monday': {
                'focus': 'Upper Body',
                'exercises': [
                    '💪 Push-ups - 4 sets x 15 reps',
                    '💪 Pike Push-ups - 3 sets x 10 reps',
                    '💪 Tricep Dips - 3 sets x 12 reps',
                    '💪 Superman - 3 sets x 15 reps'
                ]
            },
            'Tuesday': {
                'focus': 'Cardio',
                'exercises': [
                    '🏃 Jogging - 30 mins',
                    '⚡ Jumping Jacks - 3 sets x 30 reps',
                    '⚡ High Knees - 3 sets x 30 sec'
                ]
            },
            'Wednesday': {
                'focus': 'Lower Body',
                'exercises': [
                    '💪 Squats - 4 sets x 15 reps',
                    '💪 Lunges - 4 sets x 12 reps each',
                    '💪 Wall Sit - 3 sets x 45 sec',
                    '💪 Calf Raises - 4 sets x 20 reps'
                ]
            },
            'Thursday': {
                'focus': 'Cardio + Core',
                'exercises': [
                    '🏃 Running - 25 mins',
                    '💪 Planks - 3 sets x 1 min',
                    '💪 Mountain Climbers - 3 sets x 20 reps',
                    '💪 Bicycle Crunches - 3 sets x 20 reps'
                ]
            },
            'Friday': {
                'focus': 'Full Body',
                'exercises': [
                    '💪 Burpees - 4 sets x 12 reps',
                    '💪 Push-ups - 3 sets x 15 reps',
                    '💪 Squats - 3 sets x 15 reps',
                    '💪 Plank - 3 sets x 45 sec'
                ]
            },
            'Saturday': {
                'focus': 'Active Recovery',
                'exercises': [
                    '🚶 Brisk Walking - 45 mins',
                    '🧘 Yoga - 30 mins',
                    '🧘 Stretching - 15 mins'
                ]
            },
            'Sunday': {
                'focus': 'Rest Day',
                'exercises': ['😴 Complete Rest']
            }
        }
    
    return plan


if __name__ == "__main__":
    # Test the module
    plan = get_workout_plan('Weight Loss', 'Home')
    print("Weight Loss Plan (Home):")
    for day, details in plan.items():
        print(f"\n{day} - {details['focus']}")
        for exercise in details['exercises']:
            print(f"  {exercise}")
