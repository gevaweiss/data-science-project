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


<style type="text/css">
#T_50552_row0_col0, #T_50552_row0_col1, #T_50552_row1_col0, #T_50552_row1_col1, #T_50552_row1_col4, #T_50552_row2_col0, #T_50552_row2_col1, #T_50552_row2_col2, #T_50552_row2_col3, #T_50552_row2_col4, #T_50552_row3_col0, #T_50552_row3_col1, #T_50552_row3_col2, #T_50552_row3_col3, #T_50552_row3_col4, #T_50552_row4_col0, #T_50552_row4_col1, #T_50552_row4_col2, #T_50552_row4_col3, #T_50552_row4_col4 {
  background-color: #08306b;
  color: #f1f1f1;
}
#T_50552_row0_col2 {
  background-color: #3a8ac2;
  color: #f1f1f1;
}
#T_50552_row0_col3 {
  background-color: #5aa2cf;
  color: #f1f1f1;
}
#T_50552_row0_col4 {
  background-color: #f7fbff;
  color: #000000;
}
#T_50552_row1_col2 {
  background-color: #2777b8;
  color: #f1f1f1;
}
#T_50552_row1_col3 {
  background-color: #1865ac;
  color: #f1f1f1;
}
</style>
<table id="T_50552">
  <thead>
    <tr>
      <th class="index_name level0" >genre</th>
      <th id="T_50552_level0_col0" class="col_heading level0 col0" >rock</th>
      <th id="T_50552_level0_col1" class="col_heading level0 col1" >blues</th>
      <th id="T_50552_level0_col2" class="col_heading level0 col2" >pop</th>
      <th id="T_50552_level0_col3" class="col_heading level0 col3" >country</th>
      <th id="T_50552_level0_col4" class="col_heading level0 col4" >hip-hop</th>
    </tr>
    <tr>
      <th class="index_name level0" >decade</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_50552_level0_row0" class="row_heading level0 row0" >1980s</th>
      <td id="T_50552_row0_col0" class="data row0 col0" >30</td>
      <td id="T_50552_row0_col1" class="data row0 col1" >30</td>
      <td id="T_50552_row0_col2" class="data row0 col2" >20</td>
      <td id="T_50552_row0_col3" class="data row0 col3" >17</td>
      <td id="T_50552_row0_col4" class="data row0 col4" >1</td>
    </tr>
    <tr>
      <th id="T_50552_level0_row1" class="row_heading level0 row1" >1990s</th>
      <td id="T_50552_row1_col0" class="data row1 col0" >30</td>
      <td id="T_50552_row1_col1" class="data row1 col1" >30</td>
      <td id="T_50552_row1_col2" class="data row1 col2" >22</td>
      <td id="T_50552_row1_col3" class="data row1 col3" >24</td>
      <td id="T_50552_row1_col4" class="data row1 col4" >30</td>
    </tr>
    <tr>
      <th id="T_50552_level0_row2" class="row_heading level0 row2" >2000s</th>
      <td id="T_50552_row2_col0" class="data row2 col0" >30</td>
      <td id="T_50552_row2_col1" class="data row2 col1" >30</td>
      <td id="T_50552_row2_col2" class="data row2 col2" >30</td>
      <td id="T_50552_row2_col3" class="data row2 col3" >30</td>
      <td id="T_50552_row2_col4" class="data row2 col4" >30</td>
    </tr>
    <tr>
      <th id="T_50552_level0_row3" class="row_heading level0 row3" >2010s</th>
      <td id="T_50552_row3_col0" class="data row3 col0" >30</td>
      <td id="T_50552_row3_col1" class="data row3 col1" >30</td>
      <td id="T_50552_row3_col2" class="data row3 col2" >30</td>
      <td id="T_50552_row3_col3" class="data row3 col3" >30</td>
      <td id="T_50552_row3_col4" class="data row3 col4" >30</td>
    </tr>
    <tr>
      <th id="T_50552_level0_row4" class="row_heading level0 row4" >2020s</th>
      <td id="T_50552_row4_col0" class="data row4 col0" >30</td>
      <td id="T_50552_row4_col1" class="data row4 col1" >30</td>
      <td id="T_50552_row4_col2" class="data row4 col2" >30</td>
      <td id="T_50552_row4_col3" class="data row4 col3" >30</td>
      <td id="T_50552_row4_col4" class="data row4 col4" >30</td>
    </tr>
  </tbody>
</table>
