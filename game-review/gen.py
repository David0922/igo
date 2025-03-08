import os


def main():
  for dir, _, files in os.walk(os.getcwd()):
    sgfs = sorted([f for f in files if f[-4:] == '.sgf'])
    if sgfs:
      sub_dir = dir.split('game-review/')[-1]
      with open(f'{dir}/README.md', 'w') as md:
        md.write('\n\n'.join(
          f'[{f}](https://raw.githubusercontent.com/David0922/igo/refs/heads/main/game-review/{sub_dir}/{f})'
          for f in sgfs))


if __name__ == '__main__':
  main()
