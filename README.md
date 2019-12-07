# StanBase

When I was 14 years old I saw the movie Heathers for the first time. It was an accident really; I was channel-hopping and randomly settled on the opening credits of the film. From the second I saw Winona Ryder I was hooked and when I was first introduced to Christian Slater I couldn't take my eyes off the screen.

I was sad to see the film end and to cheer me up a friend from school gave me a printed IMDB list of all the movies Christian Slater starred in. I would spend the next few years hunting down his back catalog (pre-internet days!) and ticking each film watched off the list.

This is the inspiration for StanBase - it's a virtual list to tick off as you indulge in your favourite star's work. For this project, the focus is on Winona Ryder's film history. 

Why is the app called 'StanBase'? It's a database that super fans can add to. According to Urban Dictionary, a 'stan' is a crazed or obsessed fan and the term derives from the song Stan from Eminem. I feel the term encompasses those strong feelings of fandom and worship only the innocent fans of famous people know: the strong interest and admiration of someone's work and achievements.

## UX

The purpose of StanBase is to document the user's / users' quest to watch and document every film their star has made. 

This app is for film buffs, but could easily be used by music fans and other types of fans the world over as the ability add content is shared. StanBase is a place to build your own passion project and this project demonstrates my passion for the work on Winona Ryder.

Users of StanBase will have the ability to read, add, edit, update and delete films and information related to Winona Ryder's career.

#### User stories

1. As a big film fan, I want to use this app as a place where I can document the movies I've seen.

2. As a Winona Ryder fan, I want to focus on watching and documenting all her roles.

3. As someone who re-watches films, I want the ability to edit previous entries.
 
4. Because Winona Ryder is still making movies, I want the ability to add new entries.
 
5. As a fan, I'd like others to read about find information about Winona Ryder's roles.

6. 

### Wireframes

## Features

### Existing Features

#### Cover page

* Primarily a design feature to greet users to the website.

#### Navbar

* This feature was added with Materialize and styled with this tools built-in color options. The power of this feature is displayed with url_for functions in Flask. The purpose of the navbar is to direct users to the correct location of the pages on the website.

#### Form

* To add films to the database, users input their own content using a form. This form is from Materialize and has seven fields to input text and one select dropdown - this last feature was added to give users more control over how their content displays. It also engineers another way users can manipulate the web application.

#### Material icons

* Visual symbols are used throughout the website for design, style and space purposes. They function as visual representation for the input the user will add information too, while also giving added a modern and sleek field to the site. 

#### Sidenav

* The sidenav is used primarily for mobile view as a way to neatly display quicklinks to the functional elements on the site. The sidenav uses Materialize code and is rendered functional by jQuery. The sidenav can be activated by tapping the hamburger menu icon. 

#### Buttons

* There are two types of buttons on the site style-wise: block buttons with a background color and clickable icons buttons (on the genre page). The buttons' purpose is to direct visitors to the correct location and to insert, update and remove database content. Buttons are from Materialize, using their color themes too. 

#### Slider 

* The slider is Materialize code with jQuery to initialize the slider aspect and is primarily used to showcase images. Its design takes up 50% of the page, which means users can see the visual element and some content beneath it. It comes with a visual slider indicator, which has been modified to blend into the background.

#### Collapsible 

* The collapsible pop-out is used in order to display the user input. The pop-out aspect adds a jump out effect for the user and adds an element of animation to the page. It works with jQuery added in script tags in the base.html page.

#### Genre collapsible

* The genre page uses the collapsible pop-out feature but is repurposed without the collapsible body so it only displays the header, which pops out when selected - this adds a dynamic visual effect and is the main purpose of the pop-out feature - that, and continuity. Users can add new genres, edit existing genres or remove genres completely.

#### Card panels

* This feature was used throughout the website to add consistent structure to content on the site. It is mostly used on the about html page to layout the information of the three sections. The panels were then styled using the built-in design features of Materialize (which are added within the html tags) and using my own CSS specifications.

### Features Left to Implement

Login feaature

## Technologies Used

#### HTML5

* I used HTML5 to structure my web app. I started with HTML tags and then used header, body and footer sections. Using this technology helped me to keep my layout clear and organised.

#### CSS3

* I modified the look of my site using my own CSS3 code (in conjunction with Materialize - see below). Using CSS I was able to change the colors on my side and the font style. I was also able to increase padding on card-panels too.

#### Javascript

* I used Javascript to queue my jQuery. I also used an JS fix for the datepicker, which was provided by Code Institute. I added JS CDNs to enable them on my site.

#### Materialize

* I used Materialize for the main structural features, including the navbar and the add film form. I was also able to modify the look of my site using the code provided by this tool.

#### jQuery

* I used jQuery to add functionality to my HTML features. In particular, I was able to add a pop out dropdown collapsible items, select genre dropdown, menu icon and slider form images.

#### Jinja

* The template engine Jinja enabled me to extend my base html page to other pages on my website. This helped me avoid repetition throughout my code and refer to pages through links.

#### VSCode

* This tool was used to create, maintain and add to my code, instead of using an IDE that was internet dependent. I was able to add my files and keep them stored together. It also helped me with committing my code concisely. 

#### Material.io

Icons

#### GitHub

* My repository of code is stored on GitHub. It enabled me to easily commit my code and have a place to store my work. On GitHub I can refer to back to stages of my code and progress. 

#### Google Fonts

Using Google Fonts I was able to import specific font styling to my website. With this tool I was able to add Dancing Script: Cursive and Quicksand to my website. 

#### Heroku

* I used Heroku to deploy my project as it supports sites with Python and Flask, unlike GitHub Pages. Using this platform, I was also able to add my environment variables and configured my site. 

#### Balsamiq

* I used Balsamiq to outline the initial look of my web application. I mainly focused on the look of the form page and the summary page - it would have been best to consider each page and styling beforehand. 

## Testing

General

Big feature issues

Try it out features

Issues

| Number        | Issue           | Resolution  |
| ------------- | ------------- | -----|
| 1  | Datepicker | - |
| 2  | Brackets in form      |   Added specific input field for year information |
| 3  | CSS not rendering     |    Cleared cache and used Incognito Window for testing |
| 4  | Plot and recommendations not displaying | Input was textarea, moved {{}} to between tags not inside value attribute|
| 5  | Sidenav not displaying on mobile | Added meta viewport tag in head section |
| 6  | Genre page, button on next line | Changed button style to icon button to create space|
|    |  |  |


## Deployment

I deployed this application using the Master Branch on hosting platform Heroku, which I did at the beginning of the project. Deploying at the beginning of the project instead of the end meant that I could preview the python programming language and flask during the project. Deploying to GitHub Pages was not an option this time because of the Python / Flask use within the project.

I deployed my project on Heroku by creating space for the app on my Heroku account, then adding a requirements.txt file and Procfile file to my project so Heroku could recognise the Python language. During setup, I logged in to Heroku using the Heroku command line interface. Though my source code is being added to a GitHub repository, I was still able to push content and deploy my project using git push heroku master.

## Credits

### Content

### Media

### Acknowledgements

