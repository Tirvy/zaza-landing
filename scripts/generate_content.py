# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def u(*codes: int) -> str:
    return "".join(chr(c) for c in codes)


# Georgian fragments via codepoints to avoid editor encoding issues
KA = {
    "stp": u(0x10E2, 0x10D4, 0x10E5, 0x10E1, 0x10E2, 0x10D8, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10DB, 0x10D0, 0x10E0, 0x10E7, 0x10E3, 0x10DF, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20, 0x10E1, 0x10E2, 0x10E0, 0x10DD, 0x10DE, 0x10D8, 0x20)
    + "\u0421\u0422\u041f",
    "stk": u(0x10E2, 0x10D4, 0x10E5, 0x10E1, 0x10E2, 0x10D8, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10E0, 0x10D2, 0x10DD, 0x10DA, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20, 0x10E1, 0x10E2, 0x10E0, 0x10DD, 0x10DE, 0x10D8, 0x20)
    + "\u0421\u0422\u041a",
    "stk_p": u(0x10DB, 0x10E0, 0x10D2, 0x10D5, 0x10D0, 0x10DA, 0x10D7, 0x10DD, 0x10D9, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20, 0x10DB, 0x10D0, 0x10E0, 0x10E7, 0x10E3, 0x10DF, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "\u0421\u0422\u041a\u043f",
    "stk_k": u(0x10DB, 0x10E0, 0x10D2, 0x10D5, 0x10D0, 0x10DA, 0x10D7, 0x10DD, 0x10D9, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20, 0x10E0, 0x10D2, 0x10DD, 0x10DA, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "\u0421\u0422\u041a\u043a",
    "2st": u(0x10E2, 0x10D4, 0x10E5, 0x10E1, 0x10E2, 0x10D8, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10DD, 0x10E0, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "2\u0421\u0422",
    "4st": u(0x10E2, 0x10D4, 0x10E5, 0x10E1, 0x10E2, 0x10D8, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10DD, 0x10D7, 0x10EE, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "4\u0421\u0422",
    "1sc": u(0x10EF, 0x10D0, 0x10ED, 0x10D5, 0x10D8, 0x10E1, 0x20, 0x10D4, 0x10E0, 0x10D7, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "1\u0421\u0426",
    "2sc": u(0x10EF, 0x10D0, 0x10ED, 0x10D5, 0x10D8, 0x10E1, 0x20, 0x10DD, 0x10E0, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "2\u0421\u0426",
    "4sc": u(0x10EF, 0x10D0, 0x10ED, 0x10D5, 0x10D8, 0x10E1, 0x20, 0x10DD, 0x10D7, 0x10EE, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "4\u0421\u0426",
    "skp": u(0x10D9, 0x10D0, 0x10D1, 0x10D4, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10DB, 0x10D0, 0x10E0, 0x10E7, 0x10E3, 0x10DF, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "\u0421\u041a\u041f",
    "1sk": u(0x10D9, 0x10D0, 0x10D1, 0x10D4, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10D4, 0x10E0, 0x10D7, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "1\u0421\u041a",
    "4sk": u(0x10D9, 0x10D0, 0x10D1, 0x10D4, 0x10DA, 0x10D8, 0x10E1, 0x20, 0x10DD, 0x10D7, 0x10EE, 0x10E2, 0x10DD, 0x10E2, 0x10D8, 0x10D0, 0x10DC, 0x10D8, 0x20)
    + "4\u0421\u041a",
}

DOC_KA = {
    "stp": KA["stp"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "stk": KA["stk"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "2st": KA["2st"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "1sc": KA["1sc"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "2sc": KA["2sc"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "4sc": KA["4sc"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "skp": KA["skp"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
    "1sk": KA["1sk"] + " \u2014 " + u(0x10DE, 0x10D0, 0x10E1, 0x10DE, 0x10DD, 0x10E0, 0x10E2, 0x10D8),
}


def make_pdf(title: str) -> bytes:
    safe = title.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    stream = f"BT /F1 18 Tf 72 720 Td ({safe}) Tj ET".encode("latin-1", errors="replace")
    objects = [
        b"1 0 obj<< /Type /Catalog /Pages 2 0 R >>endobj\n",
        b"2 0 obj<< /Type /Pages /Kids [3 0 R] /Count 1 >>endobj\n",
        b"3 0 obj<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>endobj\n",
        f"4 0 obj<< /Length {len(stream)} >>stream\n".encode("latin-1")
        + stream
        + b"\nendstream\nendobj\n",
        b"5 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>endobj\n",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for obj in objects:
        offsets.append(len(out))
        out.extend(obj)
    xref_pos = len(out)
    out.extend(f"xref\n0 {len(offsets)}\n".encode("latin-1"))
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode("latin-1"))
    out.extend(
        f"trailer<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode(
            "latin-1"
        )
    )
    return bytes(out)


def main() -> None:
    products = [
        {
            "id": "stp",
            "category": "textile",
            "image": "images/sling-textile-loop.svg",
            "availability": "on_order",
            "priceFrom": 15,
            "name": {
                "ka": KA["stp"],
                "ru": "Стропы текстильные петлевые СТП",
                "en": "Textile loop sling STP",
            },
        },
        {
            "id": "stk",
            "category": "textile",
            "image": "images/sling-textile-round.svg",
            "availability": "in_stock",
            "priceFrom": 15,
            "name": {
                "ka": KA["stk"],
                "ru": "Стропы текстильные кольцевые СТК",
                "en": "Textile round sling STK",
            },
        },
        {
            "id": "stk-p",
            "category": "textile",
            "image": "images/sling-textile-loop.svg",
            "availability": "in_stock",
            "priceFrom": 28,
            "name": {
                "ka": KA["stk_p"],
                "ru": "Стропы текстильные круглопрядные петлевые СТКп",
                "en": "Round-strand loop sling STKp",
            },
        },
        {
            "id": "stk-k",
            "category": "textile",
            "image": "images/sling-textile-round.svg",
            "availability": "on_order",
            "priceFrom": None,
            "name": {
                "ka": KA["stk_k"],
                "ru": "Стропы текстильные круглопрядные кольцевые СТКк",
                "en": "Round-strand endless sling STKk",
            },
        },
        {
            "id": "2st",
            "category": "textile",
            "image": "images/sling-textile-loop.svg",
            "availability": "in_stock",
            "priceFrom": 145,
            "name": {
                "ka": KA["2st"],
                "ru": "Строп текстильный 2СТ",
                "en": "Two-leg textile sling 2ST",
            },
        },
        {
            "id": "4st",
            "category": "textile",
            "image": "images/sling-textile-loop.svg",
            "availability": "on_order",
            "priceFrom": 210,
            "name": {
                "ka": KA["4st"],
                "ru": "Строп текстильный 4СТ",
                "en": "Four-leg textile sling 4ST",
            },
        },
        {
            "id": "1sc",
            "category": "chain",
            "image": "images/sling-chain.svg",
            "availability": "in_stock",
            "priceFrom": 95,
            "name": {
                "ka": KA["1sc"],
                "ru": "Строп цепной одноветвевой 1СЦ",
                "en": "Single-leg chain sling 1SC",
            },
        },
        {
            "id": "2sc",
            "category": "chain",
            "image": "images/sling-chain.svg",
            "availability": "in_stock",
            "priceFrom": 160,
            "name": {
                "ka": KA["2sc"],
                "ru": "Строп цепной двухветвевой 2СЦ",
                "en": "Two-leg chain sling 2SC",
            },
        },
        {
            "id": "4sc",
            "category": "chain",
            "image": "images/sling-chain.svg",
            "availability": "on_order",
            "priceFrom": 320,
            "name": {
                "ka": KA["4sc"],
                "ru": "Строп цепной четырехветвевой 4СЦ",
                "en": "Four-leg chain sling 4SC",
            },
        },
        {
            "id": "skp",
            "category": "rope",
            "image": "images/sling-rope.svg",
            "availability": "in_stock",
            "priceFrom": 28,
            "name": {
                "ka": KA["skp"],
                "ru": "Строп канатный петлевой СКП",
                "en": "Wire-rope loop sling SKP",
            },
        },
        {
            "id": "1sk",
            "category": "rope",
            "image": "images/sling-rope.svg",
            "availability": "in_stock",
            "priceFrom": 55,
            "name": {
                "ka": KA["1sk"],
                "ru": "Строп канатный одноветвевой 1СК",
                "en": "Single-leg wire-rope sling 1SK",
            },
        },
        {
            "id": "4sk",
            "category": "rope",
            "image": "images/sling-rope.svg",
            "availability": "on_order",
            "priceFrom": None,
            "name": {
                "ka": KA["4sk"],
                "ru": "Строп канатный четырехветвевой 4СК",
                "en": "Four-leg wire-rope sling 4SK",
            },
        },
    ]

    documents = [
        {
            "id": "passport-stp",
            "file": "documents/passport-stp.pdf",
            "title": {
                "ka": DOC_KA["stp"],
                "ru": "Стропы текстильные петлевые СТП — паспорт",
                "en": "Textile loop sling STP — passport",
            },
        },
        {
            "id": "passport-stk",
            "file": "documents/passport-stk.pdf",
            "title": {
                "ka": DOC_KA["stk"],
                "ru": "Стропы текстильные кольцевые СТК — паспорт",
                "en": "Textile round sling STK — passport",
            },
        },
        {
            "id": "passport-2st",
            "file": "documents/passport-2st.pdf",
            "title": {
                "ka": DOC_KA["2st"],
                "ru": "Строп текстильный 2СТ — паспорт",
                "en": "Two-leg textile sling 2ST — passport",
            },
        },
        {
            "id": "passport-1sc",
            "file": "documents/passport-1sc.pdf",
            "title": {
                "ka": DOC_KA["1sc"],
                "ru": "Строп цепной одноветвевой 1СЦ — паспорт",
                "en": "Single-leg chain sling 1SC — passport",
            },
        },
        {
            "id": "passport-2sc",
            "file": "documents/passport-2sc.pdf",
            "title": {
                "ka": DOC_KA["2sc"],
                "ru": "Строп цепной двухветвевой 2СЦ — паспорт",
                "en": "Two-leg chain sling 2SC — passport",
            },
        },
        {
            "id": "passport-4sc",
            "file": "documents/passport-4sc.pdf",
            "title": {
                "ka": DOC_KA["4sc"],
                "ru": "Строп цепной четырехветвевой 4СЦ — паспорт",
                "en": "Four-leg chain sling 4SC — passport",
            },
        },
        {
            "id": "passport-skp",
            "file": "documents/passport-skp.pdf",
            "title": {
                "ka": DOC_KA["skp"],
                "ru": "Строп канатный петлевой СКП — паспорт",
                "en": "Wire-rope loop sling SKP — passport",
            },
        },
        {
            "id": "passport-1sk",
            "file": "documents/passport-1sk.pdf",
            "title": {
                "ka": DOC_KA["1sk"],
                "ru": "Строп канатный одноветвевой 1СК — паспорт",
                "en": "Single-leg wire-rope sling 1SK — passport",
            },
        },
    ]

    (ROOT / "data" / "products.json").write_text(
        json.dumps(products, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "data" / "documents.json").write_text(
        json.dumps(documents, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    docs_dir = ROOT / "documents"
    docs_dir.mkdir(exist_ok=True)
    pdfs = [
        ("passport-stp.pdf", "Zaza passport STP"),
        ("passport-stk.pdf", "Zaza passport STK"),
        ("passport-2st.pdf", "Zaza passport 2ST"),
        ("passport-1sc.pdf", "Zaza passport 1SC"),
        ("passport-2sc.pdf", "Zaza passport 2SC"),
        ("passport-4sc.pdf", "Zaza passport 4SC"),
        ("passport-skp.pdf", "Zaza passport SKP"),
        ("passport-1sk.pdf", "Zaza passport 1SK"),
    ]
    for filename, title in pdfs:
        (docs_dir / filename).write_bytes(make_pdf(title))

    print(f"Wrote {len(products)} products, {len(documents)} documents, {len(pdfs)} PDFs")


if __name__ == "__main__":
    main()
