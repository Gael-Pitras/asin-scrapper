import requests
from bs4 import BeautifulSoup
import json


def get_header(referer):
    
    header = {
                'dnt': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': referer,
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            }
    
    return header


def asinResolver(asin, language):
    try:
        url_amazon = "https://www.amazon."+language+"/"
        param_query = "s?k="
        header = get_header(url_amazon)
        result = {}
        response = requests.get(url_amazon+""+param_query+""+asin, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        html_cadre = soup.find("div", {"data-asin": asin})
        if html_cadre:
            a_link = html_cadre.find("a", class_="a-link-normal s-no-outline")

            if a_link:
                href_page = a_link["href"]
                
                if href_page:
                    header_page = get_header(url_amazon+""+param_query+""+asin)
                    response_page = requests.get(url_amazon+""+href_page, headers=header_page)
                    soup_page = BeautifulSoup(response_page.content, 'html.parser')
                    h1_element = soup_page.find("h1", id="title")
                    result["url"] = url_amazon+""+href_page
                   
                    if h1_element:
                        
                        titre = h1_element.find("span", id="productTitle")
                        sous_titre = h1_element.find("span", id="productSubtitle")

                        texte_titre = titre.get_text(strip=True) if titre else "Title not found"
                        texte_sous_titre = sous_titre.get_text(strip=True) if sous_titre else "Sub-Title not found"
                     
                        result["title"] = texte_titre
                        result["sub_title"] = texte_sous_titre
                        
                        description_div = soup_page.find("div", id="productDescription")
                        if description_div:
                            result["description"] = description_div.text.strip()
                            
                        price_div = soup_page.select_one("span.a-price.priceToPay")
                        if price_div:
                            result["price"] = price_div.text.strip()
                        
                        if asin or asin != '':
                            result["asin_validate"] = False
                                
                        detailBullets = soup_page.find("div", id="detailBulletsWrapper_feature_div")
                        if detailBullets:
                            ul_details = detailBullets.find("ul")
                            if ul_details:
                                li_elements = ul_details.find_all("li")  
                                for li in li_elements:
                                    items_list = li.find("span", class_="a-list-item")
                                    if items_list:
                                        spans_item = items_list.find_all("span")
                                        
                                        if len(spans_item) >= 2: 
                                            label_span = spans_item[0]
                                            value_span = spans_item[1]

                                            if "ASIN" in label_span.text.strip():
                                                result["asin"] = value_span.text.strip()
                                                if asin == result["asin"]:
                                                    result["asin_validate"] = True
                                        
                                        
                        
                            
                        detailsBullets2 = soup_page.find("table", id="productDetails_detailBullets_sections1")
                        if detailsBullets2:
                            tr_details = detailsBullets2.find_all("tr")
                            for tr in tr_details:
                                td_detail = tr.find("td")
                                if td_detail:
                                    divs_asin = td_detail.find_all("div", attrs={"data-asin": True})
                                    for div_asin in divs_asin:
                                        result["asin"] = div_asin["data-asin"]
                                        
                                        if asin == result["asin"]:
                                            result["asin_validate"] = True
                                        
                         
                        detailsTable = soup_page.find("div", class_="a-expander-content a-expander-section-content a-section-expander-inner")
                        if detailsTable:
                            specifications = {}
                            lignes = detailsTable.find_all("tr")
                            for ligne in lignes:
                                cle = ligne.find("th", class_="a-color-secondary a-size-base prodDetSectionEntry").get_text(strip=True)
                                valeur = ligne.find("td", class_="a-size-base prodDetAttrValue").get_text(strip=True)
                                cle = cle.replace('\u200e', '').replace('\u200f', '')
                                valeur = valeur.replace('\u200e', '').replace('\u200f', '')

                                specifications[cle] = valeur
                            result["details"] = specifications
                            
             
                           
        return json.dumps(result, ensure_ascii=False, indent=4)
    except requests.RequestException as e:
        print(f"Error: {e}")
        
          

asin = "B00IKI352E"
language = "fr"
result = asinResolver(asin, language)
print(result)

with open("output.json", "w", encoding="utf-8") as file:
    file.write(result)
