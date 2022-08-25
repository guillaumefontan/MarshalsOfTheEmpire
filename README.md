# Which Marshal of the Empire are you?
#### Video Demo:  https://www.youtube.com/watch?v=8iDL_NEEbyg
#### Description:
Napoleon's marshals are widely recognized as some of the very best generals in history. While all were extremely competent in their own right, they each had
very different personalities and backgrounds which were reflected in their battle tactics.
Much like Napoleon's marshals, I believe each and every one of us is extremely competent. What makes us unique are our backgrounds and personal experiences.
This software, through very intricate psychological and statistical analisys, aims to draw parallels between the user and one of Napoleon's marshalls.
After all, who is to say that 215 years ago we wouldn't have been the ones flanking our enemies?

**App description**

This application is a web application built in Python.
It first gathers the user's data through a series of forms and saves these data points in session.
Then, it compares these data points against the data of each of Napoleon's marshals (as per specs below).
The Marshal with the most matches is then displayed in the result page, alongside a photo and a short description.

I made the architectural choice to have a single, data driven template for the forms. This allows for more flexibility
when updating the questions. Indeed, having a template entirely driven by the controller means only one file need be updated
in order to modify the user journey. This is very powerful when we can expect many changes to be made.

Most of the time was actually spent researching Napoleon's marshals in order to quantify their life and skills.

**Spec definitions**

*Age*
Age at which the marshals were made marshal, and current age of the user
* 1 : 0-34
* 2 : 35-39
* 3 : 40-44
* 4 : 45-49
* 5 : 50+

*Socio-economic background*
Age at which the marshals were made marshal, and current age of the user
* 1 : Lower class
* 2 : Middle class
* 3 : Upper class
* 4 : Powerful

*Geographic background*
Age at which the marshals were made marshal, and current age of the user
* 1 : Rural plaines
* 2 : Rural mountainous
* 3 : Coastal
* 4 : Urban mid sized city
* 5 : Urban large city

*Adoption speed*
Promotional class of the marshalls, and speed at which a user adopts a new product
* 1 : First promotion (1804)/early adopter
* 2 : Second & third promotions (1807 & 1809)/majority
* 3 : Fourth - seventh promotions (1811-1815)/laggard

*Leadership style*
From authoritarian to empathetic
* 1 : Authoritarian, discipline
* 2 : Bravery, charisma, instinct
* 3 : Preparation, administration

*Death*
How did they die?
* 1 : In battle
* 2 : Peacefully, of old age
* 3 : Miserable, illness
