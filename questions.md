## Answer Sheet: Lab09

**Question 1:** What is the purpose of the `@app.route('/health')` decorator in the code?

**Answer:**
it binds a URL path (/health) to the view function that follows it.



----------------
**Question 2:** In Jinja2, what is the difference between `{{ my_variable }}` and `{% for item in my_list %}`?

**Answer:**
`{{ my_variable }}` is print the value of my_variable, while the `{% for item in my_list %}` is making `item` to pass the whole list of my_list and get the value.
(Print and Logic) 


----------------
**Question 3:** In `app.py`, why is it important to use `(?, ?)` and pass the variables as a tuple in the `conn.execute()` command instead of using f-strings to put the variables directly into the SQL string? What is this technique called?

**Answer:**

Why:If I use f'{}', and the input name is koil' rather koil, then whole string will become f"INSERT INTO messages ({koil'}, message) VALUES ", which is be divide into two string.

Called:SQL Parameter Binding




----------------
**Question 4:** What is the purpose of `event.preventDefault()` in the JavaScript code? What would happen if you removed that line?

**Answer:**
it stops the browser from executing the default behavior of the form's submit event.

If we remove it:
The form data would be sent to the server twice, and reload the page rapidly.



----------------
**Question 5:** In the `Dockerfile`, why is the `CMD` `["flask", "run", "--host=0.0.0.0"]` necessary? Why wouldn't the default `flask run` (which uses host 127.0.0.1) work?

**Answer:**




----------------
**Question 6:** In the `docker-compose.yml` setup, Nginx is configured to `proxy_pass http://flask-app:5000`. How does the Nginx container know the IP address of the `flask-app` container?

**Answer:**



