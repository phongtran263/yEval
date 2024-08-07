#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")
    langs = {"vi": 0, "en": 1, "lw": 2}
    html = template.render(
        page_title="MOS test",
        form_url="https://script.google.com/macros/s/AKfycbxMN-aoHQGyYJTg8HU1T64UC4wG-UWmvTI-8xdI2ekVGNqj8Hbam0XyFT5XlAfYF5qw_A/exec",
        form_id=1,
        questions=[
            {
                "title": str(i + 1 + langs[lang] * 5 + (j-1) * 15),
                "audio_path": f"wavs/exp{j}/{lang}/{i}.wav",
                "name": f"q{str(i + 1 + langs[lang] * 5 + (j-1) * 15)}"
            } for j in range(1, 4) for lang in langs for i in range(5)
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
