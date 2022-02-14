class Song:

    def __init__(self, name: str, composer: str, filepath: str, era: str, country: str):
        self.name = name
        self.composer= composer
        self.filepath = filepath
        self.era = era
        self.country = country
    
    def __repr__(self):
        return f"Name: {self.name}\nComposer: {self.composer}\nEra: {self.era}\nCountry: {self.country}"