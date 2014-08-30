@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


# example:
# with ignored(OSError):
#     os.remove("temp_file.tmp")

# instead of:
# try:
#     os.remove("temp_file.tmp")
# except OSError:
#     pass