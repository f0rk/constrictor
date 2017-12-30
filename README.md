constrictor - streaming gzip for python
=======================================

Python's `gzip` module allows you to compress in-memory data. Which is great if
your data fits in memory, or if you want it to be in memory.

For many users, this is not a useful outcome. Many on the internet are asking
"how do I stream gzipped data?" The solution appears to be "copy and paste this
stackoverflow answer". There are better ways.

`constrictor` works to stream both compression and decompression and acts like
a file while doing so.

Usage
=====

```
import constrictor

original_fp = open("/tmp/some_data.gz", "rb")

decompressed_fp = constrictor.decompress(original_fp)
compressed_fp = constrictor.compress(decompressed_fp)
```

The data provided to `decompress` and `compress` can also be bytes, just to
simplify use:

```
import constrictor

original_fp = open("/tmp/some_data.gz", "rb")
original_bytes = original_fp.read()

decompressed_fp = constrictor.decompress(original_bytes)
```
