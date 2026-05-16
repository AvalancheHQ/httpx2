"""Benchmarks for response decoders."""

from httpx2._decoders import ByteChunker, IdentityDecoder, LineDecoder, TextDecoder


def test_identity_decoder(benchmark):
    """Decode a payload through the identity (no-op) decoder."""
    decoder = IdentityDecoder()
    data = b"Hello, world!" * 100
    benchmark(decoder.decode, data)


def test_text_decoder(benchmark):
    """Decode bytes to text using TextDecoder."""
    data = b"Hello, world! This is a test of the text decoder. " * 50

    def run():
        decoder = TextDecoder(encoding="utf-8")
        decoder.decode(data)
        decoder.flush()

    benchmark(run)


def test_line_decoder(benchmark):
    """Split text into lines using LineDecoder."""
    text = "line1\nline2\nline3\nline4\nline5\n" * 20

    def run():
        decoder = LineDecoder()
        lines = list(decoder.decode(text))
        lines.extend(decoder.flush())
        return lines

    benchmark(run)


def test_byte_chunker(benchmark):
    """Chunk bytes into fixed-size pieces."""
    data = b"x" * 10_000

    def run():
        chunker = ByteChunker(chunk_size=1024)
        chunks = list(chunker.decode(data))
        chunks.extend(chunker.flush())
        return chunks

    benchmark(run)
