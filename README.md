# yt-playlist-scraper

1. Set up a virtual enviroment 

   ```bash
   python3 -m venv youtube_crawler_env
   source youtube_crawler_env/bin/activate  
   # On Windows, use `youtube_crawler_env\Scripts\activate`
   ```

2. Install the required libraries
   ```bash
   pip install google-api-python-client python-dotenv
   ```

3. Work on the crawler.py

4. Set up a Youtube Data API project:
   1. Go to the [Google Developers Console](https://console.cloud.google.com/cloud-resource-manager).
   2. Create a new project or select an existing one.
   3. Enable the YouTube Data API v3 for your project.
   4. Create credentials (`API Key`) for your project.
   
5. Create a .env file in the same directory as the crawler.py and add the `API key`:
   ```env
   YOUTUBE_API_KEY=<your_api_key_here>
   ```

6. When prompted, enter the YT playlist ID. For example the playlist ID for below URL is `PL4H-lo93TJHYwQ2RjaWTIf1CO923DiC82`
   ```
   https://www.youtube.com/playlist?list=PL4H-lo93TJHYwQ2RjaWTIf1CO923DiC82
   ```

## Note: Youtube Data API (v3)

注意這個 API 有些函式需要付費 
 [Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)

目前用到 `playlistItems.list()` 以及 `videos.list()`