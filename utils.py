import requests


class Utils:
    @staticmethod
    def download_file(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(url.split("/")[-1], 'wb') as f:
                    f.write(response.content)
                print(
                    f"File downloaded successfully. File name: {url.split('/')[-1]}"
                )
                return True
            else:
                print(f"Failed to download file. HTTP Status Code: {response.status_code}")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    @staticmethod
    def log(data):
 
        with open("log.txt", "a") as f:
            f.write(data + "\n")