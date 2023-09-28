document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('envio');
    
     const resultadoSpan = document.getElementById('resultado');
    

    formulario.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe de forma convencional

        // Obtener los valores de los campos de entrada
        const urlImg = document.getElementById("imageurl").value;
        console.log(urlImg)
        // Enviar los valores al servidor Flask
        fetch('/translate', {
            method: 'POST',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "url": urlImg })
            
        })
        .then(response => response.json())
        .then(data => {
            // Mostrar el resultado devuelto por el servidor en el HTML
            console.log(data)
        })
        .catch(error => {
            console.error('Error al enviar los datos al servidor', error);
        });
    }); 

   
});


function mostrarImagen(){
    event.preventDefault();
    const url = document.getElementById("imageurl").value;
    console.log(url)
    const img= document.getElementById("img2");
    img.src=url;
}






