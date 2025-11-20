# Jesus, please let this code work.
# import stuff.
import sys
from pathlib import Path
# Jesus, please let this code work.
# Verse Break definer
VerseBreak = 3  # For every 3 blank paragraph breaks, there is a verse.
# Jesus, please let this code work.
# Verse Grouping Definer.
def GroupVerses(lines, VerseBreak=VerseBreak):
    Verses = []
    CurrentWords = []
    BlankRun = 0  # this must be a number, not a list
    for RawLine in lines:
        line = RawLine.strip()
        if not line:
            # Blank line encountered
            BlankRun += 1
            continue
        # We hit real text after some blanks
        if BlankRun >= VerseBreak:
            # End the previous verse (if there was one)
            if CurrentWords:
                Verses.append(" ".join(CurrentWords))
                CurrentWords = []
        # Reset blank counter since this line is not blank
        BlankRun = 0
        CurrentWords.append(line)
    # Verse Flusher
    if CurrentWords:
        Verses.append(" ".join(CurrentWords))
    return Verses
# Jesus, please let this code work.
# Process a single file: input.txt -> output.txt
def ProcessFile(InputPath, OutputPath):
    InputPath = Path(InputPath)
    OutputPath = Path(OutputPath)
    with InputPath.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    Verses = GroupVerses(lines)
    with OutputPath.open("w", encoding="utf-8") as f:
        for Verse in Verses:
            # Makes each line its own Verse
            f.write(Verse + "\n")
    print(f"Wrote {len(Verses)} Verses to {OutputPath}")
# Process all .txt files in a folder
def ProcessFolder(FolderPath):
    FolderPath = Path(FolderPath)
    txt_files = list(FolderPath.glob("*.txt"))
    if not txt_files:
        print(f"No .txt files found in {FolderPath}")
        return
    for InputPath in txt_files:
        # create "filename_verses.txt"
        OutputPath = InputPath.with_name(InputPath.stem + "_verses.txt")
        ProcessFile(InputPath, OutputPath)
# Command-line / exe entry point
def RunFromCommandLine():
    args = sys.argv[1:]

    # 0 arguments: process all .txt in the script/exe folder
    if len(args) == 0:
        folder = Path(sys.argv[0]).resolve().parent
        print(f"No arguments passed. Processing all .txt files in {folder}")
        ProcessFolder(folder)
        try:
            input("Done! Press Enter to close...")
        except EOFError:
            # In case there's no stdin, just ignore
            pass
    # 1 argument: could be a file OR a folder
    elif len(args) == 1:
        path = Path(args[0])

        if path.is_dir():
            # Process all .txt files in this folder
            ProcessFolder(path)
        else:
            # Treat as single input file, output = file_verses.txt
            OutputPath = path.with_name(path.stem + "_verses.txt")
            ProcessFile(path, OutputPath)
    # 2 arguments: input + output (single file mode)
    elif len(args) == 2:
        InputPath = args[0]
        OutputPath = args[1]
        ProcessFile(InputPath, OutputPath)
    else:
        print("Usage:")
        print("  python group_verses.py input.txt output.txt")
        print("  python group_verses.py folder_with_txt")
        print("  (or just double-click the .exe to process its own folder)")
        sys.exit(1)
# Jesus, please let this code work.
if __name__ == "__main__":
    RunFromCommandLine()