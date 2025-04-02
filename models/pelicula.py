from mongoengine import Document, IntField, StringField, ReferenceField
from models.genero import Genero
from mongoengine.errors import ValidationError

class Pelicula(Document):
    codigo = IntField(required=True, unique=True)
    titulo = StringField(required=True, max_length=80)
    protagonista = StringField(required=True, max_length=50)
    duracion = IntField(required=True, min_value=30, max_value=200)
    resumen = StringField(required=True)
    foto = StringField()
    genero = ReferenceField(Genero, required=True)
    
    def clean(self):
        if not all([self.titulo.strip(), self.protagonista.strip(), self.resumen.strip()]):
            raise ValidationError("Los campos de texto no pueden estar vacíos")
    
    def __str__(self):
        return f"{self.titulo} ({self.codigo})"