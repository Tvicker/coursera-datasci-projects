__author__ = 'xead'
# coding: utf-8

from sentiment_classifier import SentimentClassifier

clf = SentimentClassifier()

pred = clf.get_prediction_message("Этот смартфон самый лучший")

print (pred)
