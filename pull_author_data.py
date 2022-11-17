import requests
import os
import json
import time

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url(next_token: str, iteration: int):
    tweet_fields = "tweet.fields=author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,public_metrics,referenced_tweets,reply_settings,source,text&user.fields=created_at,description,entities,id,location,name,public_metrics,username"
    start_time = 'start_time=2020-11-04T00:00:00.000Z'
    end_time = 'end_time=2020-11-14T00:00:00.000Z'
    if iteration == 0:
        url = "https://api.twitter.com/2/tweets/search/all?query=dominion%20voting%20maricopa&{}&{}&{}&max_results=100".format(start_time, end_time, tweet_fields)
    else:
        url = "https://api.twitter.com/2/tweets/search/all?query=dominion%20voting%20maricopa&{}&{}&{}&max_results=100&next_token={}".format(start_time, end_time, tweet_fields, next_token)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    authors = open("authors.txt", "r")
    data = authors.read()
    data_into_list = data.replace('\n', ' ').split(".")
    print(data_into_list)
    authors.close()

    # count = 0
    # for i in range(1, 3500, 10):
    #     ids = ids[i:i+10]
    #     ids = str(ids).replace(" ", "")[1:-1]
    #     url = create_url(None, count, ids)
    #     print(url)
    #     json_response = connect_to_endpoint(url)
    #     json_object = js.dumps(json_response, indent=4, sort_keys=True)

    #     filename = f"response{count}_user.json"
    #     with open(filename, "w") as outfile:
    #         outfile.write(json_object)


if __name__ == "__main__":
    main()
