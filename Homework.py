_exercicesList = list(input().split(";"))
_finalList = []
for _step in _exercicesList:
    try:
        _finalList.append(int(_step))
    except Exception:
        _start, _stop = [int(j) for j in _step.split("-")]
        _range = list(range(_start, _stop + 1))
        _finalList += _range

print(len(_finalList))
