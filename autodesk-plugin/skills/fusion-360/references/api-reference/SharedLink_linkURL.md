# SharedLink.linkURL Property

Parent Object: [SharedLink](SharedLink.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/SharedLink.h>

## Description

Returns the URL of the shared link. Returns an empty string in the case where isShared is False.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedLink\_var" is a variable referencing a SharedLink object. |

"sharedLink\_var" is a variable referencing a SharedLink object. ```` ``` #include <Core/Dashboard/SharedLink.h>  // Get the value of the property. string propertyValue = sharedLink_var->linkURL(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |