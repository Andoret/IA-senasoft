import requests, uuid, json, os, time,sys, asyncio,io
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition


def traducir(palabras=str):
    # Add your key and endpoint
    key = "67d68aa7abcd40f8858217bac5cc31b4"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

    location = "eastus"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['en', 'it','fr']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Cuerpo de la API, aqui ira el string a traducir.
    body = [{
        'text': palabras
    }]
    #Asignacion a la variable de la solicitud y respuesta que se genera
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    #Conversion de la respuesta a archivo JSON
    response = request.json()
    #Creacion de arreglo donde se guardaran los datos de la traduccion 
    resultados=[]
    x=response[0]['translations']
    for i in range (0,len(x)):
        resultados.append(x[i]['text'])
    return resultados

def deteccion():
   


    # Se define el Endpoint de prediccion y la clave de autorización
    endpoint = "https://cs-1.cognitiveservices.azure.com/customvision/v3.0/Prediction/62b7da73-fbc0-4791-8f6b-f9c69d53f37b/classify/iterations/Iteration1/image"
    api_key = "78d6f6120a0341b88cefc3f3fba68d71"

    # URL para la prediccion
    prediction_url = endpoint

    #Ruta de la imagen a clasificar
    image_path = "afgano.jpg"

    # Abre la imagen y la envía a la API de predicción
    with open(image_path, "rb") as image_file:
        headers = {
            "Prediction-Key": api_key,
            "Content-Type": "application/octet-stream",
        }
        response = requests.post(prediction_url, data=image_file, headers=headers)

    # Analiza la respuesta JSON
    result = response.json()
 
    resultados=[];
    x=result['predictions']
    
    for i in range (0, len(x)):
        a=result['predictions'][i]['tagName']
        b=result['predictions'][i]['probability']
        if b>0.5:
            resultados.append([a,b])
            
    
 

def face():
    # Tu clave y punto final
    key = "1c78d365197740d89147ddd16055a475"
    endpoint = "https://face-senasoft.cognitiveservices.azure.com/"

    # Archivo de imagen
    img_file = "store-camera-1.jpg"

    # URL de la imagen
    img_url = f"https://raw.githubusercontent.com/Andoret/IA-senasoft/main/Images/Personas/Personas-21.jpg"

    # Cabeceras de la solicitud
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/json"
    }

    # Cuerpo de la solicitud
    body = {
        "url": img_url
    }

    # Realizar la solicitud
    url = f"{endpoint}/face/v1.0/detect?detectionModel=detection_01"
    response = requests.post(url, headers=headers, json=body)

    # Analizar la respuesta JSON
    result = response.json()

    print("Analizando la imagen...\n")

    # Mostrar la ubicación de las caras detectadas

    for face in result:
        print(f"Ubicación de la cara: {face['faceRectangle']}\n")



face()

        
    


