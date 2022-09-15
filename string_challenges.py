# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
def countVowels(word):
   vowels = ['а','е', 'о', 'и', 'ы', 'у', 'э']
   total = 0
   for s in word:
      if s in vowels:
         total += 1
   return total
    
print(countVowels(word))    


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
letter = sentence.split()

print(letter[0][0])
print(letter[1][0])
print(letter[2])
print(letter[3][0])         




# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(letter[0]+letter[1]+letter[2]+letter[3])//len(letter))