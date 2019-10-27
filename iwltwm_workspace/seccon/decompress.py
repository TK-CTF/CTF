import zlib

def decompress():
    with open('test', mode='rb') as f:
        strf = f.read()
        decompressed_data = zlib.decompress(strf)
        with open('test2', mode='b') as g:
            g.write(decompressed_data)

decompress()
