from dotenv import dotenv_values

class Config:
   config = dotenv_values(".env")

   SECRET_KEY = "f8b3b8fedd7b06a19d390953ad19c7fbc7d90e36c2cb02f09b6a893f28168f68"
   SERVER_NAME = "127.0.0.1:5000"
   DEBUG = True

   DATABASE_USERNEME = config["DATABASE_USERNAME"]
   DATABASE_PASSWORD = config["DATABASE_PASSWORD"]
   DATABASE_HOST = config["DATABASE_HOST"]
   DATABASE_PORT = config["DATABASE_PORT"]
   
   TEMPLATE_FOLDER = "templates/"
   STATIC_FOLDER = "static_folder/"
   
    
    
    
    
    
    
    
    
    
    
