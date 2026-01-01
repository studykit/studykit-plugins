# SharedLink.objectType Property

Parent Object: [SharedLink](SharedLink.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/SharedLink.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedLink\_var" is a variable referencing a SharedLink object.  ```` ``` # Get the value of the property. propertyValue = sharedLink_var.objectType ``` ```` |

"sharedLink\_var" is a variable referencing a SharedLink object. ```` ``` #include <Core/Dashboard/SharedLink.h>  // Get the value of the property. string propertyValue = sharedLink_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |