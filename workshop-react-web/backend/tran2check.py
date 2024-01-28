import requests
import checktext
def r():
    url = "http://www.kizur.co.il/search_mobile.php?abbr=%D7%A8%22%D7%97&search_by_word=%D7%97%D7%A4%D7%A9&cat_id=0"  # הכניסו את כתובת ה-URL המתאימה

    response = requests.get(url)

    if response.status_code == 200:
      html_content = response.text
      print(html_content)

    # כעת תוכלי לעבוד עם התוכן שקיבלת מהדף
    # תוכלי להדפיס אותו, לעבוד על נתונים מתוך התוכן וכדומה
    else:
     print("Failed to fetch HTML content from the page")

def main():
  r()


main()