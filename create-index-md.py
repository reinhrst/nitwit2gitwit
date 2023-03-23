import pathlib
import typing as t

selfpath = pathlib.Path(__file__).parent
distpath = selfpath / "dist"
index_md_file = distpath / "index.md"
md_files = sorted(distpath.glob("*/*.md"))
output: t.MutableSequence[str] = []
lastfile = None
for file in md_files:
    rel_file = file.relative_to(distpath)
    if lastfile is None or lastfile.parent != file.parent:
        if lastfile is not None:
            output.append("\nvvvvvv\n")
        output.append(f"# Lesson {rel_file.parent}\n")
    lastfile = file
    output.append(f"- [{rel_file.stem}](/index.html?markdown-url={rel_file})")

index_md_file.write_text("\n".join(output))
