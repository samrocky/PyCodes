# وارد کردن کتابخانه‌های مورد نیاز
import re
import string

# تعداد کلمات دیکشنری
n = int(input())

# ایجاد یک دیکشنری خالی
dictionary = {}

# حلقه برای خواندن n کلمه و ترجمه‌هایشان
for i in range(n):
    # خواندن یک خط و تبدیل آن به لیست کلمات
    line = input().split()
    # اضافه کردن کلمه و ترجمه‌هایش به دیکشنری
    dictionary[line[0]] = line[1:]

print(dictionary)

# خواندن جمله برای ترجمه
sentence = input()

# تشخیص زبان جمله با استفاده از حرف اول آن
#language = sentence[0]

# تبدیل جمله به لیست کلمات
words = sentence.split()

# ایجاد یک لیست خالی برای نگهداری کلمات ترجمه شده
translated_words = []

# حلقه برای بررسی هر کلمه
for word in words:
    word = word.strip(string.punctuation)
    if word in dictionary.keys():
        print(True)
        print(dictionary[word])
    '''else:
        # اگر کلمه در دیکشنری نباشد، خود کلمه را برگردان
        translated_word = word'''
    # اضافه کردن کلمه ترجمه شده به لیست
    #translated_words.append(translated_word)

# تبدیل لیست کلمات ترجمه شده به یک جمله با استفاده از فاصله
#translated_sentence = " ".join(translated_words)

# چاپ جمله ترجمه شده
#print(translated_sentence)

