# iTerm2 Theme Generator

## Overview

iTerm2 Theme Generator is a Python3 program that allows you to generate color themes for [iTerm2](https://iterm2.com).

By providing a template file with hex color codes, you can create custom color themes.

## Usage

Create your theme from `theme_template.json`.  
The color codes should be in the format `#rrggbb` or `#rrggbbaa`.

Generate a single theme:

```shell
python generate.py --theme [theme_file.json]
```

Generate a theme with both light and dark modes:

```shell
python generate.py --light [light_theme_file.json] --dark [dark_theme_file.json]
```

> [!IMPORTANT]
> Themes with both light and dark modes are only available in iTerm2@3.5 or later versions.

## Arguments

The program accepts the following arguments:

- `-h`, `--help`: Displays the help message.
- `--theme [json]`: Specifies the input JSON file for generating a single theme.
- `--light [json]`: Specifies the input JSON file for generating the light mode theme.
- `--dark [json]`: Specifies the input JSON file for generating the dark mode theme.
- `--export [filename]`: Specifies the output theme file name.

## Example

Here is an example command to generate the [Iceberg](https://cocopon.github.io/iceberg.vim) theme:

```shell
python generate.py --light example/iceberg_light.json --dark example/iceberg_dark.json --export "Iceberg"
```

When you run this command, it will generate an `Iceberg.itermcolors` file.

The actual `Iceberg.itermcolors` file can be found in [Iceberg for iTerm2](https://github.com/YusukeSano/iterm2-iceberg).

## License

iTerm2 Theme Generator is released under a free and open-source license. You are welcome to contribute to the project and make any modifications or enhancements.

## Contribute

Contributions to iTerm2 Theme Generator are highly appreciated. If you'd like to contribute, feel free to submit a pull request or report issues. Together, we can make this program even better!
