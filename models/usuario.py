
from mongoengine import Document, StringField


class Usuario(Document):
    """
    Modelo que representa a un usuario en el sistema.
    Hereda de Document para persistencia en MongoDB.
    """
    
   
    # DEFINICIÓN DE CAMPOS
   
    username = StringField(
        required=True,    
        unique=True,     
        max_length=50   
    )
    
    password = StringField(
        required=True   
    ) 
    
    nombre = StringField(
        required=True,  
        max_length=100   
    )
    
    email = StringField(
        required=True,    
        unique=True,     
        max_length=100   
    )
    
   
    # CONFIGURACIÓN METADATA
  
    meta = {
        'collection': 'Nuevos_usuarios', 
        'indexes': ['username', 'email'] 
    }