# BoWood Audio

BoWood Audio is a home recording studio that provides a wide range of audio and program editing services. This websites primary intention is to display to the visitor what the setup of the studio is like and what services are available. 

## UX

### Scope

The time allocated to build this project was shorter then previous projects, luckily for me the site owner is very flexible with the scope. The site will be first made to an MVP, and if there is additional time, content/features can be added.

### Visitor Goals

1. As a visitor to this site, I want to see what services are available so I can decide if I want to do business here.
2. As a visitor to this site, I want to see pictures of the studio, so I know who what to expect.
3. As a visitor to this site, I want to be able to contact the studio, so that I can make queries or request a booking.
4. As a visitor to this site, I want to be able to view the range of products that are on sale, so that I can make an online purchase.
5. As a visitor to this site, I want to be able to view individual product details, so that I check product details before deciding to purchase.

### Owner Goals

1. As the owner of this site, I want a simple landing page, so that visitors can learn about my studio easily and quickly.
2. As the owner of this site, I want to be able to have an online store so i can sell merchandise and gift vouchers.
3. As the owner of this site, I want a receipt / proof of purchase emailed to myself and available to myself.
4. As the owner of this site, I want to showcase some of my work, so the user gets a idea of my skills and talent.


### Structure

This full stack site is put together with HTML, using the bootstrap framework along with some CSS.

The Database is integrated using Python and Django fronted onto a PostgreSQL backend.

### Skeleton

The page content is dynamic and composed of Jinja templates which are put together using Python Django.

#### Website page line up / Flask templates

- Home / Index

- Login / Logout

- Register new user

- Profile / My details / Edit my Contact details

- All products

- product details

- shopping cart

### Database Schema

#### Relational Database tables schema

##### Products table

```bash
_ID: (auto-generated) ObjectId PRIMARY KEY (Not changeable)
name : STRING

```

#### Wireframes


### Surface

#### Colours

Dark mode

#BB3C2B - red

#F5CA9F  - biege

#CCB19E - gold

#### Icons

Font Awescome is used for icons

#### Images

images are sourced from unsplash and site owner.

#### Fonts

The font used is Oswald from Google fonts.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

### Frontend

#### Languages

- HTML
- CSS
- Python
- JavaScript/Jquery

#### Libraries and Frameworks

- [Bootstrap](https://getbootstrap.com/)
- Django
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- Fonts : [Google Fonts](https://fonts.google.com/)
- Icons : FA

#### Tools

- JSfiddle : I used this online sandbox to build and play code before i adding to the project.
- [Python Tutor](http://pythontutor.com/): I used this very handy online sandbox for experimenting with Python code before applying to this project.
- Wireframe: [Balsamiq](https://balsamiq.com/)
- DB Schema diagram : Drawsql.app
- IDE: Visual Studio Code (VS Code).
- Version control: Git
- Browser Developer tools : [Google Chrome](https://www.google.com/chrome) for console.logging everything.
- Kanban planner : [Github projects](https://github.com/kenwals/BoWood-Audio/projects/1).
- Markdown editor: [Typora](https://typora.io/) was used when appropriate, VS code editor was used for most updates.
- Markdown Preview Github Styling : this brilliant vscode extension helps me read my markdown in Github format.
- File renaming utility: PowerRename from [PowerToys on Windows 10](https://www.windowscentral.com/how-bulk-rename-your-files-windows-10-powertoys)
- Pomodoro timer : [Tomato Clock](https://chrome.google.com/webstore/detail/tomato-clock/enemipdanmallpjakiehedcgjmibjihj)
- Favicon creator : [favicon.io](https://favicon.io/favicon-generator/) **
- Autoprefixer CSS : [Autoprefixer](https://autoprefixer.github.io/)
- Auto formatter for HTML, CSS and JS:  [webformatter](https://webformatter.com/html)
- px to rem convertor : [nekoCalc](https://nekocalc.com/px-to-rem-converter)
- JavaScript linter : [jshint](https://jshint.com/)
- Python linter :  [Pep8 online](http://pep8online.com/)
- markdown linter : markdownlint extension on VS Code.
- Colour names : [Name that color](https://chir.ag/projects/name-that-color/#6195ED)
- Colour swatches : [Coolors](https://coolors.co/)
- [markdown table of contents creator](https://ecotrust-canada.github.io/markdown-toc/)
- [site preview tool](http://ami.responsivedesign.is/)
- [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X