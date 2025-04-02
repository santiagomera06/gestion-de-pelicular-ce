from mongoengine import Document, StringField
from mongoengine.errors import ValidationError, NotUniqueError

class Genero(Document):
    nombre = StringField(
        required=True, 
        unique=True,
        max_length=50,
        error_messages={
            'required': 'El nombre es obligatorio',
            'unique': 'Este género ya existe',
            'max_length': 'Máximo 50 caracteres'
        }
    )
    
    def clean(self):
        if not self.nombre or not self.nombre.strip():
            raise ValidationError("El nombre no puede estar vacío")
        self.nombre = self.nombre.strip().title()
    
    def __str__(self):
        return self.nombre