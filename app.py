import requests
import logging
import sys

if __name__ == "__main__":
    print("inside main")
    url = "https://10.72.179.214:8443/api/v01/auth/login"

    try:
        res = requests.post(url)
        response = res.json()
        logging.info(f"Sign in to NIMS successful")
    
    except Exception as e:
        print("Error :",e)
        logging.error(f"Error during NIMS sign in: {e}")
        sys.exit(-1)
