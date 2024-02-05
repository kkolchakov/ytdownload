
import subprocess
#import settings

def video_download(url):

    subprocess.run(['yt-dlp','-f','bv*[height=1080]+ba', url, '-o','%(playlist_index)s -%(title)s.%(ext)s'])
    print('Finished downloading your video!')

def audio_download(url):

    subprocess.run(['yt-dlp','-x', '--audio-format', 'mp3', url])
    print("Finished downloading your audio file!")


if __name__ == '__main__':
    l = True
    url = input('Enter url:  ')
    while l:

        choice = input('Enter a-audio/v-video/c-cancel:   ')

        if choice == 'a':
            audio_download(url)
        elif choice == 'v':
            video_download(url)

        elif choice =='c':
            break
        else:
            print('Enter valid choice!')

