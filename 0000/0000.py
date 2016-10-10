from PIL import Image, ImageDraw, ImageFont
import os

#open the pic
im = Image.open("touxiang.png").convert("RGBA")

#create a white area:
white = Image.new('RGBA',im.size,(255,255,255,0))


#create a actionable draw
num = ImageDraw.Draw(white)
 
#load font arial and set font's size
font = ImageFont.truetype("arial.ttf", 20)

#draw number (line(x1,y1,x2,y2,fill,width...) works too)
num.text((75, 5), "12", font=font,fill=(255,0,0,255)) 

#combine im and white
output = Image.alpha_composite(im,white)
output.show()

#save the file as output
output.save("output.png")