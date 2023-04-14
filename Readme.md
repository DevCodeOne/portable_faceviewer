# Usage

python gen_portable_faceviewer.py data/test.mtl data/test.obj data/test.jpg -t template.html -o index.html

list of files to replace in [template.html] to write into [index.html]

- binary files will be written as base64 encoded string, a byte array wasn't helpful when trying to store as image
- text files will be written in backticks '`' as string

Format to be replaced in files:

```
/* <filename relative to exec path> here */
```

# Example

## Input template.html

```
const blob1 = new Blob([/* data/test.obj here */]);
const blob2 = new Blob([/* data/test.mtl here */]);
const imageData = new Uint8Array([/* data/test.jpg here */]);
```

## Command

```
python gen_portable_faceviewer.py data/test.mtl data/test.obj data/test.jpg -t template.html -o index.html
```

## Output index.html

```
const blob1 = new Blob([`mtllib test.mtl
v 0.000000 0.000000 -1.500000
v 0.000000 0.000000 -1.500000
...
]);
...
const imageData = new Uint8Array([0xff, 0xd8, 0xff, 0xe1, ....]);
```
