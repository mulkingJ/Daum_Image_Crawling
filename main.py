from typing import Dict,List

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
        
        # img count
        self.img_cnt = 1

    def main(self)-> None:
        urls : List[str] = [self.url + f'{page}' + f'&q={rep.quote_plus(self.keword)}' for page in range(1 ,self.page_cnt + 1)]

        # Session Open
        with rq.Session() as session :
            [self.fetch(url=url,session=session) for url in urls]

    def fetch(self,url : str , session)-> None:
        with session.get(url,headers=self.headers) as response :
            json_data : dict = response.json()
            datas : list = json_data['RESULT']['SPREAD_TAB_IMAGE']['r']['ds']['data']

            # 이미지 링크 모음
            img_urls = [data['imgurl'] for data in datas]

            # 이미지 다운로드
            [self.download_img(img_url=img_url,session=rq.Session()) for img_url in img_urls]

    def download_img(self,img_url: str,session)-> None:
        try :
            # 저장 경로 지정
            Path : str = f'./{self.keword}'
            if not os.path.exists(Path):
                os.mkdir(Path)

            # 파일 이름 지정
            fileName : str = f'Daum-{self.keword}-{self.img_cnt}.jpg'

            # 최종 다운로드 될 경로 지정
            TARGET_DIR : str = os.path.join(Path,fileName)

            # Session Open
            with session.get(img_url,headers=self.headers) as response :
                if response.ok :
                    with open(TARGET_DIR , 'wb') as file :
                        file.write(response.content)

            # 이미지 다운 출력문
            print(f'{fileName.split("Daum-")[-1]} 다운로드 완료')

            # 이미지 카운트 증가
            self.img_cnt += 1

        except ValueError as e :
            print(e)

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