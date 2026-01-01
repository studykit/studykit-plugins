# FileDialog.objectType Property

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a FileDialog object.  ```` ``` # Get the value of the property. propertyValue = fileDialog_var.objectType ``` ```` |

"fileDialog\_var" is a variable referencing a FileDialog object. ```` ``` #include <Core/UserInterface/FileDialog.h>  // Get the value of the property. string propertyValue = fileDialog_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |