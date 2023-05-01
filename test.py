from kumikolib import Kumiko
options = {'rtl': True}
k = Kumiko(options)
import ngc

for src in ngc.dirlist('E:/DL/FZG','jpg'):
    k.parse_image(src)
