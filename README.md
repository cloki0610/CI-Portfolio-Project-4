# TALES - A content share community
# Portfolio Project 4
Tales is a website focus on content creation and experience sharing.\
Creators can publish their story, creation and experience to the platform and begin a conversation about their contents.\
And the other member can leave their comment to react to the creators.\
You can click [here](https://ci-portfolio-project-4.herokuapp.com/) to the living website.\
Active website: 
![screen-capture](readme-img/screenshot_sc.png)

## **Table of Contents**
* [User Experience Design](#User-Experience-Design)
* [Feature](#Feature)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Technologies](#Technologies)
* [Credits](#Credits)

## **User Experience Design**
### **The Strategy Plane**
Tales is a request come from a anonymous group who want to create and share their own content but found themselves always be remove their posts by website owners because of their personal policies even their creations are just express their personal opinions. Although they still have other platforms to share their experience and gain a huge amount of subscribers, they still want to own a website to share their works.

Because of that, their first priority is not about payment method or security. They just need a platform simple enough to save their work and manage their creations. And build a small community to discuss their process.

And my aim is to build a responsive application that can share contents and allow to build an internal community. User should seperate into two user group: member and creator to clarify their role in their community. The creator should have right to manage their own creations and member should only have right to leave comments for the contents. And it should be as simple as possible because they also have their own chat group within their community, and also have their offical fanpage for their subscribers.
#### **Site Goal**
 - User validation to grant user to have right to share content and leave comments.
 - A website with user interface to view and manage contents.
 - Provide few forms to let user communicate wtih website admin.
#### **User Stories**
 - As a user, I can see the most upvoted posts on the top of the list on the landing page so that I can know the trend of the community.
 - As a user, I can view the list of posts order by the updated time so that I can know what's the latest content in the website.
 - As a user, I can click on a post so that I can read the full content with all comments on the posts.
 - As a user, I can view the number of likes and comments so that I can see which is the most popular or viral.
 - As a user, I can click the signup button in the navbar to register an account so that I can join the community as my own identity.
 - As a user, I can click the category button in nav bar so that I can view different types of content.
 - As a user, I can click on a theme so that I can view the overview page with all comments.
 - As a user, I can view the list of posts ordered by created date so that I can read the content from latest to oldest.
 - As an admin/creator/member, I can create, read, update, delete my own profile so that the other users can know something about me.
 - As an admin/creator/member, I can change my account's password so that I can protect my account.
 - As an admin/creator/member, I can delete my account so that I can be free to join and leave the community.
 - As an admin/creator/member, I can upvote/downvote posts and comments so that I can interact to the discussion.
 - As an admin/creator/member, I can leave my own comment on the theme page so that I can be involved in the discussion.
 - As an admin/creator/member, I can submit a form to report some sensitive/offensive content that makes me feel offended and disturbed.
 - As an admin, I can access the control panel to have full control of the website database so that I can manage the content.
 - As an admin, I can promote/demote users so that I can manage different user groups.
 - As an admin, I can search and use filters to view the data so that I can manage the database easier.
 - As an admin/creator, I can create, update, and delete my own posts so that I can manage my own content.
 - As a member, I can submit a form to send requests so that I can become the creator to share my content.
### **Scope Plane**
Planned Features the website should have:
 - Responsive Design
 - Navigation Bar
 - Category to filter the type of contents
 - User validation
 - Different user group
 - Profile image upload
 - Cover image upload
 - Article overview
 - Comments
 - Display full contents of the posts
 - User interfaces to manage their articles and contents
 - Admin platform to manage the database records
 - Filter and search function in admin platform
 - Form to report contents
 - Form to send a request to admin to grant a creator role
### **Structure Plane**

### **Skeleton Plane**
#### **Wireframes**

#### **Database Design**

#### **Security**
With heroku's config var feature, all sensitive keys are stored in their server to prevent unwanted connections to the database.

Django allauth was used to set up user registration and built in decorators allowed restricted access to certain features on the website that are not intended for regular users.
### **Surface Plane**
#### **Color Sheme**

#### **Layout**

## **Feature**
### **Existing Features**
### **Features Left to Implement**
 - Security is still need to be improve
 - Platform will allowed the user who authorized by the author of the theme to create related contents in the same theme
 - Creator will allow to upload their videos to the database

## **Testing**
 - HTML Code all pass through the W3C HTML Validator
 - CSS Code all pass through the W3C CSS Validator
 - Python Code all pass through PEP8 Validator
 - Lighthouse in Chrome Dev Tools have been used for test the performance of the website.
 ![light-house-result](readme-img/lighthouse-result.png)
### Issue found and solved
 - Slug update by website
 - Theme date update when post add or edited
 - redirect to 404 instead of redirect to target page
### Unsolved Issue
 - Even the template do not allowed, user still can sent a direct request to change the record in database\
with a exist user account. And there still many security problem same as this require to be solved.

## **Deployment**

## **Technologies**
 - HTML
 - CSS
 - JavaScript
 - Python
 - PostgreSQL
 - Bootstrap
 - hover.css
 - Google Fonts
 - GitHub
 - Git
 - Heroku

## **Credits**
### **Code**
 - https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
 - https://stackoverflow.com/questions/36317816/relatedobjectdoesnotexist-user-has-no-userprofile
 - https://stackoverflow.com/questions/28165243/cannot-upload-image-in-django-modelform
 - https://stackoverflow.com/questions/33715879/how-to-delete-user-in-django
 - https://www.itread01.com/content/1558923602.html\
   Full instruction about Paginator
 - https://michealscode.medium.com/django-ajax-like-and-upvote-button-on-listview-solved-in-5-simple-steps-96dbdc39daca
 - https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html
 - https://github.com/Daisy-McG/ChatToTheMat
 - https://github.com/Michelle3334/coaching-warriors
 - https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages
### **Acknowledgment**
 - Thanks to my mentor Daisy McGirr for all support and guidance in the process,\
 without her help my process will be far longer and complex.
 - Thanks stackoverflow's community to help me solve most of my problem.