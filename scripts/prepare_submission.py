"""Build the two source files used for the opening-report submission PDFs."""

from pathlib import Path
import re
import fitz


ROOT = Path(__file__).resolve().parents[1]
BODY = ROOT / "body"


def make_integrated_report() -> None:
    selection = (BODY / "selection-report.tex").read_text(encoding="utf-8")
    review = (BODY / "literature-review.tex").read_text(encoding="utf-8")

    review = review.split("\n", 1)[1].lstrip()
    review = re.sub(r"\\subsection\{", r"\\subsubsection{", review)
    review = re.sub(r"\\section\{", r"\\subsection{", review)
    review = review.replace(r"\subsection{本章小结}", r"\subsection{研究综述小结}")

    start = selection.index(r"\section{国内外研究综述}")
    end = selection.index(r"\section{研究问题与方法}", start)
    integrated = (
        selection[:start]
        + r"\section{国内外研究综述}" + "\n\n"
        + review.rstrip() + "\n\n"
        + selection[end:]
    )
    integrated = integrated.replace(
        r"\reportmodule{3}{三}{选题报告}",
        r"\reportmodule{1}{一}{选题报告}",
        1,
    )
    (BODY / "selection-report-integrated.tex").write_text(integrated, encoding="utf-8")

    cards = (BODY / "literature-cards.tex").read_text(encoding="utf-8")
    # \restoregeometry already starts a new page. An extra page-style command
    # before the next chapter produces an otherwise blank page.
    cards = cards.replace(
        r"\restoregeometry" + "\n" + r"\thispagestyle{empty}",
        r"\restoregeometry",
    )
    (BODY / "literature-cards-submission.tex").write_text(cards, encoding="utf-8")
    (BODY / "literature-cards-for-list.tex").write_text(
        cards.split(r"\restoregeometry", 1)[0].rstrip() + "\n",
        encoding="utf-8",
    )

    cover = (BODY / "cover.tex").read_text(encoding="utf-8")
    source_cover = ROOT / "figures" / "开题报告格式-Word导出.pdf"
    cleaned_cover = ROOT / "tmp" / "pdfs" / "cover-title-cleaned.pdf"
    cleaned_cover.parent.mkdir(parents=True, exist_ok=True)
    old_title = "大语言模型智能体故障诊断的证据链交互设计研究"
    cover_pdf = fitz.open(source_cover)
    for page_no in (0, 3):
        page = cover_pdf[page_no]
        matches = page.search_for(old_title)
        assert len(matches) == 1, (page_no, matches)
        page.add_redact_annot(matches[0], fill=(1, 1, 1))
        page.apply_redactions(images=0, graphics=0, text=0)
        assert not page.search_for(old_title)
    cover_pdf.save(cleaned_cover, garbage=4, deflate=True)
    cover_pdf.close()
    cover = cover.replace(
        "figures/开题报告格式-Word导出.pdf",
        "tmp/pdfs/cover-title-cleaned.pdf",
    )
    marker = r"\end{tikzpicture}%"
    parts = cover.split(marker)
    assert len(parts) == 3
    def check_mark(top: int) -> str:
        return (
            "\n  \\draw[line width=1.2pt] "
            rf"([xshift=186pt,yshift=-{top+10}pt]current page.north west) -- "
            rf"([xshift=190pt,yshift=-{top+15}pt]current page.north west) -- "
            rf"([xshift=198pt,yshift=-{top+3}pt]current page.north west);"
            "\n  "
        )
    # The report now contains the opening proposal only.
    cover = (
        parts[0] + check_mark(252) + marker
        + parts[1] + check_mark(199) + marker + parts[2]
    )
    (BODY / "cover-submission.tex").write_text(cover, encoding="utf-8")

    main = (ROOT / "main.tex").read_text(encoding="utf-8")
    old = "\\input{body/literature-review}\n\\input{body/selection-report}"
    assert old in main
    main = main.replace(old, r"\input{body/selection-report-integrated}")
    main = main.replace(
        r"\input{body/literature-cards}" + "\n",
        "",
    )
    main = main.replace(r"\input{body/cover}", r"\input{body/cover-submission}")
    (ROOT / "main-submission.tex").write_text(main, encoding="utf-8")


def make_reading_list() -> None:
    cards = (BODY / "literature-cards.tex").read_text(encoding="utf-8")
    serials = re.findall(r"序号：(\d\d)", cards)
    assert serials == [f"{i:02d}" for i in range(1, 41)], serials

    bib = (ROOT / "ref" / "report.bib").read_text(encoding="utf-8")
    keys = re.findall(r"^@\w+\{(ref\d\d),", bib, re.M)
    assert all(f"ref{i:02d}" in keys for i in range(1, 41))

    citations = "\n".join(rf"\nocite{{ref{i:02d}}}" for i in range(1, 41))
    source = r"""\documentclass[oneside,finalformat,mathCMR]{HUSTthesis}
\usepackage{HUSTtils}
\usepackage{geometry}
\geometry{left=1in,right=1in,top=.6in,bottom=.6in}
\setmainfont{Times New Roman}
\ExecuteBibliographyOptions{sorting=none}
\addbibresource[location=local]{ref/report.bib}
\begin{document}
\begin{center}
{\song\bfseries\erhao 精读文献清单\par}
\vspace{0.6em}
{\song\xiaosi 姓名：陈思静\qquad 学号：M202570493\qquad 共40篇\par}
\end{center}
\vspace{0.6em}
\begingroup
\small
\setstretch{1.0}
\setlength{\bibitemsep}{0pt}
\interlinepenalty=10000
""" + citations + r"""
\printbibliography[heading=none]
\endgroup
\input{body/literature-cards-for-list}
\end{document}
"""
    (ROOT / "reading-list.tex").write_text(source, encoding="utf-8")


if __name__ == "__main__":
    make_integrated_report()
    make_reading_list()
