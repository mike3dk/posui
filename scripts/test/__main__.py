from posui import Posui


def main():
    url = "https://blog.naver.com/yoriteacher/223042800348"
    posui = Posui(url)
    info = posui.info
    print(info)
    tags, images = posui.tags_images
    print(tags)
    print(images)


if __name__ == "__main__":
    main()
