const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  },
  checkups:[{patientname: String, age: Number, grade: Number, gender: String, filename: String, examination: String, view: String}]
});

const User = mongoose.model('User', UserSchema);

module.exports = User;
