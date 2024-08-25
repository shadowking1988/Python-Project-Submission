from flask import Flask, render_template, request, flash
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def scrape_movies_by_genre(genre, max_movies=25):
    try:
        base_url = f"https://www.imdb.com/search/title/?title_type=feature&genres={genre.lower()}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        movies = []
        current_page = 1
        movies_per_page = 50

        while len(movies) < max_movies:
            start_index = (current_page - 1) * movies_per_page + 1
            url = f"{base_url}&start={start_index}&ref_=adv_nxt"
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            movie_items = soup.find_all('div', class_='sc-b189961a-0 iqHBGn')
            if not movie_items:
                break

            for movie in movie_items:
                title_tag = movie.find('h3', class_='ipc-title__text')
                if title_tag:
                    title = title_tag.text.strip().split('. ', 1)[-1]
                else:
                    title = 'N/A'

                year_tag = movie.find('span', class_='sc-b189961a-8 hCbzGp dli-title-metadata-item')
                year = year_tag.text.strip() if year_tag else 'N/A'

                rating_tag = movie.find('span', class_='ipc-rating-star--rating')
                rating = rating_tag.text.strip() if rating_tag else 'N/A'

                
                metascore_tag = movie.find('span', class_='sc-b0901df4-0 bXIOoL metacritic-score-box')
                metascore = metascore_tag.text.strip() if metascore_tag else 'N/A'

                movies.append({'Title': title, 'Year': year, 'Rating': rating, 'Metascore': metascore})

                if len(movies) >= max_movies:
                    break

            current_page += 1

        return movies

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from IMDb: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    movies = []
    genre = ""
    if request.method == "POST":
        genre = request.form.get("genre")
        movies = scrape_movies_by_genre(genre)
        if not movies:
            flash("No movies found for the given genre. Please try again with a different genre.", "error")

    return render_template("index.html", movies=movies, genre=genre.capitalize())

if __name__ == "__main__":
    app.run(debug=True)