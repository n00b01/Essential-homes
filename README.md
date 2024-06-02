# Essential-homes
It is a Flask web application for managing real estate listings, feedback, and bookings.
The app.py file is a Flask web application for managing real estate listings, feedback, and bookings, connecting to a MySQL database (essential home). It provides routes for displaying homes (/index), logging out (/logout), submitting and viewing feedback (/feedback and /testimonial), and managing properties (/admin and /addproperty). Users can view booking details for specific properties (/bookings/<property_id>) and submit booking requests (/booking). The app uses HTML templates for rendering pages and includes session management with a secret key.


## The program should: 
The provided Python file is a web application built using the Flask framework. Here is a concise description of its functionality:

1. **Basic Configuration**:
   - Sets up the Flask application with a secret key for session management.
   - Connects to a MySQL database using the `pymysql` library.

2. **Routes**:
   - **`/index`**: Displays the homepage with a list of homes fetched from the database.
   - **`/logout`**: Clears the session and redirects to the index page.
   - **`/feedback`**: Handles feedback form submissions. Saves feedback to the database if the request method is POST, and displays the feedback form otherwise.
   - **`/testimonial`**: Displays testimonials (feedback) fetched from the database.
   - **`/upload`**: Handles property upload. Saves property details to the database if the request method is POST, and displays the upload form otherwise.
   - **`/bookings/<property_id>`**: Displays booking details for a specific property.
   - **`/booking`**: Handles booking form submissions. Saves booking details to the database if the request method is POST, and displays the booking form otherwise.

3. **Database Operations**:
   - Connects to a local MySQL database (`essentialhome`) for various CRUD operations like fetching homes, inserting feedback, uploading properties, and booking properties.

4. **Templates**:
   - Uses HTML templates (`index.html`, `feedback.html`, `testimonial.html`, `upload.html`, `booking.html`) for rendering web pages.

5. **SMS Integration**:
   - Imports a custom `send_sms` module (though its usage is not evident in the provided code).

The application serves as a platform for managing home listings, feedback, and bookings.

Attributes to **Greg Enos** | `@n00b01`
