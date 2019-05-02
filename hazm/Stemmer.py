# coding: utf-8

from __future__ import unicode_literals
from nltk.stem.api import StemmerI
from .Finder import finder

class Stemmer(StemmerI):
	"""
	>>> stemmer = Stemmer()
	>>> stemmer.stem('کتابی')
	'کتاب'
	>>> stemmer.stem('کتاب‌ها')
	'کتاب'
	>>> stemmer.stem('کتاب‌هایی')
	'کتاب'
	>>> stemmer.stem('کتابهایشان')
	'کتاب'
	>>> stemmer.stem('اندیشه‌اش')
	'اندیشه'
	>>> stemmer.stem('خانۀ')
	'خانه'
	"""

	def __init__(self):
		self.ends = ['ات', 'ان', 'ترین', 'تر', 'م', 'ت', 'ش', 'یی', 'ی', 'ها', 'ٔ', '‌ا', '‌']

	def stem(self, word):
		for end in self.ends:
			if word.endswith(end) and not finder(word) :
				word = word[:-len(end)]

		if word.endswith('ۀ'):
			word = word[:-1] + 'ه'

		return word
