from PIL import ImageDraw,Image,ImageOps,ImageFilter#импортирование функций из библиотеки PIL
import argparse
#image = Image.open("Python_image.webp")
#image_format = image.format
#new = image.rotate(30)
#new.save("image_test.jpg")
#image.save("image_test.png", "png")
#img = Image.new('RGBA', (91, 91), 'white')
#draw = ImageDraw.Draw(img)
#raw.ellipse((0, 0, 90, 90), 'yellow', 'blue')
#draw.ellipse((25, 20, 35, 30), 'yellow', 'blue')
#draw.ellipse((50, 20, 60, 30), 'yellow', 'blue')
#draw.arc((20, 40, 70, 70), 0, 180, 0)
#img.save('draw-smile.png')

def get_black_white (photo):#создание функции конвертирующей формат изображение в L и сохраняющей результат
    photo_bw = photo.convert('L')
    photo_bw.save("bw.jpg")


def get_contrast (photo):#создание функции изменяющей контрастность изображения и сохраняющей результат
    photo_contrast = ImageOps.autocontrast(photo, cutoff=5)
    photo_contrast.save("contrast.jpg")


def get_blur (photo):#создание функции размывающей изображение и сохраняющей результат
    photo_blur = photo.filter(ImageFilter.GaussianBlur(radius=2.4))
    photo_blur.save("blur.jpg")


def get_media_filter (photo):#создание функции добавляющей медианный фильтр и сохраняющей результат
    photo_media_filter = photo.filter(ImageFilter.MedianFilter(size=3))
    photo_media_filter.save("media_filter.jpg")


def get_frame (photo):#создание функции устанавливающей рамку на данное изображение и сохраняющее результат

    width, height = photo.size
    frame_photo = photo.transform((width + 100, height + 100), Image.EXTENT,
    (-10, -10, width + 10, height + 10), Image.BILINEAR)
    frame_photo.save("frame.jpg")


def get_sepia (photo):#создание функции сохраняющей данное изображение с эффектом сепии

    sepia_r = 112
    sepia_g = 66
    sepia_b = 20
    sepia_photo = Image.new("RGB", photo.size)
    for x in range(photo.width):
        for y in range(photo.height):
            r, g, b = photo.getpixel((x,y))
            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
            sepia_r = min(new_r, 255)
            sepia_g = min(new_g, 255)
            sepia_b = min(new_b, 255)
            sepia_photo.putpixel((x,y), (sepia_r, sepia_g, sepia_b))
    sepia_photo.save("sepia.jpg")


def main():#создание функции хранящей в себе открытие данного изображения и вызовы функций
    parser = argparse.ArgumentParser(description='Пример использования argparse')#создание парсера
    #добавление аргументов с действием store true
    parser.add_argument('-np', help='имя входного файла', default="photo.jpg")
    parser.add_argument("--get_black_white", action="store_true", help="использование черно белого фильтра")
    parser.add_argument("--get_contrast", action="store_true", help="использование контрастного фильтра")
    parser.add_argument("--get_blur", action="store_true", help="использование фильтра размытия")
    parser.add_argument("--get_media_filter", action="store_true", help="использование медиа фильтра")
    parser.add_argument("--get_frame", action="store_true", help="использование рамки")
    parser.add_argument("--get_sepia", action="store_true", help="использование фильтра сепии") 
    args = parser.parse_args()#парсим аргумент
    #принты со значениями аргументов
    print("название файла", args.np)
    print("использование черно белого фильтра : ",args.get_black_white)
    print("использование контрастного фильтра : ",args.get_contrast)
    print("использование фильтра размытия : ",args.get_blur)
    print("использование рамки : ",args.get_media_filter)
    print("использование рамки : ",args.get_frame)
    print("использование фильтра сепии : ",args.get_sepia)
    
    photo = Image.open(f"{args.np}")#открытие фотографии
    #условные конструкции с вызовами функций в зависимости от их значений
    if args.get_blur:
        get_blur(photo)
    if args.get_sepia:
        get_sepia(photo)
    if args.get_black_white:
        get_black_white(photo)
    if args.get_media_filter:
        get_media_filter(photo)
    if args.get_contrast:
        get_contrast(photo)
    if args.get_frame:
        get_frame(photo)
 
    
