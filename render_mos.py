#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS test",
        form_url="https://script.google.com/macros/s/AKfycbz79ugrzOJXZ7ovv28gSEEFKxCw35nyzJJVxts889MRYDyxrurbIQkrEsj8ZKLqKzH1Ag/exec",
        form_id=1,
        questions=[
            {
                "title": "1",
                "audio_path": "wavs/exp4/en/0.wav",
                "name": "q1"
            },
            {
                "title": "2",
                "audio_path": "wavs/exp4/en/1.wav",
                "name": "q2"
            },
            {
                "title": "3",
                "audio_path": "wavs/exp4/en/2.wav",
                "name": "q3"
            },
            {
                "title": "4",
                "audio_path": "wavs/exp4/en/3.wav",
                "name": "q4"
            },
            {
                "title": "5",
                "audio_path": "wavs/exp4/en/4.wav",
                "name": "q5"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
