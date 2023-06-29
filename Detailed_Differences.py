N = int(input())
for _ in range(N):
    # reference string
    ref = input()

    # to match string
    match = input()

    diff = [i for i in range(len(ref)) if ref[i] != match[i]]
    outdiff = ['*' if i in diff else '.' for i in range(len(ref))]

    #output final
    print(ref)
    print(match)
    print(''.join(outdiff))