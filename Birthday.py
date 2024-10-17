import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Shristee!", layout="centered")

# Welcome Screen
st.title("🎉 Happy Birthday, Shristee! 🎉")
st.write("Can you help protect the *Salix* plants from herbivores today?")
st.write("Use your knowledge of plant volatiles to attract predators and defend the plants!")

# Starting the adventure
if st.button("Start Your Adventure"):
    st.write("Your adventure begins now! 🌿")

    # Adventure Scenarios
    score = 0
    scenarios = [
        {
            "scenario": "Herbivores are attacking *Salix* plants! How will you help the plant release volatiles to attract the best predator?",
            "options": ["Increase volatile release right away", "Wait until herbivores cause more damage", "Release low levels of volatiles over time"],
            "answer": "Increase volatile release right away",
            "feedback": "Great choice! Releasing volatiles early helps attract predators before the herbivores cause too much damage."
        },
        {
            "scenario": "The herbivores are adapting to your strategy. What should the plant do next?",
            "options": ["Change the composition of volatiles", "Keep releasing the same volatiles", "Stop volatile release"],
            "answer": "Change the composition of volatiles",
            "feedback": "Smart move! Changing the volatile mix confuses herbivores and keeps predators coming."
        },
        {
            "scenario": "It's mid-season, and more predators are available. How can you maximize predator attraction?",
            "options": ["Release high bursts of volatiles during the day", "Release volatiles at night", "Release volatiles in steady low amounts"],
            "answer": "Release high bursts of volatiles during the day",
            "feedback": "Correct! Predators are more active during the day, so daytime bursts are most effective."
        }
    ]
    
    for i, scenario in enumerate(scenarios):
        st.subheader(scenario["scenario"])
        choice = st.radio("Choose your strategy:", scenario["options"], key=f"radio_{i}")
        if st.button("Submit", key=f"button_{i}"):
            if choice == scenario["answer"]:
                st.success(scenario["feedback"])
                score += 1
            else:
                st.error("Oops! Not the best strategy, but keep going!")
            time.sleep(1)  # Pause for dramatic effect
            st.write(f"Your current score: {score}/{len(scenarios)}")
    
    # Final Score
    st.balloons()
    st.write(f"🎉 You completed the adventure with a score of {score}/{len(scenarios)}! 🎉")
    if score == len(scenarios):
        st.success("Wow, perfect score! You're a *Salix* defender expert!")
    else:
        st.write("Nice try! You've done a great job protecting the *Salix* plants!")

# Footer birthday message
st.write("Wishing you a fantastic birthday filled with joy and success, Shristee! 💐")
