
class Cancion {
    constructor(titulo, artista, duracionDeSegundos, album){
        this.titulo = titulo;
        this.artista = artista;
        this.duracionDeSegundos = duracionDeSegundos;
        this.album = album;

    }
    mensaje() {
        console.log(`Titulo de la cancion: ${this.titulo} 
            El artista: ${this.artista} 
            Duracion en segundos:${this.duracionDeSegundos} 
            Del album: ${this.album}`);
    }
}

const miCancion = new Cancion("Bohemian Rhapsody", "Queen", "354s", "At night at the opera");

miCancion.mensaje();