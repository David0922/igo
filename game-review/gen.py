import os
from collections import defaultdict


def main():
  sgf = defaultdict(list)
  for dir, _, files in os.walk(os.getcwd()):
    for f in files:
      if f[-4:] == '.sgf':
        sgf[dir].append(f)
  for dir, sgfs in sgf.items():
    sub_dir = dir.split('game-review/')[-1]
    sgfs.sort()
    with open(f'{dir}/README.md', 'w+') as md:
      md.write('\n\n'.join(
        f'[{f}](https://raw.githubusercontent.com/David0922/igo/refs/heads/main/game-review/{sub_dir}/{f})'
        for f in sgfs))


if __name__ == '__main__':
  main()
