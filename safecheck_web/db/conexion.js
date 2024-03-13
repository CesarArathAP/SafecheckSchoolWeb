const mongoose = require("mongoose");

const conexion = async () => {
    try {
        await mongoose.connect("mongodb+srv://CesarArath:LT6Vg8r3skBs563e@cesar.dojvcvn.mongodb.net/safecheck?retryWrites=true&w=majority&appName=Cesar&tls=true&readPreference=primaryPreferred"        );
        console.log("Conexión establecida correctamente con MongoDB Atlas");
    } catch (error) {
        console.error("Error al conectar a MongoDB Atlas:", error);
        throw new Error("No fue posible conectarse a la base de datos");
    }
}

module.exports = {
    conexion
}