# a Python object (dict):
song_db = [{
  "id": 1,
  "artist": "John",
  "year": 2020,
  "title": "whatever", 
  "lyrics": "I went to the store yesterday and bought some shoes...."
}, 
{
  "id": 2,
  "artist": "Alicia",
  "year": 2018,
  "title": "beaches", 
  "lyrics": "Hello world, this is my first album, hope you like it..."
},
{
  "id": 3,
  "artist": "Paul",
  "year": 2022,
  "title": "icecream", 
  "lyrics": "Icecream is my favorite in summer...."
}]


# test: given a keyword: favorite, return title - artist , Icecream - Paul 
# def searchByLyrics... 
# def searchByLyrics(keyword):
#     for song in song_db: 
#         if keyword in song["lyrics"]:
#             return f"{song['title']} - {song['artist']}"
    
#     return "No result matched."

# print(searchByLyrics("album"))
