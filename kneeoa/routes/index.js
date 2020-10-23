const express = require('express');
const router = express.Router();
const fs = require('fs');
const HTMLToPDF = require('html5-to-pdf');
const multer = require('multer');
const User = require('../models/User');
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
let age = '';
let filename = '';
let gender = '';
let grade = '';

// Welcome Page
router.get('/', forwardAuthenticated, (req, res) => res.render('welcome'));

// Dashboard
router.get('/dashboard', ensureAuthenticated, (req, res) =>
  res.render('dashboard', {user: req.user})
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
  age = req.body.age;
  gender = req.body.gender;
  process.on('close',(code) => {
    res.render('preprocess', {patientname: patientname, imgname: filename+".jpg", pimgname: prfile, age: age});
  });
});

// Get Report
router.post('/getreport', ensureAuthenticated, function(req,res) {
  grade = 1; // Gets grade from dl model
  fs.copyFile("reports/sample.html", "reports/"+filename+".html", (err) => {
    if (err) throw err;
    else {
      console.log('copy successful');
      fs.readFile("reports/"+filename+".html", 'utf8', function (err,data) {
        if (err) {
          return console.log(err);
        }
        var r1 = data.replace(/sample_name/g, ''+patientname).replace(/sample_age/g, ''+age)
        .replace(/sample_grade/g, ''+grade).replace(/sample_gender/g, ''+gender)
        .replace(/sample_path/g, ''+"../uploads/"+filename+".jpg");

        fs.writeFile("reports/"+filename+".html", r1, 'utf8', function (err) {
           if (err) return console.log(err);
           else {
             const run = async () => {
                const html5ToPDF = new HTMLToPDF({
                  inputPath: "./reports/"+filename+".html",
                  outputPath: "./reports/"+filename+".pdf",
                });
                  await html5ToPDF.start();
                  await html5ToPDF.build();
                  await html5ToPDF.close();
                }

                (async () => {
                  try {
                    await run()
                    console.log("DONE")
                  } catch (error) {
                    console.error(error);
                  } finally {
                    console.log("EXITED");
                    res.render('getreport',{user: req.user, flnm: filename});
                  }
                })()
           }
        });
      });
    }
  });
});

// Finish button to save checkup
router.get('/finish', ensureAuthenticated, function(req, res) {
  User.findOne({ email: req.user.email }, function(err,data) {
    if(err) throw err;
    else {
      console.log(data);
      var topush = {patientname: patientname, age: age, grade: grade, gender: gender, filename: filename};
      data.checkups.push(topush);
      data.save();
      res.render('dashboard', {user: req.user});
    }
  });
});

router.get('/viewreports', ensureAuthenticated, function(req, res) {
  User.findOne({ email: req.user.email }, function(err,data) {
    if(err) throw err;
    else {
      res.render('viewreports', {user: req.user, data: data.checkups});
    }
  });
});

module.exports = router;
