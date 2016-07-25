# allow to disable validations
VALIDATE_SLICECOUNT = True
VALIDATE_ORIENTATION = True
VALIDATE_ORTHOGONAL = True
VALIDATE_SLICEINCREMENT = True

def disable_validate_sliceincrement():
    global VALIDATE_SLICEINCREMENT
    VALIDATE_SLICEINCREMENT = False

def disable_validate_orientation():
    global VALIDATE_ORIENTATION
    VALIDATE_ORIENTATION = False

def disable_validate_orthogonal():
    global VALIDATE_ORTHOGONAL
    VALIDATE_ORTHOGONAL = False

def disable_validate_slicecount():
    global VALIDATE_SLICECOUNT
    VALIDATE_SLICECOUNT = False

def enable_validate_sliceincrement():
    global VALIDATE_SLICEINCREMENT
    VALIDATE_SLICEINCREMENT = True

def enable_validate_orientation():
    global VALIDATE_ORIENTATION
    VALIDATE_ORIENTATION = True

def enable_validate_orthogonal():
    global VALIDATE_ORTHOGONAL
    VALIDATE_ORTHOGONAL = True

def enable_validate_slicecount():
    global VALIDATE_SLICECOUNT
    VALIDATE_SLICECOUNT = True