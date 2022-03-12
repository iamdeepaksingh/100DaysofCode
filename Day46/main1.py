import spotipy
from spotipy.oauth2 import SpotifyOAuth

YOUR_UNIQUE_CLIENT_ID = 'to be entered'

CLIENT_SECRET = 'to be entered'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_UNIQUE_CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

url = http://example.com/?code=AQBUMtJan3A6wupxG8QK2HK71VQ3qwyCG4LTjTHVddLP5uEH3DfcNEOeUQGRHTCwGwLyZv6bUICCsj56l4osT8MVHK3uhMjcFc_vQtl8hWen6gcciSk-UAXCLTlHQt7XIm3e5Qj1R69sZxAu-j66l_HiuwfZkQFH132P283EK1IQcP7LzYbJ2PpnbEC0wao