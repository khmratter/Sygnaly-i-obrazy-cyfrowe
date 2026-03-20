# Demosaicing

Demosaicing is a digital image processing algorithm used to reconstruct a full colour image from incomplete samples output from an image sensor overlaid with a colour filter array (I've used Bayer and Fuji X-Trans filters). Demosaicing is an example of application of interpolation as it involves interpolation of missing colour values from nearby pixels. Interpolation algorithms are used to estimate the missing colour information for each pixel, producing a complete and accurate colour image. Other goals are noise reduction and maximum preservation of the image resolution.


# Colour filter arrays (CFA)


Colour filter array is an array of tiny colour filters placed over the pixel sensors of an image sensor of the camera to capture colour. I took a look and simulated Bayer CFA and Fujifilm X-Trans CFA. 


## Bayer filter

A Bayer filter mosaic consists of a repeating grid of red, green and blue filters. The photosites have a repeated 2 by 2 pattern. The Bayer pattern uses twice as many green filters as red or blue in order to mimic the human eye's greater sensitivity to green light.


## Fujifilm X-Trans filter

A Fujifilm X-Trans filter is a CFA developed by Fujifilm and used in its Fujifilm cameras. Unlike most sensors (including Bayer filter), these sensors have an irregular 6 by 6 pattern of photosites. Such pattern minimizes the likelihood of interference and increases resolution. In addition, Fujifilm claims that X-Trans sensors have an improved colour reproduction, because all horizontal and vertical lines contain at least one red, blue and green pixels out of every 6 (on the contrary, Bayer filters don't have red and blue photosites in the same horizontal or vertical lines). 


