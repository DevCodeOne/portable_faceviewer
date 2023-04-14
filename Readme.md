# Usage

python gen_portable_faceviewer.py data/test.mtl data/test.obj data/test.jpg -t template.html -o index.html

list of files to replace in [template.html] to write into [index.html]

- binary files will be written into array list as bytes
- text files will be written in backticks '`' as string

Format to be replaced in files:

> /* <filename relative to exec path> here */