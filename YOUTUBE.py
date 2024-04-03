import requests
import webbrowser

def search_youtube(query):
    api_key = "AIzaSyBVyQs45hXYtLY9LbD7e3-G5WjgzJidcec"
    URL = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&type=video&q={query}&maxResults=20"
    
    req = requests.get(URL)
    
    if req.status_code == 200:
        dados_recebidos = req.json()
        for item in dados_recebidos["items"]:
            video_id = item["id"]["videoId"]
            video_title = item["snippet"]["title"]
            print(f"Title: {video_title}, Video ID: {video_id}")
        
        video_id_to_watch = input("Digite o ID do vídeo que deseja assistir: ")
        watch_url = f"https://www.youtube.com/watch?v={video_id_to_watch}"
        webbrowser.open(watch_url)
    else:
        print(f"A solicitação falhou com o código de status: {req.status_code}")

def main():
    search_query = input("Digite o que você deseja pesquisar no YouTube: ")
    search_youtube(search_query)

if __name__ == "__main__":
    main()