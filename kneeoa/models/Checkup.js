const mongoose = require('mongoose');

const CheckupSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  },
  patientname: {
    type: String
  },
  age: {
    type: Number
  },
  grade: {
    type: Number
  },
  gender: {
    type: String
  },
  filename: {
    type: String
  },
  examination: {
    type: String
  },
  view: {
    type: String
  }
});

const Checkup = mongoose.model('Checkup', CheckupSchema);

module.exports = Checkup;
