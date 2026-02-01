# SharedPointCoincident.objectType Property

Parent Object: [SharedPointCoincident](SharedPointCoincident.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SharedPointCoincident.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedPointCoincident\_var" is a variable referencing a SharedPointCoincident object.  ```` ``` # Get the value of the property. propertyValue = sharedPointCoincident_var.objectType ``` ```` |

"sharedPointCoincident\_var" is a variable referencing a SharedPointCoincident object. ```` ``` #include <Fusion/Sketch/SharedPointCoincident.h>  // Get the value of the property. string propertyValue = sharedPointCoincident_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |