# data-science-project
## Dataset Data Dictionary

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

<img width="989" height="590" alt="טבלת סיכום כמות שירים" src="https://github.com/user-attachments/assets/41fac251-9f8a-45ad-a78e-b2d92de93a71" />
