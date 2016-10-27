from header_data import load_data
import markovify

datum = load_data()
print "Loading data set: %s items" % len(datum)

header_entry_lists = [d[1] for d in datum]
flattened_header_titles = [item for sublist in header_entry_lists for item in sublist]
text = " ".join(flattened_header_titles)

text_model = markovify.Text(text)
while True:
    start_words = raw_input('Start with the first header: ')
    print(start_words)
    print(text_model.make_sentence_with_start(start_words))
