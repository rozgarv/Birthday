import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Happy Birthday Shristee!", layout="centered")

# Initialize session state to keep track of the current question and score
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0

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
        st.experimental_rerun()  # Refresh the app to move to the first question

# Show the current question based on the progress
if st.session_state.current_question > 0 and st.session_state.current_question <= len(scenarios):
    scenario = scenarios[st.session_state.current_question - 1]
    st.subheader(scenario["scenario"])
    choice = st.radio("Choose your strategy:", scenario["options"], key=f"radio_{st.session_state.current_question}")

    if st.button("Submit", key=f"button_{st.session_state.current_question}"):
        if choice == scenario["answer"]:
            st.success(scenario["feedback"])
            st.session_state.score += 1
        else:
            st.error("Oops! Not the best strategy, but keep going!")

        time.sleep(1)  # Pause for dramatic effect

        # Move to the next question
        st.session_state.current_question += 1
        st.experimental_rerun()  # Refresh the app to display the next question

# Show the final score and message only after all questions are answered
if st.session_state.current_question > len(scenarios):
    st.balloons()
    st.write(f"🎉 You completed the adventure with a score of {st.session_state.score}/{len(scenarios)}! 🎉")
    
    if st.session_state.score == len(scenarios):
        st.success("Wow, perfect score! You're a *Salix* defender expert!")
    else:
        st.write("Nice try! You've done a great job protecting the *Salix* plants!")

    # Footer birthday message
    st.write("Wishing you a fantastic birthday filled with joy and success, Shristee! 💐")
