import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2



# パスの定義
static_path = "static/"
img_folder = static_path + "img/"
font_file_path = static_path + "font/gothic_font/GenShinGothic-Bold.ttf"



def read_rgb_img(img_path: str) -> np.ndarray:
    """ 特定のパスからRGBの画像をnp形式で取得する関数 """
    bgr_img: np.ndarray = cv2.imread(img_path)
    if bgr_img is None:
        return None
    rgb_img: np.ndarray = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img

def write_rgb_img(img_path: str , rgb_img: np.ndarray):
    """ np形式のRGBの画像を特定パスに保存する関数 """
    bgr_img: np.ndarray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(img_path , bgr_img)

def draw_telop_and_add_img(telop_text , input_img_path , output_img_path = "output.png"):
    """ 下部中央にテロップを追加し、上部中央に画像を追加する関数 """
    b,g,r,a = 255 , 255 , 255 , 0 #B(青)・G(緑)・R(赤)・A(透明度)
    font_size = 90

    # 背景黒のベースのフレームを用意
    basic_width, basic_height = 1920, 1080  # Youtubeフレームサイズ「1920px×1080px」
    basic_frame_rgb_img = np.zeros((basic_height, basic_width, 3), np.uint8)

    # 画像を上部と下部（テロップ）に分離
    upper_ratio , lower_ratio = 7 , 2
    # 上下に横線を引く位置を計算
    divides_line_position = int(basic_height * (upper_ratio / (upper_ratio + lower_ratio)))
    # # 横線を引く
    # basic_frame_rgb_img[divides_line_position, :, :] = [255, 255, 255]  # 白色の横線

    # テキストの高さ方向の座標
    text_y = int( divides_line_position + (basic_height - divides_line_position) / 4 )
    font = ImageFont.truetype(font_file_path, font_size) # フォントサイズが32
    basic_frame_rgb_img_pil = Image.fromarray(basic_frame_rgb_img) # 配列の各値を8bit(1byte)整数型(0～255)をPIL Imageに変換。
    draw = ImageDraw.Draw(basic_frame_rgb_img_pil) # drawインスタンスを生成

    center_x, y, x2, y2 = draw.textbbox((basic_width / 2, basic_height / 2), telop_text, font=font, anchor='md')
    position = (center_x , text_y) # テキスト表示位置

    draw.text(
        position, telop_text, font = font ,
        align='center' ,
        fill = (b, g, r, a) ,
    ) # drawにテキストを記載 fill:色 BGRA (RGB)
    basic_frame_rgb_img = np.array(basic_frame_rgb_img_pil) # PIL を配列に変換

    # 入力画像をリサイズ
    input_rgb_img: np.ndarray = read_rgb_img(input_img_path) 
    input_height , input_width = input_rgb_img.shape[0] , input_rgb_img.shape[1]
    resized_width = int( input_width * divides_line_position / input_height )
    resized_rgb_img = cv2.resize(input_rgb_img, (resized_width, divides_line_position))

    # 画像を横方向に中央に配置
    start_x = (basic_width - resized_width) // 2
    end_x = start_x + resized_width
    start_y = 0
    end_y = divides_line_position

    basic_frame_rgb_img[start_y:end_y, start_x:end_x, :] = resized_rgb_img

    write_rgb_img(output_img_path , basic_frame_rgb_img)


