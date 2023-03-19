import yaml

from posui import Posui


def main():
    with open("scripts/test/answerkey.yaml") as file:
        posts = yaml.safe_load(file)

    for idx, expected in enumerate(posts):
        print(f">>>{idx}: {expected['url']}")

        posui = Posui(expected["url"])

        info = posui.blog_info
        tags, images = posui.post_tags_images
        print(info)
        print(tags)
        for img in images:
            print(img)

        assert info == expected["info"]
        assert tags == expected["tags"]
        assert images == expected["images"]

        print(">>> all good!!!")


if __name__ == "__main__":
    main()
