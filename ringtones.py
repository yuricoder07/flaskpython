import random
import pytube
link_data = []
links = ["https://www.youtube.com/watch?v=St6eQnpjSGY",
"https://www.youtube.com/watch?v=Sv8LHpezbLw",
"https://www.youtube.com/watch?v=5LCvj6Z_LrA",
"https://www.youtube.com/watch?v=10y2X-WNSrc", 
"https://www.youtube.com/watch?v=VDvFcn6icXo" 
]
def main():
    for i in links:
        pytube.YouTube(i).streams.filter(file_extension="mp3").first()