import yt_dlp as youtube_dl
import pygame as pyg
import button

# const
FPS=120
WHITE = (255,255,255)
BLACK = (0,0,0)
DEFAULT_BG_COLOR=(202,228,241)
WIDTH = 1280
HEIGHT = 720

# setup
pyg.init()
screen = pyg.display.set_mode((WIDTH, HEIGHT))
clock = pyg.time.Clock()
running = True
pyg.display.set_caption("網路影片下載器")

# initialize
# DEFAULT_FONT = pyg.font.match_font("Minecraft Regular")
DEFAULT_FONT = pyg.font.match_font("arial")

# define objects style
button_default = pyg.image.load("youtube_video_downloader/button_default.png").convert_alpha()
button_clicked = pyg.image.load("youtube_video_downloader/button_clicked.png").convert_alpha()

def draw_text(surf, text, font, size, color, x, y, isantialiased):
    set_font = pyg.font.Font(font, int(size))
    text_surface = set_font.render(text, isantialiased, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


# define button
class Button():
    def __init__(self, x, y, image, scale, text, font, color, surf):
        width = image.get_width()
        height = image.get_height()
        self.image = pyg.transform.scale(image, (int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.text = text
        self.font = font
        self.clicked = False
        self.surface = surf
        self.scale = scale
        self.text_color = color

    def draw(self):
        draw_text(self.surface, self.text, self.font, self.scale, self.text_color, self.rect.topleft[0], self.rect.topleft[1], True)

        # get mouse pos
        pos = pyg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pyg.mouse.get_pressed()[0]==1 and not self.clicked:
                self.clicked = True
            elif pyg.mouse.get_pressed()[0]==0 and self.clicked:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

# define some common used buttons
download_button = Button(100, 200, button_default, 1.0, "下載 download", DEFAULT_FONT, BLACK, screen)

while running:
    clock.tick(FPS)

    # 畫面顯示
    screen.fill(DEFAULT_BG_COLOR)

    download_button.draw()

    # 取得事件
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    #

    

    # 畫面更新
    pyg.display.update()

pyg.quit()

# url = ""

# with youtube_dl.YoutubeDL() as ydl:
#     result = ydl.download(url)
