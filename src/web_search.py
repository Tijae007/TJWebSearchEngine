from pattern.web import Google, DuckDuckGo, Yahoo, SEARCH, IMAGE, NEWS

#Program goes here

class WebSearch:
    def __init__(self, text, search_engine='Google', license=None):
        self.text = text
        self.search_engine = search_engine
        self.license = license
    
    def get_search_engine(self):
        #get search engine
        engine = None
        if self.search_engine.lower() == 'google':
            engine = Google(license=self.license)
        elif self.search_engine.lower() == 'yahoo':
            engine = Yahoo(license=self.license)
        else:engine=DuckDuckGo(license=self.license)

        return engine

    def get_search_result(self):
        engine = self.get_search_engine()
        results = [] #empty result list
        for i in range(1, 10):
            for result in engine.search(self.text, cached=False, type=SEARCH, start=i):
                results.append(result)
        return results 
