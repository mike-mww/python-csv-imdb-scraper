# Python CSV IMDB Scraper
Python script for scraping and compiling IMDB page data from a list of URLs to a resulting CSV file.

## Getting Started
### Prerequisities
* [Python 3.9.7](https://www.python.org/downloads/release/python-397/) or higher
* [Requests 2.26](https://pypi.org/project/requests/) or higher
* [Beautiful Soup 4.10](https://pypi.org/project/beautifulsoup4/) or higher

### Installation
Download the repository files and run the command below to install the necessary packages:
```
pip install requests bs4
```

## Built with
* [Python 3.9.7](https://www.python.org/downloads/release/python-397/)
* [Requests 2.26](https://pypi.org/project/requests/)
* [Beautiful Soup 4.10](https://pypi.org/project/beautifulsoup4/)

## Usage
### Using the reference CSV file
Included in this repository is a **"imdb-data-reference.csv"** file containing a list of **[3]** IDMB page URLs. This file must consist of **[1]** or more valid URLs, with each URL on a separate line. 

**NOTE:** Script execution can be impacted the length of this list.

### Running the script
Run the following command to initialize the script:
```
python csv-imdb-scraper.py
```
Upon completion, a CSV file prefixed with **"imdb-scraping-results"** will be generated adjacent to the other script files. This file should contain all of the relevant data from the scraping process.

### Customization
While most of the data scraped from each IMDB page is as-provided, the following methods of the **MovieDataClass** class provide some degree of result tailoring:

* ***getGenres()***\
IMDB data can consist of a varied length of the genre listings. By default, this method is set to return **[3]** listings, but can accept any number in a range of **[1]** to the total number of listings scraped.

* ***getCast()***\
IMDB data can consist of a varied length of the "Top Cast" listings, which may be more/less than desired. By default, this method is set to return **[5]** listings, but can accept between a range of **[1]** to the total number of listings scraped.