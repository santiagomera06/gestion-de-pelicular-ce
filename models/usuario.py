from mongoengine import Document, StringField

class Usuario(Document):
    username = StringField(required=True, unique=True, max_length=50)
    password = StringField(required=True)
    nombre = StringField(required=True, max_length=100)
    email = StringField(required=True, unique=True, max_length=100)
    
    meta = {
        'collection': 'Nuevos_usuarios',
        'indexes': ['username', 'email']
    }