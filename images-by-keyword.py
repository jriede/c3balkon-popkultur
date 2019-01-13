# pip install google_images_download
# or
# git clone https://github.com/hardikvasa/google-images-download.git

# Bill Clinton, Erwin Honecker, Margaret Thatcher, Helmut Kohl, Michail Gorbatschow, Nina Hagen, Ronald Reagan
#

from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

arguments = {"keywords":"Michail Gorbatschow","limit":50,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   # passing the arguments to the function, downloads images
print(paths)   # printing absolute paths of the downloaded images
