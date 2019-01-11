Script that goes through all youtube clips in specified playlist and saves their titles into file

## Usage

```python
# username and password are mandatory. Provide them only if you plan to scrape private playlists
# output is also mandatory. if not provided file will save in folder containing the python file

save_youtube_playlist_titles_in_file.py -username "username@gmail.com" -password "password" -playlist "playlist url"

save_youtube_playlist_titles_in_file.py -playlist "playlist url"

save_youtube_playlist_titles_in_file.py -username "username@gmail.com" -password "password" -playlist "playlist url" -output "C:/output/path/scrapped_videos.txt"
```
