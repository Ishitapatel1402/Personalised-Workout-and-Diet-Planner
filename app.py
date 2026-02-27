"""
Personalized Workout and Diet Planner - Streamlit Application
An AI-powered fitness recommendation system for students
"""

import streamlit as st
import pandas as pd
from bmi_calculator import get_fitness_metrics
from workout_planner import get_workout_plan
from diet_planner import get_diet_plan, format_meal_time
from model import predict_from_saved_model, rule_based_prediction
import os


# Page configuration
st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FF6347;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .workout-day {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 5px solid #4CAF50;
    }
    .meal-box {
        background-color: #fff9e6;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 5px solid #FFA500;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6347;
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)


def main():
    """
    Main application function
    """
    
    # Header
    st.markdown('<p class="main-header">💪 AI-Powered Fitness Planner</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Personalized Workout & Indian Diet Recommendation System for Students</p>', 
                unsafe_allow_html=True)
    
    # Sidebar for user inputs
    st.sidebar.header("📝 Your Profile")
    st.sidebar.markdown("---")
    
    # Personal Information
    st.sidebar.subheader("Personal Information")
    age = st.sidebar.number_input("Age (years)", min_value=15, max_value=100, value=22, step=1)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    
    # Body Metrics
    st.sidebar.subheader("Body Metrics")
    height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170, step=1)
    weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70, step=1)
    
    # Lifestyle
    st.sidebar.subheader("Lifestyle")
    activity_level = st.sidebar.selectbox(
        "Activity Level",
        [
            "Sedentary (little or no exercise)",
            "Lightly Active (exercise 1-3 days/week)",
            "Moderately Active (exercise 3-5 days/week)",
            "Very Active (exercise 6-7 days/week)",
            "Extra Active (very intense exercise daily)"
        ]
    )
    
    # Preferences
    st.sidebar.subheader("Preferences")
    equipment = st.sidebar.selectbox("Available Equipment", ["Home", "Gym"])
    food_preference = st.sidebar.selectbox("Food Preference", ["Vegetarian", "Non-Vegetarian"])
    budget = st.sidebar.selectbox("Budget", ["Low", "Medium", "High"])
    
    st.sidebar.markdown("---")
    
    # Generate button
    generate_plan = st.sidebar.button("🚀 Generate My Plan")
    
    # Main content area
    if generate_plan:
        with st.spinner("🔄 Analyzing your profile and generating personalized plan..."):
            
            # Calculate fitness metrics
            metrics = get_fitness_metrics(weight, height, age, gender, activity_level, "Maintenance")
            bmi = metrics['bmi']
            category = metrics['category']
            health_status = metrics['health_status']
            bmr = metrics['bmr']
            tdee = metrics['tdee']
            
            # Predict fitness goal using AI
            try:
                predicted_goal, confidence = predict_from_saved_model(
                    age, gender, height, weight, bmi, activity_level
                )
            except:
                # Fallback to rule-based
                predicted_goal, confidence = rule_based_prediction(bmi, age, activity_level)
            
            # Recalculate target calories based on predicted goal
            final_metrics = get_fitness_metrics(weight, height, age, gender, activity_level, predicted_goal)
            target_calories = final_metrics['target_calories']
            
            # Display results in tabs
            tab1, tab2, tab3, tab4 = st.tabs(["📊 Health Metrics", "🤖 AI Prediction", "💪 Workout Plan", "🍽️ Diet Plan"])
            
            # Tab 1: Health Metrics
            with tab1:
                st.header("📊 Your Health Metrics")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("BMI", f"{bmi}", category)
                
                with col2:
                    st.metric("BMR", f"{bmr} cal", "Basal Metabolic Rate")
                
                with col3:
                    st.metric("TDEE", f"{tdee} cal", "Daily Energy Expenditure")
                
                with col4:
                    st.metric("Target Calories", f"{target_calories} cal", "For Your Goal")
                
                st.markdown("---")
                
                # Health status
                st.subheader("Health Status")
                st.info(f"{health_status}")
                
                # Metrics explanation
                with st.expander("ℹ️ Understanding Your Metrics"):
                    st.markdown("""
                    **BMI (Body Mass Index)**: Measure of body fat based on height and weight
                    - Underweight: < 18.5
                    - Normal: 18.5 - 24.9
                    - Overweight: 25.0 - 29.9
                    - Obese: ≥ 30.0
                    
                    **BMR (Basal Metabolic Rate)**: Calories your body burns at rest
                    
                    **TDEE (Total Daily Energy Expenditure)**: Total calories you burn per day including activity
                    
                    **Target Calories**: Recommended daily calorie intake based on your fitness goal
                    """)
            
            # Tab 2: AI Prediction
            with tab2:
                st.header("🤖 AI-Powered Goal Prediction")
                
                st.success(f"**Recommended Fitness Goal: {predicted_goal}**")
                
                st.subheader("Confidence Scores")
                
                # Create a dataframe for better visualization
                conf_df = pd.DataFrame({
                    'Goal': list(confidence.keys()),
                    'Confidence (%)': list(confidence.values())
                })
                conf_df = conf_df.sort_values('Confidence (%)', ascending=False)
                
                # Display as bar chart
                st.bar_chart(conf_df.set_index('Goal'))
                
                # Display table
                st.dataframe(conf_df, use_container_width=True)
                
                # Explanation
                st.markdown("---")
                st.subheader("Why This Goal?")
                
                if predicted_goal == "Weight Loss":
                    st.info("""
                    **Weight Loss Recommended** because:
                    - Your BMI indicates you're above the healthy weight range
                    - Creating a calorie deficit will help you reach a healthier weight
                    - Combined with cardio and strength training for optimal results
                    """)
                elif predicted_goal == "Muscle Gain":
                    st.info("""
                    **Muscle Gain Recommended** because:
                    - Your BMI is in the lower range
                    - Your activity level suggests you're ready for strength training
                    - Building muscle will improve your overall health and metabolism
                    """)
                else:
                    st.info("""
                    **Maintenance Recommended** because:
                    - Your BMI is in the healthy range
                    - Focus on maintaining your current weight while staying fit
                    - Balanced approach to nutrition and exercise
                    """)
            
            # Tab 3: Workout Plan
            with tab3:
                st.header("💪 Your Personalized Workout Plan")
                
                st.info(f"**Goal**: {predicted_goal} | **Equipment**: {equipment}")
                
                # Get workout plan
                workout_plan = get_workout_plan(predicted_goal, equipment)
                
                # Display weekly plan
                for day, details in workout_plan.items():
                    with st.expander(f"**{day}** - {details['focus']}", expanded=(day == 'Monday')):
                        for exercise in details['exercises']:
                            st.markdown(f"- {exercise}")
                
                # Workout tips
                st.markdown("---")
                st.subheader("💡 Workout Tips")
                st.markdown("""
                - ✅ Warm up for 5-10 minutes before each workout
                - ✅ Cool down and stretch for 5-10 minutes after workout
                - ✅ Stay hydrated throughout your workout
                - ✅ Listen to your body and rest when needed
                - ✅ Maintain proper form to prevent injuries
                - ✅ Progress gradually - don't rush
                """)
            
            # Tab 4: Diet Plan
            with tab4:
                st.header("🍽️ Your Personalized Indian Diet Plan")
                
                st.info(f"**Daily Calories**: {target_calories} cal | **Food**: {food_preference} | **Budget**: {budget}")
                
                # Get diet plan
                diet_plan = get_diet_plan(target_calories, food_preference, budget, predicted_goal)
                
                # Display macros
                st.subheader("📊 Daily Macro Distribution")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("🥩 Protein", diet_plan['macros']['protein'])
                with col2:
                    st.metric("🍚 Carbs", diet_plan['macros']['carbohydrates'])
                with col3:
                    st.metric("🥑 Fats", diet_plan['macros']['fats'])
                
                st.markdown("---")
                
                # Display meal plan
                st.subheader("📅 Daily Meal Plan")
                
                meal_order = ['breakfast', 'mid_morning', 'lunch', 'evening', 'dinner', 'before_bed']
                
                for meal_type in meal_order:
                    if meal_type in diet_plan:
                        meal = diet_plan[meal_type]
                        
                        with st.expander(f"**{meal_type.upper().replace('_', ' ')}** - {format_meal_time(meal_type)}", 
                                       expanded=(meal_type == 'breakfast')):
                            st.markdown(f"### {meal['meal']}")
                            
                            st.markdown("**Items:**")
                            for item in meal['items']:
                                st.markdown(f"- {item}")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown(f"**Calories:** {meal['calories']}")
                            with col2:
                                st.markdown(f"**Cost:** {meal['cost']}")
                
                # Diet tips
                st.markdown("---")
                st.subheader("💡 Diet Tips")
                for tip in diet_plan['tips']:
                    st.markdown(f"- {tip}")
                
                # Additional tips
                st.markdown("""
                - ✅ Eat at regular intervals
                - ✅ Don't skip meals, especially breakfast
                - ✅ Meal prep on weekends to save time
                - ✅ Avoid processed and junk food
                - ✅ Get adequate sleep (7-8 hours)
                """)
            
            # Summary section
            st.markdown("---")
            st.header("📋 Quick Summary")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                ### Your Plan Overview
                - **Goal**: {goal}
                - **BMI**: {bmi} ({category})
                - **Daily Calories**: {calories} cal
                - **Workout Focus**: {equipment}-based {goal} program
                """.format(
                    goal=predicted_goal,
                    bmi=bmi,
                    category=category,
                    calories=target_calories,
                    equipment=equipment
                ))
            
            with col2:
                st.markdown("""
                ### Key Actions
                - 🏃 Follow the workout routine consistently
                - 🍽️ Stick to the meal plan and timings
                - 💧 Drink 3-4 liters of water daily
                - 😴 Get 7-8 hours of sleep
                - 📊 Track your progress weekly
                """)
            
            # Download section
            st.markdown("---")
            st.subheader("📥 Save Your Plan")
            
            # Create a summary text
            summary = f"""
PERSONALIZED FITNESS PLAN
=========================

PROFILE:
- Age: {age} years
- Gender: {gender}
- Height: {height} cm
- Weight: {weight} kg
- Activity: {activity_level}

HEALTH METRICS:
- BMI: {bmi} ({category})
- BMR: {bmr} cal/day
- TDEE: {tdee} cal/day
- Target Calories: {target_calories} cal/day

RECOMMENDED GOAL: {predicted_goal}

WORKOUT PLAN ({equipment}):
"""
            for day, details in workout_plan.items():
                summary += f"\n{day} - {details['focus']}\n"
                for exercise in details['exercises']:
                    summary += f"  • {exercise}\n"
            
            summary += f"\n\nDIET PLAN ({food_preference} - {budget} Budget):\n"
            summary += f"Daily Macros: Protein={diet_plan['macros']['protein']}, Carbs={diet_plan['macros']['carbohydrates']}, Fats={diet_plan['macros']['fats']}\n\n"
            
            for meal_type in meal_order:
                if meal_type in diet_plan:
                    meal = diet_plan[meal_type]
                    summary += f"{meal_type.upper().replace('_', ' ')}: {meal['meal']}\n"
                    summary += f"Time: {format_meal_time(meal_type)}\n"
                    summary += f"Calories: {meal['calories']}\n\n"
            
            st.download_button(
                label="📄 Download Plan as Text File",
                data=summary,
                file_name="my_fitness_plan.txt",
                mime="text/plain"
            )
            
    else:
        # Welcome message when no plan is generated
        st.info("👈 Fill in your details in the sidebar and click **Generate My Plan** to get started!")
        
        # Feature highlights
        st.header("✨ Features")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🤖 AI-Powered")
            st.write("Machine learning model predicts your optimal fitness goal based on your profile")
        
        with col2:
            st.subheader("🇮🇳 Indian Diet")
            st.write("Meal plans tailored to Indian cuisine with both veg and non-veg options")
        
        with col3:
            st.subheader("💰 Budget-Friendly")
            st.write("Diet recommendations that fit your budget - Low, Medium, or High")
        
        st.markdown("---")
        
        st.header("🎯 How It Works")
        
        st.markdown("""
        1. **Enter Your Details**: Provide your age, gender, height, weight, and activity level
        2. **AI Analysis**: Our ML model analyzes your profile and predicts the best fitness goal
        3. **Get Personalized Plan**: Receive customized workout routines and Indian meal plans
        4. **Track Progress**: Follow the plan and achieve your fitness goals!
        """)
        
        st.markdown("---")
        
        st.header("📊 About This System")
        
        st.markdown("""
        This intelligent fitness recommendation system uses:
        - **Machine Learning**: Random Forest classifier for goal prediction
        - **BMI & BMR Calculations**: Scientific formulas for accurate metrics
        - **Personalized Recommendations**: Tailored to Indian students' lifestyle
        - **Budget Consideration**: Affordable meal options
        - **Equipment Flexibility**: Plans for both home and gym workouts
        """)


if __name__ == "__main__":
    main()
