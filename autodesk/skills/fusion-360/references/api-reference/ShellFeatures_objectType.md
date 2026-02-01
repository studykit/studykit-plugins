# ShellFeatures.objectType Property

Parent Object: [ShellFeatures](ShellFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatures\_var" is a variable referencing a ShellFeatures object.  ```` ``` # Get the value of the property. propertyValue = shellFeatures_var.objectType ``` ```` |

"shellFeatures\_var" is a variable referencing a ShellFeatures object. ```` ``` #include <Fusion/Features/ShellFeatures.h>  // Get the value of the property. string propertyValue = shellFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |