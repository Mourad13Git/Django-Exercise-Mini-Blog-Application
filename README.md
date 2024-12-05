# Django Mini Blog Application

This is a **Mini Blog Application** built using **Django**. The project demonstrates basic CRUD (Create, Read, Update, Delete) operations for blog posts and comments, and it follows the **Model-View-Template (MVT)** architecture.

### **Main Idea of the Project**
The Mini Blog Application allows users to:
- **Create**, **view**, **edit**, and **delete blog posts**.
- **Add**, **edit**, and **delete comments** for blog posts.
- All actions are performed through a simple, user-friendly web interface, which follows good practices for web application development.

### **Project Structure**
The project is divided into the following components:

1. **Models**:
   - **BlogPost**:
     - Fields:
       - `title`: Title of the blog post (CharField, max length: 100).
       - `content`: Content of the blog post (TextField).
       - `created_at`: Timestamp when the blog post was created (DateTimeField, auto_now_add=True).
     - The `__str__` method returns the title of the blog post.
   - **Comment**:
     - Fields:
       - `post`: A ForeignKey to `BlogPost` (to link comments to a post).
       - `author`: The name of the comment author (CharField, max length: 50).
       - `text`: The content of the comment (TextField).
       - `created_at`: Timestamp when the comment was created (DateTimeField, auto_now_add=True).
     - The `__str__` method returns a truncated version of the comment text.

2. **Views**:
   The views handle the logic for rendering templates and performing actions on the blog posts and comments:
   - **List Blog Posts**: Displays a list of all blog posts.
   - **View Blog Post Details**: Displays a single blog post along with its comments.
   - **Create Blog Post**: A form to create a new blog post.
   - **Edit Blog Post**: A form to edit an existing blog post.
   - **Delete Blog Post**: Confirms and deletes a specific blog post.
   - **Add Comment to Blog Post**: A form to add a comment to a blog post.
   - **Edit Comment**: A form to edit an existing comment.
   - **Delete Comment**: Confirms and deletes a specific comment.

3. **Templates**:
   All pages are built with HTML templates that extend a common `base.html` file. These templates include:
   - A navigation bar with links to create posts and view the list of posts.
   - Buttons for editing, viewing, and deleting posts and comments.

4. **URLs**:
   The project includes URL routing to map views to specific URLs:
   - `/` — List of blog posts.
   - `/post/<id>/` — Blog post detail page.
   - `/post/create/` — Page to create a new blog post.
   - `/post/<id>/edit/` — Edit an existing blog post.
   - `/post/<id>/delete/` — Delete a specific blog post.
   - `/post/<id>/add_comment/` — Add a comment to a blog post.
   - `/comment/<id>/edit/` — Edit an existing comment.
   - `/comment/<id>/delete/` — Delete a specific comment.

### **Technologies Used**
- **Django**: A high-level Python web framework for rapid development.
- **SQLite**: Used as the database for storing blog posts and comments.
- **Bootstrap**: For responsive and simple UI design.
- **Git**: For version control and collaboration.

### **How to Run the Project Locally**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Django-Exercise-Mini-Blog-Application.git
