import json
import plistlib
import lib.color as color


def save_plist_from_dict(dictionary, filename="theme"):
    """
    @param dictionary: Dictionary
    @param filename: File name to save
    """
    with open(f"{filename}.itermcolors", "wb") as fp:
        plistlib.dump(dictionary, fp)


def gen_scheme(theme_dict, suffix=""):
    """
    @param theme_dict: Theme Dictionary
    @param suffix: Suffix of key
    @return: Color scheme Dictionary
    """
    with open("lib/convert_map.json", "r") as file:
        convert_map = json.load(file)
    component_dict = {
        0: "Red Component",
        1: "Green Component",
        2: "Blue Component",
        3: "Alpha Component",
    }
    scheme_dict = {}
    for group in convert_map.keys():
        for key, value in convert_map[group].items():
            color_hex = theme_dict[group][key]
            if color.validate_color_code(color_hex):
                scheme_key = value + suffix
                scheme_dict[scheme_key] = {}
                scheme_dict[scheme_key].update({"Color Space": "sRGB"})
                for i, v in enumerate(
                    [i / 255.0 for i in color.hex_to_rgba(color_hex)]
                ):
                    scheme_dict[scheme_key].update({component_dict[i]: v})
    return scheme_dict
