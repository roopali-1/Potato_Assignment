import streamlit as st

from main import get_avg_likes, get_place_distribution, get_tweets_per_day, get_unique_users

# Streamlit UI
st.title("POTATO - Twitter Data Query")

# Input term for search
term = st.text_input("Enter term to search for:", "music")

if st.button("Search"):
    # Get results for the input term
    tweets_per_day = get_tweets_per_day(term)
    unique_users = get_unique_users(term)
    avg_likes = get_avg_likes(term)
    place_distribution = get_place_distribution(term)
    # Display results
    st.write(f"### Results for '{term}':")
    
    # Tweets per day
    st.write("**Tweets per day**:")
    for day in tweets_per_day:
        st.write(f"Date: {day['key_as_string']}, Count: {day['doc_count']}")
    
    # Unique users
    st.write(f"**Unique users**: {unique_users}")

    # Average likes
    st.write(f"**Average likes**: {avg_likes}")

    # Place distribution
    st.write("**Place distribution**:")
    for place in place_distribution:
        st.write(f"Place ID: {place['key']}, Count: {place['doc_count']}")
