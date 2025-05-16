# GLO-NEWS
## Video Demo:  [Click here for video](https://youtu.be/n41SDgeEzlk)

___

###  Hello and welcome to the presentation of my final project for the CS50’s Introduction to Computer Science My name is Chirag G C and I'm from Mandya, from the state of Karnataka, India. I am a graduate from Vidyavardhaka College of Engineering Mysuru

___

## **Description**:

## GLO-NEWS: Technical Overview

**GLO-NEWS** is a dynamic, Flask-based web application designed to deliver real-time global news updates. It utilizes the **NewsAPI** to fetch and display news articles through API calls, allowing users to search for specific topics and navigate content using pagination.

The platform ensures secure API key management by leveraging environment variables and dynamically renders content with **Jinja2 templates** for an intuitive user experience. With its modular design and seamless integration of external APIs, GLO-NEWS provides a scalable and efficient solution for staying informed about the world.

____


## NewsAPI <[link here](https://newsapi.org/)>

**NewsAPI** is a powerful JSON-based REST API that provides access to real-time news articles from a wide range of publishers and blogs worldwide. It enables developers to query articles by keywords, sources, categories, and more, making it an essential tool for building news-driven applications. With features like pagination and detailed metadata, NewsAPI simplifies the process of integrating diverse news content into your projects.

___
____
___
## `app.py`

This Python script is a Flask application designed to fetch and display news articles using the **NewsAPI**. Here's a breakdown of how it works:

---

### **1. Importing Required Modules**
- **Flask**: Used to create the web application and handle routing.
- **render_template**: Renders HTML templates dynamically.
- **request**: Handles query parameters from the client.
- **requests**: Makes HTTP requests to external APIs.
- **os**: Accesses environment variables for configuration.
- **dotenv**: Loads environment variables from a `.env` file for secure key management.

---

### **2. Loading Environment Variables**
- The `load_dotenv('key.env')` function loads variables stored in a file named `key.env`. This ensures the **NewsAPI** key is securely managed and accessed using `os.getenv('NEWS_API_KEY')`.

---

### **3. `fetch_articles(query='India', page=1)`**
- This is a helper function to fetch news articles from **NewsAPI**.
- It constructs a URL with the query (`India` by default) and the page number.
- It makes a GET request to **NewsAPI** and:
  - Logs the URL and response status for debugging.
  - Returns a list of articles if the request is successful.
  - Logs an error and returns an empty list if the request fails.

---

### **4. Routes**

#### **`/` (Homepage)**
- **Purpose**: Displays news articles based on a search query and page number.
- **Logic**:
  - Retrieves query parameters (`query` and `page`) from the URL.
  - Fetches articles using the `fetch_articles` function.
  - If no articles are found, displays an error message.
  - Renders the `index.html` template with the articles, query, and page.

#### **`/about`**
- Renders the `about.html` template, which contains information about the platform.

#### **`/creator`**
- Renders the `creator.html` template to introduce the developer behind the project.

---

### **5. Running the App**
- The `if __name__ == '__main__':` block ensures the app runs in debug mode for local development.

---

### **Key Features**
- **Dynamic News Search**: Users can search for news articles by entering a query.
- **Pagination**: Allows users to navigate through multiple pages of results.
- **Secure API Key Management**: Keeps the **NewsAPI** key private by using environment variables.
- **Modular Design**: Separates concerns with helper functions and templating.

This code forms the backbone of a news aggregation platform that is both user-friendly and secure.
___
___
___
## ``key.nev``

This line is part of the `key.env` file, which securely stores environment variables for the application. Here's what it does:

---

### **NEWS_API_KEY**
- This variable, `NEWS_API_KEY`, holds the API key required to access the **NewsAPI** services.
- The API key  is a unique identifier that authenticates the application and allows it to make requests to the NewsAPI.

---

### **Why Use `key.env`?**
- **Security**: Storing the key in an environment file keeps it out of the main source code, preventing accidental exposure in public repositories.
- **Convenience**: Developers can load this file using the `dotenv` library, making it easy to manage and update without modifying the application code.

---

### **Important Note**
- Ensure that the `key.env` file is included in the `.gitignore` file to avoid exposing the API key when pushing code to version control systems like GitHub.

____
____
____

## Index.html

---

### **1. Document Structure**

- `<!DOCTYPE html>`: Specifies that this is an HTML5 document.
- `<html lang="en">`: Sets the language of the document to English.
- `<head>`: Contains metadata for the page such as character set, viewport settings, title, and SEO-related meta tags.
  - **Meta Tags**:
    - `<meta charset="UTF-8">`: Specifies the character encoding for the page.
    - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Ensures proper scaling on mobile devices.
    - `<meta name="description" content="Stay updated with the latest news articles from around the world.">`: Provides a description for search engines.
    - `<meta name="keywords" content="news, articles, latest news, GLO-NEWS">`: Specifies keywords to help search engines index the page.

---

### **2. External Resources**

- **Bootstrap**: Includes the Bootstrap CSS framework from a CDN (`https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css`) for responsive design and pre-built styles.
- **Custom Styles**: Links to a custom CSS file (`/static/style.css`) for additional styling specific to the GLO-NEWS platform.

---

### **3. Body Content**

#### **Header**
- **Logo and Title**: Displays an image (globe holding a newspaper) and the title "GLO-NEWS."
- **Navigation**: Includes links to the home page, about page, and creator page, all styled as Bootstrap buttons.

#### **Main Content**
- **Search Form**:
  - Allows users to input a preferred news topic.
  - The form sends a GET request to the homepage with the search query.
  - The input is required and offers a placeholder for guidance (e.g., "India").

#### **News Articles**
- If articles are available, they are displayed in a grid layout (`<div class="row mt-4">`).
- Each article is presented in a Bootstrap card with:
  - A conditional image (`{% if article['urlToImage'] %}`) if the article has an image.
  - The article's title, description, and a "Read More" button linking to the full article.

#### **Load More Button**
- If there are more pages of articles, a button is provided to load the next set of articles (`<a href="?query={{ query }}&page={{ page + 1 }}" class="btn btn-primary">Load More Articles</a>`).

#### **Error Handling**
- If no articles are found, a warning message is shown to the user.

#### **Footer**
- A simple footer with copyright information (`&copy; 2025 News Articles`).

---

### **Key Features**
- **Responsive Design**: The use of Bootstrap ensures that the page is responsive on various devices.
- **Dynamic Rendering**: The news articles are dynamically inserted into the page using Jinja2 templating. If articles are available, they are displayed; otherwise, a warning message is shown.
- **Search and Pagination**: Users can search for articles based on topics and load more articles as needed using pagination.

This structure ensures a clean, user-friendly interface for displaying news articles dynamically, while also maintaining a simple and effective layout.
___
____
___

## ``About.html``

This HTML code defines the structure of the **About** page for the **GLO-NEWS** application. The main differences from the previous code are as follows:

---

### **1. Title and Meta Tags**
- The title of the page is changed to **"About"**, as indicated in the `<title>` tag.
- The description and keywords meta tags are absent in this version, focusing instead on the structure and design.

---

### **2. Inline Styles**
- There is additional inline CSS to define the appearance of the **About** page:
  - **Body Background**: The background color is set to `#e0f7f1`, a light color, contrasting with the content for visual appeal.
  - **About Card**:
    - A white background, rounded corners, and subtle shadow effects are applied to the card to give it a clean, modern look.
    - Padding inside the card and a top margin are added for better spacing.

  - **About Title**: The title of the page is styled with dark blue text (`#0056b3`), bold font weight, uppercase letters, and letter spacing for emphasis.

---

### **3. Body Content Changes**
- The **main content** now includes an image (`/static/globe1.jpeg`) displayed in a responsive manner, scaling according to the screen size.
- The **about-card** content describes the mission and purpose of **GLO-NEWS**:
  - It highlights that the platform brings users the latest global news articles and provides a summary of the site's functionality.
  - It also mentions that the platform is powered by **NewsAPI** and built using **Flask** for the backend and **Bootstrap** for the front end.

---

### **4. Footer**
- The footer in this page version includes a copyright notice specific to **GLO-NEWS 2025**.

---

### **Key Differences**
- **About Page Content**: This page explains the purpose of the **GLO-NEWS** platform, focusing on its mission to provide users with global news and describing its technical foundation (Flask and Bootstrap).
- **Styling**: New inline CSS has been added to give the **About** page a distinct design, including background color, card styling, and title enhancements.
- **Image**: A new image has been added to enhance the visual appeal of the page, making it more engaging for users.

___
___
___
## ``Creator.html``

This **"About the Creator"** page differs from the previous pages primarily in its focus on the developer behind the **GLO-NEWS** application. Unlike the homepage or the about page, which discuss the functionality and mission of the site, this page is dedicated to sharing the personal background and motivation of the creator, Chirag G C. It provides insight into their engineering background, passion for technology, and the creation of the platform.

In terms of similarity, the page maintains the same **background color** (`#e0f7f1`) and card design as the other pages to ensure consistency in the overall look and feel of the website. The layout also includes a **header** with navigation links and a **footer** with copyright information, similar to the structure used throughout the site.

___
____
___




### **Conclusion**

The **GLO-NEWS** project integrates **NewsAPI** with a user-friendly interface to deliver global news updates. Built with **Flask** and **Bootstrap**, it provides a responsive and dynamic experience.


The project showcases proficiency in Python and web development while creating a functional platform. With dedicated pages for news content and creator information, **GLO-NEWS** offers both utility and transparency. It highlights the importance of combining technical skills with thoughtful design in web development.

### **Thank you**

I would like to sincerely thank [CS50x](https://cs50.harvard.edu/x/) for giving me the opportunity to present my final project. I am also extremely grateful for providing this course for free. and truly appreciate the chance to showcase my work
