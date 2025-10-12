import streamlit as st
import random
import time

#PAGE CONFIG
st.set_page_config(page_title="🎮 Mini Game Hub", page_icon="🎲", layout="centered")

#SESSION INITIALIZATION
for key, default in {
    "page": "Home",
    "p1_score": 0,
    "p2_score": 0,
    "rounds_dice": 0,
    "last_p1_roll": None,
    "last_p2_roll": None,
    "weather_score": 0,
    "weather_rounds": 0,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

#NAVIGATION BAR

st.sidebar.title("🎮 Mini Game Hub")
page = st.sidebar.radio("Choose a game:", ["🏠 Home", "🎲 Dice Duel", "☀️ Weather Predictor"])
st.session_state.page = page

#HOME PAGE
if page == "🏠 Home":
    st.title("🎮 Welcome to Mini Game Hub")
    st.write("Choose a fun mini-game to play!")
    st.markdown("---")
    st.subheader("Available Games:")
    st.write("🎲 **Dice Duel** — Challenge a friend to a dice battle.")
    st.write("☀️ **Weather Predictor** — Test your forecasting skills.")
    st.markdown("---")
    st.info("Select a game from the left sidebar to start playing!")

#DICE DUEL GAME
elif page == "🎲 Dice Duel":
    st.title("🎲 Dice Duel Game")
    st.subheader("Roll the dice and see who wins each round!")

    col1, col2 = st.columns(2)
    with col1:
        p1 = st.text_input("👤 Player 1 name:", "Player 1", key="p1_name")
    with col2:
        p2 = st.text_input("👤 Player 2 name:", "Player 2", key="p2_name")

    if st.button("🎯 Roll Dice"):
        st.session_state.rounds_dice += 1
        with st.spinner("Rolling dice... 🎲"):
            time.sleep(0.8)
        p1_roll = random.randint(1, 6)
        p2_roll = random.randint(1, 6)
        st.session_state.last_p1_roll = p1_roll
        st.session_state.last_p2_roll = p2_roll

        st.write(f"{p1} rolled: **{p1_roll}** 🎲")
        st.write(f"{p2} rolled: **{p2_roll}** 🎲")

        if p1_roll > p2_roll:
            st.success(f"{p1} wins this round! 🏆")
            st.session_state.p1_score += 1
        elif p2_roll > p1_roll:
            st.success(f"{p2} wins this round! 🏆")
            st.session_state.p2_score += 1
        else:
            st.info("It's a draw! 🤝")

    st.markdown("---")
    st.subheader("📊 Scoreboard")
    col1, col2 = st.columns(2)
    col1.metric(f"{p1}'s Score", st.session_state.p1_score)
    col2.metric(f"{p2}'s Score", st.session_state.p2_score)
    st.write(f"Total Rounds Played: **{st.session_state.rounds_dice}**")

    if st.session_state.last_p1_roll is not None:
        st.write(f"🎲 Last rolls → {p1}: {st.session_state.last_p1_roll}, {p2}: {st.session_state.last_p2_roll}")

    if st.button("🔄 Restart Dice Duel"):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.rounds_dice = 0
        st.session_state.last_p1_roll = None
        st.session_state.last_p2_roll = None
        st.rerun()

# WEATHER PREDICTOR GAME 
elif page == "☀️ Weather Predictor":
    st.title("🌦️ Weather Predictor Game")
    st.subheader("Test your weather prediction skills!")

    rain_prob = st.slider("🌧️ Probability of Rain (%)", 0, 100, 30, 5)

    st.write("Make your prediction:")
    guess = st.radio("What do you think the weather will be?", ["☀️ Sunny", "🌧️ Rainy"])

    if st.button("🔮 Predict Weather"):
        st.session_state.weather_rounds += 1
        st.info("Forecasting...")
        time.sleep(1)

        weather = "🌧️ Rainy" if random.random() < rain_prob / 100 else "☀️ Sunny"
        st.write(f"The actual weather is: **{weather}**")

        if guess == weather:
            st.success("You predicted correctly! +10 points 😌")
            st.session_state.weather_score += 10
        else:
            st.error("Oops! Wrong prediction 😅")

    st.markdown("---")
    st.subheader("🏆 Your Stats")
    st.metric("Score", st.session_state.weather_score)
    st.metric("Rounds Played", st.session_state.weather_rounds)

    if st.button("🔁 Restart Weather Game"):
        st.session_state.weather_score = 0
        st.session_state.weather_rounds = 0
        st.rerun()