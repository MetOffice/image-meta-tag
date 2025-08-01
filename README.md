ImageMetaTag is a python package built around a wrapper for savefig in matplotlib, which adds metadata tags to supported image file formats.

Once the images have been tagged, it can also be used to manage an SQL database of images and their metadata. The image metadata can be used to produce an ImageMetaTag.ImageDict object: a structured/heirachical dictionary of dictionaries which can be used to easily create web pages to present large numbers of images.

As the image metadata tagging process involves reading the image using the Image library, a few common image post-processing options are included such as cropping, logo addition and colour palette manipulation to reduce filesizes.

All ImageMetaTag source code, unless explicitly stated, is © British Crown copyright, 2015-2023 and is released under a [BSD 3-Clause License](LICENSE). Details on how to contribute to ImageMetaTag are given [here](CONTRIBUTING.md).

The file ImageMetaTag/javascript/pako_inflate.js has been copied from [pako](https://github.com/nodeca/pako "pako") and is © 2014-2017 by Vitaly Puzrin and Andrei Tuputcyn and released under a MIT License, detailed within the file.

The files ImageMetaTag/javascript/img_comparison_slider_styles.css and ImageMetaTag/javascript/img_comparison_slider_styles.js have been copied from [img-compatison-slider](https://github.com/sneas/img-comparison-slider "img-compatison-slider") and is © 2019 by Dmytro Snisarenko and released under a MIT License, detailed within the files.

Supported image file formats: png

Documentation is available via [GitHub Pages](http://metoffice.github.io/image-meta-tag/build/html/index.html "ImageMetaTag Documentation on GitHub Pages")
