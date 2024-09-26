# Smart Speak Solutions

<img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/logo.png">

## A e-commerce site designed to provide services from a profesional writer specialized on writing unique speeches.

### By Maria Fernanda Dias Padilha

## [Live Site](https://smart-speak-solutions-d06084558783.herokuapp.com/)  |  [Repository](https://github.com/MariaPadilha32/smart-speak-solution)


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
 10. [Post-Failure Updates](#post)
 11. [ Credits](#credits)
 12. [ Content](#content)  
 13. [ Acknowledgements](#acknowledgements) 

<a name="business"></a>

## Business Overview

Smart Speak Solutions is a B2C e-commerce platform designed to provide services from a professional writer specialized in writing unique speeches. 
Customers can purchase various types of speeches tailored to their specific needs.

### Search Engine Optimization and Social Media Marketing

To improve the business's visibility on search engines, an approach incorporating meta tags, keywords, a sitemap.xml file, and a robots.txt file was used.
A newsletter is available for users to subscribe to and receive updates on services.
A Facebook, WhatsApp, and Instagram has been set up to promote the business online and allow customers to contact the company.


1. [ Facebook ](https://www.facebook.com/profile.php?id=61560352866469)
<img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021423.png">

2. [ Instagram ](https://www.instagram.com/smartspeaksolutions.ie/)
<img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021444.png">

3. [ Whatsapp ](https://wa.me/353833679626)


### Keywords
To enhance the site's SEO and improve visibility, relevant keywords were carefully chosen and included in the meta tags within the head element of the base.html page. These keywords help search engines understand the content and context of your site, making it easier for potential customers to find you through search queries. Below is a screenshot of the head element from the base.html page, showcasing these keywords.


<summary>Keywords</summary>
<img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/meta.png">


### Sitemaps
A sitemap.xml file was generated using [ XML-Sitemaps ](https://www.xml-sitemaps.com/download/smart-speak-solutions-d06084558783.herokuapp.com-da3d5398b/sitemap.xml?view=1) and included in the root level of the project repository to help search engines crawl the site more effectively.

### Robots
A robots.txt file was created at the root level of the project file to guide search engine crawlers on which URLs to access, avoiding site overload.

### Newsletter Marketing
A custom-designed newsletter subscription form is seamlessly integrated into the footer of the home page. This allows visitors to easily sign up for updates and special offers, effectively enhancing business marketing efforts by engaging and retaining interested customers.

## UX
<a name="ux"></a>

### Color Pallette
- The color palette used for the Smart Speak Solutions website includes the following colors:
<img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/palette.png">

* #060644 (Dark Blue): This deep blue color conveys a sense of trust, professionalism, and reliability. It is often associated with competence and calmness, helping to establish the credibility of the service offered.

* #FFD700 (Gold): Gold represents luxury, success, and high quality. It attracts attention and conveys a sense of prestige and exclusivity, fitting for a professional speech writing service.

* Black: Black signifies elegance, sophistication, and formality. It provides a strong contrast and adds a touch of modernity and professionalism to the design.

* White: White symbolizes purity, simplicity, and clarity. It provides a clean and organized look, making the content easy to read and navigate.

* Gray (for some of the writing): Gray conveys neutrality and balance. It is used to create a harmonious and modern aesthetic, ensuring that the primary colors stand out while maintaining a professional appearance.

### Wireframes

Initially, a wireframe was created as a visual aid to outline the desktop version of the website layout. This wireframe provided a guide for a user-friendly and intuitive design. As the project progressed, some changes were made, but the core layout and design principles from the original wireframe were maintained.

- WireFrames 
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/wireframe.png">

#### Database Scheme

Pre-project planning involved detailed consideration of the database structure. This planning was essential to clearly define how different database models interact with each other and to determine the necessary data fields for each model.

* The database consists of several key models:

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
|user_profile|ForeignKey|
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
|priceMin|DecimalField|
|priceMax|DecimalField|
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

[Back to Top of page](#contents)


<a name="features"></a>

## Features

This section highlights the main features of the Smart Speak Solutions website.

- Navigation
    - The navigation bar is a constant presence across the website, providing easy access to all relevant links. Admin-specific links are shown when an admin is logged in, allowing them to manage site content. The center logo directs users to the home page, while the bag icon in the top right corner shows the current cart total and links to the checkout page.
<details>
	<summary> Navigation </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021304.png">
</details>
<details>
	<summary> Admin Navigation </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+074424.png">
</details>
    - On mobile devices, the navigation bar collapses into a more compact form for better usability.
<details>
	<summary> Navigation Mobile </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022230.png">
</details>
    - The footer, present on every page, contains links to social media profiles.
<details>
	<summary> Footer Navigation </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021354.png">
</details>
- Authentication
    - Authentication is managed by Django Allauth. Users can access login, logout, and registration pages from the account section in the navbar. Error messages are displayed for incorrect inputs.
<details>
<summary> Registration Page </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+074714.png">
</details>
- Products
	Products are displayed in various categories and can be sorted by price. Users can view detailed information about each product.
<details>
<summary> Most Popular Products </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021340.png">
</details>
<details>
<summary> Product Categories </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021304.png">
</details>
<details>
<summary> Products Details </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021614.png">
</details>
<details>
<summary> Products Details </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021637.png">
</details>
<details>
<summary> Admin Products </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022030.png">
</details>
- Product Admin
	- Admins have access to additional features for product management, including editing and adding new products. 
<details>
<summary> Admin Add Products </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022119.png">
	<img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022126.png">
</details>
<details>
<summary> Bag Details </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021648.png">
</details>
-Shopping Bag
	The bag contains the list of products that the user has added to possibly purchase. The quantities of the products can be adjusted in the bag as well as product deletion. The overall price and extra charges are calculated in the bag before checkout.
<details>
<summary> Bag Remove Item </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021752.png">
</details>
<details>
<summary> Checkout Details and Payment Processing (Stripe) </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021818.png">
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021825.png">
</details>
- Checkout
	- The checkout page gathers detailed information about the user's order, including final costs and delivery address.
	- A confirmation page is displayed once the payment is processed, summarizing the transaction
<details>
<summary> Order Confirmation </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021930.png">
</details>
- Blog
	- The blog section features articles written by the admin.
<details>
<summary> Blog Page </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021530.png">
</details>
	- Admins can manage blog posts, including editing, deleting, or adding new articles.
<details>
<summary> Admin Blog </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022049.png">
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022056.png">
</details>
- Contact
	- A contact page is accessable for all users, where a FAQ is also to provide users answers to any issues they had. There is a support email that is accessable to logged-in users to help with order issues.
<details>
<summary> Contact and FAQ </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021406.png">
</details>
<details>
<summary> Contact Form </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021504.png">
</details>
<details>
- Newsletter
	- Users can subscribe to the newsletter to receive updates and special offers via email.
<details>
<summary> Newsletter Subscription </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+021346.png">
</details>
	- Admins can manage and send newsletters to subscribers.
<details>
<summary> Newsletter Admin </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022156.png">
</details>
- 404 Error Page
	- A custom 404 error page is displayed for non-existent URLs.
<details>
<summary> 404 Error </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/Captura+de+tela+2024-07-19+022601.png">
</details>
- Restrictions
	- Users are redirected from pages they do not have authorization to view, either back to the home page or to the sign-in page.

<a name="left"></a>

### Future Features
- Review Section for Products:
A dedicated section under each product where users can leave feedback and reviews. This feature is intended to enhance user interaction and provide valuable insights to future customers. It was not implemented due to time constraints but is planned for future development.

- Product Questions:
A feature allowing users to submit questions about product details, which can then be answered by site experts or the community. This will help in addressing specific user queries and improving the overall customer experience. This feature is also slated for future implementation due to time limitations.

- Comprehensive Speech Information Form:
A form designed to collect all necessary information for custom speeches. This form would allow users to provide detailed inputs about the speech they require, ensuring a tailored and high-quality output. Unfortunately, this feature was not completed due to lack of time but remains a priority for future updates to streamline the custom speech creation process. In the meantime, the solution is for the writer to contact the customer directly once payment is completed to gather all necessary details for the speech.

<summary> Future Forms </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5/future+forms.png">
</details>
[Back to top](#contents)

<a name="tech"></a>

##  Technology Used

### Html
 - Utilized to structure the content of the website, laying the foundation for all web pages.

### CSS
 - Custom CSS was crafted to style the website as per design specifications and wireframes, ensuring a visually appealing and responsive layout.

### JavaScript
 - Implemented to add interactivity and enhance user experience, such as enabling the menu on the index.html page and setting timeout functions for messages.

### Python
 -  The primary programming language used to handle backend logic, including processing data and handling requests.

### Django
 -  A front-end framework used alongside Django to facilitate design and development, ensuring the website is responsive and mobile-friendly.

### Font Awesome
 -  An icon library integrated into the navigation bar and footer to improve the visual appeal and usability of the website with various icons.

### Bootstrap 5
 - A front-end framework used alongside Django to streamline the design and development process, ensuring a responsive and mobile-friendly layout.

### GitHub
 - Used for storing the project's code and managing version control. It also hosted the project's Kanban board to track progress and manage tasks.

### Heroku
 - A cloud platform leveraged to host and deploy the website, making it accessible online.

### ElephantSQL
 - A cloud-based PostgreSQL database service used to store and manage the project's data.

### Git
- A version control system utilized to track changes in the project's source code, enabling collaboration and maintaining a history of modifications.

### AWS S3 and IAM
- Employed to host static and media files for the project, with IAM managing permission-based roles for accessing the S3 buckets..

### Stripe
- A payment processing service integrated into the website to securely handle online payments.

### Django-Crispy-Forms
- A Django application used to enhance the styling of forms, providing a more user-friendly and aesthetically pleasing form interface.

[Back to Top of page](#contents)


<a name="Testing"></a>

## Testing 

Testing documentation can be found [here.](TESTING.md)

## Bugs

<a name="bugs"></a>


1. Persistent Toast Notification:
Description: When a product is added to the basket, a toast notification appears but does not disappear after the set time. Additionally, it does not close when the corner 'x' is clicked. The user must click elsewhere to remove the toast. This issue seems to be related to the interaction between the JavaScript function and the toast HTML.

2. Order Confirmation Email:
Description: Order confirmation emails are not being sent after an order is processed. This functionality was previously working, and other emails, such as password verification, are being sent successfully.

3. Menu on Small Screens:
Description: The menu is not functioning correctly on small screens when inspected. This issue affects the usability of the site on mobile devices.

4. Payment Button on Small Screens:
Description: The payment button is not displaying properly on small screens, causing issues with the payment process on mobile devices.

5. CSS Issues with New Messages:
Description: When a new message is received, certain elements, such as buttons, move outside the visible area, affecting the layout and usability.

<a name="deployment"></a>

## Deployment and Local Development
The live deployed version of the website can be found on [Heroku](https://smart-speak-solutions-d06084558783.herokuapp.com/). The following sections detail the deployment process and the technologies used. Instructions for forking or cloning the repository are also provided.

### ElephantSQL Database

The PostgreSQL Database for this project was was set up using [ElephantSQL](https://www.elephantsql.com),  which you can sign up for using your GitHub account. After signing up, follow these steps:

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



## Post-Failure Updates
<a name="post"></a>

Following a comprehensive review and feedback session, several critical issues were identified across various areas of the project. Each issue was thoroughly addressed, and the following improvements were implemented to bring the project up to standard:

### 1.2 Confirmation Emails Not Sent on Successful Purchases

 - Reason for the fail: Confirmation e-mails are not sent on successful purchases.

 - Issue: Confirmation emails were not being sent after successful purchases, which hindered user experience and transaction reliability.

 - Solution: With the guidance from Code Institute tutors, the issue was resolved by implementing a detailed debugging process. An error.html page was added to capture error messages, which allowed for troubleshooting of the email sending process. The issue stemmed from incorrect webhook handling, which was fixed, and now, users receive confirmation emails upon completing purchases.

<details>
<summary> Confirmation Emails Test: Placing an order, confirmation, email confirmation, email detail </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-26+110154.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-26+110209.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-26+110238.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-26+110249.png">
</details>

### 1.6 Code Failing Validation Tools

 - Reason for the fail: Code does not pass validation tools.

 - Issue:  The project code did not pass validation for CSS, PEP8, and JavaScript, leading to issues in coding standards and functionality.

 - Solution: All code was refactored to pass CSS, PEP8, and JavaScript validation tools. HTML validation has also improved significantly, with only a few remaining issues that are currently being addressed.

 <details>
<summary> Test: CSS, JS, Pep8 (Gallery) </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-26+093445.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+230146.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+230421.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+230505.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-26+094948.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+223631.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+223642.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+223651.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+223729.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+223740.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/Captura+de+tela+2024-09-20+223756.png">
</details>

### 1.8 Navigation Issues

 - Reason for the fail: Issues in navigation are present.

 - Issue: The website navigation had several bugs, affecting user experience and access to site features.

 - Solution: The navigation was thoroughly tested and adjusted. Now, all navigation elements work as intended across different devices, providing smooth and intuitive access to the website's content.

### 1.12 Non-Functional Custom Data Models

 - Reason for the fail: Custom data models not functional.

 - Issue: Several custom data models, including the Blog model, were non-functional, and the newsletter system did not work as intended.

 - Solution: Several key improvements were made:
  * A Gallery feature was added with full CRUD (Create, Read, Update, Delete) functionality. Logged-in users can now upload, edit, and delete photos. Additionally, the Admin can manage inappropriate content.

<details>
<summary> Gallery Testing </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174521.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174431.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174353.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174224.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174028.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174020.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174010.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+173942.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+173832.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/gallery+test/Captura+de+tela+2024-09-25+174521.png">
</details>

	* The Contact Page was simplified, allowing users to submit messages directly to the Admin, who can view and manage these messages through a dedicated "View Messages" section.

<details>
<summary> Contact Testing </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175728.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175735.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175845.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175853.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175921.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175928.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175936.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/contact+page/Captura+de+tela+2024-09-25+175944.png">
</details>

	* The Newsletter Model was fixed, enabling users to subscribe and receive newsletters. The Admin can now draft and send newsletters to all subscribers via the /newsletter page.

<details>
<summary> Newsletter Testing </summary>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/newsletter+test/Captura+de+tela+2024-09-25+175013.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/newsletter+test/Captura+de+tela+2024-09-25+175027.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/newsletter+test/Captura+de+tela+2024-09-25+175245.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/newsletter+test/Captura+de+tela+2024-09-25+175355.png">
	<br>
    <img src="https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/readme/PP5+-+2/newsletter+test/Captura+de+tela+2024-09-25+175402.png">
</details>

### 1.15 Broken Links

 - Reason for the fail: Broken links hamper user experience.
 - Issue: Broken links throughout the site hampered user navigation and functionality.
 - Solution: All links were carefully reviewed and corrected. The entire site has been tested to ensure there are no remaining broken links, improving the overall user experience.

### 2.1 Poor UX Design and Front-End Experience

 - Reason for the fail: Missing adequate UX design leads to a poor experience at the front-end.
 - Issue: The user experience (UX) was suboptimal, with many UI elements overlapping or not displaying correctly.
 - Solution: Extensive CSS improvements were made to ensure a consistent and polished UI across devices. These changes have significantly enhanced the front-end experience, providing users with a more intuitive and visually appealing interface.

### 2.3 Insufficient Testing Documentation

 - Reason for the fail: Insufficient testing documentation.
 - Issue: The project's testing documentation was incomplete, and testing did not cover all critical functionality.
 - Solution: A thorough testing process was conducted, covering all essential site features. Detailed testing documentation has been updated, and it is now expected to meet the required project standards.

## Credits

### Media
| Source | Location | Type |
| --- | --- | --- |
|[Blog Photos](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/blog_weddingvows_mALH5iB_wckjLDx.png) | Blog Article | image |
|[Eulogies](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/eulogy.jpg) | Eulogy | image |
|[Spouse's speech](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/manspeech.jpg) | Weddings | image |
|[Parent's speech](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/father.jpg) | Weddings | image |
|[Wedding party speech](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/groomsman1.jpg) | Weddings | image |
|[Wedding Vows](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/vows.jpg) | Weddings | image |
|[Anniversaries](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/anniversaries.jpg) | Special Occasions | image |
|[Retirements](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/retirements.jpg) | Special Occasions | image |
|[Special Birthdays](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/birthday.jpg) | Special Occasions | image |
|[Other occasions](https://smartspeaksolution.s3.eu-west-1.amazonaws.com/media/confirmation.jpg) | Special Occasions | image |


### Resources
	- The Code Institute "Building an E-Commerce Platform" Boutique Ado project was very much relied upon to build this project.
	- Luke C's Trail Direct project from [GitHub](https://github.com/lukecdev/Trail-Direct) was used as inpiration in the website design.

### Acknowledgements

- I would like to acknowledge Marko Tot and my mentor Harry.
- The tutor assistance team was an amazing help during very challenging points of my project.
- Most special thanks to Ger Hickey, my father-in-law, who passed away recently. He was always an amazing support.

[Back to top](#contents)