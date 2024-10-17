import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Happy Birthday Shristee!", layout="centered")

# Initialize session state to track the current question, score, and submissions
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.submissions = [False] * 3  # 3 questions total, initially all False

# Welcome screen
st.title("🎉 Happy Birthday, Shristee! 🎉")
st.write("Can you help protect the *Salix* plants from herbivores today?")
st.write("Use your knowledge of plant volatiles to attract predators and defend the plants!")

# Adventure Scenarios
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

# Start the adventure button
if st.session_state.current_question == 0:
    if st.button("Start Your Adventure"):
        st.session_state.current_question = 1

# Display all questions, but initially make them inactive/faded
for idx, scenario in enumerate(scenarios):
    if st.session_state.current_question >= idx + 1:
        st.subheader(scenario["scenario"])
        choice = st.radio(
            "Choose your strategy:", 
            scenario["options"], 
            key=f"radio_{idx}",
            disabled=st.session_state.submissions[idx]
        )

        # Display the submit button only for the active question
        if not st.session_state.submissions[idx]:
            if st.button("Submit", key=f"submit_{idx}"):
                if choice == scenario["answer"]:
                    st.success(scenario["feedback"])
                    st.session_state.score += 1
                else:
                    st.error("Oops! Not the best strategy, but keep going!")
                st.session_state.submissions[idx] = True

        # Activate the "Next" button after the answer is submitted
        if st.session_state.submissions[idx]:
            if idx < len(scenarios) - 1:
                if st.button("Next", key=f"next_{idx}"):
                    st.session_state.current_question += 1
            else:
                # This block will execute after the third (final) question is submitted
                st.balloons()  # Balloons after the last question is answered
                st.success(f"🎉 Congratulations, Shristee! You completed the adventure with a score of {st.session_state.score}/{len(scenarios)}! 🎉")

                # Final birthday message
                st.write("Wishing you a fantastic birthday filled with joy and success, Shristee! 💐")
