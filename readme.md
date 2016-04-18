This module makes yotta config values accessible as top-level #definitions
which can be included by #including:

#include "expose-config/defs.h"

All values defined in objects in the yotta config data which are siblings of a
definitions `"$exposeDef":true` will be exported.
