import os
import subprocess


def main():
    print(os.getcwd())
    path = os.getcwd() + "/Java_Classes"
    command = "javap -c "

    for dirpath, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".class"):
                os.chdir(dirpath)
                print(os.getcwd())
                result = subprocess.run(
                    command + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print("Standard Output:")
                print(result.stdout)


if __name__ == "__main__":
    main()
