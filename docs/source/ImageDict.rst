.. ImageMetaTag documentation for ImageMetaTag.ImageDict

ImageMetaTag.ImageDict
======================

.. automodule:: ImageMetaTag.img_dict

The ImageDict Class
-------------------

.. autoclass:: ImageMetaTag.ImageDict
   :members:
      
Functions useful in preparing ImageDicts
----------------------------------------

.. autofunction:: ImageMetaTag.readmeta_from_image
.. autofunction:: ImageMetaTag.dict_heirachy_from_list
.. autofunction:: ImageMetaTag.dict_split
.. autofunction:: ImageMetaTag.simple_dict_filter
.. autofunction:: ImageMetaTag.check_for_required_keys

.. _ImgDictPayloadNotes:
Image Payloads and how to prepare them
--------------------------------------

A simple example where a web page is built with an ImageDict is :ref:`simplest` example. In that case, we cycle through all of the images, where each image has adds the path through the metadata to get browse to it, and the final 'payload' is a single image:

.. code-block:: python
		
    '''
    A code snippet example showing the sort of code to produce a simple
    image browser for single images
    '''
    # these are the image tags that are present in the metadata, and
    # the sort order we want to present them with on a web page:
    img_tags = ['metadata type 1', 'type 2', 'type 3'...]

    # now assemble the ImageDict in the simple way. See test.py for parallel versions etc.
    img_dict = None
    for img_file, img_info in images_and_tags.iteritems():
        # img_file : the relative path to the image file
	# img_info : a dictionary of all the metadata about this image
	#
        # make a temporary ordered dictionary for this image:
        tmp_dict = imt.dict_heirachy_from_list(img_info, img_file, img_tags)
        if img_dict is None:
            # turn it into an ImageDict
            img_dict = imt.ImageDict(tmp_dict, options=....)
        else:
            # append this tmp_dict to the ImageDict
            img_dict.append(imt.ImageDict(tmp_dict))

	    
This approach quickly produces simple web pages, where a single image can be browsed at a time. As long as the metadata combinations for each image is unique, every image can be browsed. However the ImageDict webpages can support more advanced 'payloads':

Dropdown webpages
^^^^^^^^^^^^^^^^^
The dropdown webpage supports payloads that contain:
 #. strings, specifying the relative path to single images to be displayed.
 #. A list of strings, or pairs of images in a list/tuple. These will be displayed for side-by-side comparison when the dropdown menus select the given metadata options.
    #. Pairs of images within this list are explicitly set sliders, where the first image is the 'main' image and the second image is one to be overlaid/slid over.


Preparation Notes
^^^^^^^^^^^^^^^^^
In order to prepare side-by-side comparisons or sliders it is usually worth preparing a ImageDict to group all of the same images, into the same tree structure, but without any comparions etc. and then use that as an input when preparing a second ImageDict, as use it to reference the images to add to the list, or pairs, for side-by-side comparison. An example of this can be found in test_make_img_dict_sliders() in test.py.

A side-by-side comparison, is worked through in test.py in the variable img_dict_multi. This example is also processed in parallel, which is neccessary for very large pages. However this scales well up to pages with multiple millions of images.
