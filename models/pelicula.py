
from mongoengine import Document, IntField, StringField, ReferenceField
from models.genero import Genero  
from mongoengine.errors import ValidationError  


class Pelicula(Document):
    """
    Modelo que representa una película en la base de datos.
    Hereda de Document para persistencia en MongoDB.
    """
    
    # DEFINICIÓN DE CAMPOS
   
    codigo = IntField(required=True, unique=True) 
    titulo = StringField(required=True, max_length=80)  
    protagonista = StringField(required=True, max_length=50)  
    duracion = IntField(
        required=True,
        min_value=30, 
        max_value=200  
    )
    resumen = StringField(required=True)  
    foto = StringField()  
    genero = ReferenceField(Genero, required=True)  
    
   
    # VALIDACIÓN PERSONALIZADA
   
    def clean(self):
        """
        Validación automática antes de guardar.
        Verifica que los campos de texto no estén vacíos.
        """
        if not all([self.titulo.strip(), self.protagonista.strip(), self.resumen.strip()]):
            raise ValidationError("Los campos de texto no pueden estar vacíos")
    
    
    # REPRESENTACIÓN DEL OBJETO
   
    def __str__(self):
        """
        Representación legible de la película.
        Se usa en interfaces administrativas y formularios.
        """
        return f"{self.titulo} ({self.codigo})"