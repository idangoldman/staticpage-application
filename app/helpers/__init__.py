import os, hashlib, time

def load_env_var( env_file = '.env_flask' ):
    if os.path.exists(env_file):
        print(' * Importing environment from %s...' % env_file)
        for line in open(env_file):
            variables = line.strip().split('=')
            if len(variables) == 2:
                # print(variables[0])
                os.environ[variables[0]] = variables[1]


def md5_identifier( identifier ):
    return hashlib.md5( identifier ).hexdigest()


def timestamp():
    return str(int(time.time()))


def path_builder( *paths ):
    full_path = ''

    for path in paths:
        full_path += '/' + os.path.sep.join( \
                        filter( None, path.split( os.path.sep ) ) )

    return full_path


def path_slicer( path, slice_path ):
    path = path_builder( path )
    slice_path = path_builder( slice_path )

    return path[ len( slice_path ) : ]
