# FilletEdgeSet.objectType Property

Parent Object: [FilletEdgeSet](FilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSet.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = filletEdgeSet_var.objectType ``` ```` |

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. ```` ``` #include <Fusion/Features/FilletEdgeSet.h>  // Get the value of the property. string propertyValue = filletEdgeSet_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |