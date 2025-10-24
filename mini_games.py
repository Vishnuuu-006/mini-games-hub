import streamlit as st
import streamlit.components.v1 as components
import random
import time
import numpy as np


# 1️⃣ Page config
st.set_page_config(page_title="🎮 Mini Game Hub", page_icon="🦇", layout="wide")


# CUSTOM CSS (NEON THEME)

st.markdown("""
    <style>
    .stApp, .block-container, body {
        background-color: #000000 !important;
        color: #9ad5ff !important;
    }
    html, body, p, span, div, label, li, ul, ol, input, textarea, select {
        color: #9ad5ff !important;
        font-family: 'Monospace', sans-serif !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #b3e0ff !important;
        text-align: center;
        text-shadow: 0 0 10px #00aaff, 0 0 25px #0088ff;
        font-family: 'Orbitron', monospace;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0077ff, #00ccff);
        color: #e6faff !important;
        border-radius: 10px;
        border: none;
        font-size: 17px;
        font-weight: bold;
        box-shadow: 0 0 10px #00aaff;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.08);
        box-shadow: 0 0 25px #00ccff;
        background: linear-gradient(90deg, #0099ff, #00ddff);
    }
    .stRadio label, .stCheckbox label, .stSelectbox label {
        color: #9ad5ff !important;
    }
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #00ccff !important;
        text-shadow: 0 0 8px #0099ff;
    }
    hr { border: 1px solid #003366 !important; }
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
        color: #9ad5ff !important;
        border-right: 1px solid #003366;
    }
    </style>
""", unsafe_allow_html=True)

# SESSION INITIALIZATION

for key, default in {
    "page": "Home",
    "p1_score": 0, "p2_score": 0, "rounds_dice": 0,
    "last_p1_roll": None, "last_p2_roll": None,
    "weather_score": 0, "weather_rounds": 0,
    "monty_rounds": 0, "monty_wins": 0,
    "coin_score": 0, "coin_rounds": 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# SIDEBAR NAVIGATION
st.sidebar.title("🎮 Mini Game Hub")
page = st.sidebar.radio(
    "Select:",
    ["🏠 Home", "🎲 Dice Duel", "☀️ Weather Predictor", "🚪 Monty Hall Game", "🪙 Coin Toss Game","🎈 Balloon Pop Game","🚗 Traffic Rush","🎆 Firefly Festival"]
)
st.session_state.page = page


# HOME PAGE
if page == "🏠 Home":
    st.markdown("""
        <h1 class="neon-text" style='text-align:center;'>🎮 Welcome to the Mini Game Hub!</h1>
        <p style='text-align:center; font-size:18px; color:#b3e0ff;'>
            Dive into interactive games built with <b>Python + Streamlit</b> 💻<br>
            Explore concepts of <b>Probability</b> and <b>Data Science</b> in the most fun way possible! 🎲🌦️🚪
        </p>
    """, unsafe_allow_html=True)
    st.subheader("🎮Click on Top left side to access SIDEBAR for playing games")


    # Game List
    st.markdown("---")
    st.subheader("🎮 Available Games:")
    st.write("🎲 **Dice Duel** — Roll the dice and challenge your friend!")
    st.write("🌦️ **Weather Predictor** — Guess the weather and earn points!")
    st.write("🚪 **Monty Hall Challenge** — A probability twist game based on the famous puzzle!")
    st.write("🪙 **Coin Flip Animation** — Experience randomness in motion!")
    st.write("🎈**Balloon Pop** — Fun simulations by pumping the balloon with certain probability!")
    st.write("🚗**Traffic Rush**-Fun game with determining the no.of cars passing with the intuition of Poisson Distribution!")
    st.write("🎇**Firefly Festival*-Fun game with determining the no.of flashes with Poisson Distribution!")
    st.markdown("---")
    st.info("👉 Click the top left bar to choose a game and start playing!")

# 🎲 DICE DUEL

elif page == "🎲 Dice Duel":
    st.title("🎲 Dice Duel Game")
    st.subheader("Roll the dice and see who wins each round! (Now with animation!)")

    col1, col2 = st.columns(2)
    with col1:
        p1 = st.text_input("👤 Player 1 name:", "Player 1", key="p1_name")
    with col2:
        p2 = st.text_input("👤 Player 2 name:", "Player 2", key="p2_name")

    # Dice display areas
    dice_area_p1 = st.empty()
    dice_area_p2 = st.empty()

    # Dice emoji lookup
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }

    if st.button("🎯 Roll Dice"):
        st.session_state.rounds_dice += 1

        with st.spinner("Rolling the dice... 🎲"):
            # Simulate dice animation (random faces for 1 second)
            for i in range(12):
                dice_area_p1.markdown(
                    f"<h1 style='text-align:center; font-size:100px'>{random.choice(list(dice_faces.values()))}</h1>",
                    unsafe_allow_html=True
                )
                dice_area_p2.markdown(
                    f"<h1 style='text-align:center; font-size:100px'>{random.choice(list(dice_faces.values()))}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(0.07)

        # Final random rolls
        p1_roll = random.randint(1, 6)
        p2_roll = random.randint(1, 6)
        st.session_state.last_p1_roll = p1_roll
        st.session_state.last_p2_roll = p2_roll

        # Show final result
        dice_area_p1.markdown(
            f"<h1 style='text-align:center; font-size:100px'>{dice_faces[p1_roll]}</h1>",
            unsafe_allow_html=True
        )
        dice_area_p2.markdown(
            f"<h1 style='text-align:center; font-size:100px'>{dice_faces[p2_roll]}</h1>",
            unsafe_allow_html=True
        )

        # Determine winner
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

    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write("""
- A die has **6 equally likely faces** → Uniform(1,6).  
- The probability of any number (1–6) is **1/6 ≈ 16.7%**.  
- The probability of a draw is **1/6**, since both must roll the same number.  
- Over many rounds, the win rates of both players should stay *close to 50–50*.  
- This shows **equiprobable outcomes** — where all possibilities are equally likely.
""")

# 🌦️WEATHER PREDICTOR

elif page == "☀️ Weather Predictor":
    st.title("🌦️ Weather Predictor Game")
    st.subheader("Test your weather prediction skills — now with animation! ⛅")

    rain_prob = st.slider("🌧️ Probability of Rain (%)", 0, 100, 30, 5)

    st.write("Make your prediction:")
    guess = st.radio("What do you think the weather will be?", ["☀️ Sunny", "🌧️ Rainy"])

    # Placeholder for animation
    weather_display = st.empty()

    if "weather_anim_state" not in st.session_state:
        st.session_state.weather_anim_state = "⛅"

    # Animate the forecast process
    if st.button("🔮 Predict Weather"):
        st.session_state.weather_rounds += 1
        st.info("Forecasting... please wait 🌍")

        # Animate transitions (simulate satellite flicker)
        for i in range(10):
            symbol = "☀️" if i % 2 == 0 else "🌧️"
            weather_display.markdown(
                f"<h1 style='text-align:center; font-size:100px'>{symbol}</h1>",
                unsafe_allow_html=True
            )
            time.sleep(0.15)

        # Actual weather outcome
        actual_weather = "🌧️ Rainy" if random.random() < rain_prob / 100 else "☀️ Sunny"
        final_symbol = "🌧️" if actual_weather == "🌧️ Rainy" else "☀️"

        # Show final result
        weather_display.markdown(
            f"<h1 style='text-align:center; font-size:100px'>{final_symbol}</h1>",
            unsafe_allow_html=True
        )

        st.session_state.weather_anim_state = final_symbol

        # Evaluate prediction
        if guess == actual_weather:
            st.success(f"You predicted correctly! 🎯 It's **{actual_weather}** ☀️🌧️")
            st.session_state.weather_score += 10
        else:
            st.error(f"Oops! It turned out **{actual_weather}**. Better luck next time 😅")

    # Restart button
    if st.button("🔁 Restart Weather Game"):
        st.session_state.weather_score = 0
        st.session_state.weather_rounds = 0
        st.session_state.weather_anim_state = "⛅"
        st.rerun()
    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write(f"""
- The slider sets the **probability of rain** (p = {rain_prob/100:.2f}).  
- Each prediction is a **Bernoulli trial**: either Rain (1) or No Rain (0).  
- Each trial is **independent** — past results don’t affect the next.  
- Over many plays, the proportion of rainy outcomes will approach *p*.  
- This is a visual form of the **Law of Large Numbers**.
""")

#🚪 MONTY HALL GAME

elif page == "🚪 Monty Hall Game":
    st.title("🚪 The Monty Hall Game (Animated & Fixed)")
    st.subheader("Pick a door, stay or switch, and see if you win the 🚗!")

    # Initialize game state
    if "monty_game" not in st.session_state:
        st.session_state.monty_game = {
            "car_door": random.randint(0, 2),
            "player_choice": None,
            "revealed_door": None,
            "stage": "choose"
        }

    game = st.session_state.monty_game

    # Create a persistent placeholder for door display
    door_area = st.empty()

    def render_doors(selected=None, revealed=None, final=None):
        """Renders 3 doors in a single update (prevents duplication)."""
        with door_area.container():
            cols = st.columns(3)
            for i in range(3):
                with cols[i]:
                    if final is not None and i == final:
                        emoji = "🚗" if i == game["car_door"] else "🐐"
                    elif revealed == i:
                        emoji = "🐐"
                    elif selected == i:
                        emoji = "🚪✨"
                    else:
                        emoji = "🚪"
                    st.markdown(
                        f"<h1 style='text-align:center; font-size:100px'>{emoji}</h1>",
                        unsafe_allow_html=True,
                    )

    # Stage 1: Player chooses a door
    if game["stage"] == "choose":
        st.write("There are 3 doors — behind one is a 🚗, behind the others are 🐐s.")
        render_doors()

        choice = st.radio("Choose your door:", [1, 2, 3])
        if st.button("🎯 Confirm Choice"):
            game["player_choice"] = choice - 1

            # Reveal one goat door
            possible = [i for i in range(3)
                        if i != game["player_choice"] and i != game["car_door"]]
            game["revealed_door"] = random.choice(possible)
            game["stage"] = "reveal"
            st.rerun()

    # Stage 2: Reveal one goat
    elif game["stage"] == "reveal":
        st.info(f"Monty opens Door {game['revealed_door'] + 1}, showing a 🐐!")
        render_doors(selected=game["player_choice"], revealed=game["revealed_door"])

        decision = st.radio("Do you want to stay or switch?", ["Stay 🚪", "Switch 🔁"])
        if st.button("🎬 Final Decision"):
            if decision == "Switch 🔁":
                available = [i for i in range(3)
                             if i not in [game["player_choice"], game["revealed_door"]]]
                game["player_choice"] = available[0]
            game["stage"] = "final"
            st.rerun()

    # Stage 3: Final reveal
    elif game["stage"] == "final":
        final_choice = game["player_choice"]

        # Door flip animation
        for i in range(6):
            render_doors(selected=final_choice)
            time.sleep(0.1)
            render_doors()  # blink effect
            time.sleep(0.1)

        # Final reveal (replace door with car or goat)
        render_doors(final=final_choice)

        if final_choice == game["car_door"]:
            st.success("🏆 You won the **CAR**! Smart choice!")
        else:
            st.error("🐐 You got a goat! Try again!")

        if st.button("🔁 Play Again"):
            del st.session_state.monty_game
            st.rerun()

    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write("""
- You first choose 1 of 3 doors → **1/3 chance** of picking the car.  
- Monty then opens a door with a goat, but never the car.  
- That means the *other unopened door* holds a **2/3 chance** of the car.  
- So switching doors *doubles your chance of winning* — from 1/3 to 2/3.  
- This demonstrates **conditional probability** — how knowing new info changes odds.
""")
    
#COIN TOSS GAME

elif page == "🪙 Coin Toss Game":
    st.title("🪙 Animated Coin Toss")
    st.subheader("Flip the coin and test your luck! 🎯")

    # Initialize state
    if "coin_side" not in st.session_state:
        st.session_state.coin_side = "🪙"  # neutral state before flip

    # Display coin emoji (big size)
    coin_display = st.empty()
    coin_display.markdown(
        f"<h1 style='text-align:center; font-size:120px'>{st.session_state.coin_side}</h1>",
        unsafe_allow_html=True
    )

    # Flip button
    if st.button("🎬 Flip Coin"):
        with st.spinner("Flipping... 🌀"):
            # Animate the flip sequence
            for i in range(12):
                side = "🌕" if i % 2 == 0 else "🌑"  # simulate flip faces
                coin_display.markdown(
                    f"<h1 style='text-align:center; font-size:120px'>{side}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(0.08)

        # Random result
        result = random.choice(["Heads", "Tails"])
        final_emoji = "🙂" if result == "Heads" else "🙃"
        st.session_state.coin_side = final_emoji

        # Display final result
        coin_display.markdown(
            f"<h1 style='text-align:center; font-size:120px'>{final_emoji}</h1>",
            unsafe_allow_html=True
        )
        st.success(f"🪙 It's **{result}!** 🎉")

    # Reset button
    if st.button("🔁 Reset"):
        st.session_state.coin_side = "🪙"
        st.rerun()

    # Probability section
    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write("""
- Each toss has 2 possible outcomes → Heads or Tails.  
- Both are equally likely → **P(Heads) = P(Tails) = 0.5**.  
- Each toss is **independent** — the coin doesn’t remember its last result.  
- Over many flips, the outcomes will roughly balance (≈50–50).  
- This demonstrates **independent and identically distributed events (i.i.d)**.
""")
# BALLOON POP GAME

elif page == "🎈 Balloon Pop Game":
    st.title("🎈 Balloon Pop Probability Game")
    st.subheader("Pump carefully — each pump increases the chance of it popping!")

    # Initialize state
    if "balloon_pumps" not in st.session_state:
        st.session_state.balloon_pumps = 0
        st.session_state.balloon_popped = False
        st.session_state.balloon_score = 0
        st.session_state.balloon_size = 120  # base emoji size in %
        st.session_state.balloon_emoji = "🎈"

    # Display current balloon
    balloon_display = st.empty()
    size = st.session_state.balloon_size
    balloon_display.markdown(
        f"<h1 style='text-align:center; font-size:{size}px'>{st.session_state.balloon_emoji}</h1>",
        unsafe_allow_html=True
    )

    if not st.session_state.balloon_popped:
        # Increase pop chance each pump
        pop_chance = min(10 + st.session_state.balloon_pumps * 10, 95)  # starts at 10%, +10% per pump
        st.write(f"💣 Current pop chance: **{pop_chance}%**")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎈 Pump Balloon"):
                st.session_state.balloon_pumps += 1
                with st.spinner("Pumping... 💨"):
                    # Animate balloon inflation
                    for step in range(3):
                        new_size = st.session_state.balloon_size + step * 10
                        balloon_display.markdown(
                            f"<h1 style='text-align:center; font-size:{new_size}px'>🎈</h1>",
                            unsafe_allow_html=True
                        )
                        time.sleep(0.1)

                # Check if balloon pops
                if random.random() < pop_chance / 100:
                    st.session_state.balloon_popped = True
                    st.session_state.balloon_emoji = "💥"
                    balloon_display.markdown(f"<h1 style='text-align:center; font-size:150px'>💥</h1>",unsafe_allow_html=True)
                    st.error("💥 The balloon popped! You lost your points for this round.")
                else:
                    st.session_state.balloon_score += 5
                    st.session_state.balloon_size += 20
                    st.success("Nice! Balloon survived, +5 points! 🎉")

        with col2:
            if st.button("🏁 Cash Out"):
                st.success(f"You cashed out safely with **{st.session_state.balloon_score} points!** 🎊")
                st.session_state.balloon_popped = True

    else:
        # After balloon pops or cash-out
        balloon_display.markdown(
            f"<h1 style='text-align:center; font-size:150px'>{st.session_state.balloon_emoji}</h1>",
            unsafe_allow_html=True
        )
        if st.button("🔁 Play Again"):
            # Reset
            st.session_state.balloon_pumps = 0
            st.session_state.balloon_popped = False
            st.session_state.balloon_score = 0
            st.session_state.balloon_size = 120
            st.session_state.balloon_emoji = "🎈"
            st.rerun()

    # Stats section
    st.markdown("---")
    st.subheader("📊 Balloon Stats")
    st.metric("Pumps", st.session_state.balloon_pumps)
    st.metric("Score", st.session_state.balloon_score)

    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write("""
- Each balloon has a **chance p** of popping when tapped.  
- Over n balloons, the total number popped follows a **Binomial(n, p)** distribution.  
- The average number of pops = n·p.  
- This shows how multiple independent events combine into predictable patterns.
""")

# 🚗 TRAFFIC RUSH (POISSON RANDOM)

elif page == "🚗 Traffic Rush":
    st.title("🚗 Traffic Rush Game")
    st.subheader("Guess how many cars will pass this minute!")

    # Poisson mean (λ)
    lam = st.slider("Average cars per minute (λ):", 1, 10, 4)
    guess = st.number_input("Your guess for number of cars:", 0, 20, 5)

    if "cars" not in st.session_state:
        st.session_state.cars = []
        st.session_state.actual = 0

    car_area = st.empty()

    if st.button("🚦 Start Simulation"):
        st.info("Simulating car arrivals...")
        time.sleep(0.8)

        # Generate Poisson number of cars
        actual = np.random.poisson(lam)
        st.session_state.actual = actual
        st.session_state.cars = ["🚗" for _ in range(actual)]

        with car_area.container():
            cols = st.columns(10)
            for i in range(actual):
                with cols[i % 10]:
                    st.markdown(f"<h2 style='text-align:center'>{st.session_state.cars[i]}</h2>", unsafe_allow_html=True)
                time.sleep(0.2)

        st.success(f"Total cars that passed: **{actual}** 🚗")

        # Scoring
        diff = abs(actual - guess)
        if diff == 0:
            st.balloons()
            st.success("🎯 Perfect prediction! +10 points")
        elif diff <= 2:
            st.info(f"Close! Off by {diff}. +5 points")
        else:
            st.error(f"Missed by {diff}. Try again!")

    if st.button("🔁 Reset Traffic Rush"):
        del st.session_state.cars
        st.rerun()

    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write("""
- The number of cars per minute follows a **Poisson(λ)** distribution.  
- λ (lambda) = average cars per minute → sets how busy the road is.  
- The Poisson model assumes:
  1. Cars arrive *independently*.  
  2. Two cars don’t arrive at exactly the same instant.  
  3. The average rate λ stays constant.  
- Great example of **rare event counting** in real life.
""")



# 🎆 FIREFLY FESTIVAL (POISSON FLASHES)

elif page == "🎆 Firefly Festival":
    st.title("🎆 Firefly Festival")
    st.subheader("Watch the fireflies blink randomly in the night sky 🌌")

    lam = st.slider("Average flashes per second (λ):", 1, 10, 3)
    duration = st.slider("Simulation duration (seconds):", 2, 10, 5)

    sky = st.empty()

    if st.button("🌟 Start Show"):
        st.info("Fireflies appearing...")
        total_flashes = 0
        with sky.container():
            for t in range(duration):
                flashes = np.random.poisson(lam)
                total_flashes += flashes
                sky.markdown(
                    "<h1 style='text-align:center'>" + "✨" * flashes + "</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(0.7)

        st.success(f"Show ended! Total flashes: **{total_flashes}** ✨")
        st.balloons()

    if st.button("🔁 Restart Festival"):
        sky.empty()
        st.rerun()
    st.markdown("---")
    st.subheader("📊 Probability Insight")
    st.write("""
- Each flash of a firefly is random but happens at a steady average rate λ.  
- The count per second follows **Poisson(λ)** — random but centered around λ.  
- Some seconds have many flashes, others have few — that’s the beauty of randomness!  
- Poisson distribution models **events per interval** — time, area, or volume.  
- Common examples: phone calls per minute, decay events, raindrops, etc.
""")


    















