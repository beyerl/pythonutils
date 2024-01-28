import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"Image downloaded successfully: {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def get_first_image_url(homepage_url):
    response = requests.get(homepage_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first image within the specified DOM structure
        image_tag = soup.select_one('#root div div img')
        
        if image_tag:
            img_url = image_tag.get('src')
            if img_url:
                full_img_url = urljoin(homepage_url, img_url)
                return full_img_url
            else:
                print("No 'src' attribute found in the first image tag.")
        else:
            print("No image tag found within the specified DOM structure.")
    else:
        print(f"Failed to fetch homepage content. Status code: {response.status_code}")

if __name__ == "__main__":
    homepage_url = "https://beyerl.github.io/viewer/"  # Replace with the actual homepage URL
    image_save_path = "downloaded_image.jpg"  # Replace with the desired save path

    first_image_url = get_first_image_url(homepage_url)
    if first_image_url:
        download_image(first_image_url, image_save_path)
