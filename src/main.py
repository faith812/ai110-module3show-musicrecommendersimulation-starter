"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(label: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    profile_summary = ", ".join(f"{key}={value}" for key, value in user_prefs.items())
    print(f"=== {label} ===")
    print(f"User profile: {profile_summary}\n")
    print("Recommendations:\n")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {rank}. {song['title']} - Score: {score:.2f}\n")
        print(f" Because: {explanation}\n")


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Example profile including acousticness, required by score_song()
    baseline_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8, "acousticness": 0.2}
    print_recommendations("Baseline", baseline_prefs, songs)

    # Edge case: genre/mood match fights energy/acousticness match
    # (classical+melancholy song vs. metal+angry song pull in opposite directions)
    conflicting_prefs = {"genre": "classical", "mood": "angry", "energy": 0.95, "acousticness": 0.0}
    print_recommendations("Conflicting genre/mood vs. energy/acoustic", conflicting_prefs, songs)

    # Edge case: genre and mood that don't naturally co-occur in the catalog
    impossible_combo_prefs = {"genre": "metal", "mood": "chill", "energy": 0.9, "acousticness": 0.9}
    print_recommendations("Impossible genre/mood combo", impossible_combo_prefs, songs)

    # Edge case: energy above the valid [0, 1] range
    out_of_range_high_prefs = {"genre": "pop", "mood": "happy", "energy": 1.8, "acousticness": 0.0}
    print_recommendations("Out-of-range energy (> 1.0)", out_of_range_high_prefs, songs)

    # Edge case: energy below the valid [0, 1] range
    out_of_range_low_prefs = {"genre": "jazz", "mood": "relaxed", "energy": -0.5, "acousticness": 1.0}
    print_recommendations("Out-of-range energy (< 0.0)", out_of_range_low_prefs, songs)

    # Edge case: genre/mood values that don't exist anywhere in the catalog
    unknown_values_prefs = {"genre": "polka", "mood": "bored", "energy": 0.5, "acousticness": 0.0}
    print_recommendations("Unknown genre/mood values", unknown_values_prefs, songs)

    # Edge case: case/whitespace mismatch against catalog values ("pop" vs "Pop")
    case_mismatch_prefs = {"genre": "Pop", "mood": "Happy", "energy": 0.8, "acousticness": 0.0}
    print_recommendations("Case-mismatched genre/mood", case_mismatch_prefs, songs)

    # Edge case: near tie between two lofi/chill songs (Midnight Coding vs. Library Rain)
    tie_prefs = {"genre": "lofi", "mood": "chill", "energy": 0.385, "acousticness": 0.785}
    print_recommendations("Near-tie scoring", tie_prefs, songs)

    # Edge case: no genre/mood preference at all, isolates energy/acousticness scoring
    no_categorical_prefs = {"genre": "", "mood": "", "energy": 0.5, "acousticness": 0.5}
    print_recommendations("No genre/mood preference (control)", no_categorical_prefs, songs)


if __name__ == "__main__":
    main()
