import  fs from 'fs;'
const formulario = document.querySelector("#envio");

const procesamiento= (event)=>{
    event.preventDefault();
const datos= new FormData(event.target)

const datosDict= Object.fromEntries(datos.entries());

console.log(JSON.stringify(datosDict))
    fs.writeFile("data.json",datosDict,(error)=>{
        if (error){
            console.log(error);
            throw error;
        }
        console.log("data.json guardado")
    })
}

formulario.addEventListener('submit',procesamiento)