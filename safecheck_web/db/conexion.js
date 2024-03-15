const mongoose = require("mongoose");

const conexion = async() => {
    try{
        await mongoose.connect("mongodb://localhost:27017/safecheckschool");
        console.log("Conectando correctamente a la base de Datos, safecheckschool");

    }catch(error){
        console.log(error);
        throw new Error("No fue posible conectarse a tu blog UnU")
    }
}

module.exports = {
    conexion
}