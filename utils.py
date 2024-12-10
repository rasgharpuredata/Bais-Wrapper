import requests
import base64

def get_basic_auth_header(username: str, password: str) -> str:
    """
    Generate the Basic Authentication header value.
    Args:
        username (str): The username.
        password (str): The password.
    Returns:
        str: The encoded Basic Auth header value.
    """
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded_credentials}"


def validate_license(api_url: str, license_key: str, username: str, password: str):

    api_token = get_basic_auth_header(username,password)

    headers = {
        "Authorization": f"{api_token}",
        "Content-Type": "application/json"
    }
    url = api_url + license_key
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Parse and return JSON response
    except requests.RequestException as exc:
        return None
    
