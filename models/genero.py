
from mongoengine import Document, StringField
from mongoengine.errors import ValidationError, NotUniqueError


class Genero(Document):
    """
    Modelo que representa un género en la base de datos.
    Hereda de Document para ser persistido en MongoDB.
    """
    
    # DEFINICIÓN DE CAMPOS
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
    
    # MÉTODO: VALIDACIÓN Y LIMPIEZA
    def clean(self):
        """
        Se ejecuta automáticamente antes de guardar.
        Realiza validaciones adicionales y normaliza datos.
        """
      
        if not self.nombre or not self.nombre.strip():
            raise ValidationError("El nombre no puede estar vacío")
        
      
        self.nombre = self.nombre.strip().title()
    
  
    # REPRESENTACIÓN DEL OBJETO
   
    def __str__(self):
        """
        Representación en string del objeto.
        Se usa en templates, forms, etc.
        """
        return self.nombre