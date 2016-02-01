#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv,unicodedata,sys

sentences={}
with open("datasetSentences.txt","rb") as f:
	rd=csv.reader(f,delimiter='\t')
	count=0
	for line in rd:
		if count==0:
			count=1
			continue
		line[1]=line[1].replace('-LRB-','(')
		line[1]=line[1].replace('-RRB-',')')
		line[1]=line[1].replace('Â', '')
		line[1]=line[1].replace('Ã©', 'e')
		line[1]=line[1].replace('Ã¨', 'e')
		line[1]=line[1].replace('Ã¯', 'i')
		line[1]=line[1].replace('Ã³', 'o')
		line[1]=line[1].replace('Ã´', 'o')
		line[1]=line[1].replace('Ã¶', 'o')
		line[1]=line[1].replace('Ã±', 'n')
		line[1]=line[1].replace('Ã¡', 'a')
		line[1]=line[1].replace('Ã¢', 'a')
		line[1]=line[1].replace('Ã£', 'a')
		line[1]=line[1].replace('\xc3\x83\xc2\xa0', 'a')
		line[1]=line[1].replace('Ã¼', 'u')
		line[1]=line[1].replace('Ã»', 'u')
		line[1]=line[1].replace('Ã§', 'c')
		line[1]=line[1].replace('Ã¦', 'ae')
		line[1]=line[1].replace('Ã­', 'i')
		line[1]=line[1].replace('\xa0', ' ')
		line[1]=line[1].replace('\xc2', '')
		sentences[line[0]]=line[1]

train={}
test={}
dev={}
sents=[]
with open("datasetSplit.txt","rb") as f:
	rd=csv.reader(f,delimiter=',')
	count=0
	for line in rd:
		if count==0:
			count=1
			continue
		if line[1]=='1':
			train[sentences[line[0]]]=0
			sents.append(sentences[line[0]])
		elif line[1]=='2':
			test[sentences[line[0]]]=0
		elif line[1]=='3':
			dev[sentences[line[0]]]=0

train_sent = train.copy()
string=" ".join(sents)
with open("dictionary.txt","rb") as f:
	rd=csv.reader(f,delimiter='|')
	for line in rd:
		line[0]=line[0].replace('é','e')
		line[0]=line[0].replace('è','e')
		line[0]=line[0].replace('ï','i')
		line[0]=line[0].replace('í','i')
		line[0]=line[0].replace('ó','o')
		line[0]=line[0].replace('ô','o')
		line[0]=line[0].replace('ö','o')
		line[0]=line[0].replace('á','a')
		line[0]=line[0].replace('â','a')
		line[0]=line[0].replace('ã','a')
		line[0]=line[0].replace('à','a')
		line[0]=line[0].replace('ü','u')
		line[0]=line[0].replace('û','u')
		line[0]=line[0].replace('ñ','n')
		line[0]=line[0].replace('ç','c')
		line[0]=line[0].replace('æ','ae')
		line[0]=line[0].replace('\xa0', ' ')
		line[0]=line[0].replace('\xc2', '')
		if line[0] in string:
			train[line[0]]=line[1]
		if line[0] in test:
			test[line[0]]=line[1]
		if line[0] in train_sent:
			train_sent[line[0]]=line[1]
		if line[0] in dev:
			dev[line[0]]=line[1]


labels={}
with open("sentiment_labels.txt","rb") as f:
	rd=csv.reader(f,delimiter='|')
	count=0
	for line in rd:
		if count==0:
			count=1
			continue
		labels[line[0]]=float(line[1])

for key in train:
	train[key]=labels[train[key]]
for key in train_sent:
	train_sent[key]=labels[train_sent[key]]
for key in test:
	test[key]=labels[test[key]]
for key in dev:
	dev[key]=labels[dev[key]]

print len(train)
print len(train_sent)
print len(test)
print len(dev)

with open("sst_train_phrases.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in train:
		wr.writerow([train[key],key])
with open("sst_train_sentences.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in train_sent:
		wr.writerow([train_sent[key],key])
with open("sst_test.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in test:
		wr.writerow([test[key],key])
with open("sst_dev.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in dev:
		wr.writerow([dev[key],key])

with open("sst5_train_phrases.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in train:
		x=train[key]
		if x<=0.2:
			x='very neg'
		elif x<=0.4:
			x='neg'
		elif x<=0.6:
			x='neu'
		elif x<=0.8:
			x='pos'
		elif x<=1:
			x='very pos'
		wr.writerow([key,x])
with open("sst5_train_sentences.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in train_sent:
		x=train_sent[key]
		if x<=0.2:
			x='very neg'
		elif x<=0.4:
			x='neg'
		elif x<=0.6:
			x='neu'
		elif x<=0.8:
			x='pos'
		elif x<=1:
			x='very pos'
		wr.writerow([key,x])
with open("sst5_test.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in test:
		x=test[key]
		if x<=0.2:
			x='very neg'
		elif x<=0.4:
			x='neg'
		elif x<=0.6:
			x='neu'
		elif x<=0.8:
			x='pos'
		elif x<=1:
			x='very pos'
		wr.writerow([key,x])
with open("sst5_dev.csv","wb") as f:
	wr=csv.writer(f,delimiter=',')
	for key in dev:
		x=dev[key]
		if x<=0.2:
			x='very neg'
		elif x<=0.4:
			x='neg'
		elif x<=0.6:
			x='neu'
		elif x<=0.8:
			x='pos'
		elif x<=1:
			x='very pos'
		wr.writerow([key,x])

