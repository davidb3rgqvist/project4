# Foorky

Foorky is the ultimate web app for storing and managing all your recipes in one place. Whether you're a culinary enthusiast or a professional chef, Foorky helps you stay organized and focused during cooking sessions with its unique toggling feature. Say goodbye to scattered recipe cards – with Foorky, cooking has never been easier.

- [Deployed page](https://project4-recipe-app-0bdc7c5f1779.herokuapp.com/)

![Responsive test](docs/responsive-test.png)

## Table of Contents
  - [UX - Five Planes](#ux---five-planes)
  - [Future Features](#future-features)
  - [Technology Used](#technology-used)
  - [Testing](#testing)
  - [Development](#development)
  - [Deployment](#deployment)
  - [Credits](#credits)

## UX - Five Planes

### Strategy:

Foorky is a recipe management web app designed to streamline the organization and accessibility of culinary recipes. The focus is on providing users with a convenient platform to store, access, and manage their recipes, whether they are culinary enthusiasts or professional chefs.

#### User Goals:

- **Recipe Organization:** Users aim to conveniently store and access their culinary recipes in one central location.
- **Efficient Management:** Users seek a platform that simplifies the process of managing and categorizing recipes for easy retrieval.
- **Collaborative Cooking:** Users may want to share recipes and collaborate with others in the culinary community.

#### Owner Goals:

- **User Engagement:** The primary goal is to keep users engaged by offering a user-friendly and efficient recipe management solution.
- **Community Building:** Foster a sense of community among users through features that encourage recipe sharing and collaboration.
- **Platform Growth:** Ensure the platform continues to attract new users and retain existing ones by delivering value and satisfaction.

### Scope:

- **Recipe Storage:** The primary function is to allow users to store and organize their recipes.
- **Accessibility:** Ensure recipes are easily accessible anytime, anywhere, with features for searching and filtering.
- **Collaboration:** Implement features that enable users to share recipes, comment on recipes, and collaborate on cooking projects.
- **Customization:** Allow users to customize their recipe library with personal notes, ratings, and favorite recipes.

![Screen shots of the pages with comments](docs/comments.png)

### Structure:

- **Recipe Dashboard:** Provide a central hub for users to view and manage their recipe collections.
- **Recipe Entry Form:** Offer a user-friendly interface for adding new recipes, including fields for ingredients, instructions, and photos.
- **Search and Filter:** Incorporate search and filter options to help users quickly find specific recipes or browse by categories.
- **Recipe Sharing:** Enable users to share recipes with others via social media links or direct sharing options.
- **Collaborative Features:** Implement features for users to comment on recipes, rate recipes, and collaborate on cooking projects with others.


### Skeleton:
- **Start Button:** Initiate the game with a "Start Game" button.
- **User Input Field:** Allow users to type their answers.
- **Submit Button:** Trigger the evaluation of user input.
- **Correct/Wrong Display:** Visually indicate correct and incorrect answers.
- **Play Again Button:** Provide an option to restart the game.
- **Exit to Scoreboard Button:** Allow users to view their high scores.

![Wireframe link](docs/wireframe.png)

### Surface:
- **Sign-Up/Login:** Initiate user interaction with a sign-up/login prompt.
- **Recipe Dashboard:** Present users with their recipe collections upon logging in.
- **Recipe Entry Form:** Provide a form for users to add new recipes, with fields for ingredients, instructions, and optional photos.
- **Search and Filter Options:** Offer search and filter options to help users navigate their recipe collections efficiently.
- **Recipe Sharing Tools:** Include options for users to share recipes via social media or direct sharing links.
- **Collaboration Features:** Integrate features for users to comment on recipes, rate recipes, and collaborate with others on cooking projects.

![Visual ID](docs/wordstream-vi.png)

## Future Features

We plan to enhance the website with the following features:

- Recipe Import: Allow users to import recipes from external sources such as websites or other recipe management platforms, making it easy to transfer existing recipes into Foorky.

- Meal Planning: Integrate a meal planning feature that enables users to schedule meals by selecting recipes from their collection, helping users organize their cooking schedule for the week or month.

- Ingredient Management: Provide users with tools to manage their ingredient inventory, including features for tracking ingredient quantities, setting reminders for low stock, and generating shopping lists based on selected recipes.

- Nutritional Information: Display nutritional information for recipes, including calorie count, macronutrient breakdown, and allergen information, helping users make informed dietary choices.

- Recipe Recommendations: Offer personalized recipe recommendations based on users' preferences, cooking history, and dietary restrictions, helping users discover new recipes they may enjoy.

- Social Integration: Enable users to connect with friends and family within the Foorky platform, allowing them to share recipes, collaborate on cooking projects, and view each other's recipe collections.

- Multi-platform Access: Develop Foorky as a cross-platform application, ensuring users can access their recipe collections seamlessly across desktop, mobile, and tablet devices.

- Offline Mode: Implement an offline mode that allows users to access their most recently viewed recipes even without an internet connection, ensuring uninterrupted access to recipes while cooking in the kitchen.

- Recipe Versioning: Provide users with the ability to create multiple versions of a recipe, allowing them to experiment with variations or adaptations without altering the original recipe.

- Integration with Smart Devices: Enable integration with smart kitchen devices such as smart scales or ovens, allowing users to follow recipes more accurately by syncing cooking instructions directly with their devices.

## Technology Used

- Frontend: HTML, CSS, JavaScript, Boostrap
- Backend: Django
- Database: PostgreSQL
- Figma for wireframes
- ChatGPT - for AI assistance
- Adobe express for image content
- Adobe Illustrator for graphic content
- www.w3.org: Utilized to perform validation test of HTML and CSS.
- https://jshint.com/: Utilized to perform validation test of JavaScript.
- https://ui.dev/amiresponsive: Utilized for a quick overview of the responsivness.

## Testing

Testing was an integral part of the website development process. We performed comprehensive tests across various devices and screen sizes to ensure a seamless user experience. This included functional testing to verify proper functionality of all features, as well as responsive testing to guarantee optimal display on different devices. Additionally we performed serval validation tests.

- [HTML Validation of index.html, no errors found](docs/index-validation.png)
- [CSS Validation of style.css, no errors found](docs/css-validation.png)
- [JavaScript Validation, no errors found](docs/javascript-validation.png)
- [Lighthouse report](docs/lighthouse-report.png)
- [Responsiveness overview](docs/responsive-test.png)

## Development

In crafting Foorky, our development journey revolves around harnessing the power of HTML, CSS, JavaScript, Bootstrap, Django, and PostgreSQL. These technologies serve as the foundation, providing a robust framework for the website's frontend, backend, and database functionalities. Our approach embraces a mobile-first philosophy, ensuring a seamless experience across various devices.

To bring our vision to life, we leverage tools such as Figma for meticulous UI/UX design and Git/GitHub for effective version control and collaboration.

As we chart the course for future development, we've identified key areas that can further enrich the Foorky experience:

- **User-Centric Enhancements:** Place a premium on user feedback to enhance the overall user experience. Consider implementing user registration, profile management, and avenues for user-generated content, fostering a more personalized connection.

- **Feature Expansion:** Enrich the platform by introducing advanced search filters, seamless integration with social media platforms, and engaging features such as community forums or cooking challenges. These additions will contribute to a vibrant and interactive culinary community.

- **Improving Accessibility:** Strive for inclusivity by ensuring adherence to accessibility standards, catering to users with diverse needs and abilities.

- **Continual Testing and Optimization:** Uphold a commitment to excellence through an ongoing testing strategy. Identify and address bugs, enhance performance, and validate design changes to ensure a polished user experience.

- **Community Engagement:** Cultivate a sense of community by encouraging user-driven content creation. Welcome feedback with open arms and respond promptly to user queries or concerns, fostering a responsive and vibrant community.

- **Security Measures:** Fortify the platform with robust security measures. Safeguard user data, mitigate potential vulnerabilities, and proactively prevent security breaches to uphold user trust.

By embracing these strategic steps, our vision for Foorky is not just a web app but a dynamic hub for recipe management and culinary exploration. This roadmap emphasizes user-centric design, feature richness, accessibility, continuous improvement, community engagement, and robust security. As we embark on this journey, we remain committed to delivering a culinary experience that exceeds expectations.

## Deployment

The Foorky web application is deployed using Heroku, a cloud platform as a service (PaaS). Here are the steps for deployment:

1. **GitHub Repository:** The Foorky codebase resides in a GitHub repository. - [Repository](https://github.com/davidb3rgqvist/project4)

2. **Heroku Setup:** Sign up for a Heroku account and create a new app.

3. **Deployment Configuration:** Set up the Heroku app to deploy from the GitHub repository, either manually or using automatic deployment hooks.

4. **Database Setup:** Configure the PostgreSQL database add-on on Heroku to host the Foorky database.

5. **Environment Variables:** Set any necessary environment variables, such as Django secret key or database credentials, in the Heroku app settings.

6. **Deployment:** Trigger the deployment process either manually or by pushing to the main branch of the GitHub repository.

7. **Verification:** Verify the deployment status and ensure the Foorky web application is live and accessible on the specified Heroku URL.

### Accessing the Deployed Site

The deployed Foorky web application can be accessed using the following URL: [Heroku App URL](https://project4-recipe-app-0bdc7c5f1779.herokuapp.com/)

Heroku provides a reliable platform for hosting and scaling web applications, ensuring accessibility to users worldwide.

Feel free to explore the live version of the Foorky web application.

## Credits

The development and creation of the Foorky web application would not have been possible without the contributions, support, and resources from various individuals and organizations. We would like to extend our gratitude and credit to the following:

### Open-Source Libraries

- **Google Fonts:** Utilized for typography and font styles throughout the Foorky web application.
- **Font Awesome:** Provided icons for various UI elements, enhancing the user experience.
- **Bootstrap:** Leveraged for its responsive design components, streamlining the development of Foorky's frontend.

### External Resources

- **Unsplash:** Provided high-quality images used in Foorky's interface, contributing to an engaging user experience.
- **GitHub:** Facilitated version control and hosting of the Foorky project repository.

### Inspirations and Mentors

- **Brian O'Hare:** As a mentor from Code Institute, Brian provided valuable guidance and inspiration during the development of Foorky.

We express our sincere appreciation to everyone who contributed directly or indirectly to the Foorky project, helping shape and enhance this platform for users seeking a seamless solution for recipe management and culinary exploration.
