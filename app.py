import streamlit as st
import random

st.title("🥊 Turn-Based Brawler")

# Initialize game state
if 'p1_hp' not in st.session_state:
    st.session_state.p1_hp = 100
    st.session_state.p2_hp = 100
    st.session_state.turn = "Player 1"

def attack(attacker, defender):
    damage = random.randint(10, 20)
    if defender == "Player 1":
        st.session_state.p1_hp -= damage
    else:
        st.session_state.p2_hp -= damage
    return damage

# Display Health Bars
st.write(f"**Player 1 HP:** {st.session_state.p1_hp}")
st.progress(st.session_state.p1_hp)

st.write(f"**Player 2 HP:** {st.session_state.p2_hp}")
st.progress(st.session_state.p2_hp)

# Game Actions
if st.button("🔥 Attack!"):
    if st.session_state.turn == "Player 1":
        dmg = attack("Player 1", "Player 2")
        st.write(f"Player 1 dealt {dmg} damage!")
        st.session_state.turn = "Player 2"
    else:
        dmg = attack("Player 2", "Player 1")
        st.write(f"Player 2 dealt {dmg} damage!")
        st.session_state.turn = "Player 1"
    st.rerun()

if st.session_state.p1_hp <= 0 or st.session_state.p2_hp <= 0:
    st.success("Game Over! Restart to play again.")
    if st.button("Reset"):
        st.session_state.p1_hp = 100
        st.session_state.p2_hp = 100
        st.rerun()
