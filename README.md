<p align="center">
  <img src="Figures/banner.png" alt="Lyric Evolution Banner" width="100%">
</p>
# 🎵 Lyric Evolution Across Decades: Are Songs Getting Simpler?

<!-- Badges Section -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Domain-NLP%20%26%20EDA-orange?style=for-the-badge" alt="Domain" />
  <img src="https://img.shields.io/badge/Course-HUJI%2071253-red?style=for-the-badge" alt="HUJI Course" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status" />
</p>

---

> ### 💡 The Core Question & Key Takeaway
> **Did song lyrics actually become simpler or lower in quality over the last decades?**  
> **The Short Answer:** Not overall. While repetitive structures exist in modern music, our data shows no statistical decline in lyrical complexity across decades. However, specific genres (like *Blues* and *Country*) actually show a significant increase in lexical richness over time.

---

## 📑 Table of Contents
<details>
<summary><b>Click to expand Table of Contents</b></summary>

- [Overview](#overview)
- [Team Members](#team-members)
- [Dataset Description](#dataset-description)
- [Primary Variables](#primary-variables)
- [Data Cleaning & Preprocessing](#data-cleaning--preprocessing)
- [Key Findings](#key-findings)
  - [1. Overall Lyric Quality & Lexical Richness](#1-overall-lyric-quality--lexical-richness)
  - [2. Lexical Dynamics](#2-lexical-dynamics-the-rise-and-fall-of-words)
  - [3. Cultural Shifts & Profanity](#3-cultural-shifts--profanity)
  - [4. AI & LLM Detection](#4-ai--large-language-model-llm-detection)
- [Full Data Dictionary](#variables)
</details>

---

## Overview
This repository contains the Data Science final project for course **71253** at **The Hebrew University of Jerusalem**. 

Using **Exploratory Data Analysis (EDA)** and **Natural Language Processing (NLP)** techniques—including lexical richness metrics, profanity evolution tracking, and decade-level TF-IDF analysis—we analyze trends in lyric complexity, vocabulary trajectories, and the potential presence of AI/LLM influences in modern music.

---

## 👥 Team Members
* **Geva Weiss**
* **Amit Schraub**

---
---

## Dataset Description
* **Source:** [genius](https://genius.com/)
* **Data:** [Data Set](Data/final_genius_enriched_songs_by_dacades_patched.csv)
* **Records:** [785](#records)
* **Variables:** [25](#variables)

### Primary Variables
* `song_title` – Title of the track
* `artist_name` – Performing artist or group
* `release_year` / `decade` – Release year and binned decade
* `genre` – Musical genre classification (e.g., Rock, Blues, Country, Hip-Hop)
* `unique_ratio_no_repeted_chorus` – Core Lexical Diversity Metric: The ratio of unique words to total words no stop-words and without repeated chours (closer to 1 = highly diverse, closer to 0 = highly repetitive).
* `total_word_count` – Total word count per song
* `profanity_ratio` – Frequency of profane terms per track

### Data Cleaning & Preprocessing
* Handled missing values in lyric metadata.
* Cleaned stop words, punctuation, and standardized text formatting.
* Conducted lemmatization and aggregated lyrics by decade corpora for TF-IDF tracking.

---

## Key Findings

### 1. Overall Lyric Quality & Lexical Richness
* No statistical evidence indicates a general decline in song lyric quality over the years.
* A statistically significant increase in lexical richness was observed in specific genres (such as Blues and Country) across decade periods.

### 2. Lexical Dynamics: The Rise and Fall of Words
* Binary occurrence metrics (word presence per song) vs. decade-level TF-IDF frequency metrics revealed distinct trends regarding within-song repetition vs. overall era vocabulary.
* Tracked specific "Emerging Words" that surged during particular decades and subsequently faded.

### 3. Cultural Shifts & Profanity
* Identified a clear upward trend in profanity across decades, strongly aligned with the rise of Hip-Hop culture and its mainstream influence.

### 4. AI & Large Language Model (LLM) Detection
* Found no evidence of LLM usage or adoption among popular songwriters.
* Demonstrated that benchmark LLM wordlists (typically derived from scientific literature) present a domain mismatch when applied to poetic and creative song lyrics.

---





# Variables:

This table describes all the features available in the final enriched dataset, divided into logical categories: Metadata, Popularity Targets, Song Structure, and Linguistics/NLP.

| Feature Name | Category | Data Type | Description |
| :--- | :--- | :--- | :--- |
| **`song_title`** | Metadata | String | The exact title of the song as listed on Genius. |
| **`artist_name`** | Metadata | String | The name of the primary performing artist. |
| **`release_year`** | Metadata | Integer | The official release year of the song. |
| **`decade`** | Metadata | Categorical | The specific decade the song belongs to (e.g., `1990s`, `2010s`). |
| **`genre`** / **`primary_tag`** | Metadata | Categorical | The primary genre of the song (Pop, Rock, Hip-Hop, Country, Blues). |
| **`source_url`** | Metadata | String | A direct URL to the song's page on Genius. |
| **`featured_artists_count`** | Metadata | Integer | The number of guest artists (features) on the track. |
| **`pageviews`** | Popularity (Target) | Integer | Total pageviews for the song's lyrics on Genius. Serves as the primary popularity metric. |
| **`pyongs_count`** | Popularity (Target) | Integer | The number of upvotes ("Pyongs") from the Genius community. Indicates audience engagement. |
| **`lyrics`** | Structure | String | The full, raw text of the song's lyrics. |
| **`total_word_count`** | Structure | Integer | Total words in the song, excluding punctuation and meta-tags. |
| **`count_chorus`** | Structure | Integer | The number of times a chorus (or pre-chorus) section appears. |
| **`count_verse`** | Structure | Integer | The number of verse sections in the song. |
| **`count_intro`** | Structure | Integer | The number of intro sections identified. |
| **`count_bridge`** | Structure | Integer | The number of bridge sections identified. |
| **`unique_special_word`** | Linguistics (NLP) | Integer | The count of words in the song, excluding common stop-words and repetative words. |
| **`special_word_without_chorus`**| Linguistics (NLP) | Integer | Total special word count where repeated chorus sections are counted only **once** to avoid bias. |
| **`unique_ratio_no_repeated_chorus`**| Linguistics (NLP) | Float (Ratio)| **Core Lexical Diversity Metric:** The ratio of unique words to total words no stop-words and without repeated chours (closer to 1 = highly diverse, closer to 0 = highly repetitive). |
| **`special_words_ratio`** | Linguistics (NLP) | Float (Ratio)| Standard lexical diversity ratio (before chorus normalization). |
| **`profanity_count`** | Linguistics (NLP) | Integer | Total occurrences of profanity or explicit language. |
| **`profanity_ratio`** | Linguistics (NLP) | Float (Ratio)| The percentage of explicit words relative to the total word count. |
| **`adjectives_count`** | Linguistics (NLP) | Integer | Total count of adjectives identified using POS tagging. |
| **`adjectives_ratio`** | Linguistics (NLP) | Float (Ratio)| The percentage of adjectives relative to the total word count, indicating descriptive depth. |

# Records:
<img width="989" height="590" alt="טבלת סיכום כמות שירים" src="https://github.com/user-attachments/assets/41fac251-9f8a-45ad-a78e-b2d92de93a71" />

# The Fresh effect:
<img width="1454" height="728" alt="ezgif com-resize" src="https://github.com/user-attachments/assets/67c2b81e-28da-4206-a066-5f59201da19c" />
