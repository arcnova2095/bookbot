def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        return len(file_contents.split())  # Return an integer, not a set

def get_num_alphabet(path):
    with open(path) as f:
        file_contents = f.read().lower()
        alpha_count = {}
        for i in file_contents:
            if i.isalpha():
                alpha_count[i] = 1 + alpha_count.get(i, 0)
        return alpha_count

def alpha_sort(d):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    x = ""
    for key, value in sorted_dict.items():
        x += f"{key}: {value}\n"
    return x
