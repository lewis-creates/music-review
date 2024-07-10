## **Vibe Verdicts**

PLACEHOLDER FOR DEPLOYED PROJECT LINK

PLACEHOLDER FOR IMAGE ON DEVICES

## **Site Overview**

Vibe Verdicts is an online application for music lovers to read and post reviews of their favourite music, or new music they have found. Users are able to see limited features of the site until they register an account, but when registered they are able to create, edit and delete their own reviews quickly and easily.

## **Table of contents** 

- [**Vibe Verdicts**](#vibe-verdicts)
- [**Site Overview**](#site-overview)
- [**Table of contents**](#table-of-contents)
- [**Planning stage**](#planning-stage)
  - [**Target Audiences**](#target-audiences)
  - [**User Stories**](#user-stories)
  - [**Site Aims**](#site-aims)
  - [**Wireframes**](#wireframes)
  - [**Color Scheme**](#color-scheme)
- [**Typography**](#typography)
- [**Features**](#features)
- [**Future Enhancements**](#future-enhancements)
- [**Testing Phase**](#testing-phase)
  - [**Responsiveness**](#responsiveness)
  - [**Functionality**](#functionality)
  - [**Validators**](#validators)
  - [**Lighthouse**](#lighthouse)
  - [**Testing user stories**](#testing-user-stories)
- [**Bugs**](#bugs)
- [**Deployment**](#deployment)
- [**Tech**](#tech)
- [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)

## **Planning stage**

### **Target Audiences**

- Users with an interest or love of any music
- Users who attend music festivals
- Users looking for new music to listen to
- Users thinking about getting into other genres of music

### **User Stories**

- As a user, I want the site to be easy to use.
- As a user, I want to the site to be responsive.
- As a user, I want the ability to read reviews posted by other users.
- As a user, I want the ability to post new reviews.
- As a user, I want the ability to read my own reviews.
- As a user, I want the ability to edit my own reviews.
- As a user, I want the ability to delete my own reviews.
- As a user, I want the ability to search for reviews by song or artist name.
- As a user, I want the ability to create an account.

### **Site Aims**

- Offer a simple to use application where users can create, read, edit and delete music reviews.
- Offer the ability to register an account, alloweing the user to see and manage their own reviews on a single page.
- To keep the user informed as they create, edit and delete reviews with confirmation of each step.
- To allow the user to search for reviews quickly and easily.

### **Wireframes**

Wireframes are all based on a central responsive design using bootstrap, so only desktop wireframes have been provided.

PLACEHOLDER WIREFRAME IMAGES NEEDED

### **Color Scheme**

Navbar and footer background #212529 Dark Grey
<br>
Secondary buttons: #6c757d Light grey
<br>
Supporting text: #585c5f Grey
<br>
Footer text: #9a9d9e Grey

The [WCAG Color Contrast Checker](https://accessibleweb.com/color-contrast-checker/) was used to ensure the grey text against the dark grey background met accessibility standards. All results passed, except for the small text in the AAA test. However, it was deemed acceptable, as the criteria for AAA compliance are exceptionally stringent and are rarely met.

![Color contrast](documentation/color-contrast/colorcontrast.png)

## **Typography**

I decided to import the Oswald font from Google Fonts as I felt it had a modern vibe to it without compromising on readability. It's stylish, clear to read and worked well with all of the applications features.

## *Features**

**Features common to all pages**

Navigation - The navbar appears on every page of the application. However, the links shown in the image only appear when the user is logged in. If the user is not logged in, they will see Home, Login and Register. The nav bar is fully responsive and collapses inside of a 'burger' icon on smaller devices. If the user wishes to logout, they are prompted with a confirmation modal to ensure they didn't press it by mistake.

This feature helps the user as it gives them a clear, easy way to navigate around the website and find what they need.

![Navigation](documentation/features/navbar.png)

Footer - The footer sticks to the bottom of the page, regardless of the page height, so on shorter pages, there is no white gap at the bottom of the page. It includes a contact email address if the user wishes to get in touch with Vibe Verdicts, and also links to their social media accounts. The colour scheme is consistent with the navbar to provide an aesthetic look.

This feature helps the user as they are able to get in touch with the website owner and look for more information and content on their social media accounts.

![Footer](documentation/features/footer.png)

Flash messages - Flash messages, such as 'You are logged out. Bye for now!'  and various others are set to appear in the same place on every page (only when required/prompted via the app.py file). They appear above the first main heading of the page, below the nav bar, to keep consistency.

This feature helps the user as it keeps them informed as they navigate through and use the website. It also provides confirmation when they ask the website to perform a certain action, reassuring them that what they intended to happen, did in fact happen.

![Flash messages](documentation/features/flashmessages.png)

**Home Page**

Main crowd image - This is the first feature the user sees when they enter the website. It immediately fits the theme of the website, as it depicts a crowd at a live show gig. If the user isn't logged in, they see the register button and also a login prompt below if they already have an account. If the user is logged in, the button changes to 'Browse Reviews' and the login prompt is removed.

This feature helps the user because they have a quick way to register for an account and start reading and posting reviews if they haven't already registered, and also provides a quick way to browse reviews if they are logged in.

![Main crowd image](documentation/features/crowd.png)

Home welcome text - This is the next section the user sees on the home page. It's a basic explanation of the website with some instructions how to get the most out of it. It also nicely separates the large image above from the recent reviews cards below it. This feature helps the user as it informs them what they need to do to get the most out of the website.

![Home welcome text](documentation/features/homewelcome.png)

Recent reviews - This feature displays three randomly selected reviews stored in the database. If the user is logged in, they can click the read more button to be taken to the specific page of that review, however if the user is not logged in, the button does not appear, as this section is for registered users only. If there are no reviews found in the database, a message displays to tell the user no reviews have been found

This feature helps the user as it gives them a preview of the reviews on offer, which should help them decide if they wish to see more.

![Recent reviews](documentation/features/homerecentreviews.png)

**Reviews Page**

Search box - This feature allows users to search for songs or artists, rather than scrolling through all of the reviews. The feature includes a reset button, so if the user has searched for something but wishes to reset the process, they are returned to the reviews page where they started.

This feature helps the user as they can easily find a specific song or artist if they are looking for a particular one and saves them a lot of time scrolling through and reading a list of reviews, when the website can do it for them.

![Search box](documentation/features/searchreview.png)

All reviews - Below the search box, all reviews found in the database are neatly displayed. If no reviews can be found, a message is displayed to inform the user, with a prompt to be the first one to post a review. If a review belongs to a particular user, they will see the edit and delete buttons, otherwise they will only see read more, which directs them to the page for that specific review.

If the review content is above 90 characters, the preview is capped at this amount with trailing dots, to show there is more to read by clicking on read more. If the content is below 90 characters, the content is shown in the preview as normal.

The ! tooltip is displayed if a user selects that the song contains explicit language when creating their review. When hovered over, it displays the relevant message to warn the user. If the user wishes to delete a review, they are prompted with a confirmation modal to ensure they didn't press it by mistake.

This feature helps the user as it's the main reason they are here, to read reviews! It's a neatly structured grid system, including a consistent design throughout every review, and offers the ability to read reviews further if they are interested.

![All reviews](documentation/features/allreviews.png)

**New Review Page**

New Review form - This form is used to create a new review. The genre is a dropdown, which is populated by the genres pulled from the database. The song name, artist name and review title input fields include validation to allow a max length of 60 characters as this is long enough to describe the song, artist and provide a short & sharp title. Without it, the user could enter unlimited characters which could make the other pages messy where review previews are shown.

An info message was only included for the review title explaining this because people are more likely to use more than 60 characters for a title than the song and artist name. I also found that too many instruction messages were too much on one page. If the user chooses that a song does include explicit language, a tooltip / warning appears in the relevant place with the review to inform the other users reading it.

The review content is a large text box, where the user can type as much as they want as this is cut down on the review previews elsewhere on the website, however it's only shown at full length on the reviews specific page, which has plenty of room for an endless amount of content.

This feature helps the user as it allows them to get involved with the website and its users, by creating their own reviews and sharing their own thoughts on any particular genre.

![New review](documentation/features/newreview.png)

