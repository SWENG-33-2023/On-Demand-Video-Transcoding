const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();
const port = 3000;
const fs = require('fs');

const chokidar = require('chokidar');

let fileList = [];

const directoryPath = path.resolve(__dirname, 'assets');

// Watch for changes in the directory and update the file list and endpoint
chokidar.watch(directoryPath).on('all', (event, filePath) => {
  if (event === 'add' || event === 'unlink') {
    updateFileList();
  }
});

// Update the file list array and endpoint
function updateFileList() {
  fs.readdir(directoryPath, (err, files) => {
    if (err) {
      console.log('Error getting directory information:', err);
    } else {
      fileList = files.filter(file => file !== '.gitkeep');
      console.log(fileList);
      app.get('/files', (req, res) => {
        res.json({ files: fileList });
      });
    }
  });
}

// Initial update of the file list and endpoint
updateFileList();

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadPath = path.join(__dirname, 'assets/');
    console.log('Upload Path:', uploadPath);
    cb(null, uploadPath);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});

const upload = multer({ storage: storage });

app.use(express.static(__dirname));

app.post('/upload', upload.single('file'), (req, res) => {
  console.log('File uploaded:', req.file);
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
