# snatch
This works for most popular publications including:
* cnn
* npr
* washington post
* economist
* wired
* atlantic
* politico
* vox
* mit technology review
* jacobin
* new yorker
* the new york times
* smithsonian
* current affairs

### GetArticle.py
Takes a URL argument and outputs a text file labeled with the article's title and source publication. Uses the **Newspaper** package: https://newspaper.readthedocs.io/en/latest/

To install Newspaper, enter this into your command line interpreter:
```
pip install Newspaper3k
```

### GetArticle_input.py
Prompts the user for a URL and outputs a text file labeled with the article's title and source publication. Also uses **Newspaper**.

Output example:

```
Article is at abc3340.com$energy-secretary-rick-perry-is-designated-survivo.txt
Article is at knpr.org$senator-no-trust-sec-rick-perry-after-plutonium-transpor.txt
Article is at www.nbcnews.com$rick-perry-designated-survivor-n96788.txt
Article is at www.washingtonexaminer.com$rick-perry-braces-for-outages-from-the-polar-vorte.txt
Article is at www.star-telegram.com$article224607935.htm.txt
Article is at www.washingtonexaminer.com$daily-on-energy-rick-perry-and-democrats-in-brawl-over-secret-plutonium-shipmen.txt
Article is at www.washingtonexaminer.com$nevada-delegation-bashes-rick-perry-for-secretly-shipping-weapons-grade-plutonium-into-their-stat.txt
Article is at www.energy.gov$secretary-perry-attend-world-government-summit-ua.txt
Article is at www.fbherald.com$article_5708d3f9-ac9a-510a-8026-779eef51f6c3.htm.txt
Article is at www.expressnews.com$Perry-urges-battery-recycling-to-reduce-13541030.ph.txt
Article is at lasvegassun.com$.txt
Article is at www.mrt.com$Baker-Hughes-lands-equipment-contract-with-Golden-13598473.ph.txt
Article is at www.usnews.com$globe-trotting-political-donor-eyed-in-trump-inaugural-prob.txt
Article is at www.mohavedailynews.com$article_333eff26-2b6b-11e9-a57d-939ef3119872.htm.txt
```

### GetArticles.py
Takes an **RSS** feed link as an argument then uses **FeedParser** (https://pythonhosted.org/feedparser/introduction.html) to retrieve article links, creating a list of URLs. It iterates through this list and outputs a text file for each URL item. You do not need to install **FeedParser**, as it comes with your Python installation by default.

Example:
```

```


