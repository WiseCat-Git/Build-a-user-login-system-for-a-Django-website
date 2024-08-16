# Build-a-user-login-system-for-a-Django-website

# Project Objectives:

# User Authentication & Registration:

# Objective: 

Implement a secure user authentication and registration system.

# Approach:

We created a custom user model using Django's AbstractUser to allow flexibility for future enhancements.

The UserRegisterForm was implemented using Django's UserCreationForm to handle the registration process, capturing usernames, emails, and passwords.

Integrated Django's built-in authentication views (LoginView, LogoutView) for handling login and logout processes.

Added a thank you page that users are redirected to after a successful registration.

# Homepage Access Control:

# Objective: 

Restrict access to the homepage to authenticated users only.

# Approach:

Implemented a home view decorated with Django's login_required to ensure only logged-in users can access the homepage.

Configured URL routing to direct users to the login page if they attempt to access the homepage without authentication.

# User Interface & Feedback:

# Objective: 

Provide a user-friendly interface with feedback for user actions.

# Approach:

Designed simple, clean HTML templates with basic CSS for the registration, login, and homepage views.

Integrated Django's messaging framework to display success messages after user registration.

Ensured the thank you page is properly linked and displayed upon successful registration.

# Additional Note:

The registration is successful with alphanumeric passwords, but the app crashes when using numeric-only passwords like "12345."
