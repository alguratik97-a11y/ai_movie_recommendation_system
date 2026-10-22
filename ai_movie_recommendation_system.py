# AI Movie Recommendation System
# This system recommends movies based on user preferences (Genre and Mood)

def get_movie_recommendations(genre, mood):
    # Database of movies categorized by genre and mood
    movies_db = {
        "action": {
            "excited": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
            "relaxed": ["Spider-Man: Into the Spider-Verse", "Iron Man", "Avengers: Endgame"],
            "bored": ["Mission: Impossible - Fallout", "Die Hard", "The Dark Knight"]
        },
        "comedy": {
            "excited": ["Superbad", "The Hangover", "Step Brothers"],
            "relaxed": ["Paddington 2", "Toy Story", "Night at the Museum"],
            "bored": ["Free Guy", "Jumanji: Welcome to the Jungle", "Ghostbusters"]
        },
        "drama": {
            "excited": ["The Pursuit of Happyness", "Whiplash", "Rocky"],
            "relaxed": ["The Shawshank Redemption", "Forrest Gump", "The Green Mile"],
            "bored": ["Inception", "Interstellar", "The Prestige"]
        },
        "horror": {
            "excited": ["The Conjuring", "A Quiet Place", "IT"],
            "relaxed": ["Coraline", "Monster House", "Beetlejuice"],
            "bored": ["Get Out", "Hereditary", "Sinister"]
        }
    }
    
    genre = genre.lower().strip()
    mood = mood.lower().strip()
    
    if genre in movies_db and mood in movies_db[genre]:
        return movies_db[genre][mood]
    else:
        return ["Inception", "The Matrix", "Interstellar"]  # Default recommendations

def main():
    print("==================================================")
    print("      Welcome to the AI Movie Recommender!        ")
    print("==================================================")
    
    while True:
        print("\nAvailable Genres: Action, Comedy, Drama, Horror")
        genre = input("Enter your favorite movie genre (or type 'exit' to quit): ")
        
        if genre.lower() == 'exit':
            print("Enjoy your movies! Goodbye!")
            break
            
        mood = input("How are you feeling right now? (excited, relaxed, bored): ")
        
        recommendations = get_movie_recommendations(genre, mood)
        
        print("\n--- AI Recommended Movies For You ---")
        for i, movie in enumerate(recommendations, 1):
            print(f"{i}. {movie}")
        print("-------------------------------------")

if __name__ == "__main__":
    main()
