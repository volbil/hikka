# ToDo: Split into multiple files


# Auth
def request_signup(client, email, username, password):
    return client.post(
        "/auth/signup",
        json={"email": email, "username": username, "password": password},
    )


def request_login(client, email, password):
    return client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )


def request_activation(client, token):
    return client.post(
        "/auth/activation",
        json={"token": token},
    )


def request_activation_resend(client, email):
    return client.post(
        "/auth/activation/resend",
        json={"email": email},
    )


def request_password_reset(client, email):
    return client.post(
        "/auth/password/reset",
        json={"email": email},
    )


def request_password_confirm(client, token, new_password):
    return client.post(
        "/auth/password/confirm",
        json={"token": token, "password": new_password},
    )


# Oauth
def request_oauth_url(client, provider):
    return client.get(f"/auth/oauth/{provider}")


def oauth_post(client, provider, code=None):
    data = {"code": code} if code else {}

    return client.post(
        f"/auth/oauth/{provider}",
        json=data,
    )


# User
def request_me(client, token):
    return client.get(
        "/user/me",
        headers={"Auth": token},
    )


def request_profile(client, username):
    return client.get(f"/user/{username}")


# Follow
def request_follow_check(client, token, username):
    return client.get(
        f"/follow/{username}",
        headers={"Auth": token},
    )


def request_follow(client, token, username):
    return client.put(
        f"/follow/{username}",
        headers={"Auth": token},
    )


def request_unfollow(client, token, username):
    return client.delete(
        f"/follow/{username}",
        headers={"Auth": token},
    )


def request_follow_stats(client, username):
    return client.get(f"/follow/{username}/stats")


def request_following(client, username):
    return client.get(f"/follow/{username}/following")


def request_followers(client, username):
    return client.get(f"/follow/{username}/followers")


# Anime
def request_anime_search(client, filters={}):
    return client.post("/anime", json=filters)


def request_anime_genres(client):
    return client.get("/anime/genres")


def request_anime_info(client, slug):
    return client.get(f"/anime/{slug}")


def request_anime_characters(client, slug, page=1):
    return client.get(f"/anime/{slug}/characters?page={page}")


def request_anime_staff(client, slug):
    return client.get(f"/anime/{slug}/staff")


def request_anime_episodes(client, slug, page=1):
    return client.get(f"/anime/{slug}/episodes?page={page}")


def request_anime_recommendations(client, slug):
    return client.get(f"/anime/{slug}/recommendations")


def request_anime_franchise(client, slug):
    return client.get(f"/anime/{slug}/franchise")


# Characters
def request_characters_search(client, filters={}):
    return client.post("/characters", json=filters)


def request_characters_info(client, slug):
    return client.get(f"/characters/{slug}")


def request_characters_anime(client, slug):
    return client.get(f"/characters/{slug}/anime")


# Companies
def request_companies_list(client, filters={}):
    return client.post("/companies", json=filters)


def request_companies_info(client, slug):
    return client.get(f"/companies/{slug}")
