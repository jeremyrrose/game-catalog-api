# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Unit 4 Project - Build a full CRUD website application using Django Restframework + JWT

## Overview

Recreation is a gaming Ecommerce site that takes inspiration from pre-existing sites such as the Origin. Recreation Api uses the Django rest framework. Originally I was going to use an external api to hold the game information and my api would hold relationships, but decidded to seed a couple of games instead

Authentication models- Users, Login
Gaming Models - Platform, Developer, Game(connected to Platform, User, and Developer), and Review(connected to Game and User)


#### MVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Make Models,Serializers and Views | H | 5hr | 2hr | -hr|
| Test and Debug Api | H | 5hr | 6hr 30min | -hr|
| Create Urls | H | 2hr | 3hr 30min | -hr|
| Make test GS api calls | H | 2hr | 30min | -hr|
| Seeding Database | H | 3hr | 3hr | -hr|
| Alter models to accomodate frontend| H | 1hr | 5hr | -hr|
| Total | H | 13hrs| 20hrs | -hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
|Add more seed data with quality info| L | 5hr | -hr | -hr|
|Add superuser priveleges,and endpoints| L | 4hr | 7hr | -hr|
|Priority property on reviews | M | 1hr | -hr | -hr|
| Total | H | 10hrs| -hrs | -hrs |
    

The repository for the frontend of your application should include:

- A working frontend application built with HTML, CSS, Bootstrap, JQuery or vue ect.
- CRUD functionality
- Frequent commits dating back to the very beginning of the project.
- Mobile first, responsive web application (Mobile, Tablet and Desktop).

#### Deployment

- Your API Backend must be deployed to Heroku and your front-end must be deployed to
  Netlify. Applications that are not deployed will be considered incomplete.
 
#### Additional libraries

--