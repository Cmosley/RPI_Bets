<a id='top'></a>

# Introduction

The sports betting community is huge. One of the biggest problems with sports betting however is letting your emotions get the best of you and thats typical when you lose big. 

To fill this gap, I have created RPI Bets.  RPI Bets is a platform which is easy for a casual or experience bettor

The developer of this app originally created it as a Unit Project for their curriculum as a Fellow in General Assembly's Software Engineering Immersion program.  See [Appendix A](#appendix-a-assignment) for more information on the original specifications.

# Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Instructions for Use](#instructions-for-use)
- [Version Notes](#version-notes)
      - [Please note that this is raw commit data!  It will be better organized in a future version of the file.](#please-note-that-this-is-raw-commit-data--it-will-be-better-organized-in-a-future-version-of-the-file)
- [Tech Framework](#tech-framework)
    - [This app uses:](#this-app-uses)
    - [We built this app with:](#we-built-this-app-with)
    - [This app is hosted at:](#this-app-is-hosted-at)
- [Future Plans](#future-plans)
- [Contribute](#contribute)
- [Special Thanks](#special-thanks)
- [About the Developer](#about-the-developer)
    - [Christian Mosley](#christian-mosley)
- [Appendices](#appendices)
  - [Appendix A: Unit 3 Project Assignment from General Assembly](#appendix-a-unit-3-project-assignment-from-general-assembly)
    - [Databases](#databases)
    - [Wireframes & Mockups](#wireframes--mockups)
  - [Appendix C: Product Screenshots & Images](#appendix-c-product-screenshots--images)

[Back to Top](#top)
<a id='instructions'></a>

# Instructions for Use

The user first arrives at a [splash page](#appendix-c-picture-001-splash-page-not-logged-in) when navigating to the root directory of the URL and is prompted to log in or sign up for an account.  Once signed-in, the user is redirected to a [search results page](#appendix-c-picture-002-search-results-page-logged-in) that shows a central list of all uploaded snippets.  This page also features a search bar up top; as the user types a string into the search field, the page will [dynamically update the displayed snippets](#appendix-c-picture-003-dynamic-search-rendering-logged-in) to show ones which contain the search string somewhere in their content.

The nav bar in the header has a link to create a new snippet; when clicked the user is taken to a page with a [create snippet form](#appendix-c-picture-004-create-snippet-page-logged-in).  The user types information about their snippet.  Two code blocks are provided where the user can type code and see a dynamically-rendered preview with syntax highlighting.

[Back to Top](#top)
<a id='version-notes'></a>

# Version Notes

The **1.0.0** version of this app is currently uploaded.  In cases where I update the README without any updates to the website itself I do not update the version number or use branches for my work.  Each version number will lack a commit number until the next version is uploaded.  The current commit number is always added retroactively.  In general, for version number format X.Y.Z:

* X: increases in this number represent a complete overhaul of some section of the website, source code, or UI
* Y: increases in this number represent a major functional change/aesthetic change or addition to the app
* Z: increases in this number represent changes that are relatively minor but still warrant a new commit

Version XXXXXXX is the first version with the full range of intended functions successfully implemented.  Version 1.0.0 is the first to be both full functional and styled with optimized coding.

#### Please note that this is raw commit data!  It will be better organized in a future version of the file.

commit eec40b267ec9441b0533b08af2d272c44cb8c13e
Merge: 8c08b02 1f2b4f9
Author: Christian Mosley <cmosley@beholdmedia.com>
Date:   Tue Apr 13 20:49:34 2021 -0500

    Merge pull request #2 from ScriptStud-io/test-branch
    
    Test branch

commit 1f2b4f9b989fe71f6a0f49efc4865e594e287b91
Merge: 70bc1a4 5dfc87a
Author: Christian Mosley <cmosley@beholdmedia.com>
Date:   Tue Apr 13 16:25:08 2021 -0500

    Merge pull request #1 from Cmosley/christian-testing
    
    readme update

commit 5dfc87ab3e359fc06b38cc754b2c47779c991c02
Author: cmosley <cmosley@beholdmedia.com>
Date:   Tue Apr 13 15:49:22 2021 -0500

    readme update

commit 70bc1a44dcddfb4dcb9e11b04ca88c4437779105
Author: mhsmith321 <marty.smith01@yahoo.com>
Date:   Tue Apr 13 15:12:57 2021 -0400

    create test-branch

commit 8c08b02c551cb929afcc120f3e4fa513f7eea30f
Author: mhsmith321 <marty.smith01@yahoo.com>
Date:   Tue Apr 13 14:30:41 2021 -0400

    create folder-file tree

commit 8c6dd58b9557ddb7e4e547cb0a5bd18520c4a014
Author: mhsmith321 <marty.smith01@yahoo.com>
Date:   Tue Apr 13 13:57:19 2021 -0400

    delete unnecessary files from boilerplate

commit c918ead883b9d88e2f0e29b6a66c8b7a0c90ef88
Author: mhsmith321 <marty.smith01@yahoo.com>
Date:   Tue Apr 13 13:45:41 2021 -0400

    initial commit



# Tech Framework

### This app uses:
* HTML5 and CSS
* JavaScript ES6
* Python v 3.8.6
* [Django](https://www.djangoproject.com/) v 3.2.2
* [Django-Tailwind](https://tailwindcss.com/) v 2.0.1


### We built this app with:
* [VSCode](https://code.visualstudio.com/) version 1.55.2
* [PostgreSQL](https://www.postgresql.org/)
* [Google Chrome](https://www.google.com/chrome/) version 90.0.4430.85 (Official Build) (arm64)
* Zsh version with [Oh My Zsh](https://ohmyz.sh/)
* [GitHub](https://github.com/) (online, not desktop)

### This app is hosted at:
* [GitHub Repo](https://github.com/cmosley/RPIbets)
* [Heroku Hosted Site](http://rpi-bets.herokuapp.com)

[Back to Top](#top)
<a id='future-plans'></a>

# Future Plans
* Rewrite the App in the MERN stack
* Expand the functionality of bets under bet tracks
  * Includes grapping total of bets to display on bet track (Profile Model)
* Host the site on custom URL 
  * Configure Google Analytics.
* Add a password recovery feature.
* Create a custom favicon.
* Improve CSS to make the site more eye-friendly.
* Add mobile-responsive CSS.
* Add support for OAuth
  * Google, GitHub
  * Sync data models for OAuth information with the current `User` model.  Must have two-way referencing.
* Create additional pages and views.
  * Create a tutorial page with videos.
  * A leaderboard of winnings of all users
* Allow users to upload avatar images.
  * Allow the user to filter betting information based on preferred betting site
* Eliminate edge cases in betting data display
* Create dark/light modes.

[Back to Top](#top)
<a id='contribute'></a>

# Contribute

At this point in time the developers are not looking for outside collaborators on ScriptStud.io.  That may change in the future as this project grows and scale issues require more skillsets and man-hours to build and maintain the platform.  If you believe in the mission of this product the best thing you can do is utilize the product, contribute code snippets, and help build our knowledgebase.

[Back to Top](#top)
<a id='special-thanks'></a>

# Special Thanks

* Instructors (Ben Manley, David Stinson) and peers from the General Assembly SEIR-EC-2-22 cohort for collaboration in developing this app.
* The color palatte was generated with with [Coolors.co](https://coolors.co/) and [HTML Color Codes](https://htmlcolorcodes.com/) for template generation.  We used [Color Safe](http://colorsafe.co/) and [WebAIM](https://webaim.org/resources/contrastchecker/) to test our color choices for sufficient contrast to make the website accessible.
* Formatting this `README.md` file was easy with the help of the [Markdown Live Preview](https://markdownlivepreview.com/) tool and GitHub Guide's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) page.
* [Whimsical](https://whimsical.com/wireframes) was used to generate the wireframe images and ERDs seen throughout this `README.md` file.


[Back to Top](#top)
<a id='appendices'></a>

# About the Developer

### Christian Mosley

Christian is a web developer from Fort Worth, TX. With a passion for business, sports and technology, Christian decided on a career change during COVID when he found the time to cultivate his passion for web development.  Learn more about Christian at these links:

* [LinkedIn](https://www.linkedin.com/in/christian-mosley)
* [GitHub](www.GitHub.com/cmosley)


# Appendices

[Back to Top](#top)
<a id='appendix-a-assignment'></a>

## Appendix A: Unit 3 Project Assignment from General Assembly




### Databases

**Model: User**  |  (user account metadata)
* `username` user's login handle (also display name)
* `email` user's email address
* `password` user's password (encrypted)
* `timestamps` (create/update)

**Model: Snippet**  |  (snippet data)
* `title` title of snippet
* `purpose` purpose of snippet
* `generic` generic form/syntax of snippet
* `notes` usage notes and information
* `sample` example of snippet being used
* `tags` topic tags for snippet
* `addedBy` reference to `User` document of snippet creator
* `timestamps` (create/update)

**Entity Relationship Diagram (ERD)**
![entity relationship diagram from initial planning](public/images/README-images/ScriptStud-ERD.jpeg)

### Wireframes & Mockups

**Splash Page (React Component layout)**
![splash page wireframe layout of react components](public/images/README-images/scriptstudio-react-wireframe-user-hub-page.png)

**User Hub (React Component Layout)**
![user hub wireframe layout of react components](public/images/README-images/scriptstudio-react-wireframe-user-hub-page.png)

**Search Results Page (React Component Layout)**
![search result page wireframe layout of react components](public/images/README-images/scriptstudio-react-wireframe-search-results-page.png)

**Snippet View Page (React Component Layout)**
![snippet view page wireframe layout of react components](public/images/README-images/scriptstudio-react-wireframe-snippet-view-page.png)

**Create/Edit Snippet Page (React Component Layout)**
![create and edit pages wireframe layout of react components](public/images/README-images/scriptstudio-react-wireframe-create-edit-page.png)

**Snippet View Page (Mockup)**
![snippet view page mock representation](public/images/README-images/scriptstudio-snippet-view-page-mockup.png)

[Back to Top](#top)
<a id='appendix-c-pictures'></a>

## Appendix C: Product Screenshots & Images

<a id='appendix-c-picture-001-splash-page-not-logged-in'></a>

**Deployed Splash Page - User Not Logged In | Current**
![current splash page on deployed site and not logged in](public/images/README-images/deployed-splash-page.png)

---

<a id='appendix-c-picture-002-search-results-page-logged-in'></a>

**Deployed Splash Page - User Logged In | Current**
![current search results page on deployed site](public/images/README-images/deployed-search-results-page.png)

---

<a id='appendix-c-picture-003-dynamic-search-rendering-logged-in'></a>

**Deployed Splash Page - User Logged In**
![dynamic search results rednering on deployed site](public/images/README-images/deployed-search-results-page-dynamic-search-rendering.png)

---

<a id='appendix-c-picture-004-create-snippet-page-logged-in'></a>

**Deployed Create Snippet Page - User Logged In**
![create snippet page on deployed site](public/images/README-images/deployed-create-snippet-page.png)