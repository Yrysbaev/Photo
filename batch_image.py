from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageColor, ImageEnhance

import os
os.chdir("Instagram")
for path,dirc,files in os.walk("."):
    for file in files: 
        if file.endswith('.jpg') or file.endswith(".png"):
            img = Image.open(file)
            fn, flext = os.path.splitext(file)
            b_w = img.convert("L")
            detail = b_w.filter(ImageFilter.DETAIL)
            resize = detail.resize((1080, 1080))
            width, height = resize.size
            draw = ImageDraw.Draw(resize)
            watermark  = "Sultan Chai"
            color = "WHITE"
            font = ImageFont.truetype("/home/umut/Desktop/Wall Notes.otf", 60)
            textwidth, textheight = draw.textsize(watermark, font)
            edge = 10 
            p_x = width - textwidth - edge
            p_y = height - textheight - edge 
            
            draw.text((p_x, p_y), watermark, color, font=font) 
            resize.save('{0}{1}'.format(fn, flext))
                    
            
        
    
    