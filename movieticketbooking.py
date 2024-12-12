class VideoContent:
    def __init__(self, title, genre, showtimes):
        self.title = title
        self.genre = genre
        self.showtimes = showtimes

class Theater:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seats(self):
        for row in self.seats:
            print(' '.join(row))

def book_tickets(content, showtime, num_tickets):
    theater.display_seats()
    selected_seats = []
    for _ in range(num_tickets):
        row = int(input("Enter row number: ")) - 1
        seat = int(input("Enter seat number: ")) - 1
        if theater.seats[row][seat] == 'O':
            theater.seats[row][seat] = 'X'
            selected_seats.append((row, seat))
        else:
            print("Seat already booked. Please choose another seat.")
    print("Tickets booked successfully!")
    print(f"Content: {content.title} ({content.genre}), Showtime: {showtime}")
    print("Seats booked:")
    for row, seat in selected_seats:
        print(f"Row {row + 1}, Seat {seat + 1}")

if __name__ == "__main__":
    # Define movies and animes
    videos = [
        VideoContent("Money Heist", "Action", ["10:00 AM", "1:00 PM", "3:00 PM"]),
        VideoContent("Avengers", "Action", ["11:00 AM", "3:00 PM", "6:00 PM"]),
        VideoContent("The Jungle Book", "Family", ["6:00 PM", "9:00 PM"]),
        VideoContent("Naruto", "Anime", ["12:00 PM", "4:00 PM"]),
        VideoContent("Attack on Titan", "Anime", ["2:00 PM", "5:00 PM"]),
    ]
    
    theater = Theater(5, 10)

    print("Available Content:")
    genres = set()
    for idx, video in enumerate(videos, start=1):
        genres.add(video.genre)
    for genre in sorted(genres):
        print(f"\nGenre: {genre}")
        for idx, video in enumerate(videos, start=1):
            if video.genre == genre:
                print(f"{idx}. {video.title}")

    choice_type = input("Enter 'M' for Movie or 'A' for Anime: ").upper()
    if choice_type == 'M':
        video_type = "movie"
    elif choice_type == 'A':
        video_type = "anime"
    else:
        print("Invalid choice. Exiting.")
        exit()

    video_choice = int(input(f"Enter the {video_type} number: "))
    selected_video = videos[video_choice - 1]

    print(f"Available showtimes for {selected_video.title}:")
    for idx, showtime in enumerate(selected_video.showtimes, start=1):
        print(f"{idx}. {showtime}")

    showtime_choice = int(input("Enter the showtime you prefer: "))
    selected_showtime = selected_video.showtimes[showtime_choice - 1]

    num_tickets = int(input("Enter the number of tickets: "))
    book_tickets(selected_video, selected_showtime, num_tickets)