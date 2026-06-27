import urllib.request, csv
from bs4 import BeautifulSoup

ptt = []

def open_ptt_url(url,page):

    for i in range(0,page):
        with urllib.request.urlopen(url)as web1:
            soup1 = BeautifulSoup((web1.read().decode("utf-8")), "html.parser")
            web1_outer_later_div = soup1.find_all("div", class_ = "r-ent")
            #找下一頁
            next_page= soup1.find("div", id = "main-container").find("div", id="action-bar-container").find("div", class_ = "action-bar").find("div", class_ = "btn-group btn-group-paging").find_all("a", class_ = "btn wide")
            for next_page_a in next_page:
                if next_page_a.text.strip() == "‹ 上頁":
                    #更新url變數
                    url = "https://www.ptt.cc" + next_page_a["href"]


        for article in web1_outer_later_div:
            web1_title_div = article.find("div", class_ = "title")
            a_tag = web1_title_div.find("a")
            if a_tag:
                web1_title_text = a_tag.text.strip()
                inner_url = "https://www.ptt.cc" + a_tag["href"]

                heart_div = article.find("div", class_ = "nrec")
                heart = heart_div.find("span")
                if heart:
                    heart = heart.text.strip()
                else:
                    heart = "0"
                
                time = "找不到時間"

                with urllib.request.urlopen(inner_url)as web2:
                    web2_open_url = web2.read().decode("utf-8")
                    soup2 = BeautifulSoup(web2_open_url, "html.parser")
                    web2_outer_layer_div = soup2.find("div", id = "main-container")
                    web2_inner_layer_div = web2_outer_layer_div.find("div", class_ = "bbs-screen bbs-content")
                    time_div = web2_inner_layer_div.find_all("div", class_ = "article-metaline")

                    for meta_tag in time_div:
                        time_name = meta_tag.find("span", class_ = "article-meta-tag").text.strip()
                        
                        if time_name == "時間":
                            time = meta_tag.find("span", class_ = "article-meta-value").text.strip()
                            break

                ptt.append([web1_title_text, heart, time])
            else:
                title_text = "文章被刪除"
                inner_url = "文章被刪除"
                heart = "文章被刪除"
                time_span = "文章被刪除"
                ptt.append([title_text, heart, time_span])
    
    with open("articles.csv", "w", newline = "", encoding = "utf-8")as f:
        writer = csv.writer(f)
        writer.writerows(ptt)

url = "https://www.ptt.cc/bbs/Steam/index.html"

open_ptt_url(url, 3)