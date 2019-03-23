# Semi-Restful TV Shows
In this assignment from Coding Dojo I will be further practicing Django routing
and trying to meet RESTful naming conventions of my routes for a full CRUD application.

Updated on 3/23 to add validation to models and error messaging to create/edit show pages.

Routes:
* /shows - GET - method should return a template that displays all the shows in a table
* /shows/new- GET - method should return a template containing the form for adding a new TV show
* /shows/create - POST - method should add the show to the database, then redirect to /shows/<id>
* /shows/<id> - GET - method should return a template that displays the specific show's information
* /shows/<id>/edit - GET - method should return a template that displays a form for editing the TV show with the id specified in the url
* /shows/<id>/update - POST - method should update the specific show in the database, then redirect to /shows/<id>
* /shows/<id>/destroy - POST - method should delete the show with the specified id from the database, then redirect to /shows
* / - GET - Root route redirects to /shows
