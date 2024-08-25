## IMDB Movie Scraper

IMDB Movie Scraper is a web application built with Flask that allows users to search for movies by genre. The application scrapes movie data from IMDB and displays the top 25 movies for the specified genre, including the title, year, rating, and metascore.

## Features

- Search by Genre: Users can search for movies by entering a genre (e.g., action, comedy, drama).
- Top 25 Movies: The application displays the top 25 movies for the specified genre.
- Dynamic Title: The title on the results page reflects the genre searched by the user (e.g., "Top 25 Action Movies”).
- Error Handling: The application handles invalid genre inputs and displays user-friendly error messages.
- User-Friendly Interface: Built with Bootstrap, the application provides a clean and responsive user interface.

## Technologies Used

### Backend

- Flask: A lightweight WSGI web application framework in Python used to build the web server.
- BeautifulSoup: A Python library used for web scraping to extract movie data from IMDB.
- Requests: A simple, yet powerful HTTP library for making API requests to fetch movie data.

### Frontend

- HTML5: The standard markup language used to structure the web page content.
- Bootstrap: A popular CSS framework for developing responsive and mobile-first web pages.
