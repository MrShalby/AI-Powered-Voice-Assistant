import requests

def query_gemini_api(user_query):
    api_url = ""  # Replace with the actual Gemini API endpoint
    headers = {
        "Authorization": "",  # Replace with your actual API key
        "Content-Type": "application/json"
    }
    payload = {
        "query": user_query
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        return {"error": "Failed to fetch response from Gemini API."} 
