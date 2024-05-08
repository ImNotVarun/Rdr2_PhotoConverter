import os
import errno
import time

# Get the current working directory
current_dir = os.getcwd()
print("Searching in %s" % current_dir)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def convert(name):
    in_filename = os.path.join(current_dir, name)
    out_filename = os.path.join("Images", os.path.splitext(name)[0] + '.jpg')

    with open(in_filename, 'rb') as in_file:
        statinfo = os.stat(in_filename)
        with open(out_filename, 'wb') as out_file:
            out_file.write(in_file.read()[300:])
            os.utime(out_filename, (statinfo.st_atime, statinfo.st_mtime))
    print(f"Conversion completed")


mkdir_p("Images")

files_to_convert = [filename for filename in os.listdir(
    current_dir) if filename.startswith('PRDR')]
total_files = len(files_to_convert)

if total_files > 0:
    print(f"Found {total_files} files to convert.\n")
    for i, filename in enumerate(files_to_convert, start=1):
        print(f"Converting file {i}/{total_files}: {filename}")
        convert(filename)
    print("\nAll conversions complete.")
    input("Press Enter to quit...")
else:
    print("No files found to convert.")
