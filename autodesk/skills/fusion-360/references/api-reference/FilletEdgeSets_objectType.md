# FilletEdgeSets.objectType Property

Parent Object: [FilletEdgeSets](FilletEdgeSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSets.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSets\_var" is a variable referencing a FilletEdgeSets object.  ```` ``` # Get the value of the property. propertyValue = filletEdgeSets_var.objectType ``` ```` |

"filletEdgeSets\_var" is a variable referencing a FilletEdgeSets object. ```` ``` #include <Fusion/Features/FilletEdgeSets.h>  // Get the value of the property. string propertyValue = filletEdgeSets_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |