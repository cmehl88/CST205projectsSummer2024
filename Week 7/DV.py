import string

# The long text from a random book 
the_text = """
From the rising to the setting of the sun, Deal and its environs daily presented to the eye of a stranger, a singular and interesting picture. Afloat and on shore, 
the first disturbers of our nocturnal repose, were the morning guns, and reveille. By their united efforts, thousands of dormant spirits were daily roused into action, 
some to prepare for a long and a tough pull at the oar—others for a hard cruise on shore. From day-break all was life and gaiety on board; and ere the sun had advanced 
far on his diurnal journey, hundreds of boats filled with naval and military heroes, were skimming along the surface of the briny deep, and with fearful velocity hastening 
towards the landing-place. The foraging parties returned to their ships on procuring the provisions of which they stood in need; those on pleasure remained on shore to enjoy 
the sports of the day. On the departure of the former, stillness reigned through every corner of the town, till noon, when boats, as formidable in point of numbers as before, 
again approached the beach, and poured fresh cargoes of emigrants into it, to the great annoyance of all, save shopkeepers and publicans. On landing, each officer pursued the 
route which fancy pointed out. The politician retired to some place of entertainment, and scanned the pages of the newspapers; the sedate and prudent had an eye to their personal 
comforts; and the loungers made arrangements for a cruise through the town, to torment some unfortunate billiard marker, or make some confectioner, or milliner's shop girl fancy 
herself a goddess. Engaged in similar interesting and honourable employments, the various groups promenaded the streets, till old father time, pointing to the hour of four, gave 
the whole a hint to retire and partake of Deal hospitality, or the good things which their friends had provided for them on board. From the latter hour, every hotel, and minor 
place of public resort, were crowded with warriors of every description, whence hundreds of them, after dedicating many a full flowing cup to those they had left behind, went 
daily reeling to their boats, as happy as the juice of the grape, or malt could make them, all the way singing,
"""

# The stop words list from the lab example
stop_words = [
    "a", "about", "above", "after", "again", "against", "all", "also", "am", "an", "and", "any", "are", "aren't", 
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "can't", 
    "cannot", "com", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", 
    "each", "else", "ever", "few", "for", "from", "further", "get", "had", "hadn't", "has", "hasn't", "have", "haven't", 
    "having", "he", "he'd", "he'll", "he's", "hence", "her", "here", "here's", "hers", "herself", "him", "himself", 
    "his", "how", "how's", "however", "http", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", 
    "it", "it's", "its", "itself", "just", "k", "let's", "like", "me", "more", "most", "mustn't", "my", "myself", 
    "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "otherwise", "ought", "our", "ours", 
    "ourselves", "out", "over", "own", "r", "same", "shall", "shan't", "she", "she'd", "she'll", "she's", "should", 
    "shouldn't", "since", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", 
    "themselves", "then", "there", "there's", "therefore", "these", "they", "they'd", "they'll", "they're", 
    "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", 
    "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", 
    "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "www", "you", 
    "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
]