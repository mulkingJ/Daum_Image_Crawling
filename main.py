from typing import Dict

class DaumImageDownloader:
    def __init__(self)-> None:
        # Keword
        self.keword : str = self.input_keword()

        # Base URL
        self.url : str = 'https://search.daum.net/qsearch?mk=Yt5b8ihdcrGgezL9K9NHuwAAAJI&uk=Yt5b8ihdcrGgezL9K9NHuwAAAJI&_caller1=tot_daum&at=auto&w=spread&qsearch_ver=v2&exp=IIM&viewtype=json&lpp=80&m=tab_img&req=qtab&page='

        # headers
        self.headers Dict[str,str] = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.57 Whale/3.14.133.23 Safari/537.36'}

        # page COunt
        self.page_count : int = self.page_cnt()
        
    def input_keword(self)-> str:
    while True :
        keword : str = input('검색어를 입력해주세요\n\n:')
        if not keword :
            pyautogui.alert('입력된 검색어가 없습니다')
            continue
        return keword
    
    def input_page_cnt(self)-> int:
    while True :
        page_cnt : str = input('크롤링할 페이지 수를 입력해주세요\n\n:')
        if not page_cnt :
            pyautogui.alert('페이지 수가 입력되지 않았습니다!')
            continue
        if re.match('[가-힣ㄱ-ㅎA-Za-z]',page_cnt) :
            pyautogui.alert('숫자로 입력해주세요!')
            continue
        else :
            return int(page_cnt)