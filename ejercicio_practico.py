class Cancion:
    def __init__(self, titulo, artista, duracion_segundos, album):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos
        self.album = album

    def mensaje(self):
        minutos, segundos = divmod(self.duracion_segundos, 60)
        print(f"Titulo de la cancion: {self.titulo}")
        print(f"El artista: {self.artista}")
        print(f"Duracion: {self.duracion_segundos}s")
        print(f"Del album: {self.album}")


micancion = Cancion("Bohemian Rhapsody", "Queen", 354, "A Night at the Opera")
micancion.mensaje()
