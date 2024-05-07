import os
import errno

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
    print("Converting %s " % in_filename)
    with open(in_filename, 'rb') as in_file:
        statinfo = os.stat(in_filename)
        with open(out_filename, 'wb') as out_file:
            out_file.write(in_file.read()[300:])
    os.utime(out_filename, (statinfo.st_atime, statinfo.st_mtime))


mkdir_p("Images")

for filename in os.listdir(current_dir):
    if filename.startswith('PRDR'):
        convert(filename)
