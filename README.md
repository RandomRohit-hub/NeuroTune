


# 🎵 NeuroTune - A Spotify-like Song Recommendation System

**NeuroTune** is a content-based music recommendation system inspired by Spotify. It suggests songs based on audio and metadata similarity using machine learning techniques. Built with a simple, interactive interface using **Streamlit**, it enables users to explore similar tracks effortlessly.

---

## 📌 Features

- ✅ Select a song and get **top 10 similar recommendations**
- ✅ Interactive UI powered by **Streamlit**
- ✅ Fast and efficient recommendations using **cosine similarity**
- ❌ *Artist-based recommendations are still under development*

---

## 🛠️ How It Works

1. **Dataset**: A cleaned version of a Spotify-like song dataset containing song names and features.
2. **Feature Extraction**: Used `TfidfVectorizer` on the `song` names (or lyrics/features, if available).
3. **Similarity Matrix**: Generated using `cosine_similarity` to compute the closeness of songs.
4. **Recommendation**: For a selected song, the app retrieves and displays the top 10 most similar tracks.
5. **Deployment**: Built as a web app using `Streamlit`.

---

## 💻 Libraries Used

| Library           | Purpose                              |
|------------------|--------------------------------------|
| `pandas`         | Data loading and preprocessing       |
| `scikit-learn`   | TF-IDF vectorization and similarity  |
| `pickle`         | Saving and loading precomputed data  |
| `streamlit`      | Web app UI and interactivity         |
| `os`             | File checks and safe execution       |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/NeuroTune.git
cd NeuroTune
