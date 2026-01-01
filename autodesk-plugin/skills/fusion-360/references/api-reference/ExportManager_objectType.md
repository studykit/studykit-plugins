# ExportManager.objectType Property

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an ExportManager object.  ```` ``` # Get the value of the property. propertyValue = exportManager_var.objectType ``` ```` |

"exportManager\_var" is a variable referencing an ExportManager object. ```` ``` #include <Fusion/Fusion/ExportManager.h>  // Get the value of the property. string propertyValue = exportManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |