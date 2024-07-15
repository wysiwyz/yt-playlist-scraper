import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# YouTube API setup
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def get_playlist_videos(playlist_id):
    videos = []
    next_page_token = None

    while True:
        playlist_request = youtube.playlistItems().list(
            part='snippet,contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()

        for item in playlist_response['items']:
            video_id = item['contentDetails']['videoId']
            video_request = youtube.videos().list(
                part='snippet,contentDetails',
                id=video_id
            )
            video_response = video_request.execute()

            video = video_response['items'][0]
            title = video['snippet']['title']
            duration = video['contentDetails']['duration']
            url = f"https://www.youtube.com/watch?v={video_id}"

            videos.append({
                'title': title,
                'duration': duration,
                'url': url
            })

        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break

    return videos

def main():
    playlist_id = input("Enter the YouTube playlist ID: ")
    videos = get_playlist_videos(playlist_id)

    for video in videos:
        print(f"Title: {video['title']}")
        print(f"Duration: {video['duration']}")
        print(f"URL: {video['url']}")
        print("---")

if __name__ == "__main__":
    main()