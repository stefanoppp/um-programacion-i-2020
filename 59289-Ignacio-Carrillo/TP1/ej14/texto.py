class Texto():

    def __init__(self):
        self.texto=""

    def setTexto(self):
        self.texto="""
        No es algo nuevo, pero sí un material a tener muy presente por 
        las aplicaciones presentes y futuras que tiene y puede tener. 
        El grafeno es un material proveniente del grafito y surge cuando 
        las partículas del carbono se agrupan de forma densa en láminas 
        con forma hexagonal. El grafeno es, además, el material más fuerte 
        que existe. Lo han confirmado científicos en la universidad 
        de Columbia y publicando el hallazgo en la revista 'Science'."""
        self.texto=self.texto.lower()
        self.texto=self.texto.replace(",","")
        self.texto=self.texto.replace(".","")
        self.texto=self.texto.replace("'","")
        self.texto=self.texto.replace("\n","")

    def getTexto(self):
        return self.texto