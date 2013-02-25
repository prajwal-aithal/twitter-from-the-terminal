Twitter From the Terminal
=========================

---

This app allows us to use some features of twitter from the command-line. Currently this bot includes only the search feature
You can search for any query and it gives out the top tweets about that query.

Work to be done
---------------
1. Improvisation - Include OAuth and other operations that need authentication.

User Manual
-----------
1. Search - `$ python twitterbot.py search query rpp result_type`
	
	query - Escaped search query

	rpp - rpp number is the number of results (maximum of 100)
	
	result_type - mixed / recent/ popular.

2. Trend - `$ python twitterbot.py trending timeframe`
	
	timeframe - daily/ weekly/ or nothing.