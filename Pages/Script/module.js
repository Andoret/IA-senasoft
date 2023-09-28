/* const fs = require('fs');
const img = JSON.stringify(datosDict)   
    fs.writeFile('envio.json', img, (error)=>{
        if  (error) throw error
        console.log("succes");
    })
 */

    const obtenNombreCompleto = (nombre, apellido) => {
        return `Mi nombre completo es ${nombre} ${apellido}`;
    };

    module.exports= obtenNombreCompleto