import segno

def make_qr(url, image):
    qr = segno.make_qr(url)
    qr.save(image, scale=16)

make_qr("https://southernmethodistuniversity.github.io/hpc_docs/", 
        "images/hpc_docs_qr.png")

make_qr("https://libcal.smu.edu", 
        "images/libcal_qr.png")

