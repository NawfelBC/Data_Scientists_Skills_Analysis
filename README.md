# Most popular Data Science skills in France

This is a small project to find out what are the most popular Data Science skills in France.

## Get the data

To answer this question, I first extracted skills of 1000 French Data Scientists from their LinkedIn profile using tools like [Selenium](https://selenium-python.readthedocs.io/) 
and [Linkedin-Api](https://github.com/tomquirk/linkedin-api) and stored them into a CSV file.

Code : [Id Scraper](https://github.com/NawfelBC/Portfolio/blob/main/Web%20Scraping/Linkedin%20Scraping/id_scraper.py), [Skills Scraper](https://github.com/NawfelBC/Portfolio/blob/main/Web%20Scraping/Linkedin%20Scraping/skills_scraper.py) 
<br>CSV File : [CSV](https://github.com/NawfelBC/Portfolio/blob/main/Web%20Scraping/Linkedin%20Scraping/Output/skills.csv)</br>

## Analyze the data

To analyze the data, I used Python libraries such as Pandas and Matplotlib to find out what are the most common skills in the dataset.

Code : [Notebook](https://github.com/NawfelBC/Portfolio/blob/main/Web%20Scraping/Linkedin%20Scraping/Analysis.ipynb)

## Summarize the results

With no surprise, we can see that Python, SQL and R are by far the top 3 skills mastered by Data Scientists in France. But we also see that C++ and Java are right behind occupying a respectable position.
<em>"Many organizations are turning to Java application development to meet their needs. Also, learning C/C++ offers excellent capabilities for building statistical and data tools."</em> <br>(cf. [C++ for Data Science](https://opensource.com/article/20/2/c-data-science), [Java for Data Science](https://www.kdnuggets.com/2020/04/java-used-machine-learning-data-science.html))</br>
<br></br>
<p align="center">
<img src="https://user-images.githubusercontent.com/79513906/130333650-bc08377d-b575-46ed-9312-26cdf8c8e995.PNG" width="600" height="300">
<br><strong>Figure 1 : Histogram of the 20 most popular skills by occurrences</br></strong>
<br></br>
<img src="https://user-images.githubusercontent.com/79513906/130333658-2db2928b-eee4-4cfa-be4c-8c1887ce3d31.png" width="800" height="400">
<br><strong>Figure 2 : Word Cloud of 75 skills</br></strong>
</p>

## Python Packages used :
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Numpy](https://numpy.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [wordcloud](https://amueller.github.io/word_cloud/)
- [csv](https://docs.python.org/fr/3/library/csv.html)
