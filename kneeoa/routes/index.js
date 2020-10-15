const express = require('express');
const router = express.Router();
const multer = require('multer');
const storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, './uploads/');
    },
    filename: function(req, file, cb) {
        const now = new Date().toISOString(); const date = now.replace(/:/g, '-'); cb(null, date + file.originalname);
    }
});
const upload = multer({storage: storage});
const { ensureAuthenticated, forwardAuthenticated } = require('../config/auth');

// Welcome Page
router.get('/', forwardAuthenticated, (req, res) => res.render('welcome'));

// Dashboard
router.get('/dashboard', ensureAuthenticated, (req, res) =>
  res.render('dashboard', {
    user: req.user
  })
);

// Dashboard post request
router.post('/dashboard', ensureAuthenticated, upload.single('xray'), function(req,res) {
  console.log(req.file);
  var spawn = require('child_process').spawn;
  var process = spawn('python', ['./Preprocessing/Main.py',req.file.filename]);
  process.stdout.on('data', (data) => {
    console.log(data.toString());
  });
  let fl = req.file.filename;
  let prfile = fl.slice(0,-4)+'p.jpg';
  res.render('preprocess',{patientname: req.body.patientname, imgname: req.file.filename, pimgname: prfile});
});

// Get Report
router.post('/getreport', ensureAuthenticated, function(req,res) {
  let grade = 1;
  res.send("<h1>grade = "+grade+"</h1>");
});

module.exports = router;
