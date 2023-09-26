import React from 'react';
import ReactDOM from 'react-dom/client';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid'
function Translate(){

   
    let key = "67d68aa7abcd40f8858217bac5cc31b4";
    let endpoint = "https://api.cognitive.microsofttranslator.com";
    let location = "eastus";
   
    const headers={
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': uuidv4().toString()
    }
    axios({
        method:'post',
        url: endpoint+'/translate',
        headers,
        params: {
            'api-version': '3.0',
            'from': 'es',
            'to': ['fr']
        },
        data: [{
            'text': 'Ohh que genial!'
        }],
        
    })
    .then((response => {
       
        const x= response.data
        console.log(x[0].translations[0].text)
    }))
    .catch((error => {
        console.log(error)
    }))
}

export default Translate