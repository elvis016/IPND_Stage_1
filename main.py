# import os library to enable path function
import os
# import jinja library to enable html template
import jinja2
# import webapp2 to enable Google App Engine
import webapp2


# Define directory of HTML templates
html_dir = os.path.join(os.path.dirname(__file__), "html")

# Setup JinJa environment
# Use JinJa built-in function, autoescape = Ture instead of cgi.escape function
# Prevents unintended HTML code from rendering on the browser,
# stopping malicious users from abusing the site.
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(html_dir),
    autoescape = True)

# Define class Handler for write and render the page
# self.response.out.write("hello world")
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        # render index.html
        # pass variables to html file
        self.render("index.html")

app = webapp2.WSGIApplication([
    ("/.*", MainPage)
], debug=True)
