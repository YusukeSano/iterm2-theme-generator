import re


def validate_color_code(hex_str):
    """
    @param hex_str: Hex color code '#rrggbb', '#rrggbbaa'
    @return: Boolean
    """
    pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$"
    return bool(re.match(pattern, hex_str))


def has_alpha(hex_str):
    """
    @param hex_str: Hex color code '#rrggbb', '#rrggbbaa'
    @return: Boolean
    """
    pattern = r"^#([A-Fa-f0-9]{6})$|^#([A-Fa-f0-9]{8})$"
    match = re.match(pattern, hex_str)
    if match:
        return bool(match.group(2))
    else:
        raise ValueError("invalid color code")


def hex_to_rgba(hex_str):
    """
    @param hex_str: Hex color code '#rrggbb', '#rrggbbaa'
    @return: List of 0~255 color values [r, g, b], [r, g, b, a]
    """
    _has_alpha = has_alpha(hex_str)
    r = int(hex_str[1:3], 16)
    g = int(hex_str[3:5], 16)
    b = int(hex_str[5:7], 16)
    res = [r, g, b]
    if _has_alpha:
        res.append(int(hex_str[7:9], 16))
    return res
