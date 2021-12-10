Please navigate to the root difrectory of the project to run the followings:

## Solution

See original [google code competition](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004) for the details of the challenge.

My solution parses the dictionary file first to build up a python dictionary. A dictionary item `axpaj` should generate the following key-value pair in the internal python directory:
```{python}
'a': [{'middle': 'apx', 'lastChar': 'j', 'original': 'axpaj', 'len': 5, 'used': False}]
```
where the key `a` is derived from the first letter of the item. It allows us to look up items fast based on their first letter.

Processing the input file is straightforward. The program iterates through all the letters of the given input line and tries to match one or more dictionary items starting with the current letter. The internal part of the item is normalized (ordered alphabetically) before comparison to implement the 'scrambled' version of match. The normalized internal part is stored in the 'middle' property of the dictionary item (see above). Matches are counted and displayed for every line. Matched items are marked (`'used'=True`) to prevent double counting. Match count and markers are reset for every line.

I'm not aware of any non-functional requirements. Let me know if this solution is not fast enough.

## Usage

Documentation of the CLI interface is available via the following command:
`python scrambled-strings.py --help`

```{bash}
usage: scrambled-strings.py [-h] [--dictionary DICT] [--input INPUT]

Count scrambled occurrences of dictionary items for each input line.

optional arguments:
  -h, --help         show this help message and exit
  --dictionary DICT  path of dictionary file
  --input INPUT      path of input file
```

## Test

`python test`

## Build

Let's presume `pyinstaller` is installed properly.
(Execute `pip install pyinstaller` otherwise.)
The following command runs on both Win and Unix distributions.

```{bash}
pyinstaller --distpath ./dist scrambled-strings.py --onefile
```

## Docker
I used [docker-pyinstaller](https://github.com/cdrx/docker-pyinstaller) to implement this feature. Docker files cover many python versions and register sizes:

File suffix  | Register width | Guest distribution
---------- | -------------- | ------------
py2-amd64  | 64             | FROM ubuntu:12.04
py2-win32  | 32             | FROM ubuntu:14.04
py3-amd64  | 64             | FROM ubuntu:12.04
py3-i386   | 32             | FROM i386/ubuntu:12.04
py3-win64  | 64             | FROM ubuntu:16.04
py3-win32  | 32             | FROM ubuntu:16.04


Since Windows Server 2016 comes packaged with a base image of the Ubuntu OS, ubuntu images can run over Windows too.

### create new image from modified docker file

I focus only on the py3-amd64 version.

Build docker image from dockerfile:
`docker build ./docker/`

Run image
`docker run [IMG_NAME]`

### use remote docker image to build project

Generate .`.spec` file:
`docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux "pyinstaller scrambled-strings.py"`

Build project into `dist` folder using `.spec` file
docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux

## Notes

Unfortunately, my Ubuntu PC is not fully functional.
I have package installation problems (ubuntu updates, pyinstaller).
This problem affects the docker image build process as well.
So, the docker-related section must be incomplete since it hasn't been tested yet.
