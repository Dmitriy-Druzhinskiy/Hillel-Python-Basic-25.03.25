def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)
assert (difference(1, 2, 3))
assert (difference(5, -5))
assert (difference(10.2, -2.2, 0, 1.1, 0.5))
assert (difference())

print('OK')
