# Copyright 2017, Ryan P. Kelly.

import io
import zlib

import constrictor


PLAIN = b'some data to compress'
COMPRESSED = b'\x1f\x8b\x08\x00\xd8\xd3FZ\x02\xff+\xce\xcfMUHI,IT(\xc9WH\xce\xcf-(J-.\x06\x00\xf6g\xab\xde\x15\x00\x00\x00'


def test_round_trip():

    data = io.BytesIO(PLAIN)

    compressed_fp = constrictor.compress(data)
    compressed = compressed_fp.read()

    # strip off the header, just to compare the contents
    compressed_no_header = compressed[32 + zlib.MAX_WBITS:]
    assert compressed_no_header == COMPRESSED[32 + zlib.MAX_WBITS:]

    decompressed_fp = constrictor.decompress(compressed)
    decompressed = decompressed_fp.read()

    assert decompressed == PLAIN


def test_reading_size_decompress():

    for i in range(16):
        dfp = constrictor.decompress(COMPRESSED)

        data = dfp.read(i)
        assert len(data) == i


def test_reading_size_compress():

    for i in range(16):

        cfp = constrictor.compress(PLAIN)

        data = cfp.read(i)
        assert len(data) == i
