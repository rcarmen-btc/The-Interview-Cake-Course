from pathlib import Path


def file(p: Path):
    with open(str(p.absolute()), 'r+') as file:
        src = file.read()
        src.replace('[[')


def dir(p: Path):
    for obj in p.iterdir():
        if obj.name == '.git':
            continue
        elif obj.is_dir():
            dir(obj)
        else:
            file(obj)

if __name__ == '__main__':
    dir_path = './'

    p = Path(dir_path)
    dir(p)