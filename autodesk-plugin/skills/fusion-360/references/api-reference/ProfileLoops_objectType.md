# ProfileLoops.objectType Property

Parent Object: [ProfileLoops](ProfileLoops.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoops.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoops\_var" is a variable referencing a ProfileLoops object.  ```` ``` # Get the value of the property. propertyValue = profileLoops_var.objectType ``` ```` |

"profileLoops\_var" is a variable referencing a ProfileLoops object. ```` ``` #include <Fusion/Sketch/ProfileLoops.h>  // Get the value of the property. string propertyValue = profileLoops_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |