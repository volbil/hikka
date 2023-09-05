from client_requests import request_anime_search
from fastapi import status

# score
# media_type
# rating
# status
# source
# season
# producers
# studios
# genres


async def test_anime_filter_sort(client, aggregator_anime):
    # Check for desc sort
    response = await request_anime_search(client, {"sort": ["score:desc"]})

    assert response.status_code == status.HTTP_200_OK

    assert (
        response.json()["list"][0]["score"]
        > response.json()["list"][11]["score"]
    )

    # Check for asc sort
    response = await request_anime_search(client, {"sort": ["scored_by:asc"]})

    assert response.status_code == status.HTTP_200_OK

    assert (
        response.json()["list"][0]["scored_by"]
        < response.json()["list"][11]["scored_by"]
    )

    # Check for bad sort field
    response = await request_anime_search(client, {"sort": ["bad_field:asc"]})

    assert response.json()["code"] == "validation_error"
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Check for bad sort value
    response = await request_anime_search(client, {"sort": ["scored_by:bad"]})

    assert response.json()["code"] == "validation_error"
    assert response.status_code == status.HTTP_400_BAD_REQUEST


async def test_anime_filter_years(client, aggregator_anime):
    # Check year range between 2010 and 2018
    response = await request_anime_search(client, {"years": [2010, 2018]})

    assert response.status_code == status.HTTP_200_OK

    min_year_anime = min(response.json()["list"], key=lambda x: x["year"])
    max_year_anime = max(response.json()["list"], key=lambda x: x["year"])

    assert min_year_anime["year"] >= 2010
    assert max_year_anime["year"] <= 2018

    # Check year range between 2020 and 2023 (just in case)
    response = await request_anime_search(client, {"years": [2020, 2023]})

    assert response.status_code == status.HTTP_200_OK

    min_year_anime = min(response.json()["list"], key=lambda x: x["year"])
    max_year_anime = max(response.json()["list"], key=lambda x: x["year"])

    assert min_year_anime["year"] >= 2020
    assert max_year_anime["year"] <= 2023

    # Check for bad year placement
    response = await request_anime_search(client, {"years": [2023, 2020]})

    assert response.json()["code"] == "validation_error"
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Check for negative value
    response = await request_anime_search(client, {"years": [None, -1]})

    assert response.json()["code"] == "validation_error"
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# async def test_anime_filter_score():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_media_type():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_rating():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_status():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_source():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_season():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_producers():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_studios():
#     response = await request_anime_search(client, {})


# async def test_anime_filter_genres():
#     response = await request_anime_search(client, {})