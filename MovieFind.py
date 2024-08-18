import requests

def get_movie_info(movie_name):
    api_key = "29e67efc"  # Replace with your OMDb API key
    base_url = "http://www.omdbapi.com/"
    
    params = {
        "t": movie_name,  # Search by movie title
        "apikey": api_key
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return data
        else:
            return f"Error: {data['Error']}"
    else:
        return f"Error: Unable to connect to the OMDb API (Status code: {response.status_code})"

def main():
    movie_name = input("Enter the name of the movie: ")
    movie_info = get_movie_info(movie_name)
    
    if isinstance(movie_info, dict):
        # Pretty-print the movie information
        for key, value in movie_info.items():
            print(f"{key}: {value}")
    else:
        print(movie_info)

if __name__ == "__main__":
    main()
