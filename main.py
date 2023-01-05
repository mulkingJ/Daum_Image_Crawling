class DaumImageDownloader:
    def __init__(self):
        # Keword
        self.keword : str = self.input_keword()

        # Base URL
        self.url = 'https://search.daum.net/qsearch?mk=Yt5b8ihdcrGgezL9K9NHuwAAAJI&uk=Yt5b8ihdcrGgezL9K9NHuwAAAJI&_caller1=tot_daum&at=auto&w=spread&qsearch_ver=v2&exp=IIM&viewtype=json&lpp=80&m=tab_img&req=qtab&page='

        # headers
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.57 Whale/3.14.133.23 Safari/537.36'}

    def input_keword(self):
    while True :
        keword = input('검색어를 입력해주세요\n\n:')
        if not keword :
            pyautogui.alert('입력된 검색어가 없습니다')
            continue
        return keword