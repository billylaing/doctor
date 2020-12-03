import io


def pdf_bytes_from_images(image_list):
    """Make a pdf given an array of Image files

    :param image_list: List of images
    :type image_list: list
    :return: pdf_data
    :type pdf_data: PDF as bytes
    """
    with io.BytesIO() as output:
        image_list[0].save(
            output,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=image_list[1:],
        )
        pdf_data = output.getvalue()

    return pdf_data


def convert_tiff_to_pdf_bytes(single_tiff_image):
    """

    :param single_tiff_image:
    :return:
    """
    width, height = single_tiff_image.size
    image_list = []
    i, page_width, page_height = 0, width, (1046 * (float(width) / 792))
    while i < (height / page_height):
        single_page = single_tiff_image.crop(
            (0, (i * page_height), page_width, (i + 1) * page_height)
        )
        image_list.append(single_page)
        i += 1

    return pdf_bytes_from_images(image_list)
