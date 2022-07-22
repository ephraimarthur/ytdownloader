#import pytube
import pytube

link = input("Enter Youtube video url")
yt = pytube.YouTube(link)

#download the link
yt.streams.first().download()

#print outpude result
print("Downloaded", link)
