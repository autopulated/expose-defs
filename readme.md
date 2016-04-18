#expose-defs

This module makes yotta config values accessible as top-level #definitions
which can be included by #including:

```C
#include "expose-config/defs.h"
```

All values defined in objects in the yotta config data which are siblings of a
definitions `"$exposeDef":true` will be exported.

To depend on this module in your project, run:

```
yotta install expose-defs
```

### WARNING

**Needless to say, use of this module comes with some risk of namespace collisions with other users of the module, so be careful to only expose values which have _some_ namespacing convention, even if it is different to yotta's**
