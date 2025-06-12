const express = require("express");
const cors = require('cors');
const path = require("path");
const app = express();
app.use(express.static("public"));
app.use(cors());
app.listen(3000, () => console.log("App: http://localhost:3000"));
