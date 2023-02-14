def most_frequent(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_freq.items():
        print(k,":", v,end=",")


most_frequent("HelloWorld")