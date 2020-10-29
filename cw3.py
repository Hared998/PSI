print('%s %s' %('Adrian', 'Merchel'))
print('{} {}'.format('Kolega', 'Mariusz'))

print("\n")


class Data(object):

    def __str__(self):
        return 'Pierwsze'

    def __repr__(self):
        return 'Drugie'

print('%s %r' % (Data(), Data()))
print('{0!s} {0!r}'.format(Data()))

print("\n")

print('%25s' % ('Wiele liter',))
print('{:>15}'.format('trudne sprawy'))

print("\n")

print('%-5s' % ('Wielki oscyloskop prawny',))
print('{:4}'.format('Czterolistna'))

print("\n")

print('%.7s' % ('Wszystko Jedno',))
print('{:.5}'.format('Jeszcze jedno'))