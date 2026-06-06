# --- איסוף נתונים ממוקד ומאוזן לפי עשורים וז'אנרים עם Early Exit ---

import random
import re
import lyricsgenius
import pandas as pd

token = "MM3rhwjFkBZVZU5k7fixqT4u_rCu9u7kPnLCEWZdKiEoxm0ggcRLFvIwbgg98cEL"
genius = lyricsgenius.Genius(token, timeout=20, skip_non_songs=True)

# שינינו מ-rap ל-hip-hop כדי לתפוס את שנות ה-80 וה-90
genres = ['pop', 'rock', 'hip-hop', 'country', 'blues']

decades_mapping = {
    '1970s': (1970, 1979),
    '1980s': (1980, 1989),
    '1990s': (1990, 1999),
    '2000s': (2000, 2009),
    '2010s': (2010, 2019),
    '2020s': (2020, 2026)
}

def get_decade_name(year):
    if not year:
        return None
    for decade, (start, end) in decades_mapping.items():
        if start <= year <= end:
            return decade
    return None

def get_official_song_metadata(title: str, artist_name: str) -> dict:
    search_term = f"{title} {artist_name}".strip()
    try:
        res = genius.search_songs(search_term, per_page=1, page=1)
        hits = res.get('hits', [])
        if hits:
            return hits[0].get('result', {})
    except:
        pass
    return {}

TARGET_PER_BUCKET = 30  

bucket_counters = {genre: {decade: 0 for decade in decades_mapping.keys()} for genre in genres}
collected_songs_registry = set()
all_songs_data = []

ENGLISH_ONLY_REGEX = re.compile(r'^[a-zA-Z0-9\s\.,\'\"\!\?\-\(\)\&\s\’\‘\“\”\:\/\u00C0-\u017F]+$')

print("=== מתחיל איסוף ממוטב ומהיר: שיטת Early Exit + Hip-Hop ===")

for genre in genres:
    print(f"\n==========================================")
    print(f"  מתחיל לסרוק ז'אנר: {genre.upper()}")
    print(f"==========================================")
    
    for page in range(1, 30):
        try:
            res = genius.tag(genre, page=page)
        except Exception as e:
            continue

        if not res or 'hits' not in res:
            break
            
        hits = res['hits']
        print(f"\n[עמוד {page}] נמצאו {len(hits)} להיטים פוטנציאליים.")
        
        for idx, hit in enumerate(hits, 1):
            raw_title = hit.get('title', '')
            raw_artist = hit.get('artist', '')
            if not raw_artist and hit.get('artists'):
                raw_artist = hit['artists'][0]
                
            if not raw_title or not raw_artist:
                continue
            
            # סינון שפות וקאברים (מהיר מאוד)
            if not ENGLISH_ONLY_REGEX.match(raw_title) or not ENGLISH_ONLY_REGEX.match(raw_artist):
                continue
                
            invalid_keywords = ['cover', 'tribute', 'karaoke', 'remix', 'instrumental', 'version', 'live']
            if any(kw in f"{raw_title.lower()} {raw_artist.lower()}" for kw in invalid_keywords):
                continue
                
            # --- אופטימיזציה (Early Exit): בדיקת שנה מהירה לפני הפנייה לשרת! ---
            raw_year = None
            if hit.get('release_date_components'):
                raw_year = hit['release_date_components'].get('year')
            elif hit.get('release_date'):
                match = re.search(r'\b(19\d{2}|20\d{2})\b', str(hit['release_date']))
                if match: raw_year = int(match.group(1))
            elif hit.get('year'):
                raw_year = int(hit.get('year'))
                
            if raw_year:
                raw_decade = get_decade_name(raw_year)
                # אם העשור לא רלוונטי או שהמשבצת שלו כבר מלאה - מדלגים בלי לבזבז זמן!
                if not raw_decade or bucket_counters[genre][raw_decade] >= TARGET_PER_BUCKET:
                    continue
            
            # --- שלב 2: פעימת החילוץ הרשמי (מתבצע רק לשירים שבאמת צריכים) ---
            song_info = get_official_song_metadata(raw_title, raw_artist)
            if not song_info:
                continue
                
            official_title = song_info.get('title', raw_title)
            official_artist = song_info.get('primary_artist', {}).get('name', raw_artist)
            
            song_key = f"{official_title.lower().strip()} ||| {official_artist.lower().strip()}"
            if song_key in collected_songs_registry:
                continue
                
            # חילוץ שנת היציאה האמינה והסופית
            release_year = None
            if song_info.get('release_date_components'):
                release_year = song_info['release_date_components'].get('year')
                
            if not release_year:
                continue
                
            decade_name = get_decade_name(release_year)
            if not decade_name or bucket_counters[genre][decade_name] >= TARGET_PER_BUCKET:
                continue
                
            # מילים
            song_url = song_info.get('url')
            if not song_url:
                continue
                
            lyrics = ""
            try:
                lyrics = genius.lyrics(song_url=song_url) or ""
            except:
                continue
                
            if not lyrics or len(lyrics.strip()) < 200:
                continue
            
            pageviews = song_info.get('stats', {}).get('pageviews', 0)
            
            # שמירה
            all_songs_data.append({
                'song_title': official_title,
                'artist_name': official_artist,
                'release_year': int(release_year),
                'decade': decade_name,
                'genre': genre,
                'lyrics': lyrics,
                'pageviews': pageviews,
                'featured_artists_count': len(song_info.get('featured_artists', [])),
                'primary_tag': genre,
                'source_url': song_url
            })
            
            collected_songs_registry.add(song_key)
            bucket_counters[genre][decade_name] += 1
            print(f"  >>> [הצלחה] {official_title} | עשור: {decade_name} | מונה: [{bucket_counters[genre][decade_name]}/{TARGET_PER_BUCKET}]")
            
        if all(count >= TARGET_PER_BUCKET for count in bucket_counters[genre].values()):
            print(f"\n[V] כל העשורים עבור {genre} מלאים בהצלחה! עובר לז'אנר הבא.")
            break

# שמירת הקובץ
raw_df = pd.DataFrame(all_songs_data)
raw_df.to_csv('decades_raw_balanced_songs.csv', index=False, encoding='utf-8-sig')

print("\n==========================================")
print("             הריצה הסתיימה!                ")
print("==========================================")
print(f"סה\"כ נאספו בהצלחה: {len(raw_df)} שירים.")
print("\nסיכום המשבצות:")
for g, decades in bucket_counters.items():
    print(f"{g}: {decades}")



# --- ניתוח טקסטואלי מתקדם עם מנגנון הגנה מפני כפל ספירה של Pre-Chorus וכולל מדדים נוספים כמו קללות ומילות תואר ---

import re
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import stopwords
from better_profanity import profanity

# --- הורדת משאבי NLP ---
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True) 
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)                       

STOP_WORDS = set(stopwords.words('english'))

def analyze_lyrics_advanced(lyrics):
    # הגדרת ערכי ברירת מחדל למקרה של טקסט ריק
    default_metrics = {k: 0 for k in ['total_word_count', 'count_chorus', 'count_verse', 'count_intro', 'count_bridge', 'unique_special_word', 'special_words_ratio', 'special_word_without_chorus', 'unique_ratio_no_repeated_chorus', 'profanity_count', 'profanity_ratio', 'adjectives_count', 'adjectives_ratio']}
    
    if not lyrics or not isinstance(lyrics, str):
        return default_metrics
    
    # 1. ספירת חלקי השיר עם מנגנון הגנה מפני כפל ספירה של Pre-Chorus
    raw_tags = re.findall(r'\[(.*?)\]', lyrics)
    
    chorus_count = 0
    verse_count = 0
    intro_count = 0
    bridge_count = 0
    
    # משתנה עזר כדי לדעת אם כבר ספרנו פזמון ברצף הנוכחי
    inside_chorus_zone = False
    
    for tag in raw_tags:
        tag_lower = tag.lower()
        
        # אם מדובר בפזמון או טרום-פזמון
        if 'chorus' in tag_lower:
            if not inside_chorus_zone:
                chorus_count += 1
                inside_chorus_zone = True # מסמנים שספרנו את אזור הפזמון הנוכחי
        else:
            # אם הגענו לחלק אחר (כמו Verse), מאפסים את הflag של אזור הפזמון
            inside_chorus_zone = False
            
            if 'verse' in tag_lower:
                verse_count += 1
            elif 'intro' in tag_lower:
                intro_count += 1
            elif 'bridge' in tag_lower:
                bridge_count += 1
            
    # 2. הסרת פזמונים חוזרים (מנקה את כל אזור הפזמון - כולל Pre-Chorus מהפזמון השני והלאה)
    blocks = re.split(r'(\[.*?\])', lyrics)
    modified_blocks = []
    
    actual_chorus_sessions = 0
    skip_current_block = False
    inside_repeated_chorus_zone = False
    
    for block in blocks:
        if block.startswith('[') and block.endswith(']'):
            block_lower = block.lower()
            
            if 'chorus' in block_lower:
                if not inside_repeated_chorus_zone:
                    actual_chorus_sessions += 1
                    if actual_chorus_sessions > 1:
                        inside_repeated_chorus_zone = True
                
                if inside_repeated_chorus_zone:
                    skip_current_block = True
                    continue
            else:
                inside_repeated_chorus_zone = False
                
            skip_current_block = False
            modified_blocks.append(block)
        else:
            if skip_current_block:
                continue
            modified_blocks.append(block)
            
    lyrics_no_repeated_chorus = "".join(modified_blocks)
    
    def get_clean_words(text):
        text = re.sub(r'\[.*?\]', '', text) # הסרת התגיות מהטקסט
        text = re.sub(r'[^\w\s]', '', text).lower() # הסרת סימני פיסוק
        return text.split()
    
    words_all = get_clean_words(lyrics)
    words_no_repeated_chorus = get_clean_words(lyrics_no_repeated_chorus)
    
    total_words_count = len(words_all)
    if total_words_count == 0:
        return default_metrics
        
    special_words = [w for w in words_all if w not in STOP_WORDS]
    special_words_no_chorus = [w for w in words_no_repeated_chorus if w not in STOP_WORDS]
    
    # 3. ספירת קללות ומילות תואר
    profanity_count = sum(1 for w in special_words if profanity.contains_profanity(w))
    
    tokens = nltk.word_tokenize(re.sub(r'\[.*?\]', '', lyrics))
    tagged_words = nltk.pos_tag(tokens)
    adjectives_count = sum(1 for word, tag in tagged_words if tag in ('JJ', 'JJR', 'JJS'))
    
    # 4. חישוב מדדים ויחסים
    unique_special_word = len(set(special_words))
    total_special_words = len(special_words)
    special_word_without_chorus = len(special_words_no_chorus)
    
    special_words_ratio = unique_special_word / total_special_words if total_special_words > 0 else 0
    unique_ratio_no_repeated_chorus = unique_special_word / special_word_without_chorus if special_word_without_chorus > 0 else 0
    profanity_ratio = profanity_count / total_words_count
    adjectives_ratio = adjectives_count / total_words_count
    
    return {
        'total_word_count': total_words_count,
        'count_chorus': chorus_count, # מכיל כעת פזמונים וטרום-פזמונים משולבים ללא כפל ספירה
        'count_verse': verse_count,
        'count_intro': intro_count,
        'count_bridge': bridge_count,
        'unique_special_word': unique_special_word,
        'special_words_ratio': special_words_ratio,
        'special_word_without_chorus': special_word_without_chorus,
        'unique_ratio_no_repeated_chorus': unique_ratio_no_repeated_chorus,
        'profanity_count': profanity_count,
        'profanity_ratio': profanity_ratio,
        'adjectives_count': adjectives_count,
        'adjectives_ratio': adjectives_ratio
    }

# --- טעינת קובץ המקור ועיבודו ---
print("טוען קובץ גולמי ומעבד נתונים...")
df = pd.read_csv('decades_raw_balanced_songs.csv')

print("מריץ ניתוח טקסטואלי (NLP)...")
nlp_results = df['lyrics'].apply(analyze_lyrics_advanced)
nlp_df = pd.DataFrame(list(nlp_results))

# איחוד כלל המשתנים לטבלה הסופית
final_df = pd.concat([df, nlp_df], axis=1)

# שמירת הדאטה-סט הסופי והמועשר
final_df.to_csv('final_genius_enriched_songs_by_dacades.csv', index=False, encoding='utf-8-sig')
print("הסתיים! הקובץ הסופי מוכן, ה-Pre-Chorus צומד לפזמונים בצורה נקייה.")
