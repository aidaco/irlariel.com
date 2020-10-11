import os

def set_var(self, key: str, value: str):
    """Sets the given environment variable (*env var*).

    :param key: name of the env var to set.
    :type key: str
    :param value: value to be set for the given env var.
    :type str: str
    """

    os.environ['key'] = value
    # os.setenv(k,v) # Alternative, not sure why it's different.


def from_object(import_path: str):
    """Imports the python config file from the specified path and sets the \
        contained environment variables.

    :param path: importpath
    :type path: str
    """
    path = __import__(import_path)
    raw_conf = dir(path.Config)
    conf = { str(k):str(v) for k,v in raw_conf}
    for k,v in conf.items():
        set_var(k, v)
        