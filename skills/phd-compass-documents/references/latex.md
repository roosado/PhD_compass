# Building LaTeX documents

Templates: `assets/latex/cv.tex`, `letter.tex`, `proposal.tex`, all loading `assets/latex/phd-compass.sty` from the same folder. Copy the `.sty` next to every `.tex` you write.

## Options
`\usepackage[letterpaper]{phd-compass}` for US Letter (default A4); `[compact]` tightens section spacing when a page limit is close.

## Build
1. Check for a TeX installation: `latexmk -v` or `pdflatex --version`.
2. With TeX: `latexmk -pdf -interaction=nonstopmode <file>.tex` (or `pdflatex` twice). Run it in the document's folder.
3. Read the log: fix every `Error`, and every `Overfull \hbox` by rewording or allowing a break (not by shrinking fonts). Then check the page count against the limit (`Output written on … (N pages)`).
4. Remove build clutter (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.out`) from the outputs in chat mode, keeping the `.tex`, `.sty` and `.pdf`.

## No TeX available (usual in chat)
Deliver the `.tex` and `phd-compass.sty` together and give the owner these steps:
1. On Overleaf, create a blank project.
2. Upload both files, replacing `main.tex` or setting the uploaded file as the main document.
3. Set the compiler to pdfLaTeX, recompile, and download the PDF.
Say that the page count and overfull-box checks were not run, and ask the owner to report the page count.

## Writing LaTeX safely
- Escape `& % $ # _ { } ~ ^ \` in text (`\&`, `\%`, `\$`, `\#`, `\_`, `\{`, `\}`, `\textasciitilde{}`, `\textasciicircum{}`, `\textbackslash{}`).
- Accented letters can be typed directly (the style loads UTF-8 input).
- Dates as en-dash ranges: `2024-09 -- 2026-06`.
- Links: `\href{https://…}{text}`; email: `\href{mailto:…}{…}`.
