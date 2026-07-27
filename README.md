# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Include your finalized "Algorithm Recipe" and a brief note on any potential biases you expect (e.g., "This system might over-prioritize genre, ignoring great songs that match the user's mood").

Algorithm Recipe:
Genre match: +2.0 if exact match, else 0
Mood match: +1.0 if exact match, else 0
Energy similarity: +1.0 x (1 - abs(song.energy - target_energy))
Acousticness similarity: +1.0 x (1 - abs(song.acousticness - target_acousticness))

The genre feature has the most weight compared to the other features. Therefore, this system may recommend songs based on genre first and give less priority to the other three features. 

---


In the How The System Works section, write a short paragraph explaining your understanding of how real-world recommendations work and what your version will prioritize. List the specific features your Song and UserProfile objects will use in your simulation.


Real-world recommendations use collaborative filtering, content-based filtering, and often a combination of these two techniques along with other methods. Collaborative filtering allows systems to give new recommendations that users may enjoy based on other users with similar preferences. For example, you and your sister both liked Young Sheldon and Kim's Convenience on Netflix. If your sister also liked KPop Demon Hunters, Netflix may recommend that same movie to you. Content-based filtering allows systems to give recommendations based on the user's preferences about the actual item. For example, Spotify may recommend more lofi songs or songs of a similar nature if you liked a lofi song. Spotify uses a combination of techniques for their recommendation system. Spotify's Discover Weekly uses collaborative filtering to find users with similar music tastes and based on the listening behavior analysis, it recommends new songs. Spotify also analayzes the features (e.g. energy, danceability, etc.) of each song (content-based filtering), and uses Natural Lanaguage Processing to study media related to songs and artists (in order to gain an understanding on what area songs/artists can be categorized into). 

In my simulation, the system will prioritize content-based filtering. The specific features that will be used are genre, mood, energy, and acousticness. 

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

User profile: genre=pop, mood=happy, energy=0.8, acousticness=0.2

Recommendations:

  1. Sunrise City - Score: 4.96

 Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98), acousticness similarity (+0.98)

  2. Gym Hero - Score: 3.72

 Because: genre match (+2.0), energy similarity (+0.87), acousticness similarity (+0.85)

  3. Rooftop Lights - Score: 2.81

 Because: mood match (+1.0), energy similarity (+0.96), acousticness similarity (+0.85)

  4. Night Drive Loop - Score: 1.93

 Because: energy similarity (+0.95), acousticness similarity (+0.98)

  5. Pulse Horizon - Score: 1.84

 Because: energy similarity (+0.92), acousticness similarity (+0.92)


---------------------


Sample Output when added edge case user profiles:


=== Baseline ===
User profile: genre=pop, mood=happy, energy=0.8, acousticness=0.2

Recommendations:

  1. Sunrise City - Score: 4.96

 Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98), acousticness similarity (+0.98)

  2. Gym Hero - Score: 3.72

 Because: genre match (+2.0), energy similarity (+0.87), acousticness similarity (+0.85)

  3. Rooftop Lights - Score: 2.81

 Because: mood match (+1.0), energy similarity (+0.96), acousticness similarity (+0.85)

  4. Night Drive Loop - Score: 1.93

 Because: energy similarity (+0.95), acousticness similarity (+0.98)

  5. Pulse Horizon - Score: 1.84

 Because: energy similarity (+0.92), acousticness similarity (+0.92)

=== Conflicting genre/mood vs. energy/acoustic ===
User profile: genre=classical, mood=angry, energy=0.95, acousticness=0.0

Recommendations:

  1. Iron Verdict - Score: 2.95

 Because: mood match (+1.0), energy similarity (+0.98), acousticness similarity (+0.97)

  2. Autumn Elegy - Score: 2.40

 Because: genre match (+2.0), energy similarity (+0.35), acousticness similarity (+0.05)

  3. Gym Hero - Score: 1.93

 Because: energy similarity (+0.98), acousticness similarity (+0.95)

  4. Storm Runner - Score: 1.86

 Because: energy similarity (+0.96), acousticness similarity (+0.90)

  5. Concrete Kingdom - Score: 1.82

 Because: energy similarity (+0.90), acousticness similarity (+0.92)

=== Impossible genre/mood combo ===
User profile: genre=metal, mood=chill, energy=0.9, acousticness=0.9

Recommendations:

  1. Iron Verdict - Score: 3.06

 Because: genre match (+2.0), energy similarity (+0.93), acousticness similarity (+0.13)

  2. Library Rain - Score: 2.41

 Because: mood match (+1.0), energy similarity (+0.45), acousticness similarity (+0.96)

  3. Spacewalk Thoughts - Score: 2.36

 Because: mood match (+1.0), energy similarity (+0.38), acousticness similarity (+0.98)

  4. Midnight Coding - Score: 2.33

 Because: mood match (+1.0), energy similarity (+0.52), acousticness similarity (+0.81)

  5. Wildflower Path - Score: 1.48

 Because: energy similarity (+0.58), acousticness similarity (+0.90)

=== Out-of-range energy (> 1.0) ===
User profile: genre=pop, mood=happy, energy=1.8, acousticness=0.0

Recommendations:

  1. Sunrise City - Score: 3.84

 Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.02), acousticness similarity (+0.82)

  2. Gym Hero - Score: 3.08

 Because: genre match (+2.0), energy similarity (+0.13), acousticness similarity (+0.95)

  3. Rooftop Lights - Score: 1.61

 Because: mood match (+1.0), energy similarity (+-0.04), acousticness similarity (+0.65)

  4. Iron Verdict - Score: 1.14

 Because: energy similarity (+0.17), acousticness similarity (+0.97)

  5. Storm Runner - Score: 1.01

 Because: energy similarity (+0.11), acousticness similarity (+0.90)

=== Out-of-range energy (< 0.0) ===
User profile: genre=jazz, mood=relaxed, energy=-0.5, acousticness=1.0

Recommendations:

  1. Coffee Shop Stories - Score: 4.02

 Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.13), acousticness similarity (+0.89)

  2. Autumn Elegy - Score: 1.15

 Because: energy similarity (+0.20), acousticness similarity (+0.95)

  3. Spacewalk Thoughts - Score: 1.14

 Because: energy similarity (+0.22), acousticness similarity (+0.92)

  4. Library Rain - Score: 1.01

 Because: energy similarity (+0.15), acousticness similarity (+0.86)

  5. Focus Flow - Score: 0.88

 Because: energy similarity (+0.10), acousticness similarity (+0.78)

=== Unknown genre/mood values ===
User profile: genre=polka, mood=bored, energy=0.5, acousticness=0.0

Recommendations:

  1. Concrete Kingdom - Score: 1.57

 Because: energy similarity (+0.65), acousticness similarity (+0.92)

  2. Velvet Whisper - Score: 1.55

 Because: energy similarity (+1.00), acousticness similarity (+0.55)

  3. Night Drive Loop - Score: 1.53

 Because: energy similarity (+0.75), acousticness similarity (+0.78)

  4. Gym Hero - Score: 1.52

 Because: energy similarity (+0.57), acousticness similarity (+0.95)

  5. Sunrise City - Score: 1.50

 Because: energy similarity (+0.68), acousticness similarity (+0.82)

=== Case-mismatched genre/mood ===
User profile: genre=Pop, mood=Happy, energy=0.8, acousticness=0.0

Recommendations:

  1. Concrete Kingdom - Score: 1.87

 Because: energy similarity (+0.95), acousticness similarity (+0.92)

  2. Gym Hero - Score: 1.82

 Because: energy similarity (+0.87), acousticness similarity (+0.95)

  3. Sunrise City - Score: 1.80

 Because: energy similarity (+0.98), acousticness similarity (+0.82)

  4. Iron Verdict - Score: 1.80

 Because: energy similarity (+0.83), acousticness similarity (+0.97)

  5. Pulse Horizon - Score: 1.80

 Because: energy similarity (+0.92), acousticness similarity (+0.88)

=== Near-tie scoring ===
User profile: genre=lofi, mood=chill, energy=0.385, acousticness=0.785

Recommendations:

  1. Midnight Coding - Score: 4.89

 Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.97), acousticness similarity (+0.92)

  2. Library Rain - Score: 4.89

 Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.96), acousticness similarity (+0.93)

  3. Focus Flow - Score: 3.98

 Because: genre match (+2.0), energy similarity (+0.98), acousticness similarity (+0.99)

  4. Spacewalk Thoughts - Score: 2.76

 Because: mood match (+1.0), energy similarity (+0.90), acousticness similarity (+0.86)

  5. Wildflower Path - Score: 1.89

 Because: energy similarity (+0.91), acousticness similarity (+0.98)

=== No genre/mood preference (control) ===
User profile: genre=, mood=, energy=0.5, acousticness=0.5

Recommendations:

  1. Velvet Whisper - Score: 1.95

 Because: energy similarity (+1.00), acousticness similarity (+0.95)

  2. Backroad Memories - Score: 1.85

 Because: energy similarity (+0.95), acousticness similarity (+0.90)

  3. Island Sunbeam - Score: 1.78

 Because: energy similarity (+0.88), acousticness similarity (+0.90)

  4. Midnight Coding - Score: 1.71

 Because: energy similarity (+0.92), acousticness similarity (+0.79)

  5. Wildflower Path - Score: 1.68

 Because: energy similarity (+0.98), acousticness similarity (+0.70)

----------------------

 Sample Output when implemented Weight Shift: 

 === Baseline ===
User profile: genre=pop, mood=happy, energy=0.8, acousticness=0.2

Recommendations:

  1. Sunrise City - Score: 4.94

 Because: genre match (+1.0), mood match (+1.0), energy similarity (+1.96), acousticness similarity (+0.98)

  2. Rooftop Lights - Score: 3.77

 Because: mood match (+1.0), energy similarity (+1.92), acousticness similarity (+0.85)

  3. Gym Hero - Score: 3.59

 Because: genre match (+1.0), energy similarity (+1.74), acousticness similarity (+0.85)

  4. Night Drive Loop - Score: 2.88

 Because: energy similarity (+1.90), acousticness similarity (+0.98)

  5. Concrete Kingdom - Score: 2.78

 Because: energy similarity (+1.90), acousticness similarity (+0.88)

=== Conflicting genre/mood vs. energy/acoustic ===
User profile: genre=classical, mood=angry, energy=0.95, acousticness=0.0

Recommendations:

  1. Iron Verdict - Score: 3.93

 Because: mood match (+1.0), energy similarity (+1.96), acousticness similarity (+0.97)

  2. Gym Hero - Score: 2.91

 Because: energy similarity (+1.96), acousticness similarity (+0.95)

  3. Storm Runner - Score: 2.82

 Because: energy similarity (+1.92), acousticness similarity (+0.90)

  4. Pulse Horizon - Score: 2.74

 Because: energy similarity (+1.86), acousticness similarity (+0.88)

  5. Concrete Kingdom - Score: 2.72

 Because: energy similarity (+1.80), acousticness similarity (+0.92)

=== Impossible genre/mood combo ===
User profile: genre=metal, mood=chill, energy=0.9, acousticness=0.9

Recommendations:

  1. Iron Verdict - Score: 2.99

 Because: genre match (+1.0), energy similarity (+1.86), acousticness similarity (+0.13)

  2. Library Rain - Score: 2.86

 Because: mood match (+1.0), energy similarity (+0.90), acousticness similarity (+0.96)

  3. Midnight Coding - Score: 2.85

 Because: mood match (+1.0), energy similarity (+1.04), acousticness similarity (+0.81)

  4. Spacewalk Thoughts - Score: 2.74

 Because: mood match (+1.0), energy similarity (+0.76), acousticness similarity (+0.98)

  5. Storm Runner - Score: 2.18

 Because: energy similarity (+1.98), acousticness similarity (+0.20)

=== Out-of-range energy (> 1.0) ===
User profile: genre=pop, mood=happy, energy=1.8, acousticness=0.0

Recommendations:

  1. Sunrise City - Score: 2.86

 Because: genre match (+1.0), mood match (+1.0), energy similarity (+0.04), acousticness similarity (+0.82)

  2. Gym Hero - Score: 2.21

 Because: genre match (+1.0), energy similarity (+0.26), acousticness similarity (+0.95)

  3. Rooftop Lights - Score: 1.57

 Because: mood match (+1.0), energy similarity (+-0.08), acousticness similarity (+0.65)

  4. Iron Verdict - Score: 1.31

 Because: energy similarity (+0.34), acousticness similarity (+0.97)

  5. Storm Runner - Score: 1.12

 Because: energy similarity (+0.22), acousticness similarity (+0.90)

=== Out-of-range energy (< 0.0) ===
User profile: genre=jazz, mood=relaxed, energy=-0.5, acousticness=1.0

Recommendations:

  1. Coffee Shop Stories - Score: 3.15

 Because: genre match (+1.0), mood match (+1.0), energy similarity (+0.26), acousticness similarity (+0.89)

  2. Spacewalk Thoughts - Score: 1.36

 Because: energy similarity (+0.44), acousticness similarity (+0.92)

  3. Autumn Elegy - Score: 1.35

 Because: energy similarity (+0.40), acousticness similarity (+0.95)

  4. Library Rain - Score: 1.16

 Because: energy similarity (+0.30), acousticness similarity (+0.86)

  5. Focus Flow - Score: 0.98

 Because: energy similarity (+0.20), acousticness similarity (+0.78)

=== Unknown genre/mood values ===
User profile: genre=polka, mood=bored, energy=0.5, acousticness=0.0

Recommendations:

  1. Velvet Whisper - Score: 2.55

 Because: energy similarity (+2.00), acousticness similarity (+0.55)

  2. Island Sunbeam - Score: 2.36

 Because: energy similarity (+1.76), acousticness similarity (+0.60)

  3. Backroad Memories - Score: 2.30

 Because: energy similarity (+1.90), acousticness similarity (+0.40)

  4. Night Drive Loop - Score: 2.28

 Because: energy similarity (+1.50), acousticness similarity (+0.78)

  5. Concrete Kingdom - Score: 2.22

 Because: energy similarity (+1.30), acousticness similarity (+0.92)

=== Case-mismatched genre/mood ===
User profile: genre=Pop, mood=Happy, energy=0.8, acousticness=0.0

Recommendations:

  1. Concrete Kingdom - Score: 2.82

 Because: energy similarity (+1.90), acousticness similarity (+0.92)

  2. Sunrise City - Score: 2.78

 Because: energy similarity (+1.96), acousticness similarity (+0.82)

  3. Pulse Horizon - Score: 2.72

 Because: energy similarity (+1.84), acousticness similarity (+0.88)

  4. Gym Hero - Score: 2.69

 Because: energy similarity (+1.74), acousticness similarity (+0.95)

  5. Storm Runner - Score: 2.68

 Because: energy similarity (+1.78), acousticness similarity (+0.90)

=== Near-tie scoring ===
User profile: genre=lofi, mood=chill, energy=0.385, acousticness=0.785

Recommendations:

  1. Midnight Coding - Score: 4.86

 Because: genre match (+1.0), mood match (+1.0), energy similarity (+1.93), acousticness similarity (+0.92)

  2. Library Rain - Score: 4.85

 Because: genre match (+1.0), mood match (+1.0), energy similarity (+1.93), acousticness similarity (+0.93)

  3. Focus Flow - Score: 3.96

 Because: genre match (+1.0), energy similarity (+1.97), acousticness similarity (+0.99)

  4. Spacewalk Thoughts - Score: 3.66

 Because: mood match (+1.0), energy similarity (+1.79), acousticness similarity (+0.86)

  5. Coffee Shop Stories - Score: 2.87

 Because: energy similarity (+1.97), acousticness similarity (+0.90)

=== No genre/mood preference (control) ===
User profile: genre=, mood=, energy=0.5, acousticness=0.5

Recommendations:

  1. Velvet Whisper - Score: 2.95

 Because: energy similarity (+2.00), acousticness similarity (+0.95)

  2. Backroad Memories - Score: 2.80

 Because: energy similarity (+1.90), acousticness similarity (+0.90)

  3. Island Sunbeam - Score: 2.66

 Because: energy similarity (+1.76), acousticness similarity (+0.90)

  4. Wildflower Path - Score: 2.66

 Because: energy similarity (+1.96), acousticness similarity (+0.70)

  5. Midnight Coding - Score: 2.63

 Because: energy similarity (+1.84), acousticness similarity (+0.79)

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I ran the Weight Shift experiment (Double the importance of energy and half the importance of genre). When I ran this experiment, the recommendation output was generally similar to the original output. However, some songs swapped places in their rankings or new songs were included in the recommendation list. Since the energy weight was doubled, that feature held more weight and priority when recommending songs. 

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



