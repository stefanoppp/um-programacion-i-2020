import requests

class Coronavirus():
    
    def __init__(self):
        self.ingreso= input("Ingrese el pais de inspeccion:\n")
        self.lista=[]
        self.pais=[]
        self.lista1=["Puesto","Pais","Total de casos","Nuevos casos","Total de muertes","Nuevas muertes diarias","Recuperados","Activos","Críticos","Casos"]

    def datos(self):

        URL = 'https://corona-stats.online/'
        page = requests.get(URL)
        texto=page.text
        texto = texto.replace("╔", "")
        texto = texto.replace("║", "")
        texto = texto.replace(",", ".")
        texto = texto.replace("│", ",")
        texto = texto.replace("─", "")
        texto = texto.replace("╢", "")
        texto = texto.replace(" ", "")
        texto = texto.replace("┼", "")
        texto = texto.replace("\t", " ")
        texto = texto.replace("╟", "\n")
        texto = texto.replace("=", "")
        texto = texto.replace(" ", "")
        #texto = texto.replace("▲", "")
        print(texto)
        
        self.pais = texto[texto.find(self.ingreso)-2:]
        self.pais = self.pais[:self.pais.find("\n")]
        self.lista=self.pais.split(sep=",")
        print("\nLa informacion en tiempo real es:\n")
        
        for i in range(len(self.lista)):
            
            print(self.lista1[i]+":  "+self.lista[i]+"\n")
        #print(self.lista)

if __name__ == "__main__":
    p = Coronavirus()
    p.datos()