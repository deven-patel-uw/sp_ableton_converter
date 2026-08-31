def build_wav_project_folder(sp_project_folder: str, wav_folder: str) -> None:
    """
    Creates a folder structure for WAV files in the specified project folder.

    :param sp_project_folder: Path to the exported SP-404MKII project folder.
    :param wav_folder: Path to the folder that will contain the output .WAV files.
    """
    import os
    import python_tests.convert_smp_to_wav as convert_smp_to_wav

    # find the "samples" folder in the SP project folder
    samples_folder = os.path.join(sp_project_folder, "SMPL")


    # for each .SMP file in the "samples" folder, convert it to .WAV and save it in the "wav" folder
    for file in os.listdir(samples_folder):
        if file.endswith(".SMP"):
            smp_file_path = os.path.join(samples_folder, file)
            wav_file_name = os.path.splitext(file)[0] + ".wav" # change the extension to .wav
            wav_file_path = os.path.join(wav_folder, wav_file_name)
            convert_smp_to_wav.smp_to_wav(smp_file_path, wav_file_path)

def main():
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Convert SP-404MKII .SMP files to .WAV format.")
    parser.add_argument("sp_project_folder", help="Path to the exported SP-404MKII project folder.")
    parser.add_argument("wav_folder", help="Path to the folder that will contain the output .WAV files.")

    args = parser.parse_args()

    # create the wav folder if it doesn't exist
    if not os.path.exists(args.wav_folder):
        os.makedirs(args.wav_folder)

    build_wav_project_folder(args.sp_project_folder, args.wav_folder)

if __name__ == "__main__":
    main()