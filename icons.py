from PIL import Image, ImageDraw
import os
A=(45,226,192);B=(139,123,255);DK=(6,16,26)
BOLT=[(.57,.10),(.29,.56),(.47,.56),(.41,.90),(.71,.43),(.52,.43)]
def grad(n):
    g=Image.new('RGB',(n,n));px=g.load()
    for y in range(n):
        for x in range(n):
            t=(x+y)/(2*n-2);px[x,y]=tuple(int(A[i]+(B[i]-A[i])*t) for i in range(3))
    return g
def tile(n,shape):
    S=4*n;g=grad(256).resize((S,S))
    m=Image.new('L',(S,S),0);d=ImageDraw.Draw(m)
    if shape=='circle': d.ellipse([0,0,S-1,S-1],fill=255)
    else: d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*.24),fill=255)
    g=g.convert('RGBA');g.putalpha(m)
    ImageDraw.Draw(g).polygon([(x*S,y*S) for x,y in BOLT],fill=DK+(255,))
    return g.resize((n,n),Image.LANCZOS)
for k,n in {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192}.items():
    d=f'icons/res/mipmap-{k}';os.makedirs(d,exist_ok=True)
    tile(n,'rr').save(f'{d}/ic_launcher.png');tile(n,'circle').save(f'{d}/ic_launcher_round.png')
    F=int(n*108/48);fg=Image.new('RGBA',(F,F),(0,0,0,0));t=tile(int(F*.56),'rr')
    fg.paste(t,((F-t.width)//2,(F-t.height)//2),t);fg.save(f'{d}/ic_launcher_foreground.png')
os.makedirs('icons/res/values',exist_ok=True)
open('icons/res/values/ic_launcher_background.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#070B14</color>\n</resources>\n')
