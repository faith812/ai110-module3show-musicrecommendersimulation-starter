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

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

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



