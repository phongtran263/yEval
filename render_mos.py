#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")
    langs = {"vi": 0, "en": 1, "lw": 2}
    html = template.render(
        page_title="MOS test",
        form_url="https://script.google.com/macros/s/AKfycbz79ugrzOJXZ7ovv28gSEEFKxCw35nyzJJVxts889MRYDyxrurbIQkrEsj8ZKLqKzH1Ag/exec",
        form_id=1,
        questions=[
            {
                "title": str(i + 1 + langs[lang] * 5 + (j-1) * 15),
                "audio_path": f"wavs/exp{j}/{lang}/{i}.wav",
                "name": f"q{i}"
            } for j in range(1, 6) for lang in langs for i in range(5)
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
