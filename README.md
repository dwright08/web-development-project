# Mid-Course Project: Web Development

In this project, you'll practice these concepts from your lessons:

* Basic HTTP and API concepts, including:
   * Different types of HTTP requests: GET, POST, PATCH, DELETE
   * Understanding the ideas of Requests and Responses
   * The JSON data format
* Using API browsing software such as Insomnia
* Using the Flask library to create an API
* Using the Flask library to create a Web app
* Writing routes in Flask
* Understanding of the RESTful routes and the importance of each route
* Flask templates
   * Basic HTML
   * Programmable logic and control flow in templates
* File I/O
   * CSV Files

You can choose to work on the project individually or with a partner, but each person must turn in their own work.

## Deliverables and Submitting

You know what you're doing by now! **Make a Copy from the Template**/**Clone**/**Commit**/**Push**/**Submit** :grin:

---

# Exercise 1: Make an API!

The idea of this exercise is simple.

*Re-do* the **API Development with Flask** lesson -- Write an API!

> Do your work in the existing `exercise_1_api/server.py` file

But, instead of keeping track of Movies, keep track of another idea of your own choosing!

* Music
* Cat
* Dog

Whatever concept you choose, make sure it has 3-5 **fields**. For example:

* If you are managing a music collection, you might want to keep track of the following for each album:
   * Name (e.g. "Nevermind")
   * Artist (e.g. "Nirvana")
   * Year (e.g. 1991)

* If you're herding cats or dogs, you might keep track of the following for each cat:
   * Name (e.g. "Cora")
   * Breed (e.g. "Abyssinian" or "N/A")
   * Age (e.g. 3)

* You get the idea!

Replicate all of the RESTful routes that we covered in class.

| Action Name | Method | Path | Purpose | 
| --- | --- | --- | --- |
| **index** | **GET** | `/cats` | Shows a list of this collection |
| **show** | **GET** | `/cats/<id>` | Show details of a specific item |
| **create** | **POST** | `/cats` | Add a new item to the collection |
| **update** | **PATCH** | `/cats/<id>` | Update details of a specific item |
| **delete** | **DELETE** | `/cats/<id>` | Delete a specific item |

## Hints

* We've emphasized throughtout the course the importance of data types and recognizing the type of data you're working with.
   * Be **very aware** at all times what **type of data** (i.e. **data type**) you are dealing with at any moment. Is it a string? An integer? A dictionary? A list? A list of what?
   * Keep this in mind for the entirety of exercise 1 and exercise 2


* Make sure your Exercise 1 is working well before moving on to Exercise 2

---

# Exercise 2: Make a Web App!

In the second exercise, you will now write a web app version of what you did in Exercise 1.

This web app will now allow users to look at your data on a web page!

## Goal 1: Minimum Requirements

* To Start:
   * Start from the API app you made in Exercise 1
   * Copy the contents of your `exercise_1_api/server.py` into `exercise_2_webapp/server.py`
* Start with your **index** route
   * Add an `index.html` file in the `templates` folder for the HTML template for this route
   * Update your `index` route to render this template instead of returning JSON data
   * Write the appropriate HTML in the template to show all items on the web page
   * Including links to each individual item's details page 
* Continue with your **show** route
   * Add a `show.html` HTML template file in the `templates` folder
   * Update your `show` route to render this template instead of returning JSON data
   * Show the details of just one of the items in the show template
* Make sure your **create**, **update**, and **delete** routes still work
   * These routes do not require HTML templates
   * Be sure to test these routes using POST, PATCH, and DELETE requests with Insomnia
   * Make sure the newly added/edited/deleted data is reflected when you visit the **index** route and the **show** route for those particular records

At this point your web app should alow your user to CREATE, READ, UPDATE, and DELETE data!

Make sure all of that is working before you proceed to the next goal.

## Goal 2: Pull Data from a CSV File

You may have noticed that whenever you stop and restart your server, you lose all the changes to the data! That's a pretty bad problem. What you need is **persistent storage**.

In real life programs, we would use a **database** to store data permanently. That's out of the scope of this course, but we'll use something already familiar to you to make a "poor man's database": a CSV file!

Using a CSV file for persistent storage will allow your data to survive restarts of the program.

* Add some starting data into the blank `data.csv` file.
   * Write one row for the column names
   * Then, add a few rows of data, as "seed data" for use while developing your program
   * Recall that CSV files are formatted like this:

   ```csv
   id,name,age,cuteness
   1,Cora,4,10
   2,Mittens,3,9
   3,Felix,2,8
   ```

* Now, instead of hard-coding the data, **load** the contents of the CSV file into your variable that's holding the data
   * You should probably write a function to read the data from the CSV file and load it into your variable

   * Instead of:

   ```python
   cats = [
     { 'id': '1', 'name': 'Cora', 'age': 4 },
     { 'id': '2', 'name': 'Mittens', 'age': 3 },
     { 'id': '3', 'name': 'Felix', 'age': 2 }
   ]
   ```

   * Now you can just start with an empty list:

   ```python
   cats = []
   ```

   * Now that you have an empty list to start with, what should your function do with each row of data it reads from the csv file?
   * Remember that when you read data from a `csv` file, the data is always a string!

* Once you have succeeded in loading the data from the CSV file, when you start up your app, your **index** and **show** routes should be showing the data you have in the CSV file! You shouldn't have to mess with these routes at all.
   * Try updating the CSV file manually with more rows, and when you restart your app, you should see the data reflected in your **index** and **show** routes

* Make sure that your **create**, **update**, and **delete** routes are still working like before -- but notice that they do not affect the contents of the CSV file. Of course not, we haven't written the code for that yet!

## Goal 3

* Update your **create** route so that the new record that the user creates is saved to the CSV file
* You will have to write a function that **appends** a line of data the CSV file
* Be sure to test your route using Insomnia once you're done to make sure that it still works
* Check that the new line is appended to the CSV file!

## (STRETCH) Goal 4

* **Hint:** If you are doing the stretch goals of the **delete** and **update** routes, beware that it is much more difficult to synchronize data to a `csv` file with these routes. It'll be a challenge!
   * `csv` files are not meant for you to be able to easily access just one specific row -- so don't try to do that. Instead, you'll have to *overwrite* the **entire file** whenever you intend to update or delete a row!
      * You will likely have to implement an additional function to write data to the CSV file
   * (This is one of the problems that databases are meant to solve, something that you can learn in the future!)

* Update the **delete** route that allows users to delete a certain record (as specified by an `id`)
   * Update the route to remove the specific line from the CSV file
   * This route should accept a DELETE request
   * This route does not require an HTML template
   * Make sure that records that don't exist are not deleted!
   * Be sure to test your route using Insomnia

* Update the **update** route that allows users to update a certain record (as specified by an `id`)
   * Update the route to 
   * This route should accept a PATCH request with the new data in JSON format
   * This route does not require an HTML template
   * Make sure that records that don't exist are not updated!
   * Be sure to test your route using Insomnia

## (STRETCH) Goal 5

* Add error handling to the **create** and **update** routes, so that users cannot create/update records with invalid data
   * For example, quantities should be positive integers, not strings
   * Recall that the status code typically used to indicate this sort of situation is [422 - Unprocessable Entity](http://http.cat/422)

## Hints

* Not a strict requirement, but just to make sure you're not going off the deep end:
   * You should be able to accomplish the minimum requirements of Goals 1-3 in less than 75 lines of code
   * If you're doing the stretch goals 4-5, you should be able to accomplish everything in less than 100 lines of code total

---

# Epic Work

You've just created a very nice API and web app!

![](https://media.giphy.com/media/wepUQluC5smgEd4Qz4/giphy.gif)
