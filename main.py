import json
import re
import sys


def usage():
    print("Usage: main.py ChannelData.json")


def parse_and_gen_playlist(data_file: str):
    reduced_channel_data = []

    with open(data_file, "r", encoding="utf-8") as input_f:
        channel_data = json.load(input_f)

        if channel_data is not None:
            for channel in channel_data:
                playlist_item = {
                    "title": channel["name"],
                    "url": re.split("&", channel["uAddress"])[0],
                    "no": channel["sort"]
                }

                reduced_channel_data.append(playlist_item)  # type: ignore
        else:
            print("Failed to parse.")

    with open("channels.m3u8", mode="w", encoding="utf-8") as output_f:
        # header
        output_f.write("#EXTM3U\n\n")

        for channel in reduced_channel_data:
            output_f.write(
                f"#EXTINF:-1, {channel['title']}\n")

            output_f.write(channel["url"])
            output_f.write("\n")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    else:
        parse_and_gen_playlist(sys.argv[1])
