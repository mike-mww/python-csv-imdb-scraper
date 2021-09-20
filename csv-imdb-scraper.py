import os.path
import csv
import requests
import bs4
from datetime import datetime
from MovieData import MovieDataClass

# Establish the incoming CSV file to reference...
inCsv = '.\imdb-data-reference.csv'

# Begin reading and parsing the incoming CSV file...
if (os.path.exists(inCsv)):
    inData = open(inCsv, encoding='UTF-8')
    inCsvData = csv.reader(inData)
    dataLines = list(inCsvData)
    
    # Prepare a list for compiled movies data...
    outCsvData = []
    
    # Loop through all page URLs...
    for line in dataLines:
        pageUrl = line[0]
        
        # Download the page...
        response = requests.get(pageUrl)
        
        # Begin scraping the valid page...
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
        
            # Gather the raw data for this page...
            rawMovieData = {
                'title':        soup.find('h1', {'data-testid': 'hero-title-block__title'}).text,
                'release_date': soup.find('section', {'data-testid': 'Details'}).find(attrs={'data-testid': 'title-details-releasedate'}).find(attrs={'class': 'ipc-metadata-list-item__list-content-item'}).text,
                'mpaa_rating':  soup.find(attrs={'data-testid': 'hero-title-block__metadata'}).findAll('li')[1].findNext('span').text,
                'runtime':      soup.find(attrs={'data-testid': 'hero-title-block__metadata'}).findAll('li')[2].text,
                'genres':       soup.find('section', {'data-testid': 'Storyline'}).find(attrs={'data-testid': 'storyline-genres'}).find('ul', {'class': 'ipc-metadata-list-item__list-content'}).findAll('li'),
                'synopsis':     soup.find('section', {'data-testid': 'Storyline'}).find(attrs={'data-testid': 'storyline-plot-summary'}).findChild().findChild().text,
                'cast':         soup.find('section', {'data-testid': 'title-cast'}).findAll(attrs={'data-testid': 'title-cast-item'}),
                'cast_meta':    soup.find('section', {'data-testid': 'title-cast'}).findAll('li', {'class': 'ipc-metadata-list__item'})
            }
        
            # Compile the movie data into human-readable format...
            movieData = MovieDataClass(rawMovieData)
            
            rowData = []
            rowData.append(pageUrl)
            rowData.append(movieData.getTitle())
            rowData.append(movieData.getReleaseDate())
            rowData.append(movieData.getMpaaRating())
            rowData.append(movieData.getRuntime())
            rowData.append(movieData.getGenres())
            rowData.append(movieData.getSynopsis())
            rowData.append(movieData.getCast(5))
            rowData.append(movieData.getDirector())
            
            # Add movie data to the compiled movies data list...
            outCsvData.append(rowData)
        else:
            continue
    
    # Prepare a CSV file for the results...
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    
    outCsv = f"imdb-scraping-results-{timestamp}.csv"
    outCsvFile = open(outCsv, mode='w', newline='')
    outCsvWriter = csv.writer(outCsvFile, delimiter=',')
    
    # Create the header row...
    outCsvWriter.writerow(['URL', 'Title', 'Release Date', 'MPAA Rating', 'Runtime', 'Genres', 'Synopsis', 'Cast', 'Director'])
    
    # Add the compiled movies data list...
    outCsvWriter.writerows(outCsvData)
    
    # Close the CSV file...
    outCsvFile.close()
    