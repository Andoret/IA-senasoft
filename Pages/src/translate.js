import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom/client';
import axios from 'axios';
import './Translate.css';
import { v4 as uuidv4 } from 'uuid'


function Translate() {

    let key = "67d68aa7abcd40f8858217bac5cc31b4";
    let endpoint = "https://api.cognitive.microsofttranslator.com";
    let location = "eastus";
    const headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': uuidv4().toString()
    }
    const [traducciones, setTraducciones] = useState([]);
    useEffect(() => {
        axios({
            method: 'post',
            url: endpoint + '/translate',
            headers,
            params: {
                'api-version': '3.0',
                'from': 'es',
                'to': ['fr', 'it', 'pt',]


            },
            data: [{
                'text': 'Bien!'
            }],


        })
            .then((response) => {
                setTraducciones(response.data)
                
                
               
            })
            .catch((error) => {
                console.log(error)
            });
    }, [setTraducciones]);

    return (

        <div>

            <div className='app'>
            {traducciones.map((item, index) => (
    <h3 key={index}>{item.translations.map(translation => translation.text)}</h3>
))}
                
            </div>
        </div>
    )
}
export default Translate;