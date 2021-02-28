from PIL import Image, ImageEnhance
import os


ASCII11 = ["@", "#", "S", "%", "?", "*", ";", ":", ",", ".", " "]


# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

ASCII70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def img_to_gray(image):
    gray = image.convert("L")
    return gray


def pixels_to_ascii(image, selected_ascii):
    pixels = image.getdata()
    asc = ASCII11

    if selected_ascii == 2:
        asc = ASCII70

    chars = []

    d = int(255 / len(asc))

    for pixel in pixels:
        idx = pixel // d
        if idx >= len(asc):
            idx = len(asc) - 1
        chars.append(asc[idx])

    return "".join(chars)


def enhance_image(image):
    enhancer = ImageEnhance.Contrast(image)
    enhanced = enhancer.enhance(2)
    return enhanced


def load_images_from_folder(folder):
    images = []
    names = []
    for filename in os.listdir(folder):
        img = Image.open(folder + filename)
        if img is not None:
            images.append(img)
            base = os.path.basename(folder + filename)
            names.append(os.path.splitext(base)[0])

    return images, names


def generate_ascii(image, name, ascii_dir, new_width, ascii):

    enhanced = enhance_image(image)
    resized = resize_image(enhanced, new_width)
    gray = img_to_gray(resized)

    new_image_data = pixels_to_ascii(gray, ascii)
    count = len(new_image_data)

    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, count, new_width))

    with open(ascii_dir + name + ".txt", "w") as f:
        f.write(ascii_image)


def main():
    try:
        images, names = load_images_from_folder("./photos/")
        ascii_dir = "./generated_ascii/"

        print("Enter desired width in px:")
        new_width = int(input())

        print("Choose desired ascii scheme (1 or 2, leave empty for default):")
        ascii = input()

        if ascii == '':
            ascii = 1
        else:
            ascii = int(ascii)

        if not os.path.exists(ascii_dir):
            os.mkdir(ascii_dir)

        for i in range(0, len(images)):
            generate_ascii(images[i], names[i], ascii_dir, new_width, ascii)

        print("Great success!")

    except:
        print("Stonks, looks like you did some dumb shit D: Read the --> readme.md <--")


if __name__ == "__main__":
    main()
