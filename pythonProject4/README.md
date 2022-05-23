# Django_Views_URLs_Templates

# Task#1

Update your Movie website to have a splash page that welcomes users and lets them know what site they are on.

## These steps will help you complete your task:
- In your index view, render the base.html template.
- Update the base.html template to contain the welcome message. It should be in both the tag in \<head> and in a new \<h1> tag in the body.


# Task#2

A useful feature for a site like Movies is the ability to search through the data to find something on the site quickly. You need to implement movie searching, to allow users to find a particular movie by part of its title. While we don't have any movies to find yet, we can still implement a page that shows the text the user searched for. The user enters the search string as part of the URL parameters.


## These steps will help you complete your task:
- Create a search result HTML template. It should include a variable placeholder to show the search word(s) that were passed in through the render context. Show the passed-in variable in the and \<h1> tags. Use an \<em> tag around the search text in the body to make it italic.
- Add a search view function in views.py. The view should read a search string from the URL parameters (in the request's GET attribute). It should then render the template you created in the previous step, passing in the search value to be substituted, using the context dictionary.
- Add a URL mapping to your new view to urls.py. The URL can be something like /movies-search.
