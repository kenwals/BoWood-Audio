# BoWood Audio

[BoWood Audio](https://bowood-audio.herokuapp.com/) is a home recording studio that provides a wide range of audio and program editing services. This website's primary intention is to display to the visitor what the studio setup is like and what services are available.

![ipad preview](/wireframe/ipad-view.png)

---

## Table of contents

- [UX](#ux)
  - [Scope](#scope)
  - [Visitor Goals](#visitor-goals)
  - [Owner Goals](#owner-goals)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [Website page line up](#website-page-line-up)
  - [Database Schema](#database-schema)
    - [Relational Database tables schema](#relational-database-tables-schema)
    - [Wireframes of pages](#wireframes-of-pages)
  - [Surface](#surface)
    - [Colours](#colours)
    - [Icons](#icons)
    - [Images](#images)
    - [Fonts](#fonts)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Frontend](#frontend)
    - [Languages](#languages)
    - [Libraries, Frameworks and Packages include](#libraries-frameworks-and-packages-include)
    - [Tools](#tools)
      - [Productivity](#productivity)
      - [Toolbox](#toolbox)
- [Testing](#testing)
  - [Performance Testing](#performance-testing)
  - [Bugs encountered on the way](#bugs-encountered-on-the-way)
  - [Known issues](#known-issues)
    - [Not secure warning or Unsecure connection](#not-secure-warning-or-unsecure-connection)
    - [Linting errors](#linting-errors)
  - [Project barriers and solutions](#project-barriers-and-solutions)
    - [Time and work life balance](#time-and-work-life-balance)
  - [Version control](#version-control)
  - [Functionality Testing](#functionality-testing)
  - [Responsiveness Testing](#responsiveness-testing)
  - [CSS3 validator](#css3-validator)
  - [HTML5 validator](#html5-validator)
  - [Python validator](#python-validator)
  - [JavaScript validator](#javascript-validator)
  - [Usability Testing](#usability-testing)
  - [Compatibility Testing](#compatibility-testing)
  - [Testing User Stories](#testing-user-stories)
    - [Visitor Stories](#visitor-stories)
    - [Owner Stories](#owner-stories)
- [Deployment](#deployment)
  - [Pre-Requisites for Deployment](#pre-requisites-for-deployment)
  - [Local Deployment](#local-deployment)
  - [For VScode and Pipenv](#for-vscode-and-pipenv)
  - [Remote Deployment on Heroku](#remote-deployment-on-heroku)
  - [Contribution and Forking](#contribution-and-forking)
- [Credits](#credits)
  - [Content](#content)
  - [Resources](#resources)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

<!-- <small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small> -->

## UX

### Scope

The time allocated to build this project was shorter than previous projects, luckily for me, the site owner is very flexible with the scope. The site will be first made to an MVP, and if there is additional time, content/features can be added.

### Visitor Goals

1. As a visitor to this site, I want to see what services are available so I can decide if I want to do business here.
2. As a visitor to this site, I want to see pictures of the studio, so I know what to expect.
3. As a visitor to this site, I want to be able to contact the studio, so that I can make queries or request a booking.
4. As a visitor to this site, I want to be able to view the range of products that are on sale, so that I can make an online purchase.
5. As a visitor to this site, I want to be able to view individual product details, so that I check product details before deciding to purchase.
6. As a visitor to this site, I want to be able to see and post reviews of the products on sale, so that I get a second opinion before I buy or share my opinion with other visitors.

### Owner Goals

1. As the owner of this site, I want a simple landing page, so that visitors can learn about my studio easily and quickly.
2. As the owner of this site, I want to be able to have an online store so I can sell merchandise and gift vouchers.
3. As the owner of this site, I want a receipt/proof of purchase emailed to me and available to myself.
4. As the owner of this site, I want to showcase some of my work, so the user gets an idea of my skills and talent.

### Structure

This full-stack site is put together with HTML, using the Bootstrap framework along with some CSS and JavaScript on the frontend.

The frontend is integrated into the backend using Python and Django with a PostgreSQL Database.

### Skeleton

The page content is dynamic and composed of Jinja templates which are put together using Python Django.

#### Website page line up

- Home / Index

- What we do

- Contact

- Gallery

- Login / Logout

- Register new user

- Profile / My details / Edit my Contact details

- All products

- Product details / reviews add/edit/delete

- Shopping bag

- Checkout

- New product addition

### Database Schema

#### Relational Database tables schema

![DB schema chart](wireframe/db-schema-20210815.png)

[image source](https://drawsql.app/code-institute-3/diagrams/ms04#)

##### Order table

```bash

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

```

##### OrderLineItem table

```bash

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

```

##### PhotoGallery table

```bash

    label = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

```

##### Contact table

```bash
# This Model is just used for the contact form rendering, no data is saved

    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=3000)

```

##### Product table

```bash

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

```

##### UserProfile table

```bash

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

```

##### Review table

```bash

    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=90)
    review_text = models.TextField()

```

#### Wireframes of pages

#### Home

![Home page ](wireframe/wireframe1.png)

#### What we do

![What we do](wireframe/wireframe2.png)

#### Contact

![Contact ](wireframe/wireframe3.png)

#### Gallery

![Gallery ](wireframe/wireframe4.png)

### Surface

#### Colours

Colours were sourced from a work in progress design on branding and logo for BoWood Audio.

Colours are mainly Dark mode using:

- #323232 - Graphite or Jet

- #BB3C2B - Tall poppy or International Orange Gold

- #F5CA9F  - Manhattan or Peach Crayola

- #CCB19E -  Rodeo Dust or Desert Sand

![colour swatch ](wireframe/colour-swatch.png)

#### Icons

[Font Awesome](https://fontawesome.com/v5.15/icons?d=gallery&p=1) is used for icons

#### Images

Images are sourced from [Unsplash](https://unsplash.com/) and the site owner.

#### Fonts

  ![font sample ](wireframe/font-sample.PNG)

The font used is Oswald from [Google fonts](https://fonts.google.com/specimen/Oswald?query=oswal).

back to [contents](#table-of-contents)

---

## Features

### Existing Features

- Online Shop purchases payment can be accepted using the Stripe API.

- Messages inputted on the Contact form are emailed to the site owner.

- Responsiveness display is experienced on all screen sizes.

- Toasts feedback messages to the user.

- The Photo gallery is connected to a database table, so it can be updated by the site owner on an admin portal.

- Visitors have full CRUD access to the product reviews they submit.

- The Product review ratings are updated automatically by [Django signals](https://docs.djangoproject.com/en/3.2/topics/signals/). Each change on the reviews model table triggers the particular product's rating to be re-calculated.

- Results for Products and review listing in the shop are paginated.

- The Shopping cart icon on the navbar only displays outstanding balances above zero.

### Features Left to Implement

- Gift Voucher journal handling.

- Official logo and fresh showcase work (still in progress).

back to [contents](#table-of-contents)

---

## Technologies Used

### Frontend

#### Languages

- HTML
- CSS
- Python
- JavaScript/Jquery

#### Libraries, Frameworks and Packages include

- [Bootstrap](https://getbootstrap.com/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- Fonts: [Google Fonts](https://fonts.google.com/)
- Icons: [FontAwesome](https://fontawesome.com/v5.15/icons?d=gallery&p=1)
- [django](https://www.djangoproject.com/)
- django-allauth
- pillow
- crispy-bootstrap5
- django-crispy-forms
- stripe
- django-countries
- dj-database-url
- psycopg2-binary
- gunicorn
- boto3
- django-storages

#### Tools

##### Productivity

- [Notion](https://www.notion.so/): I used Notion for gathering requirements, content, documenting personal notes, and planning workload.
- Pomodoro timer: [Tomato Clock](https://chrome.google.com/webstore/detail/tomato-clock/enemipdanmallpjakiehedcgjmibjihj) is perfect for keeping my work progressing while also making me take breaks!.
- Kanban planner: [Github projects](https://github.com/kenwals/BoWood-Audio/projects/1).

##### Toolbox

- JSfiddle: I used this online sandbox to build and play code before adding it to the project.
- Wireframe: [Balsamiq](https://balsamiq.com/)
- DB Schema diagram: [Drawsql.app](https://drawsql.app/code-institute-3/diagrams/ms04#)
- IDE: [Visual Studio Code (VS Code)](https://code.visualstudio.com/).
- Virtual Environment: [Pipenv](https://pipenv.pypa.io/en/latest/)
- Version control: Git and GitHub Desktop app
- Markdown editor: [Typora](https://typora.io/) was used when appropriate, VS code editor was used for most updates.
- Markdown Preview Github Styling: this brilliant vscode extension helps me read my markdown in Github format.
- [markdown table of contents creator](https://ecotrust-canada.github.io/markdown-toc/)
- File renaming utility: PowerRename from [PowerToys on Windows 10](https://www.windowscentral.com/how-bulk-rename-your-files-windows-10-powertoys)
- Favicon creator: [favicon.io](https://favicon.io/favicon-generator/)
- Autoprefixer CSS: [Autoprefixer](https://autoprefixer.github.io/)
- Auto formatter for HTML, CSS and JS:  [webformatter](https://webformatter.com/html)
- px to rem convertor: [nekoCalc](https://nekocalc.com/px-to-rem-converter)
- JavaScript linter: [jshint](https://jshint.com/)
- Python linter:  [Pep8 online](http://pep8online.com/)
- Markdown linter: Markdownlint extension on VS Code.
- Colour names: [Name that color](https://chir.ag/projects/name-that-color/#6195ED)
- Colour swatches: [Coolors](https://coolors.co/)
- [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)
- Image editing/cropping: MS Paint

back to [contents](#table-of-contents)

---

## Testing

### Performance Testing

- Home / Index :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse1.png)

- What we do :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse2.png)

- Contact :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse3.png)

- Gallery :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse4.png)

- Login / Logout :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse5.png)

- Register new user :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse6.png)

- Profile / My details / Edit my Contact details :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse7.png)

- All products :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse8.png)

- Product details / reviews add/edit/delete :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse9.png)

- Shopping bag :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse10.png)

- Checkout :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse11.png)

- New product addition :heavy_check_mark:

    ![lighthouse audit results passed](wireframe/lighthouse12.png)

### Bugs encountered on the way

#### 500 server error

The contact page was giving a 500 server error at one point when the user was attempting to send messages. It turns out, I had reset my Gmail password recently and I didn't realise that this also makes all my current SMTP passcodes invalid(they disappeared from my Gmail settings). So the simple fix was to create and replace the passcode and make sure I remember what to do next time I change my Gmail password.

### Known issues

#### Not secure warning or Unsecure connection

This Web Application has a "not secure" warning displayed on the browser address bar, this prevents me from using certain online tools for responsiveness testing, so I had to manually test these.

#### Linting errors

As Django autogenerates HTML and Python, I had to ignore some linting issues. For HTML, W3 validation errors from crispy forms happen on the contact page and the new product page. The Python ones are coming such things as migration scripts and webhooks. I believe these errors can safely be ignored.

### Project barriers and solutions

#### Time and work-life balance

Finding time to complete this project on schedule was a big push, but I think I have managed to get the MVP delivered.

### Version control

For version control, I used the UI on VS Code for making git commits or the GitHub desktop app, Merging was done on the GitHub site. I used branches when I was working on new features or bundles of changes.

### Functionality Testing

To check if all the links are working, I used the wget spider command below. It found 59 links, none of which are broken.

```bash
wget --spider -r http://bowood-audio.herokuapp.com/ -o wget.log
```

- Home / Index :heavy_check_mark:

This is a simple landing page, on a small width screen, the navbar is transparent.
The Navbar is dynamic based on user type and device type. The shopping cart also hides zero balances from the user.

- What we do :heavy_check_mark:

This page lists out what BoWood Audio does. It is responsive to screen size.

- Contact :heavy_check_mark:

This page contains a contact form. All fields are compulsory, if the message delivery is successful or fails the user is notified immediately.

- Gallery :heavy_check_mark:

This page contains photo images, it is responsive to screen size. The contents can be changed from the Admin portal in the Django backend.

- Login / Logout :heavy_check_mark:

This login/logout screen works are expected.

- Register new user :heavy_check_mark:

This Registration screen works are expected.

- Profile / My details / Edit my Contact details :heavy_check_mark:

On the page, the user can update contact details or view previous orders. This screen is only accessible when a user is logged in.

- All products :heavy_check_mark:

This page listed all the products available, it also can be used to search for products. If a superuser is logged in they can edit or delete products.

- Product details / reviews add/edit/delete :heavy_check_mark:

This Page displays details on each product. The user can submit a review. They can also edit or delete reviews they previously made. The user is prevented from submitting a second new review.

- Shopping bag :heavy_check_mark:

The shopping bag displays the current total and items are displayed in cards. Users can still make a change to the bag contents.

- Checkout :heavy_check_mark:

On this screen, the user has to be logged in to complete the purchase. Credit Card validation is working as expected.

- New product addition :heavy_check_mark:

Only superusers can access this screen.

### Responsiveness Testing

As this web application is not secure, I had to manually test responsiveness with my own devices and Chrome Dev Tools.
No issues were found on the screen sizes below.

| Screen size                          | Result |
| -------------------------------------------- | ------ |
| iPhone 5/SE DevTools emulation (Screen width 326px) xs | Pass |
| Android Mobile phone (Screen width 412px) xs | Pass |
| Android Tablet (Screen width 600px) sm       | Pass |
| iPad Tablet DevTools emulation (Screen width 768px) md| Pass |
| Windows laptop (Screen width 2560px) xxl        |   Pass |

### CSS3 validator

No errors.  Resource: <https://jigsaw.w3.org/css-validator/>

- base.css :heavy_check_mark:

- checkout.css :heavy_check_mark:

- profile.css :heavy_check_mark:

### HTML5 validator

No errors for the pages listed below. Resource: <https://validator.w3.org/>

- Home / Index :heavy_check_mark:

- What we do :heavy_check_mark:

- Gallery :heavy_check_mark:

- Login / Logout :heavy_check_mark:

- Register new user :heavy_check_mark:

- Profile / My details / Edit my Contact details :heavy_check_mark:

- All products :heavy_check_mark:

- Product details / reviews add/edit/delete :heavy_check_mark:

- Shopping bag :heavy_check_mark:

- Checkout :heavy_check_mark:

Pages below have minor errors due to the automatically rendered forms made by crispy forms.

- New product addition

- Contact

### Python validator

No issues. Apart from files, I didn't create such as the settings, webhooks, migrations files.
I believe the below linting error is a false one and can safely be ignored.

```bash
.\checkout\apps.py:9:9: F401 'checkout.signals' imported but unused
```

Resources:  <https://pep8online.com/> and [Flake8](https://flake8.pycqa.org/en/latest/)

### JavaScript validator

No issues. Resource:  <https://jshint.com/>

### Usability Testing

I shared the project on the peer-review channel on slack, and also with friends/family.

I tested and improved accessibility with lighthouse and Firefox developer tools.

Any issues found were resolved.

### Compatibility Testing

| Screen size\Browser                          | Chrome | Firefox | Edge |
| -------------------------------------------- | ------ | ------- | ---- |
| Android Mobile phone (Screen width 412px) xs | Pass | Pass | Pass |
| Android Tablet (Screen width 600px) sm       | Pass | Pass | Pass |
| Windows laptop (Screen width 2560px)         |   Pass |  Pass |  Pass    |

### Testing User Stories

#### Visitor Stories

1. As a visitor to this site, I want to see what services are available so I can decide if I want to do business here.

    ![visitor story 1](wireframe/visitor-story1.png)

    *BoWood Audios list of services and facilities are listed on the What We Do page.*

2. As a visitor to this site, I want to see pictures of the studio, so I know what to expect.

    ![visitor story 2](wireframe/visitor-story2.png)

    *Photos of the Studio are shown on the Gallery page. This page is also updatable from the admin section which the Owner has access.*

3. As a visitor to this site, I want to be able to contact the studio, so that I can make queries or request a booking.

    ![visitor story 3](wireframe/visitor-story3.png)

    *The Contact page has a form that the visitor can fill in and send. The message can be sent to a list of email addresses(currently only one).*

4. As a visitor to this site, I want to be able to view the range of products that are on sale, so that I can make an online purchase.

    ![visitor story 4](wireframe/visitor-story4.png)

    *Visitors can browse the products selection on the Shop/All items page.*

5. As a visitor to this site, I want to be able to view individual product details, so that I check product details before deciding to purchase.

    ![visitor story 5](wireframe/visitor-story5.png)

    *When the visitor clicks on a product from the products page, they are taken to a page giving more details on the product.*

6. As a visitor to this site, I want to be able to see and post reviews of the products on sale, so that I get a second opinion before I buy or share my opinion with other visitors.

    ![visitor story 6](wireframe/visitor-story6.png)

    *Reviews are visible on the Product detail page, the visitors can contribute when logged in.*

#### Owner Stories

1. As the owner of this site, I want a simple landing page, so that visitors can learn about my studio easily and quickly.

    ![owner story 1](wireframe/owner-story1.png)

    *The homepage is simple and responsive to screen size, on smaller screens, the navbar is transparent initially.*

2. As the owner of this site, I want to be able to have an online store so I can sell merchandise and gift vouchers.

    ![owner story 2](wireframe/visitor-story4.png)

    *The shop has various products and gift vouchers on sale.*

3. As the owner of this site, I want a receipt/proof of purchase emailed to me and available to myself.

    *The emails from this web app are set up to be sent by Gmail, so the site owner has full access to the email history.*

4. As the owner of this site, I want to showcase some of my work, so the user gets an idea of my skills and talent.

    ![owner story 4](wireframe/owner-story4.png)

    *Visitors can view upcoming work on the BoWood Audios Youtube or Soundcloud pages.*

back to [contents](#table-of-contents)

---

## Deployment

I developed this application in VScode, While developing this application I used a virtual environment called [pipenv](https://pipenv.pypa.io/en/latest/). I would recommend you do the same. This repo includes the pipenv compatible dependency setup files, the only thing you need to configure is the environmental variable file (filename: ".env").

**Please note** The Production and Development versions of this project contains several Environmental variable keys that will not work outside of this project without you refactoring in your keys. Here is a sample of the Local Environmental variables file I used on the development version with keys masked. You will need to replace it with your own.

```bash

STRIPE_PUBLIC_KEY=SECRET_KEY
STRIPE_SECRET_KEY=SECRET_KEY
STRIPE_WH_SECRET=SECRET_KEY
SECRET_KEY=SECRET_KEY
EMAIL_HOST_PASS=SECRET_KEY
EMAIL_HOST_USER=email_address
DEVELOPMENT=True
```

### Pre-Requisites for Deployment

You will need :

- [Python](https://www.python.org/) installed.

- A [Stripe](https://stripe.com/ie) account.

- An email address STMP server password or passkey, I recommend using Gmail.

- A Django Secret Key. You can generate your unique one [here](https://djecrety.ir/)

- An [Heroku](https://www.heroku.com/) account with a PostGresSQL app installed.

- A [GitHub](https://github.com/) account.

- An (optional) [Amazon Web Services](https://aws.amazon.com/) account.

### Local Deployment

To deploy locally on your preferred Desktop IDE, you can clone the repository to your desktop by the following steps.

1. Go to [the BoWood Audio github page](https://github.com/kenwals/bowood-audio).
2. Above the list of files, click on the **code** button.
3.
    - To clone the repository using **HTTPS,** under "Clone with HTTPS", click the paste icon.
    - To clone the repository using an **SSH key**, click Use SSH, then click the paste icon.
    - To clone a repository using **GitHub CLI,** click Use GitHub CLI, then click the paste icon.
4. Open your preferred Terminal interface.
5. Change the current working directory to the location where you want the cloned directory.
6. Type **git clone**, then paste the URL you copied earlier above. The example below is HTTPS for a Windows PC.

    ```bash
    git clone https://github.com/kenwals/BoWood-Audio.git
    ```

7. Press Enter to create your local clone. more detailed instructions are available [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### For VScode and Pipenv

1. To run the manage.py in the VScode terminal you will need supporting Environmental variables inputted in the .env file(example above).
2. Your VScode should have Python installed already, if it does please ensure it's thereby entering the command below.

    ```bash
    python --version
    ```

3. Now you need to install Pipenv, enter the command below.

    ```bash
    pip install pipenv
    ```

4. As this repository has the setup files made already, you can start the environment by entering the command below. More info on Pipenv [here](https://www.youtube.com/watch?v=6Qmnh5C4Pmo) and [here](https://pipenv.pypa.io/en/latest/)

    ```bash
    pipenv shell
    ```

5. You should notice a message like below saying loading ".env environment variables..." this is good, it means your keys are in place.

    ![pipenv success image](wireframe/pipenv.png)

6. Now to run the application on your desktop, enter the command below and open <http://localhost:8000/> on your preferred browser.

    ```bash
    python manage.py runserver
    ```

### Remote Deployment on Heroku

[Heroku](https://www.heroku.com/) is a cloud platform that can hosts dynamic web applications. Once you have the completed site in your repository, you can deploy it to Heroku by the following steps.

1. Before you set up Heroku, you first need to create some files that are necessary for it to run on the Heroku server.
2. Open a terminal window in your IDE on the root folder of the project, run the command below, this will create a new file called procfile.

    ``` echo web: gunicorn bowood.wsgi:application > Procfile ```

3. Now run the command line below. this will create a new file called requirements.txt

    ``` pip3 freeze --local > requirements.txt ```

4. Create a [Heroku user account](https://signup.heroku.com/login)
5. Click on the New button and choose to create a new app.
6. Input an app name and choose a region that is closest to you.
7. To input the necessary environmental variables, simply go to the Settings tab, and under Config Vars, Click on Reveal Config Vars, Below is the list I use on my Heroku deployed version. The AWS keys are optional.

    ![Heroku environmental variable](wireframe/heroku1.png)

    ![Heroku environmental variable ](wireframe/heroku2.png)

8. Now you can deploy, the simplest way is to deploy from GitHub
    - Click on the Deploy tab, Under the Deployment method click on GitHub.
    - A search window will prompt you to connect to the appropriate repository.
    - You can then choose to do a manual or automatic deployment. I recommend Automatic, that way whenever a change is pushed to your main branch on your GitHub repository the Heroku application is re-deployed automatically.

### Contribution and Forking

You may wish to contribute to this website and have your contribution published, if so, you are welcome to follow these steps below.

1. Go to the GitHub website and log in.
2. Open <https://github.com/kenwals/bowood-audio>
3. In the top right-hand corner, you will see a fork button, click on this **Fork button**.
4. This will create a copy of the BoWood Audio repository in your Github account.
5. Run the project locally and make your required changes.
6. You can push these changes to your repository.
7. Once you're finished making changes you can locate the **New Pull Request** button just above the file listing in the original repository (<https://github.com/kenwals/bowood-audio>).
8. Your pull request will be reviewed and if approved, it will be merged into the main version of the BoWood Audio repository at a future date.

more detailed instructions are available [here](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)

back to [contents](#table-of-contents)

---

## Credits

### Content

- The foundation of this site is sourced from [Code Institute Educational material - Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
- The Review app is influenced by [LigaMoons Prikly](https://github.com/LigaMoon/Prickly/tree/main/reviews)
- BoWood Audio is a home studio belonging to Paul O'Hara (aka Lego from the band Royseven), content was provided by Paul O'Hara and Paul Walsh.
- Points of reference used for making this web app were [Camden Recording Studios](https://www.camdenrecordingstudios.com/) and [Grouse Lodge](http://grouselodge.com/).

### Resources

- [Django documentation](https://www.djangoproject.com/)

- [Trick used for navbar icon](https://stackoverflow.com/questions/42586729/how-can-i-change-the-bootstrap-4-navbar-button-icon-color)

- Codemy.com youtube videos on Django contact page setup [here](https://www.youtube.com/watch?v=xNqnHmXIuzU) and
[here](https://www.youtube.com/watch?v=w4ilq6Zk-08)

- CodingEntrepreneurs youtube video on [how to use Django signals](https://www.youtube.com/watch?v=rEX50LJrFuU)

- [How to make javascript dynamic to screen width](https://stackoverflow.com/questions/17237935/jquery-execute-scripts-based-on-screen-size/17237975). This is used on the homepage to make the navbar background transparent on mobile for this initial load.

- [How to add a favicon to Django in 4 steps](https://simpleit.rocks/python/django/django-favicon-adding/)

- Pagination in Django [here](https://docs.djangoproject.com/en/3.2/topics/pagination/) and [here](https://www.ordinarycoders.com/blog/article/django-pagination)

- [Djangos built-in views for error messages](https://docs.djangoproject.com/en/3.2/ref/views/)

- [Crash course in Pipenv](https://www.youtube.com/watch?v=6Qmnh5C4Pmo)

- [Bootstrap components](https://getbootstrap.com/)

- [W3schools](https://www.w3schools.com/)

- [Code institute's Slack workspace channels](https://slack.com)

- [Stack Exchange](https://stackexchange.com/)

- [MDN Web Docs](https://developer.mozilla.org/en-US/)

### Media

Product Images that were sourced from Unsplash are credited below:

1. Mug          [https://unsplash.com/photos/nDd3dIkkOLo](https://unsplash.com/photos/nDd3dIkkOLo)
2. T-shirt       [https://unsplash.com/photos/m1MRYp556Ew](https://unsplash.com/photos/m1MRYp556Ew)
3. Sweatshirt     [https://unsplash.com/photos/ikLELWYbyxk](https://unsplash.com/photos/ikLELWYbyxk)
4. Baseball cap   [https://unsplash.com/photos/b9hqQkKCnqw](https://unsplash.com/photos/b9hqQkKCnqw)
5. Drum sticks    [https://unsplash.com/photos/bRG2C0FAQEY](https://unsplash.com/photos/bRG2C0FAQEY)  
6. Water Bottle   [https://unsplash.com/photos/POAQXzBwF7g](https://unsplash.com/photos/POAQXzBwF7g)
7. Gift Voucher 50 euro  [https://unsplash.com/photos/RNlVIhXrz-Y](https://unsplash.com/photos/RNlVIhXrz-Y)
8. Gift Voucher 20 euro  [https://unsplash.com/photos/HwU5H9Y6aL8](https://unsplash.com/photos/HwU5H9Y6aL8)
9. Guitar pick  [https://unsplash.com/photos/s2efxWujA-o](https://unsplash.com/photos/s2efxWujA-o)
10. Bottle opener  [https://unsplash.com/photos/voJB2goG0us](https://unsplash.com/photos/voJB2goG0us)
11. Tea towel [https://unsplash.com/photos/8yIYQDR8Qr8](https://unsplash.com/photos/8yIYQDR8Qr8)
12. Tote Bag [https://unsplash.com/photos/nKK32qJheBY](https://unsplash.com/photos/nKK32qJheBY)
13. Wallet [https://unsplash.com/photos/9Huby3g9fN0](https://unsplash.com/photos/9Huby3g9fN0)
14. Phone Cover [https://unsplash.com/photos/fCO3tBcnkhg](https://unsplash.com/photos/fCO3tBcnkhg)
15. Gift Voucher 500 [https://unsplash.com/photos/Y20JJ_ddy9M](https://unsplash.com/photos/Y20JJ_ddy9M)
16. Gift Voucher 100 [https://unsplash.com/photos/8QrPJ3Kfie4](https://unsplash.com/photos/8QrPJ3Kfie4)
17. Gift Voucher 250 [https://unsplash.com/photos/MEL-jJnm7RQ](https://unsplash.com/photos/MEL-jJnm7RQ)

### Acknowledgements

- Thanks to the Lego and Paul from BoWood Audio.
- My Mentor [Maranatha Ilesanmi](https://github.com/mbilesanmi) for helpful guidance throughout.

back to [contents](#table-of-contents)
