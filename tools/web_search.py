from serpapi import GoogleSearch
from config.settings import SERP_API_KEY


def web_search(query: str):

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    organic_results = results.get("organic_results", [])

    if not organic_results:
        return "No results found."

    output = ""

    for i, result in enumerate(organic_results[:5], start=1):

        title = result.get("title", "")
        snippet = result.get("snippet", "")
        link = result.get("link", "")

        output += (
            f"{i}. {title}\n"
            f"{snippet}\n"
            f"{link}\n\n"
        )

    return output