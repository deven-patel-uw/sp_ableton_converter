def smp_to_wav(in_path: str, out_path: str) -> bool:
    '''
    Converts SP-404MKII .SMP files to .WAV format using SoX.

    :param in_path: Path to the input .SMP file.
    :param out_path: Path to the output .WAV file.
    :return: True if conversion is successful.
    :raises RuntimeError: If SoX encounters an error during conversion.
    '''
    from sox.core import sox

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
        raise RuntimeError(stderr) # Failed to convert .SMP to .WAV
        
    return True # Successfully converted .SMP to .WAV