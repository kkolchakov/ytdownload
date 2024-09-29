
import subprocess
#import settings
def module_update(module):
    try:
        subprocess.run(['pip', 'install', '--upgrade', '--upgrade-strategy', 'only-if-needed', module])
    except Exception:
        print(f'Unable to update {module}!')
        
def video_download(url):

    subprocess.run(['yt-dlp','-f','bv*[height=1080]+ba', url, '-o','%(playlist_index)s -%(title)s.%(ext)s'])
    print('Finished downloading your video!')

def audio_download(url):

    subprocess.run(['yt-dlp','-x', '--audio-format', 'mp3', url])
    print("Finished downloading your audio file!")


if __name__ == '__main__':
    l = True
    module_update('yt-dlp)
    while l:
        url = input('Enter url:  ')
        choice = input('Enter a-audio/v-video/c-cancel:   ')

        if choice == 'a':
            audio_download(url)
        elif choice == 'v':
            video_download(url)

        elif choice =='c':
            break
        else:
            print('Enter valid choice!')

        choice = input('Exit? (y/n)\t')
        if choice == 'y':
            l = False

