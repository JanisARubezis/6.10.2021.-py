import os
#os.remove('fails.txt')
if os.path.exists('img.py'):
    os.rename('img.py','img2.py')
else:
    print("Fails neeksistē")