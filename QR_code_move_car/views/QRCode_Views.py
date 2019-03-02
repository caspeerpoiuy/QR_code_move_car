import qrcode
from PIL import Image
from flask_restful import Resource


class Apply_QrCode(Resource):
    def get(self):
        qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data("right")
        qr.make(fit=True)
        img = qr.make_image(fill_color="red", back_color="white")
        img = img.convert("RGBA")
        icon = Image.open("1.png")
        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        img.save("123.png")


    def post(self):
        pass