class Airplane:
    def __init__(self, type, crew, destination):
        self.type = type
        self.crew = crew
        self.destination = destination

    def add_memeber(self, new_member):
        self.crew.append(new_member)

    def check_glue(self):
        return "This is the wrong day to stop sniffing glue"
    
    def hasShirley(self):
        if 'Shirley' not in self.crew:
            return "Don't call me Shirley"
        else:
            return "Please, call me Shirley"
    