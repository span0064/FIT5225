import requests
import json
import base64

BASE_URL = "https://2582k2a918.execute-api.us-east-1.amazonaws.com/dev/api/"


def list_images(access_token):
    endpoint = BASE_URL + "images"
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.request("GET", endpoint, headers=headers, data=payload)
    print(json.dumps(json.loads(response.text), indent=2))


def send_upload_request(access_token, encoded_image):
    endpoint = BASE_URL + "upload"

    payload = json.dumps({
        "image": encoded_image
    })

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", endpoint, headers=headers, data=payload)

    print(json.dumps(json.loads(response.text), indent=2))


def upload_image(access_token):
    print("Please enter the path of the image:")
    file_path = input(">>> ")

    with open(file_path, 'rb') as image_file:
        data = base64.b64encode(image_file.read()).decode('utf-8')
    send_upload_request(access_token, data)


def send_delete_request(access_token, url):
    endpoint = BASE_URL + "images"

    payload = json.dumps({
        "url": url
    })

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "DELETE", endpoint, headers=headers, data=payload)
    print(json.dumps(json.loads(response.text), indent=2))


def delete_image(access_token):
    print("Please enter the url of the image:")
    url = input(">>> ")
    send_delete_request(access_token, url)


def search_tag(access_token):
    print("Please enter tags to search seperated by commas:")
    tags = input(">>> ").split(', ')

    endpoint = BASE_URL + 'images/find'

    payload = json.dumps({"tags": tags})

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", endpoint, headers=headers, data=payload)
    print(json.dumps(json.loads(response.text), indent=2))


def search_image(access_token):
    print("Please enter the path of the image:")
    file_path = input(">>> ")

    with open(file_path, 'rb') as image_file:
        data = base64.b64encode(image_file.read()).decode('utf-8')

    endpoint = BASE_URL + 'images/find-image'

    payload = json.dumps({
        "image": data
    })

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", endpoint, headers=headers, data=payload)
    print(json.dumps(json.loads(response.text), indent=2))


def modify_tag_request(access_token, url, flag, tags):
    endpoint = BASE_URL + 'images/modify'

    payload = json.dumps({
        "url": url,
        "tags": tags,
        "type": flag
    })

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", endpoint, headers=headers, data=payload)
    print(json.dumps(json.loads(response.text), indent=2))


def add_tag(access_token):
    print("Please enter the url of the image:")
    url = input(">>> ")

    print("Please enter tags to add seperated by commas:")
    tags = input(">>> ").split(', ')

    modify_tag_request(access_token, url, 1, tags)


def delete_tag(access_token):
    print("Please enter the url of the image:")
    url = input(">>> ")

    print("Please enter tags to delete seperated by commas:")
    tags = input(">>> ").split(', ')

    modify_tag_request(access_token, url, 0, tags)


def get_user_auth():
    print("Please enter your access token:")
    access_token = input(">>> ")
    return access_token


def get_input():
    print("Avaliable Commands:")
    print("  [1] List all images")
    print("  [2] Upload new image")
    print("  [3] Delete Image")
    print("  [4] Search based on tags")
    print("  [5] Search based on image")
    print("  [6] Add tag to image")
    print("  [7] Delete tag from image")
    print("  [q] Quit")
    print("Type 1-7 or q to quit")
    user_in = input(">>> ")
    return user_in


def run_interface():
    token = get_user_auth()

    user_in = get_input()
    while user_in != 'q':
        if user_in in INPUT_MAPPING:
            INPUT_MAPPING[user_in](token)
        else:
            print("Please type 1-7 or q to quit")
        input("Press any key to continue")  # Wait for user to continue
        user_in = get_input()


INPUT_MAPPING = {'1': list_images,
                 '2': upload_image,
                 '3': delete_image,
                 '4': search_tag,
                 '5': search_image,
                 '6': add_tag,
                 '7': delete_tag}

if __name__ == "__main__":
    run_interface()
