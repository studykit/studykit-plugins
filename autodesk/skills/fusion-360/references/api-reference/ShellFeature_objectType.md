# ShellFeature.objectType Property

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a ShellFeature object.  ```` ``` # Get the value of the property. propertyValue = shellFeature_var.objectType ``` ```` |

"shellFeature\_var" is a variable referencing a ShellFeature object. ```` ``` #include <Fusion/Features/ShellFeature.h>  // Get the value of the property. string propertyValue = shellFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |