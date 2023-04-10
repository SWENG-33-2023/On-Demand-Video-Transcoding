const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();
const port = 3000;
const fs = require('fs');


const { spawn } = require('child_process');

const directoryPath = path.resolve(__dirname, '..', '..', 'back-end', 'assets');

fs.readdir(directoryPath, (err, files) => {
  let videoButtonsHTML = '';
  if (err) {
    console.log('Error getting directory information:', err);
  } else {
    let fileList= [];
    console.log('List of files in directory:');
    files.forEach(file => {
      if(file !=".gitkeep"){
        
        fileList.push(file);
        videoButtonsHTML += `<button onclick="transcode('${file}')">${file}</button>`;

        const filePath = path.join(directoryPath, file);

        const ffprobeProcess = spawn('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', filePath]);

        ffprobeProcess.stdout.on('data', (data) => {
          const [width, height] = data.toString().trim().split(',');
          console.log(`${file}: ${width}x${height}`);
        });

        ffprobeProcess.stderr.on('data', (data) => {
          console.error(`Error processing file ${file}: ${data}`);
        });
      }
    });

    console.log(fileList);

    app.get('/files', (req, res) => {
      res.json({ files: fileList });
    });
  }
});


const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadPath = path.join(__dirname, 'back-end/assets');
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
