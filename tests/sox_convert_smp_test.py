import sox


def test_sox_convert_smp(in_path=r"C:\Users\dish7\Documents\ROLAND\SP-404MKII\PROJECT_PROJECT_07\SMPL\BANK2-16.SMP",
                          out_path=r"C:\Users\dish7\Documents\ROLAND\SP-404MKII\PROJECT_PROJECT_07\SMPL\BANK02-16_python.wav"):
    from sox.core import sox

    # .SMP default parameters for SP-404MKII
    # Note that sample data itself only starts after 200 samples, so we trim the first 200 samples to avoid noise.
    # Low-level wrapper is used since pysox does not support assigning byte-order for raw input, which is required for .SMP files. (Explicitely big endian)

    RATE = 48000
    BITS = 16
    CHANNELS = 2
    trim_seconds = 200 / RATE

    args = [
        "sox",
        "-t", "raw",
        "-e", "signed",
        "-b", str(BITS),
        "-c", str(CHANNELS),
        "-r", str(RATE),
        "-B",          # big-endian raw input
        in_path,
        out_path,
        "trim",
        str(trim_seconds),
    ]

    status, stdout, stderr = sox(args)
    if status != 0:
        raise RuntimeError(stderr)
    print(f"Converted {in_path} to {out_path} successfully.")

    if stdout != "":
        print(f"stdout: {stdout}")

def main():
    test_sox_convert_smp()


if __name__ == "__main__":
    main()