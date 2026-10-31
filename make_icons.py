from PIL import Image, ImageDraw

def make_icon(size, path):
    img = Image.new("RGB", (size, size), "#7c4dff")
    d = ImageDraw.Draw(img)
    s = size / 100
    # eenvoudig kubusje (3D-print) in lichte tinten
    top = [(50*s, 22*s), (78*s, 36*s), (50*s, 50*s), (22*s, 36*s)]
    left = [(22*s, 36*s), (50*s, 50*s), (50*s, 80*s), (22*s, 66*s)]
    right = [(78*s, 36*s), (50*s, 50*s), (50*s, 80*s), (78*s, 66*s)]
    d.polygon(top, fill="#ffffff")
    d.polygon(left, fill="#d9ccff")
    d.polygon(right, fill="#b39dff")
    img.save(path, "PNG")

make_icon(192, "icon-192.png")
make_icon(512, "icon-512.png")
print("done")
