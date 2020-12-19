
## Minor Project: Osteoarthritis Checkup System 

<div style="margin: 0 auto; width: 100px;" ><b> Group ID - 3</b></div>

<p style="text-align: center;">Mentor: Dr. Trilok Chand<p>

<table style="margin-left: auto;margin-right: auto;">
  <tr><th>Group Members</th><th>StudentID</th></tr>
  <tr><td>Saarisht Thaman</td><td>18103063</td></tr>
  <tr><td>Gaurav Sharma</td><td>18103050</td></tr>
  <tr><td>Aditya Kumar</td><td>18103010</td></tr>
  <tr><td>Aditya</td><td>18103075</td></tr>
</table>
<br>

### Overview
The whole system can be summed up as an <b>Osteoarthritis Grade Prediction and Concise Report Generation System</b>. The main motivation behind the project was that the traditional method to observe XRay and report generation by a Radiologist takes too much time mainly due to high population, dependence on experience of Radiologist, artefacts on X-ray images, management of physical reports and Lack of proper infrastructure and services in rural regions.
<br><br>
A full-fledged system with <b>1/5th the size of industry standard model</b> (published by University of California San Francisco in early 2019(Fine-tuned VGG19 Model). [link to Publication](https://www.sciencedirect.com/science/article/abs/pii/S0895611118304956?via%3Dihub)) and an<b> increment in accuracy from 69.7% to 75.42% </b>([more details](https://github.com/Gauravsharma-20/Minor-Project/blob/master/SystemDetails/ModelDetails.png)) and a proprietary Pre-processing method which is able to resolve most of defects from images ([sample results](https://github.com/Gauravsharma-20/Minor-Project/blob/master/SystemDetails/SamplePreprocessedResults.jpg)). Alongside that, a robust web application with a proper database management system.System is designed in a way to be more scalable in future.


Project Report Document
https://docs.google.com/document/d/1j_cdjuVCV-zeR9E3uTQzxpLFHNmp_dfE5mQoNqFuQmc

### Instructions for getting the webapp running on your local computer

 1. Make sure you're connected to the internet through the entirety of the process
 2. Clone the repository
 3. Download Node js and install it
 4. Download and set-up MongoDB local server or Make an account on MongoDBatlas, create a new cluster then add your credentials in keys.js present in the config folder and make sure to change mongodb access in the app.js file
 5. Open up any terminal, navigate to the kneeoa directory, then write out the following two commands in succession:
 npm i 
 node app.js
 6. Now that the server is running, it will display a message in the terminal. Open up any web browser and type in http://localhost:3000/ into the address bar to access it
 7. From here on out you can create an account, login, generate reports etc.
 8. To close the server, simply hit ctrl+c in the terminal to end the process
   
### Future of the project
The project in its current state is not much usable in a real scenario where a doctor can blindly rely on the website to give absolutely correct predictions and comments. So, some improvement is required which is not difficult to do given that the current state of the project is good.
The model in question needs more training with actual data that a doctor collects himself from scanning real world patients. Also, the build of the website deployed on heroku cannot run the model as the RAM requirement is not met (500MB RAM on heroku servers is not enough to run the model). This issue can be fixed by purchasing heroku's services or deploying the website on AWS servers with a subscription.
