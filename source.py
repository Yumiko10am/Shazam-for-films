import imageio
from imageio.core import CannotReadFrameError
import math
from PIL import Image, ImageDraw
from tqdm import tqdm
reader=imageio.get_reader('8.avi', size=(100,100))

height=100
width=1024

Image_itog=Image.new("RGB", (width,height), (0,0,0)) 
draw=ImageDraw.Draw(Image_itog)

num_frames=0
try:
    for i, im in tqdm(enumerate(reader)):
         num_frames += 1
except CannotReadFrameError:
    pass
print(num_frames)

k=0
try:
    for i, im in tqdm(enumerate(reader)):
        if width<num_frames:
            n=num_frames/width
            n=math.ceil(n)
            
            if i%n==0:
                r=im[:,:,0]
                g=im[:,:,1]
                b=im[:,:,2]
            
                draw.line((k,0,k,height), fill=(r,g,b))
                k+=1
            
               
        
        else:
            n=width/num_frames
            n=math.ceil(n)
            r=im[:,:,0]
            g=im[:,:,1]
            b=im[:,:,2]
           
            draw.line((0+(i*n),0,0+(i*n),height), width=n, fill=(r,g,b))
            
except CannotReadFrameError:
    pass               
            
del draw        
Image_itog.save('C:\\Users\\User\\Documents\\Project\\itog.png', 'PNG')
print('done')
