import json
import pathlib

PLAY_HTML = (
    pathlib.Path(__file__).resolve().parents[1]
    / "KAAVACH Smart Helmet Presentation"
    / "play.html"
)


def maybe_replace(text: str, old: str, new: str, *, expected_count: int) -> str:
    count = text.count(old)
    if count == 0:
        return text
    if count != expected_count:
        raise SystemExit(f"Expected {expected_count} occurrences of {old!r}, found {count}.")
    return text.replace(old, new)


def maybe_remove(text: str, old: str, *, expected_count: int) -> str:
    return maybe_replace(text, old, "", expected_count=expected_count)


def load_slides(play_html: str) -> tuple[list[str], int, int]:
    start = play_html.find("var SLIDES = ")
    if start == -1:
        raise SystemExit("Could not find 'var SLIDES = ' in play.html")
    start += len("var SLIDES = ")

    marker = "];\n        var iframe"
    end = play_html.find(marker, start)
    if end == -1:
        raise SystemExit("Could not find SLIDES array end marker in play.html")
    end += 1  # include closing ]

    slides = json.loads(play_html[start:end])
    return slides, start, end


def dump_slides(play_html: str, slides: list[str], start: int, end: int) -> str:
    # Important: `play.html` embeds SLIDES inside a `<script>` tag.
    # Any literal `</script>` inside slide HTML would prematurely terminate the script tag.
    arr = json.dumps(slides, ensure_ascii=False)
    arr = arr.replace("</script>", "<\\/script>")
    return play_html[:start] + arr + play_html[end:]


def patch_slide_3(slide_html: str) -> str:
    # Title + heading
    slide_html = slide_html.replace(
        "<title>KAAVACH Smart Helmet - About Team</title>",
        "<title>KAAVACH Smart Helmet - TEAM MEMBERS</title>",
    )
    slide_html = slide_html.replace(
        ">\\n                            About Team\\n                        </h1>",
        ">\\n                            TEAM MEMBERS\\n                        </h1>",
    )

    start_marker = "<!-- Team Points -->"
    photo_marker = "<!-- Photo Card (40% width) -->"
    s_idx = slide_html.find(start_marker)
    p_idx = slide_html.find(photo_marker, s_idx + 1)
    if s_idx == -1 or p_idx == -1:
        raise SystemExit("Could not locate Team Points block in slide 3.")

    members_block = """<!-- Team Points -->
                        <div class="flex flex-col gap-4">
                            <ul class="list-disc pl-6 text-lg font-normal text-white/90 leading-[1.7] space-y-2">
                                <li><span class="font-bold">Jitin Rajput</span> (202501100200168)</li>
                                <li><span class="font-bold">Kanishk Chinmay Singh</span> (202501100200174)</li>
                                <li><span class="font-bold">Kishika Singh</span> (202501100200182)</li>
                                <li><span class="font-bold">Kratika Jaiswal</span> (2025011002001840)</li>
                                <li><span class="font-bold">Mayank</span> (202501100200203)</li>
                            </ul>
                        </div>
                    </div>
"""

    return slide_html[:s_idx] + members_block + slide_html[p_idx:]


def main() -> None:
    play = PLAY_HTML.read_text(encoding="utf-8")
    slides, start, end = load_slides(play)

    # Slide 3 (index 2)
    slides[2] = patch_slide_3(slides[2])

    # Slide 8: keep text above image; remove helmet image (only that one).
    slides[7] = maybe_replace(
        slides[7],
        '<div class="hud-element ',
        '<div class="hud-element z-30 ',
        expected_count=6,
    )
    slides[7] = maybe_remove(
        slides[7],
        '<img src="assets/smart_helmet.png" alt="KAAVACH Smart Helmet Prototype" class="w-[420px] h-[400px] object-contain opacity-35 relative z-0 drop-shadow-[0_0_40px_rgba(59,130,246,0.4)] glow-pulse" data-editable="image">',
        expected_count=1,
    )

    # Slide 13: text replacements + remove helmet image (only that one).
    slides[12] = maybe_replace(slides[12], "Additional health monitoring sensors", "Smart camera integration", expected_count=1)
    slides[12] = maybe_replace(
        slides[12],
        "Integration of heart rate and temperature sensors for vital tracking.",
        "Real-time accident recording using onboard smart cameras for evidence collection and improved emergency response.",
        expected_count=1,
    )
    slides[12] = maybe_replace(slides[12], "Insurance and emergency services", "Alcohol detection and ignition control", expected_count=1)
    slides[12] = maybe_replace(
        slides[12],
        "Direct integration with insurance providers and first responders.",
        "Integrated alcohol sensor that detects intoxication levels and automatically prevents the bike from starting if alcohol is detected.",
        expected_count=1,
    )
    slides[12] = maybe_remove(
        slides[12],
        '<img src="assets/smart_helmet.png" alt="KAAVACH Smart Helmet Prototype" class="helmet-glow w-full h-full object-contain" style="animation: float 6s ease-in-out infinite;">',
        expected_count=1,
    )

    PLAY_HTML.write_text(dump_slides(play, slides, start, end), encoding="utf-8")
    print("Patched:", str(PLAY_HTML))


if __name__ == "__main__":
    main()

