const express = require('express');
const router = express.Router();
const fs = require('fs');
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

// Specific variables
let patientname = '';
let dob = '';
let filename = '';

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
  patientname = req.body.patientname;
  filename = fl.slice(0,-4);
  dob = req.body.DOB;
  res.render('preprocess', {patientname: patientname, imgname: filename+".jpg", pimgname: prfile, dob: dob});
});

// Get Report
router.post('/getreport', ensureAuthenticated, function(req,res) {
  let grade = 1; // Gets grade from dl model
  fs.copyFile("reports/sample.html", "reports/"+filename+".html", (err) => {
    if (err) throw err;
    else {
      console.log('copy successful');
      fs.readFile("reports/"+filename+".html", 'utf8', function (err,data) {
        if (err) {
          return console.log(err);
        }
        var r1 = data.replace(/sample_name/g, ''+patientname).replace(/sample_dob/g, ''+dob).replace(/sample_grade/g, ''+grade);

        fs.writeFile("reports/"+filename+".html", r1, 'utf8', function (err) {
           if (err) return console.log(err);
        });
      });
    }
  });
  res.render('getreport',{user: req.user});
});

module.exports = router;
