"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Example profile including acousticness, required by score_song()
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8, "acousticness": 0.2}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    profile_summary = ", ".join(f"{key}={value}" for key, value in user_prefs.items())
    print(f"User profile: {profile_summary}\n")
    print("Recommendations:\n")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {rank}. {song['title']} - Score: {score:.2f}\n")
        print(f" Because: {explanation}\n")


if __name__ == "__main__":
    main()
