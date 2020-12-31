"""
Given the page number and its content, return hashmap where
the key is the word and values are the page numbers the word
appears. Please note that if a word appears more than once
in a page, that page should only be displayed once. E.g.:

page_1 = 'this is a test this'
page_2 = 'test this'

output:
{
  'this': [1,2],
  'is': [1],
  'a': [1],
  'test': [1,2],
}

"""

from collections import defaultdict

def read_book(book):
  word_indices = defaultdict(lambda: [])

  # bp -> book page
  # pn -> page number
  for pn, bp in enumerate(book):
    words = bp.split(" ")
    # w -> word
    for w in words:
      if pn+1 not in word_indices[w]:
        word_indices[w].append(pn + 1)

  word_indices_tuple = tuple((w, tuple(pn)) for w, pn in word_indices.items())
  return word_indices, word_indices_tuple

page_1 = 'the brown fox ate the chicken'
page_2 = 'the chicken was tasty'
book = [page_1, page_2]

read_book(book)