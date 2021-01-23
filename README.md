
## Minor Project: Osteoarthritis Check-up System <a href="https://oa-checkup-system.herokuapp.com/" target="_blank">[Live]</a>

<div style="margin: 0 auto; width: 100px;" ><b> Group ID - 3</b></div>

<p style="text-align: center;">Mentor: Dr. Trilok Chand</p>
<p style="text-align: center;">Supervisor: Mr. Deepak Saini</p>


<table style="margin-left: auto;margin-right: auto;">
  <tr><th>Group Members</th><th>StudentID</th></tr>
  <tr><td>Gaurav Sharma</td><td>18103050</td></tr>
  <tr><td>Saarisht Thaman</td><td>18103063</td></tr>
  <tr><td>Aditya</td><td>18103075</td></tr>
  <tr><td>Aditya Kumar</td><td>18103010</td></tr>
</table>
<br>

### Overview
The whole system can be summed up as an <b>Osteoarthritis Grade Prediction and Concise Report Generation System</b>. The main motivation behind the project was that the traditional method to observe X-Ray and report generation by a Radiologist takes too much time mainly due to high population, dependence on experience of Radiologist, artefacts on X-ray images, difficulty in management of physical reports and Lack of proper infrastructure and services in rural regions.
<br><br>
A full-fledged system with <b>1/5th the size of industry standard model</b> (published by University of California San Francisco in early 2019(Fine-tuned VGG19 Model). [link to Publication](https://www.sciencedirect.com/science/article/abs/pii/S0895611118304956?via%3Dihub)) and an<b> increment in accuracy from 69.7% to 75.42% </b>([more details](https://github.com/Gauravsharma-20/Minor-Project/blob/master/SystemDetails/ModelDetails.png)) and a proprietary Pre-processing method which is able to resolve most of defects from images ([sample results](https://github.com/Gauravsharma-20/Minor-Project/blob/master/SystemDetails/SamplePreprocessedResults.jpg)). Alongside that, a robust web application with a proper database management system.System is very modular and is designed in a way to be more scalable in future.

### DEMO:
&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/Gauravsharma-20/Minor-Project/blob/master/SystemDetails/Demo.gif" width="75%" height="60%"><br>


### How To Run:

 1. Make sure you're connected to the internet through the entirety of the process
 2. Clone the repository
 3. Download Node js and install it
 4. Download and set-up MongoDB local server or Make an account on MongoDBatlas, create a new cluster then add your credentials in keys.js present in the config folder and make sure to change mongodb access in the app.js file
 5. Open up any terminal, navigate to the kneeoa directory, then write out the following two commands in succession:
<code>npm i</code> and after that
<code>node app.js</code>
 6. Now that the server is running, it will display a message in the terminal. Open up any web browser and type in http://localhost:3000/ into the address bar to access it.
 7. From here on out you can create an account, login, generate and manage reports etc.
 8. To close the server, simply hit ctrl+c in the terminal to end the process
 
 ### References:

1. https://arxiv.org/pdf/1412.6806 - For models to experiments with Dataset.
2. https://ard.bmj.com/content/annrheumdis/16/4/494.full.pdf - Different Grades description.
3. https://mongoosejs.com/docs/guide.html - Documentation for dealing with database.
4. https://developers.google.com/web/tools/puppeteer - For pdf generation.
5. https://github.com/albarqouni/Deep-Learning-for-Medical-Applications - For Deep Learning Research Papers.
6. https://github.com/asalmada/x-ray-images-enhancement - System’s preprocessing method uses this as the basis.
7. https://data.mendeley.com/datasets/56rmx5bjcr/1 - For Dataset and Industry Standard Model Metrics.
8. https://www.sciencedirect.com/science/article/abs/pii/S0895611118304956?via%3Dihub - Published article for Industry Standard Model
