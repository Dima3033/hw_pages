try:
   txt = 'The self-study lessons in this section are written and organised by English level based on the Common European Framework of Reference for languages (CEFR). There are different types of texts and interactive exercises that practise the reading skills you need to do well in your studies, to get ahead at work and to communicate in English in your free time.'
   print(txt)
   wordsTxt = input('words ->')
   words = wordsTxt.split()
   print(words)
   for word in words:
      if txt.count(word) > 0:
         temp = word.upper()
         txt = txt.replace(word, temp)
         print(txt)
except Exception as ex:
   print(f'Erorr information: {ex}')