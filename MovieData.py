class MovieDataClass():
    def __init__(self, movieData:dict):
        self.title          = movieData['title']
        self.release_date   = movieData['release_date']
        self.mpaa_rating    = movieData['mpaa_rating']
        self.runtime        = movieData['runtime']
        self.genres         = movieData['genres']
        self.synopsis       = movieData['synopsis']
        self.cast           = movieData['cast']
        self.cast_meta      = movieData['cast_meta']
        
    # getTitle
    # Returns the movie's title
    def getTitle(self):
        return self.title
        
    # getReleaseDate
    # Returns the movie's release date
    def getReleaseDate(self):
        return self.release_date
    
    # getMpaaRating
    # Returns the movie's MPAA rating
    def getMpaaRating(self):
        return self.mpaa_rating
    
    # getRuntime
    # Returns the movie's total runtime length in minutes
    def getRuntime(self):
        hours, minutes = self.runtime.split()
        hours   = (int(hours.strip('h')) * 60)
        minutes = int(minutes.strip('min'))
        totalMinutes = (hours + minutes)
        
        return f"{totalMinutes} minutes"
        
    # getGenres
    # @param    int limit   (default: 3)
    # Returns the movie's genres as a comma-delimited string
    def getGenres(self, limit:int=3):
        if (limit not in range(1, len(self.cast))):
            limit = 3
        
        data = []
        for genre in self.genres[:limit]:
            data.append(genre.findChild().text)
            
        return ", ".join(data)
        
    # getSynopsis
    # Returns the movie's synopsis
    def getSynopsis(self):
        return self.synopsis
    
    # getCast
    # @param    int limit   (default: 5)
    # Returns the first [5] actors of the movie's cast
    def getCast(self, limit:int=5):
        if (limit not in range(1, len(self.cast))):
            limit = 5
            
        data = []
        for actor in self.cast[:limit]:
            data.append(actor.find(attrs={'data-testid': 'title-cast-item__actor'}).text)
            
        return ", ".join(data)
    
    # getDirector
    # Returns the movie's director
    def getDirector(self):
        director = ''
        for meta in self.cast_meta:
            metaLabel = meta.findChild(class_='ipc-metadata-list-item__label')
            
            if ('Director' in metaLabel.text):
                director = metaLabel.find_next_sibling(class_='ipc-metadata-list-item__content-container').find('li').text
                break
        
        return director