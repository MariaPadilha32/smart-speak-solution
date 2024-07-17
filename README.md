# Smart Speak Solutions

<img src="media/logo-readme.jpg">

## A e-commerce site designed to provide services from a profesional writer specialized on writing unique speeches.

### By Maria Fernanda Dias Padilha

## [Live Site](https://TOBECHANGED.herokuapp.com/)  |  [Repository](https://github.com/MariaPadilha32/smartspeaksolutionsp5)


## Table of contents
<a name="contents">Back to Top</a>
 1. [ Business Model ](#business)
 2. [ UX ](#ux)
 3. [Agile Development](#agile)
 4. [ Features ](#features)  
 5. [ Features Left to Implement ](#left)  
 6. [ Technology used ](#tech) 
 7. [ Testing ](#testing)  
 8. [ Bugs ](#bugs)  
 9. [ Deployment](#deployment)
 10. [ Credits](#credits)
 11. [ Content](#content)  
 12. [ Acknowledgements](#acknowledgements) 

<a name="business"></a>

## Business Overview

Smart Speak Solutions is a B2C e-commerce platform designed to provide services from a professional writer specialized in writing unique speeches. 
Customers can purchase various types of speeches tailored to their specific needs.

### Search Engine Optimization and Social Media Marketing

To improve the business's visibility on search engines, an approach incorporating meta tags, keywords, a sitemap.xml file, and a robots.txt file was used.
A newsletter is available for users to subscribe to and receive updates on services.
A Facebook, WhatsApp, and Instagram has been set up to promote the business online and allow customers to contact the company.


[ Facebook ] (#https://www.facebook.com/profile.php?id=61560352866469)
[ Instagram ] (#https://www.instagram.com/smartspeaksolutions.ie/)
[ Whatsapp ] (#https://wa.me/353833679626)


### Keywords
To enhance the site's SEO and improve visibility, relevant keywords were carefully chosen and included in the meta tags within the head element of the base.html page. These keywords help search engines understand the content and context of your site, making it easier for potential customers to find you through search queries. Below is a screenshot of the head element from the base.html page, showcasing these keywords.


<summary>Keywords</summary>
<img src="TOBEADDED">


### Sitemaps
A sitemap.xml file was generated using XML-Sitemaps and included in the root level of the project repository to help search engines crawl the site more effectively.

### Robots
A robots.txt file was created at the root level of the project file to guide search engine crawlers on which URLs to access, avoiding site overload.

### Newsletter Marketing
A custom-designed newsletter subscription form is seamlessly integrated into the footer of the home page. This allows visitors to easily sign up for updates and special offers, effectively enhancing business marketing efforts by engaging and retaining interested customers.

## UX
<a name="ux"></a>

### Color Pallette
- The color palette used for the Smart Speak Solutions website includes the following colors:
<img src="TOBEADDED">

* #060644 (Dark Blue): This deep blue color conveys a sense of trust, professionalism, and reliability. It is often associated with competence and calmness, helping to establish the credibility of the service offered.

* #FFD700 (Gold): Gold represents luxury, success, and high quality. It attracts attention and conveys a sense of prestige and exclusivity, fitting for a professional speech writing service.

* Black: Black signifies elegance, sophistication, and formality. It provides a strong contrast and adds a touch of modernity and professionalism to the design.

* White: White symbolizes purity, simplicity, and clarity. It provides a clean and organized look, making the content easy to read and navigate.

* Gray (for some of the writing): Gray conveys neutrality and balance. It is used to create a harmonious and modern aesthetic, ensuring that the primary colors stand out while maintaining a professional appearance.

### Wireframes

Wireframes were meticulously crafted to outline the website layout, mostly focusing on desktop versions.
These wireframes serve as a visual guide, ensuring a user-friendly and intuitive design. 
While the final website has slight variations from the initial wireframes, the core layout and design principles remain consistent.

- WireFrames 
    <img src="TOBEADDED">

<details>
	<summary> Index page </summary>
	<br>
    <img src="TOBEADDED">
</details>

<details>
	<summary> Login Wireframe </summary>
	<br>
    <img src="TOBEADDED">
</details>

<details>
	<summary> Register Wireframe </summary>
	<br>
    <img src="TOBEADDED">
</details>

<details>
	<summary> Product Page Wireframe </summary>
	<br>
    <img src="TOBEADDED">
</details>

#### Database Schema

Pre-project planning involved detailed consideration of the database structure. This planning was essential to clearly define how different database models interact with each other and to determine the necessary data fields for each model.

<details>
	<summary>Entity Relationship Diagram</summary>
<img src="media/readme/TD-ERG.jpg">
</details>

The database consists of several key models:

* UserProfile Model: This model stores user-related information such as contact details and address. Each user has a unique profile associated with them.

* Post Model: This model is used to manage blog posts. Each post includes details such as the title, content, author, and timestamps for creation and updates. The author field links to the user model via a ForeignKey.

* Order Model: This model handles order information, including the order number, user details, and total costs. Each order is linked to a user through a ForeignKey relationship.

* OrderLineItem Model: This model represents individual items within an order, including product details, quantity, and total cost for each line item. It links to the Order model and the Product model through ForeignKey relationships.

* Contact Model: This model captures user inquiries or messages, including the user's email, subject, and message content.

* Newsletter Model: This model manages newsletter subscriptions, storing the subscriber's name, email, and subscription status.

* SubscribedUsers Model: Similar to the Newsletter model, this model also tracks users subscribed to the newsletter, along with the date they subscribed.

* Category Model: This model categorizes products, aiding in organizing and filtering products on the site.

* Product Model: This model details the products available for sale, including the name, category, description, price, stock level, and other relevant attributes. It links to the Category model via a ForeignKey.

* The relationships between these models, such as ForeignKey associations, help maintain data integrity and establish clear connections between different parts of the application. For example, the UserProfile model is linked to the User model, and the Order model is linked to both the User and OrderLineItem models, facilitating a comprehensive and organized database structure.


<summary> Database Structure</summary>
<br>

<summary>Profiles App</summary>

#### UserProfile Model
| id | Field |
|--|--|
|user|OneToOneField|
|default_phone_number|CharField|
|default_street_address1|CharField|
|default_street_address2|CharField|
|default_town_or_city|CharField|
|default_county|CharField|
|default_postcode|CharField|
|default_country|CharField|
|first_name|CharField|
|last_name|CharField|
|country|CharField|

<summary>Blog App</summary>

#### Post Model

| id | Field |
|--|--|
|title|CharField|
|slug|SlugField|
|author|ForeignKey|
|image_url|URLField|
|image|ImageField|
|excerpt|TextField|
|updated_on|DateTimeField|
|content|TextField|
|created_on|DateTimeField|
|status|IntegerField|

<summary>Checkout App</summary>

#### Order Model

| id | Field |
|--|--|
|order_number|CharField|
|user|ForeignKey|
|full_name|CharField|
|email|EmailField|
|phone_number|CharField|
|country|CountryField|
|street_address1|CharField|
|street_address2|CharField|
|town_or_city|CharField|
|postcode|CharField|
|county|CharField|
|date|DateTimeField|
|deliver_cost|DecimalField|
|order_total|DecimalField|
|grand_total|DecimalField|
|original_cart|TextField|
|stripe_pid|CharField|

#### OrderLineItem Model

| id | Field |
|--|--|
|order|ForeignKey|
|product|ForeignKey|
|product_size|CharField|
|quantity|IntegerField|
|lineitem_total|DecimalField|

<summary>Contact App</summary>

#### Contact Model

|id|Field|
|--|--|
|email|EmailField|
|subject|CharField|
|message|TextField|
|reason|CharField|

<summary>Home App</summary>

#### Newsletter Model

|id|Field|
|--|--|
|name|CharField|
|email|EmailField|
|created|DateTimeField|
|subscribed|BooleanField|

#### SubscribedUsers Model

|id|Field|
|--|--|
|name|CharField|
|email|EmailField|
|created_date|DateTimeField|

<summary>Products App</summary>

#### Category Model

|id|Field|
|--|--|
|name|CharField|
|display_name|CharField|

#### Product Model

|id|Field|
|--|--|
|name|CharField|
|category|CharField|
|sku|CharField|
|description|TextField|
|price|DecimalField|
|stock|IntegerField|
|in_stock|BooleanField|
|image_url|URLField|
|image|ImageField|
|rating|DecimalField|
|created|DateTimeField|



<a name="agile"></a>

## Agile Development

### Agile Overview
Once I had settled on the website idea for Smart Speak Solutions, I began preplanning by creating a GitHub Projects page to track the epics, user stories, and tasks required for the project. This structured approach allowed me to manage my workload more effectively and ensure that all aspects of the project were addressed systematically.

Throughout the development process, I actively maintained and updated my Kanban board, ensuring that each task moved from "Not Started" to "In Progress" and finally to "Completed." I made it a priority to log all significant information and steps taken, keeping the board as current and detailed as possible. This thorough documentation helped me stay organized and provided a clear view of the project's progress at any given time.

Each epic comprised multiple user stories associated with various tasks, providing a comprehensive breakdown of the project's requirements. The full details of these user stories can be found in the project board.

By continuously updating the Kanban board and logging each step, I was able to identify potential bottlenecks early and adjust my workflow to maintain steady progress. This methodical approach was instrumental in keeping the project on track and ensuring a smooth development process.

### GitHub Project Board
I used the github projects as a agile tool to manage the planning and implamentation of functions to the site. 
[Project Board](https://github.com/users/MariaPadilha32/projects/12)

#### Epics
**************************** OLHAR NO ORIGINAL******************************************
	1. [Epic: User Registration & Accounts](TOBEADDED)
	2. [Epic: Shopping Bag](TOBEADDED)
	3. [Epic: Product Admin](TOBEADDED)
	4. [Epic: Blog](TOBEADDED)
	5. [Epic: Newsletter](TOBEADDED)
	6. [Epic: Profiles](TOBEADDED)
	7. [Epic: Site Navigation](TOBEADDED)
	8. [Epic: Contact & FAQ](TOBEADDED)
	9. [Epic: SEO & Marketing](TOBEADDED)
	10. [Epic: ReadMe.md](TOBEADDED)
	11. [Epic: Deploy Project](TOBEADDED)


[Back to Top of page](#contents)


<a name="features"></a>

## Features

This section highlights the main features of the Smart Speak Solutions website.

- Navigation
    - The navigation bar is a constant presence across the website, providing easy access to all relevant links. Admin-specific links are shown when an admin is logged in, allowing them to manage site content. The center logo directs users to the home page, while the bag icon in the top right corner shows the current cart total and links to the checkout page.
<details>
	<summary> Navigation </summary>
    <img src="media/readme/features/desk-nav-feature.jpg">
</details>
<details>
	<summary> Admin Navigation </summary>
    <img src="media/readme/features/navbar-admin-sc-features.jpg">
</details>
    - On mobile devices, the navigation bar collapses into a more compact form for better usability.
<details>
	<summary> Navigation Mobile </summary>
    <img src="media/readme/features/mobile-nav-sc.jpg">
</details>
    - The footer, present on every page, contains links to social media profiles.
<details>
	<summary> Footer Navigation </summary>
    <img src="media/readme/features/footer-sc-features.jpg">
</details>
- Authentication
    - Authentication is managed by Django Allauth. Users can access login, logout, and registration pages from the account section in the navbar. Error messages are displayed for incorrect inputs.
<details>
<summary> Registration Page </summary>
    <img src="media/readme/features/register-sc.jpg">
</details>
- Confirmation Email
	- New users receive an email to confirm their registration details.
<details>
<summary> Email Confirmation </summary>
    <img src="media/readme/features/signup-email-sc.jpg">
</details>
- Products
	Products are displayed in various categories and can be sorted by price. Users can view detailed information about each product.
<details>
<summary> Products Overview </summary>
    <img src="media/readme/features/products-sc-feature.jpg">
</details>
- Categories can be selected on the home page via cards displayed below the hero image.
<details>
<summary> Product Categories </summary>
    <img src="media/readme/features/products-sc-feature.jpg">
</details>
<details>
<summary> Products Details </summary>
    <img src="media/readme/features/product-deta-sc-features.jpg">
</details>
<details>
<summary> Products Details </summary>
    <img src="media/readme/features/product-description-sc-features.jpg">
</details>
<details>
<summary> Product Catagory Home Page </summary>
    <img src="media/readme/features/catagory-sc-features.jpg">
</details>
- Product Admin
	- Admins have access to additional features for product management, including editing and adding new products. 
<details>
<summary> Admin Products </summary>
    <img src="media/readme/features/edit-delete-product-sc.jpg">
</details>
<details>
<summary> Admin Edit Products </summary>
    <img src="media/readme/features/edit-product-1-sc.jpg">
	<img src="media/readme/features/edit-product-2-sc.jpg">
	<img src="media/readme/features/product-edit-success-sc.jpg">
</details>
<details>
<summary> Admin Add Products </summary>
    <img src="media/readme/features/add-product-sc.jpg">
</details>
-Shopping Bag
	The bag contains the list of products that the user has added to possibly purchase. The quantities of the products can be adjusted in the bag as well as product deletion. The overall price and extra charges are calculated in the bag before checkout.
<details>
<summary> Bag Details </summary>
    <img src="media/readme/features/blog-details.jpg">
</details>
<details>
<summary> Bag Remove Item </summary>
    <img src="media/readme/features/bag-remove-sc.jpg">
</details>
- Checkout
	- The checkout page gathers detailed information about the user's order, including final costs and delivery address.
<details>
<summary> Checkout Details </summary>
    <img src="media/readme/features/checkout-details-sc.jpg">
</details>
<details>
<summary> Payment Processing (Stripe) </summary>
    <img src="media/readme/features/stripe-sc.jpg">
</details>
	- A confirmation page is displayed once the payment is processed, summarizing the transaction
<details>
<summary> Order Confirmation </summary>
    <img src="media/readme/features/order-confirmation-screen.jpg">
</details>
- Blog
	- The blog section features articles written by the admin.
<details>
<summary> Blog Page </summary>
    <img src="media/readme/features/blog-user-sc.jpg">
</details>
<details>
<summary> Blog Detail </summary>
    <img src="media/readme/features/blog-details.jpg">
</details>
	- Admins can manage blog posts, including editing, deleting, or adding new articles.
<details>
<summary> Admin Blog </summary>
    <img src="media/readme/features/blog-sc.jpg">
</details>
- Contact
	- A contact page is accessable for all users, where a FAQ is also to provide users answers to any issues they had. There is a support email that is accessable to logged-in users to help with order issues.
<details>
<summary> Contact </summary>
    <img src="media/readme/features/contact-sc.jpg">
</details>
<details>
<summary> Contact Form </summary>
    <img src="media/readme/features/contact-form-sc.jpg">
</details>
<details>
<summary> FAQ </summary>
    <img src="media/readme/features/faq-sc.jpg">
</details>
- Newsletter
	- Users can subscribe to the newsletter to receive updates and special offers via email.
<details>
<summary> Newsletter Subscription </summary>
    <img src="media/readme/features/newsletter-sc-features.jpg">
</details>
	- Admins can manage and send newsletters to subscribers.
<details>
<summary> Newsletter Admin </summary>
    <img src="media/readme/features/send-newsletter.jpg">
</details>
- Privacy Policy
	- A comprehensive privacy policy is available, outlining how user data is handled.
<details>
<summary> Privacy Policy </summary>
    <img src="media/readme/features/privacy-policy-sc.jpg">
</details>
- 404 Error Page
	- A custom 404 error page is displayed for non-existent URLs.
<details>
<summary> 404 Error </summary>
    <img src="media/readme/features/404-sc.jpg">
</details>
- Restrictions
	- Users are redirected from pages they do not have authorization to view, either back to the home page or to the sign-in page.

<a name="left"></a>

### Future Features
	- A review section under each product for users to leave feedback. This feature was not implemented due to time constraints.
	- Adding FAQ sections to the contact form from the front end.
	- Product questions: Users can submit questions about product details that are answered by site experts.

[Back to top](#contents)

<a name="tech"></a>

##  Technology Used

### Html
 - Used to structure the content of the website, providing the foundation for the web pages.

### CSS
 - Custom CSS was written to style the website according to the design specifications and wireframes, ensuring a visually appealing and responsive layout.

### JavaScript
 - Used to add interactivity and enhance user experience. For example, JavaScript was used to implement the timeout function for messages and to enable the menu on the index.html page.

### Python
 -  The primary programming language used for the backend logic of the project, including handling requests and processing data.

### Django
 -  The web framework used to build this project, providing a robust and scalable structure. Django facilitated the development of the backend, including models, views, and templates.

### Font Awesome
 -  An icon library used in the navigation bar and footer to enhance the visual appeal and usability of the website with various icons.

### Bootstrap 5
 - A front-end framework used alongside Django to streamline the design and development process, ensuring a responsive and mobile-friendly layout.

### GitHub
 - Used to store the project's code and manage version control. The GitHub repository also includes the project's Kanban board, which was used to track progress and manage tasks.

### Heroku
 - A cloud platform used to host and deploy the website, ensuring it is accessible to users online.

### ElephantSQL
 - A cloud-based PostgreSQL database service used to store and manage the project's data.

### Git
- A cloud-based PostgreSQL database service used to store and manage the project's data.

### AWS S3 and IAM
- Used to host static and media files for this project and IAM for the permissions based roles for accessing the S3 buckets.

### Stripe
- A payment processing service integrated into the website to handle secure online payments.

### Django-Crispy-Forms
- A Django application used to style forms, providing a more user-friendly and aesthetically pleasing form interface.

[Back to Top of page](#contents)


<a name="Testing"></a>

## Testing 

Testing documentation can be found [here.](TESTING.md)

## Bugs

<a name="bugs"></a>

Known:
	- When a product gets added to the basket, a toast is displayed but it does not disapear after the set time. It does also not close when the cornor 'x' is clicked. The user has to click on something else to remove the toast. I belive this is an issue with how my JS function is interacting with the toast html.
	- In the shopping bag, the sub-total is still in $ instead of €. When an item is added to the baf, the icon changes but still has the $ instead of euro symbol. 
	- The mobile site is not fully respionsive as some product images do not scale down correctly, this is an issue with the scaling and break points in the css.
	- The search bar doesn't bring all the items forward. This is because the q value is not added correctly to new products added.
	- Order confirmation email were not being sent after the order has been processed. This was perviously working and other emails such as password verification are sending. 
	- blog CSS
	- Bag bug  - getting int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
  - Exception Location:	/workspace/smart-speak-solution/bag/views.py, line 17, in add_to_bag

<a name="deployment"></a>

## Deployment and Local Development
The live deployed version of the website can be found on [Heroku](OBEADDED). The steps and technologies involved in deploying it are outlined below. The steps on how to fork or clone the repository for the website are also outlined.

### ElephantSQL Database

The PostgreSQL Database for this project was obtained using [ElephantSQL](https://www.elephantsql.com), a service which you can sign-up to with your GitHub account. Once signed up follow these steps:

- Click **Create New Instance** to start a new database.
- Name used: `smartspeaksolution`.
- Select the **Tiny Turtle (Free)** plan.
- **Tags** can be left blank.
- Normally you select the **Region** and **Data Center** closest to you in this case EU-West-1.
- For my project, I had to select a differnt region (West-US) as this provided a newer Postgres version that was needed for my project requirements.
- Once created, click on the new database name, where you can view the database URL which will be needed for the Heroku Config Vars.

### Amazon AWS

This project uses [Amazon Web Services (AWS)](https://aws.amazon.com) to store its media and static files.

Once you've created an AWS account and logged-in, navigate to the **AWS Management Console** page & follow these series of steps to get your project connected.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Name: `smartspeaksolutionp5`
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into the "Resource" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Name: `smartspeaksolution`
	- Provide a description:
		- "Access to S3 Bucket for Smart Speak Solutions static files."
	- Click **Create Policy**.
- From **User Groups**, click `manage-smartspeaksolution`.
- Click **Attach Policy**.
- Search for the policy you've just created (`smartspeaksolution`) and select it, then click **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Name: `TOBEADDED`
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `TOBEADDED`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
- If you don't see an option to downlod the CSV file go to IAM and select **Users**
- Select the user for whom you wish to create a CSV file.
- Select the **Security Credentials** tab.
- Scroll to **Access Keys** and click **Create access key**
- Select **Application running outside AWS**, and click next.
- On the next screen, you can leave the **Description tag** value blank. Click **Create Access Key**.
- Click the **Download .csv file** button.
    - **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**
- These will be needed for the Heroku Config Vars.

#### Final AWS Setup

- Follow the steps described later for [Heroku Deployment](#heroku-deployment) and then return here to follow these final AWS steps below.
- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Inside the media file select **Upload** and **Add Files**.
- Select the images from your hard-drive that you wish to upload.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click next through to the end and **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click **API keys for developers**.
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key - click **Reveal test key** (starts with **sk**)

As a backup, in case users prematurely close the checkout page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://8000-mariapadilh-smartspeaks-40dfhnkowno.ws.codeinstitute-ide.net/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here under "Signing secret":
	- `STRIPE_WH_SECRET` = Under signing Secret - click `Reveal` (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **See all settings** link.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- This opens a page in a new tab, select **Security** on the left.
- Select **2-Step Verification** to turn it on (verify your password and account).
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or the project name.
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com) for deployment to the web. The deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own postgres value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's gmail |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file need to be updated using:

- `pip3 freeze --local > requirements.txt`

Create a **Procfile** at the root level of the project:

- Open the Procfile and enter the following line of code: `web: gunicorn app_name.wsgi:application` and save.
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- Ensure Heroku is installed for these following commands to work.
- If it is not run `curl https://cli-assets.heroku.com/install.sh | sh` in the terminal/CLI.
- Then connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Development
The steps below describe how to fork or clone the repository if desired.
#### How to Fork
1. Log in to Github.
2. Navigate to the [repository](https://github.com/MariaPadilha32/smart-speak-solution) for this website.
3. Click the Fork button in the top right corner.
4. You will be brought to a new page with a short form to be completed.
5. Upon completing, click on the "Create fork" button and this will create a fork of the repository in your personal account.

#### How to Clone
1. Log in to GitHub.
2. Navigate to the [repository](https://github.com/MariaPadilha32/smart-speak-solution) for this website.
3. Click on the **Code** button and a modal will appear.
4. Within this modal select the local tab.
5. Within this tab there are HTTPS, SSH, or GitHub CLI tabs.
6. Click on the HTTPS tab and copy the link shown.
7. In your development environment open the terminal.
8. Change the current working directory to the location where you want the cloned directory to be.
9. Type `git clone` into the terminal, then paste the URL you copied in step 6.
10. Press **Enter** to create your local clone.
11. In the terminal install the requirements by using the following: `pip3 install -r requirements.txt`.
12. If you have your own packages that have been installed, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`.
13. Next create the env.py file which tells our project which variables to use.
14. Add env.py the file to a .gitignore file to prevent it from being pushed to github.
15. Start the Django app: `python3 manage.py runserver`.
16. Make migrations by running : `python3 manage.py makemigrations`
17. Then migrate those changes with `python3 manage.py migrate`
18. To view the website type `python3 manage.py runserver` into the terminal and open port 8000.
19. The project is now ready to work on locally and any changes made can viewed using port 8000.

[Back to top](#contents)

## Credits

### Media
| Source | Location | Type |
| --- | --- | --- |
|[Blog Photos](TOBEADDED) | Blog Article | image |
|[Eulogies](TOBEADDED) | Products | image |
|[Spouse's speech](TOBEADDED) | Products | image |
|[Parent's speech](TOBEADDED) | Products | image |
|[Wedding party speech](TOBEADDED) | Products | image |
|[Wedding Vows](TOBEADDED) | Products | image |
|[Anniversaries](TOBEADDED) | Products | image |
|[Retirements](TOBEADDED) | Products | image |
|[Special Birthdays](TOBEADDED) | Products | image |
|[Other occasions](TOBEADDED) | Products | image |


### Resources
	- The Code Institute "Building an E-Commerce Platform" Boutique Ado project was very much relied upon to build this project.
	- Luke C's Trail Direct project from [GitHub](https://github.com/lukecdev/Trail-Direct) was used as inpiration in the website design.

### Acknowledgements

	- 
	- 
	- 

[Back to top](#contents)