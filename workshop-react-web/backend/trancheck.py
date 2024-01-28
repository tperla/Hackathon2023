import requests
from bs4 import BeautifulSoup
def rashei_Tevot(word):
    url = f"http://www.kizur.co.il/search_mobile.php?abbr={word}&search_by_word=%D7%97%D7%A4%D7%A9&cat_id=0"  # הכניסו את כתובת ה-URL המתאימה

    response = requests.get(url)

    if response.status_code == 200:
      html_content = response.content.decode()
      results = []
      soup = BeautifulSoup(html_content, 'html.parser')
      a = soup.find_all('div', {'class' : 'result_row'})
      for elem in a:
         key = elem.contents[0].text
         value =elem.contents[1].text[::-1]
         print(key, word)
         results.append(value)
      return results[0]
 
    else:
     print("Failed to fetch HTML content from the page")



def main():
    res=rashei_Tevot("רמטכ\"ל")
    print(res)

if __name__ == '__main__':
    main()