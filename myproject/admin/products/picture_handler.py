import os
from PIL import Image
from flask import url_for,current_app

def add_product_pic(photo_upload,product_name):
    filename = photo_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(product_name) +'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/upload_products', storage_filename)
    output_size = (200,200)

    pic = Image.open(photo_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
