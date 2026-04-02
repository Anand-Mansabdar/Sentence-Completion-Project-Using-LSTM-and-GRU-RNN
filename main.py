import pandas as pd
import string

quotes = pd.Series(["Hello!", "Python is great.", "NLP, ML & AI"])

translator = str.maketrans("", "", string.whitespace)
punct_trans = str.maketrans("", "", string.punctuation)
quotes = quotes.apply(lambda x: x.translate(translator))
quotes =quotes.apply(lambda x: x.translate(punct_trans))

print(quotes)