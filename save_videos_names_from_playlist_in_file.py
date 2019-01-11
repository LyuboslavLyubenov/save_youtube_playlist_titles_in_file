#! /usr/bin/env python
import argparse
import youtube_dl


def run(args):
    username = args.username
    password = args.password
    playlist = args.playlist
    output_path = args.output_path

    ydl = youtube_dl.YoutubeDL({
        'username': username,
        'password': password,
        'ignoreerrors': True
    })

    with open(output_path, 'w') as file:
        with ydl:
            playlist_videos = ydl.extract_info(playlist, download=False)

            for video in playlist_videos['entries']:
                if not video:
                    continue

                title = video.get('title')

                if not title or len(title) == 0:
                    continue

                file.write(title + '\n')
                file.flush()


def main():
    parser = argparse.ArgumentParser(description='Saves titles from playlist in youtube in file (default videos.txt in same directory as this python script)')
    parser.add_argument('-username', help='youtube email', dest='username', type=str)
    parser.add_argument('-password', help='youtube password', dest='password', type=str)
    parser.add_argument('-playlist', help='playlist you want to scrape', dest='playlist', type=str, required=True)
    parser.add_argument('-output', help='output file path', dest='output_path', type=str, default='./videos.txt')
    args = parser.parse_args()
    run(args)

if __name__ == '__main__':
    main()
o
