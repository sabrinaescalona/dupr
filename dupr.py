import requests
import logging
from lxml import html

email = "bria55555@gmail.com"
password = "DexterTheDog123!"
api_base_url = 'https://api.dupr.gg'
api_version = 'v1.0'
dupr_login_url = f'{api_base_url}/auth/{api_version}/login'
players_url = f'{api_base_url}/user/{api_version}/profile'
login_payload = {
    "email": email,
    "password": password
}

def main():
    headers = set_headers()
    players_response(headers)

def handle_login():
    login_response = requests.post(dupr_login_url, json=login_payload)
    if login_response.status_code == 200:
        logging.debug("Login Success!")
        print("Login Success!")
        return login_response
    else:
        print("Login Failed!")
        logging.error(f'Login failed with error code:{login_response.status_code} {login_response.reason}')
        return login_response

def players_response(headers):
    players_response = requests.post(players_url, headers=headers)
    if players_response.status_code == 200:
        print("Players success", players_response.json())
    else:
        print("Players response unsuccessful", players_response)
        
def get_access_token():
    login_response = handle_login()
    if login_response:
        try:
            response_json = login_response.json()
            access_token = response_json.get('result').get('accessToken')
            if access_token:
                return access_token
            else:
                print("Access token missing in the response")
                return None
        except ValueError:
            print("Failed to parse login response as JSON.")

def set_headers():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    return headers
     
# def start_browser():
#     options = Options()
#     options.add_argument("--disable-headless")  # Optional: Run in headless mode
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument('--start-maximized')
#     options.add_argument(f"user-agent={user_agent}")
    
#     # Use Service to configure the driver with ChromeDriverManager
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)  # Pass both service and options here
#     return driver

# def scrape_content(access_token):
#     driver = start_browser()
#     set_access_token_cookie(driver, dupr_dashboard_url, access_token)
#     try:
#         driver.get(dupr_dashboard_url)
#         try:
#             # Wait for CAPTCHA to appear
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "custom-captcha")))
#             print("CAPTCHA detected! Please solve it manually.")
#         except:
#             print("No CAPTCHA detected.")

#         # Wait for the root div to load
#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.ID, "root"))
#         )
        
#         # Fetch the root div
#         root_div = driver.find_element(By.ID, "root")

#         # Debug: Check if th e element has text
#         print("Root Div Text Content:")
#         print(root_div.text)

#         # Additional Debug: Check child elements
#         children = root_div.find_elements(By.XPATH, "./*")
#         print(f"Number of Child Elements in Root: {len(children)}")
#         for idx, child in enumerate(children):
#             print(f"Child {idx + 1}:")
#             print(child.get_attribute("outerHTML"))
#     except:
#         print("couldnt't access the site.")
#     # finally:
#     #     driver.quit()
    
if __name__ == "__main__":
    main()

