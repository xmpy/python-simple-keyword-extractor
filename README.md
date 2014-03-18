#python-simple-keyword-extractor

This is simple application which can extract some keywords from any text in english. Here is the example.
####Examlpe1
***input:***
	
	North Carolina Lawmakers Hope to Even Road for Drivers By Charging Fees for Green Cars
***output:***

	[(u'green car', 11.698208550017846), (u'lawmakers', 10.456571685325445), (u'charging', 8.923121620752825), (u'drivers', 8.342368639313554), (u'fees', 7.656597987262219), (u'road', 6.100696524274138), (u'north carolina', 5.989348036266919), (u'hope', 5.51657495071713)]

####Examlpe2
***input:***

	Vine, Twitter’s New Video Tool, Hits 13 Million Users
***output:***

	[(u'twitter', 12.139233693611638), (u'new video', 11.519009855805118), (u'vine', 9.337887497855448), (u'users', 6.901533219066751), (u'tool', 6.282244406813816), (u'million', 6.074440357050916), (u'13', 5.666799707014712)]
	
##Quick Start
If you are on Mac or Ubuntu, you could start with:

	git clone git://github.com/xmpy/python-simple-keyword-extractor.git
	cd python-simple-keyword-extractor && make sysdeps && make install

Then you can see the demo webpage in `http://127.0.0.1:9876/`

##How it works?
It used a dictionary which from Wikipedia. And to calculate the IDF of these wikipedia entities, I used the [Google Ngrams](https://books.google.com/ngrams) data. In this demo, I only used 1gram and 2gram Google Ngram data, all the 1gram and 2gram Wikipedia Entities and their IDF is in the file `build_trie\1_2gram_idf`.

Given the IDF score of one word, the score of this word is calculated base on the TF/IDF.

##How I used google ngram to get IDF?
TO DO ..