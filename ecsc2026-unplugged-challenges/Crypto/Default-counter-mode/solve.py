ct = b'ffa292f18ebe650b716451ce187d6858729a520904eb34cb'
ct2 = b'e7a292f18ebe650b716451ce187d6858729a520904eb34cb '

print(bytes([a^b for a,b in zip(ct,ct2)]))
