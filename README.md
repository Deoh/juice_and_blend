# Your Project's Name

This is my juice and smoothie recipe webiste. 
 
## UX
 
### User stories
As an athlete who needs to keep in shape, i wanted to be able to go online and find healther alterneratives and more natural alternatives 
to the typical sports drinks.

As a pearant trying the get my childen to drink and eat healthy, I wanted a website where I could find excitng delicious 
juice and smoothie recipes that i can make with my children.

As a person that regulaly drinks smoothies i want be able to share my favorite recipes, find new recipes try new ingredients.

[Wireframe](https://github.com/Deoh/juice_and_blend/blob/master/wireframe/juice-and-blend.pdf)

## Features

Features include:
- The homepage which displays a list of juice and smoothie recipes.
- Add drink page that allow the user to input and share thier recipe.
- Add ingredients page allowing the user to add less commenly used ingredients
- A delete and edit function for each recipe.
- A side navigation bar for mobile divices.

### Features Left to Implement
- nutritional information to display for each ingredient in the ingredientas list.
- Add a Global heat map to show the suicide rates between countries.
- the ability for the user to add an image to their drinks recipe.

## Technologies Used

- [HTML](https://html.com)

- CSS

- [Javascript](https://www.javascript.com)

- [JQuery](https://jquery.com)

- [Python](https://www.python.org/)

- [Flask](https://palletsprojects.com/p/flask/)
    - web application framework

- [Materialize](https://materializecss.com/)
    - The project uses **Materialize**, a front-end framework to to help build a responsive, mobile-first website.

- [MongoDB](https://www.mongodb.com/)
    -  The project uses **MongoDB** for the Back-end database.

## Testing

The website was tested using `Google Chrome Dev tools` for various devices sizes to check scalability across different devicees and screen size.

Through manual testing both desktop and mobile:

- The navbar should scales correctly across different browsers and screen sizes sticking to the top as the user scroll the page and the navbar brand link works correctly.
- The Sidenav should work on mobile divices
- The website title should scales correctly across different screen sizes.



The website navigation bar should have a chickable logo which brings you back to the homepage (drinks list) and links to different pages of the website, clicking these links should take you to the intended page. 
on mobile devices the navbar should appear from the side with the same clickable links.

The website should scale well from mobile to desktops.

The website should work similarly across different browsers and screen sizes.

- homepage (same applies to ingredient List page):
    - Go to the navbar. Each link (including the logo which takes you the the homepage) should take you to thier intended page.
    - Click on any of the drinks on the list and verify the instructions appear
    - Try to delete a drinks recipe by clicking on the del button within the chosen drink and verify that it does so.
    - Try to click on the edit button within the chosen drink to verify it takes you to the edit drink page.

- Add Drink Page (applies to Add ingredient):
    - fill out the all the input fields and verify that clicking on the 'add drink' (or 'add ingredient) button submits the form and shows on the homepage

- Edit Drink Page (applies to Edit ingredient):
    - verify the input field have been pre-selected with the correct data.
    - change the pre-selected inputs and verify that clicking on the 'edit drink' (or 'edit ingredient) button changes the original data and it shows on the homepage




### Certain issues discovered when navigating the website were:
- The navbar dropdown links doesn't properly indicate (highlight) what section of the website you are currently in.
- The scrollbar appears on the mobile version of the site.
- Using the carousel feature from bootstrap for embedded music videos from youtube confilicted with each other when trying to use the youtube nav icon (full screen, play/pause etc). the carousel next and prev button needed to be resized.

### HTML, CSS & JavaScript code
- HTML and CSS validation via [w3.org](https://www.w3.org/).


## Deployment

This project is deployed though Heroku.
- A new app was created in Heroku.
- On the CLI type in "heroku login" to get acces to the heroku account.
- link the local Git repository to Heroku. On the CLI type in "heroku git:remote -a juice-and-blend"
- create a requirements.txt file, which contains a list of our dependencies. On the CLI type in "pip3 freeze --local > requirements.txt"
- create a Procfile. On the CLI type in "echo web: python app.py"
- Git add/ commit the code.
- Push the code to Heroku. On the CLI type in "git push heroku master"
- run the Heroku app by typing in the CLI "heroku ps:scale web=1"
- In the heroku page specify the IP and PORT. go into settings and under config variables add the IP and PORT key and set thier values.

## Credits

### Acknowledgements

- I received inspiration for this project from [Jason Vale "Juice Master"](https://www.amazon.co.uk/Juice-Master-Keeping-Simple-Delicious/dp/0007225172/ref=sr_1_1?keywords=jason+vale+juice+master&qid=1580308517&sr=8-1) book.