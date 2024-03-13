import os


def show_data_list(dir):
    if not os.path.isdir(dir):
        return None

    files = os.listdir(dir)
    print(f"ls {dir}:")
    for file in files:
        print(file)


# show_data_list("src/data/initial")

ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_ROOT = os.path.join(ROOT, "data", "initial")
# print(ROOT)
# print(DATA_ROOT)


def crea_dirs(dirs):
    for dir in dirs:
        new_dir = os.path.join(DATA_ROOT, dir)
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            print(f"{new_dir} created")
        else:
            print(f"{new_dir} already exists")


# dirs = ["personal", "work"]
# crea_dirs(dirs)


def classify(dict):
    for clas, items in dict.items():
        # print(clas)
        clas_dir = os.path.join(DATA_ROOT, clas)

        for file in items:
            ffrom = os.path.join(DATA_ROOT, file)
            fto = os.path.join(clas_dir, file)
            try:
                os.replace(ffrom, fto)
                print(f"{ffrom} moved to {fto}")
            except FileNotFoundError:
                print(f"{ffrom} not found")


# categories = {
#     "personal": ["todos.txt", "bookmarks.txt"],
#     "work": ["customers.csv", "jobs.csv"],
# }

# classify(categories)
