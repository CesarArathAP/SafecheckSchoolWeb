const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose"); // Agregado para importar Mongoose
const { conexion } = require("./db/conexion");

const app = express();
const port = 3900;

// Habilitar CORS
app.use(cors());

// Conectar a la base de datos
conexion()
    .then(() => {
        // Ruta para obtener todos los documentos de la colección docentes
        app.get("/", async (req, res) => {
            try {
                const docentes = await mongoose.connection.collection("directores").find().toArray();
                res.json(docentes);
            } catch (error) {
                console.error("Error al obtener los docentes:", error);
                res.status(500).json({ error: "Error al obtener los docentes" });
            }
        });

        // Iniciar el servidor
        app.listen(port, () => {
            console.log(`Servidor corriendo en el puerto ${port}`);
        });
    })
    .catch(error => {
        console.error("Error al conectar a la base de datos:", error);
    });
