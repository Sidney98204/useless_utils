options = {
    0: lambda x: x + 1, 1:lambda x: x + 2
}
l = list(range(5))

print(options.get(0)(l))