import streamlit as st
import random

st.title("🥊 Multi-Player Brawler")

# Configuration
NUM_PLAYERS = 6

# Initialize game state for all players
if 'players' not in st.session_state:
    st.session_state.players = {f"Player {i+1}": 100 for i in range(NUM_PLAYERS)}
    st.session_state.turn_idx = 0
    st.session_state.active_players = NUM_PLAYERS

# Helper to get current player name
player_names = list(st.session_state.players.keys())
current_player = player_names[st.session_state.turn_idx]

# Display Health for all players
st.subheader("Health Status")
for name, hp in st.session_state.players.items():
    col1, col2 = st.columns([1, 3])
    col1.write(f"**{name}**")
    col2.progress(max(0, hp) / 100)

# Game Logic
if st.session_state.active_players > 1:
    st.write(f"It is **{current_player}'s** turn!")
    
    # Choose a target
    target = st.selectbox("Select target to attack:", 
                          [p for p in player_names if p != current_player and st.session_state.players[p] > 0])
    
    if st.button("🔥 Attack!"):
        damage = random.randint(10, 20)
        st.session_state.players[target] = max(0, st.session_state.players[target] - damage)
        
        # Check if target died
        if st.session_state.players[target] == 0:
            st.session_state.active_players -= 1
            
        # Move to next player's turn
        st.session_state.turn_idx = (st.session_state.turn_idx + 1) % NUM_PLAYERS
        # Skip dead players
        while st.session_state.players[player_names[st.session_state.turn_idx]] <= 0:
            st.session_state.turn_idx = (st.session_state.turn_idx + 1) % NUM_PLAYERS
            
        st.rerun()
else:
    winner = [name for name, hp in st.session_state.players.items() if hp > 0][0]
    st.success(f"Game Over! {winner} is the Champion! 🎉")

if st.button("Reset Game"):
    st.session_state.players = {f"Player {i+1}": 100 for i in range(NUM_PLAYERS)}
    st.session_state.turn_idx = 0
    st.session_state.active_players = NUM_PLAYERS
    st.rerun()
