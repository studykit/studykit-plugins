# ProfileCurves.objectType Property

Parent Object: [ProfileCurves](ProfileCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileCurves.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileCurves\_var" is a variable referencing a ProfileCurves object.  ```` ``` # Get the value of the property. propertyValue = profileCurves_var.objectType ``` ```` |

"profileCurves\_var" is a variable referencing a ProfileCurves object. ```` ``` #include <Fusion/Sketch/ProfileCurves.h>  // Get the value of the property. string propertyValue = profileCurves_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |