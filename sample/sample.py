from pytesseract import pytesseract
from PIL import Image
import os

if __name__ == '__main__':

    # 1枠の縦横ピクセル
    w = 80;
    h = 65;

    # 枠線を除去するマージンピクセル。縦横共通。
    margin_w = 20;
    margin_h = 15;

    for imgid in range(1, 5):
        img = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/sample" + str(imgid) + ".png", "r");

        for pos_h in range(0, 3):
            # 読み取るマスの左上位置
            leftpos_y = margin_h + (h * pos_h) + (margin_h * pos_h);
            for pos_w in range(0, 3):
                # 読み取るマスの左上位置
                leftpos_x = margin_w + (w * pos_w) + (margin_w * pos_w);

                # 該当のマスをトリミング
                crop = img.crop((leftpos_x, leftpos_y, leftpos_x + w, leftpos_y + h));
                # crop.save("/opt/crop" + str(imgid) + "-" +  str(pos_h) + "-" + str(pos_w) + ".png");

                # インストールしたtesseractコマンドのパス
                pytesseract.tesseract_cmd = "/usr/bin/tesseract";

                # -psm 8は1文字判定のフラグ
                result = pytesseract.image_to_string(crop, config="--psm 10", lang="eng+jpn");

                print(result);
