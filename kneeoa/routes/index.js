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

// Specific variables (tentative storage)
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
  // Spawns preprocessing scripts and executes it
  // var spawn = require('child_process').spawn;
  // var process = spawn('python', ['./Preprocessing/Main.py',req.file.filename]);
  // process.stdout.on('data', (data) => {
  //   console.log(data.toString());
  // });

  let errors = [];

  patientname = req.body.patientname;
  age = req.body.age;
  gender = req.body.gender;
  if(!patientname || !age) {
    errors.push({ msg: 'Please enter all the fields' });
  }
  if(!req.file) {
    errors.push({ msg: 'Please upload the x-ray file' });
  }
  if(errors.length > 0) {
    res.render('dashboard',{errors, user: req.user});
  }
  else {
    let fl = req.file.filename;
    filename = fl.slice(0,-4);
    res.render('preprocess', {patientname: patientname, imgname: fl, age: age});
  }
  // process.on('close',(code) => {
  //   res.render('preprocess', {patientname: patientname, imgname: filename+".jpg", pimgname: prfile, age: age});
  // });
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

        // Replaces data in sample report with actual data
        var r1 = data.replace(/sample_name/g, ''+patientname).replace(/sample_age/g, ''+age)
        .replace(/sample_grade/g, ''+grade).replace(/sample_gender/g, ''+gender)
        .replace(/sample_path/g, ''+"../uploads/"+filename+".jpg");

        fs.writeFile("reports/"+filename+".html", r1, 'utf8', function (err) {
           if (err) return console.log(err);
           else {
             // Generates pdf after html file is written
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
                    res.render('getreport',{user: req.user, flnm: filename, patientname: patientname});
                  }
                })()
           }
        });
      });
    }
  });
});

// Finish button to save current checkup
router.get('/finish', ensureAuthenticated, function(req, res) {
  User.findOne({ email: req.user.email }, function(err,data) {
    if(err) throw err;
    else {
      console.log(data);
      var topush = {patientname: patientname, age: age, grade: grade, gender: gender, filename: filename};
      data.checkups.push(topush);
      data.save();
      req.flash('success_msg', 'Checkup saved');
      res.redirect('dashboard');
    }
  });
});

// Spits out all checkups to date in a tabular form
router.get('/viewreports', ensureAuthenticated, function(req, res) {
  User.findOne({ email: req.user.email }, function(err,data) {
    if(err) throw err;
    else {
      if(!data) res.render('viewreports', {user: req.user, data: "nothing"});
      else res.render('viewreports', {user: req.user, data: data.checkups});
    }
  });
});

// Processes search query
router.post('/viewreports', ensureAuthenticated, function(req, res) {
  console.log(req.body);
  let query = req.body.searchquery;
  let searchtype = req.body.searchtype;

  let errors = [];

  if(query == '') {
    errors.push({ msg: 'Please enter a query' });
    User.findOne({ email: req.user.email }, function(err,data) {
      if(err) throw err;
      else {
        if(!data) res.render('viewreports', {errors, user: req.user, data: "nothing"});
        else res.render('viewreports', {errors, user: req.user, data: data.checkups});
      }
    });
  }

  // If statements for different search types
  else {
    if(searchtype == 'pn') {
      User.findOne({ email: req.user.email }, {checkups: {$elemMatch: {patientname: {'$regex': query, '$options' : 'i'}}}}, function(err,data) {
        if(err) throw err;
        else {
          if(!data || data.checkups.length == 0) res.render('viewreports', {user: req.user, data: "nothing"});
          else res.render('viewreports', {user: req.user, data: data.checkups});
        }
      });
    }
    if(searchtype == 'gn') {
      User.findOne({ email: req.user.email }, {checkups: {$elemMatch: {gender: {'$regex': query, '$options' : 'i'}}}}, function(err,data) {
        if(err) throw err;
        else {
          if(!data || data.checkups.length == 0) res.render('viewreports', {user: req.user, data: "nothing"});
          else res.render('viewreports', {user: req.user, data: data.checkups});
        }
      });
    }
    if(searchtype == 'gr') {
      User.findOne({ email: req.user.email }, {checkups: {$elemMatch: {grade: query}}}, function(err,data) {
        if(err) throw err;
        else {
          if(!data || data.checkups.length == 0) res.render('viewreports', {user: req.user, data: "nothing"});
          else res.render('viewreports', {user: req.user, data: data.checkups});
        }
      });
    }
    if(searchtype == 'ag') {
      User.findOne({ email: req.user.email }, {checkups: {$elemMatch: {age: query}}}, function(err,data) {
        if(err) throw err;
        else {
          if(!data || data.checkups.length == 0) res.render('viewreports', {user: req.user, data: "nothing"});
          else res.render('viewreports', {user: req.user, data: data.checkups});
        }
      });
    }
  }
});

module.exports = router;
