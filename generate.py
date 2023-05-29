import argparse
import json
import lib.generator as generator

parser = argparse.ArgumentParser(
    prog="iTerm2ThemeGenerator",
    description="Generate theme for iTerm2",
    add_help=True,
)
parser.add_argument(
    "--theme",
    nargs="?",
    help="name of theme file to import",
    type=argparse.FileType("r"),
)
parser.add_argument(
    "--light",
    nargs="?",
    help="name of light_theme file to import",
    type=argparse.FileType("r"),
)
parser.add_argument(
    "--dark",
    nargs="?",
    help="name of dark_theme file to import",
    type=argparse.FileType("r"),
)
parser.add_argument(
    "--export",
    nargs="?",
    default="export",
    help="name of theme file to export",
)
args = parser.parse_args()

if args.theme != None:
    theme = json.load(args.theme)
    generator.save_plist_from_dict(generator.gen_scheme(theme), args.export)

if args.light != None and args.dark != None:
    light_theme = json.load(args.light)
    dark_theme = json.load(args.dark)
    generator.save_plist_from_dict(
        {
            **generator.gen_scheme(light_theme, " (Light)"),
            **generator.gen_scheme(dark_theme, " (Dark)"),
        },
        args.export,
    )
