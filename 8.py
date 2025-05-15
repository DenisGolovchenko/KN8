import requests
def get_cat_info():
    url = "https://api.thecatapi.com/v1/images/search?api_key=live_***&include_breeds=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        cat_data = response.json()[0]
        image_url = cat_data['url']
        if 'breeds' in cat_data and cat_data['breeds']:
            breed = cat_data['breeds'][0]['name']
            else:
            breed = 'Невідомо'  
        return image_url, breed
    except requests.RequestException as e:
        print(f"Помилка при отриманні інформації: {e}")
        return None, None
def main():
    image_url, breed = get_cat_info()
    if not image_url:
        return
    print("\nВипадкове зображення кота:")
    print(f"URL зображення: {image_url}")
    print(f"Порода кота: {breed}")
if __name__ == "__main__":
    main()
