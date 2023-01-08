import time
from datetime import date
import plyer
import requests
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.videoplayer import VideoPlayer
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.utils import platform

def remove_splash_custom():
    if(platform == 'android'):
        from android import loadingscreen #type: ignore
        loadingscreen.hide_loading_screen()
    return

try:
    response = requests.get("https://carmelcommunication.pythonanywhere.com")
    server = response.json()

    class ScrollIcon(ScrollView):
        # pass y-move event to parent instead of stopping
        def on_scroll_move(self, touch):
            super().on_scroll_move(touch)
            touch.ud['sv.handled']['y'] = False

    class Administration(MDScreen):
        def __init__(self, **kwargs):
            super().__init__()
            key_people = server['key people']
            keyp = requests.get(key_people, 'r')
            data_key = keyp.text
            self.ids.key.text = f'{data_key}'

            wardsi = server['ward']
            wardi = requests.get(wardsi, 'r')
            data_ward = wardi.text
            self.ids.ward.text = f'{data_ward}'

    class Grid(MDCard):
        def __init__(self, **kwargs):
            super().__init__()
            self.bind(minimum_height=self.setter('height'))

    class assocPopups(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.alter_angels.text = server['Altar Angels']

        def close(self):
            popupwindow.dismiss()

    class assocPopups2(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.choir.text = server['Choir']

        def close2(self):
            popupwindow.dismiss()

    class assocPopups3(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.communication.text = server['Communication']

        def close3(self):
            popupwindow.dismiss()

    class assocPopups4(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.food_committee.text = server['Food Committee']

        def close4(self):
            popupwindow.dismiss()

    class assocPopups5(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.laity.text = server['Laity']

        def close5(self):
            popupwindow.dismiss()

    class assocPopups6(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.mathruvedi.text = server['Mathruvedi']

        def close6(self):
            popupwindow.dismiss()

    class assocPopups7(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.pithruvedi.text = server['Pithruvedi']

        def close7(self):
            popupwindow.dismiss()

    class assocPopups8(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            self.ids.youth.text = server['Youth']

        def close8(self):
            popupwindow.dismiss()

    class newsPopups(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            news1 = server['news_content_1']
            news_main = requests.get(news1, 'r')
            firstnews = news_main.text
            self.ids.main_news.text = f'{firstnews}'
            self.ids.main_news.font_name = server['fontname_1']

        def close9(self):
            popupwindow.dismiss()

    class newsPopups2(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            news2 = server['news_content_2']
            news_second = requests.get(news2, 'r')
            secondnews = news_second.text
            self.ids.two_news.text = f'{secondnews}'
            self.ids.two_news.font_name = server['fontname_2']

        def close10(self):
            popupwindow.dismiss()

    class newsPopups3(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            news3 = server['news_content_3']
            news_third = requests.get(news3, 'r')
            thirdnews = news_third.text
            self.ids.three_news.text = f'{thirdnews}'
            self.ids.three_news.font_name = server['fontname_3']

        def close11(self):
            popupwindow.dismiss()

    class newsPopups4(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            news4 = server['news_content_4']
            news_fourth = requests.get(news4, 'r')
            fourthnews = news_fourth.text
            self.ids.four_news.text = f'{fourthnews}'
            self.ids.four_news.font_name = server['fontname_4']

        def close12(self):
            popupwindow.dismiss()

    class newsPopups5(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            news5 = server['news_content_5']
            news_fifth = requests.get(news5, 'r')
            fifthnews = news_fifth.text
            self.ids.fifth_news.text = f'{fifthnews}'
            self.ids.fifth_news.font_name = server['fontname_5']

        def close13(self):
            popupwindow.dismiss()

    class massPopups(Grid):
        def __init__(self, **kwargs):
            super().__init__()
            mass_time = server['mass_time']
            announce = requests.get(mass_time, 'r')
            data_mass = announce.text
            self.ids.mass_time.text = f'{data_mass}'

        def close14(self):
            popupwindow.dismiss()

    class ToolbarNavigate(MDScreen):
        def __init__(self, **kwargs):
            super().__init__()
            try:
                Clock.schedule_interval(self.slide_next, 7)
                self.ids.image1.source = 'carmel-parish.jpg'
                self.ids.image2.source = server['home_image_2']
                self.ids.image3.source = server['home_image_3']
                self.ids.image4.source = 'Church-Faithful.jpg'
                self.ids.news_image_1.source = server['news_image_1']
                self.ids.news_title_1.text = server['news_title_1']
                self.ids.news_image_2.source = server['news_image_2']
                self.ids.news_title_2.text = server['news_title_2']
                self.ids.news_image_3.source = server['news_image_3']
                self.ids.news_title_3.text = server['news_title_3']
                self.ids.news_image_4.source = server['news_image_4']
                self.ids.news_title_4.text = server['news_title_4']
                self.ids.news_image_5.source = server['news_image_5']
                self.ids.news_title_5.text = server['news_title_5']
                self.ids.news_title_1.font_name = server['fontname_1']
                self.ids.news_title_2.font_name = server['fontname_2']
                self.ids.news_title_3.font_name = server['fontname_3']
                self.ids.news_title_4.font_name = server['fontname_4']
                self.ids.news_title_5.font_name = server['fontname_5']
                self.ids.mag_image1.source = server['mag_image1']
                self.ids.mag_image2.source = server['mag_image2']
                self.ids.mag_image3.source = server['mag_image3']
                self.ids.mag_image4.source = server['mag_image4']
                self.ids.mag_image5.source = server['mag_image5']
                self.ids.mag_image6.source = server['mag_image6']
                self.ids.mag_image7.source = server['mag_image7']
                self.ids.mag_image8.source = server['mag_image8']
                self.ids.mag_image9.source = server['mag_image9']
                self.ids.mag_image10.source = server['mag_image10']
                self.ids.mag_image11.source = server['mag_image11']
                self.ids.mag_image12.source = server['mag_image12']
                self.ids.mag_image13.source = server['mag_image13']
                self.ids.mag_image14.source = server['mag_image14']
            except:
                self.ids.image2.source = 'Church-Faithful.jpg'
                self.ids.image3.source = 'carmel-parish.jpg'

            self.ids.box.add_widget(
                MDExpansionPanel(
                    content=Content(),
                    panel_cls=MDExpansionPanelOneLine(
                        text="Announcement")))

            self.ids.box2.add_widget(
                MDExpansionPanel(
                    content=Content2(),
                    panel_cls=MDExpansionPanelOneLine(
                        text="Birthday")))

            about_catech = server['cat_details']
            detailone = requests.get(about_catech)
            cat_detail = detailone.text
            self.ids.cat_details.text = f'{cat_detail}'

            staff_catech = server['staff_details']
            detailtwo = requests.get(staff_catech)
            staffs_detail = detailtwo.text
            self.ids.staff_details.text = f'{staffs_detail}'

        carmel_url1 = server['carmel_url1']
        carmel_link1 = (f'{carmel_url1}')
        carmel_url2 = server['carmel_url2']
        carmel_link2 = (f'{carmel_url2}')
        carmel_url3 = server['carmel_url3']
        carmel_link3 = (f'{carmel_url3}')
        carmel_url4 = server['carmel_url4']
        carmel_link4 = (f'{carmel_url4}')
        carmel_url5 = server['carmel_url5']
        carmel_link5 = (f'{carmel_url5}')
        carmel_url6 = server['carmel_url6']
        carmel_link6 = (f'{carmel_url6}')
        carmel_url7 = server['carmel_url7']
        carmel_link7 = (f'{carmel_url7}')
        carmel_url8 = server['carmel_url8']
        carmel_link8 = (f'{carmel_url8}')
        carmel_url9 = server['carmel_url9']
        carmel_link9 = (f'{carmel_url9}')
        carmel_url10 = server['carmel_url10']
        carmel_link10 = (f'{carmel_url10}')
        carmel_url11 = server['carmel_url11']
        carmel_link11 = (f'{carmel_url11}')
        carmel_url12 = server['carmel_url12']
        carmel_link12 = (f'{carmel_url12}')
        carmel_url13 = server['carmel_url13']
        carmel_link13 = (f'{carmel_url13}')
        carmel_url14 = server['carmel_url14']
        carmel_link14 = (f'{carmel_url14}')

        gallery_url = server['gallery_url']
        gallery_url = f'{gallery_url}'

        face_url = server['face_url']
        face_url = f'{face_url}'

        you_link = server['you_link']
        you_link = f'{you_link}'

        web_link = server['web_link']
        web_link = f'{web_link}'

        def assoc_popup(self, *args):
            show = assocPopups()
            global popupwindow
            popupwindow = Popup(title="Alter Angels", content=show)
            # open popup window
            popupwindow.open()

        def assoc_popup2(self, *args):
            show = assocPopups2()
            global popupwindow
            popupwindow = Popup(title="Choir", content=show)
            # open popup window
            popupwindow.open()

        def assoc_popup3(self, *args):
            show = assocPopups3()
            global popupwindow
            popupwindow = Popup(title="Communications", content=show)
            # open popup window
            popupwindow.open()

        def assoc_popup4(self, *args):
            show = assocPopups4()
            global popupwindow
            popupwindow = Popup(title="Food Committee", content=show)
            # open popup window
            popupwindow.open()

        def assoc_popup5(self, *args):
            show = assocPopups5()
            global popupwindow
            popupwindow = Popup(title="Laity", content=show)
            popupwindow.open()

        def assoc_popup6(self, *args):
            show = assocPopups6()
            global popupwindow
            popupwindow = Popup(title="Mathruvedi", content=show)
            popupwindow.open()

        def assoc_popup7(self, *args):
            show = assocPopups7()
            global popupwindow
            popupwindow = Popup(title="Pithruvedi", content=show)
            popupwindow.open()

        def assoc_popup8(self, *args):
            show = assocPopups8()
            global popupwindow
            popupwindow = Popup(title="Youth", content=show)
            popupwindow.open()

        def news_popup(self, *args):
            show = newsPopups()
            global popupwindow
            popupwindow = Popup(title="Youth", content=show)
            popupwindow.open()

        def news_popup2(self, *args):
            show = newsPopups2()
            global popupwindow
            popupwindow = Popup(title="Youth", content=show)
            popupwindow.open()

        def news_popup3(self, *args):
            show = newsPopups3()
            global popupwindow
            popupwindow = Popup(title="Youth", content=show)
            popupwindow.open()
        def news_popup4(self, *args):
            show = newsPopups4()
            global popupwindow
            popupwindow = Popup(title="Mass Timings", content=show)
            # open popup window
            popupwindow.open()

        def news_popup5(self, *args):
            show = newsPopups5()
            global popupwindow
            popupwindow = Popup(title="Mass Timings", content=show)
            # open popup window
            popupwindow.open()

        def mass_popup(self, *args):
            show = massPopups()
            global popupwindow
            popupwindow = Popup(title="Mass Timings", content=show)
            # open popup window
            popupwindow.open()

        def slide_next(self, *args):
            self.ids.carousel.load_next()

        def run_check(self):
            self.ids.bib_buton.disabled = True
            self.ids.bib_buton.text = 'Please Wait...'
            Clock.schedule_once(self.bible_verse, 4)

        def bible_verse(self, *args):
            try:
                response4 = requests.get("https://labs.bible.org/api/?passage=random&type=json")
                gospel = response4.json()
                text = gospel[0]['text']
                book = gospel[0]['bookname']
                chapter = gospel[0]['chapter']
                verse = gospel[0]['verse']
                random_quote = f'\r{text}\n({book} {chapter}:{verse})'
                self.ids.matter.text = (random_quote)
                self.ids.bib_buton.disabled = False
                self.ids.bib_buton.text = 'Next Verse'
            except:
                random_quote = f'Nothing is covered up that will not be revealed, or hidden that will not be known\nLuke:12:2'
                self.ids.matter.text = (random_quote)
                self.ids.bib_buton.disabled = False
                self.ids.bib_buton.text = 'Next Verse'

    class About(MDScreen):
        map_url = server['map_url']
        map_link = (f'{map_url}')

        def __init__(self, **kwargs):
            super().__init__()
            aboutit = server['About']
            about_info = requests.get(aboutit, 'r')
            data_about = about_info.text
            self.ids.about_text.text = f'{data_about}'

    class History(MDScreen):
        def __init__(self, **kwargs):
            super().__init__()
            carmel_parish = server['hist_carmel']
            carmel_hist = requests.get(carmel_parish, 'r')
            data_carmel = carmel_hist.text
            self.ids.hist_carm_text.text = f'{data_carmel}'

            kalyan = server['hist_kalyan']
            kalya = requests.get(kalyan, 'r')
            data_kalyan = kalya.text
            self.ids.hist_kalyan_text.text = f'{data_kalyan}'

    class Content(MDBoxLayout):
        def __init__(self, **kwargs):
            super().__init__()
            file_announce = server['announcement']
            announce = requests.get(file_announce)
            data_announce = announce.text
            self.ids.announcement.text = f'{data_announce}'
            self.ids.announcement.font_name = server['font-family']

    class Content2(MDBoxLayout):
        def __init__(self, **kwargs):
            super().__init__()
            file_url = server['birthday']
            file = requests.get(file_url)
            today = time.strftime('%m%d')
            flag = 0
            tday = date.today()
            d1 = tday.strftime("%d/%m/%Y")

            if (file.status_code):
                data = file.text
                for line in data.split(('\n')):
                    if today in line:
                        line = line.split('  ')
                        plyer.notification.notify(title='test', message=f"Birthdays Today: {line[1]}")
                        self.ids.birday.text = f'{d1}\n\n{line[1]}'

    class Splash_screen(MDScreen):
        pass

except:
    class No_Wifi_Page(MDScreen):
        def __init__(self, **kwargs):
            super().__init__()

class Root(MDScreen):
    def __init__(self, **kwargs):
        super(Root, self).__init__()
        try:
            global screen_manager
            screen_manager = MDScreenManager()
            self.screen_manager = screen_manager
            screen_manager.add_widget(Splash_screen(name='splash'))
            screen_manager.add_widget(ToolbarNavigate(name='toolbar_nav'))
            screen_manager.add_widget(Administration(name='admini'))
            screen_manager.add_widget(History(name='history'))
            screen_manager.add_widget(About(name='about'))
        except:
            screen_manager.add_widget(No_Wifi_Page(name='no_wifi'))

class Carmelfinal(MDApp):
    def build(self, android=None):
        if platform == 'android':
            from android import AndroidService
            service = AndroidService('my pong service', 'running')
            service.start('service started')
            self.service = service
        self.theme_cls.theme_style = "Dark"
        return Root().screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 5)

    def change_screen(self, dt):
        screen_manager.current = 'toolbar_nav'

if __name__ == '__main__':
    remove_splash_custom()
    Carmelfinal().run()



