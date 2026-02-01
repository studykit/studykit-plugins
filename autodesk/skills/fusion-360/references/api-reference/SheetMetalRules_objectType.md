# SheetMetalRules.objectType Property

Parent Object: [SheetMetalRules](SheetMetalRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRules.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRules\_var" is a variable referencing a SheetMetalRules object.  ```` ``` # Get the value of the property. propertyValue = sheetMetalRules_var.objectType ``` ```` |

"sheetMetalRules\_var" is a variable referencing a SheetMetalRules object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRules.h>  // Get the value of the property. string propertyValue = sheetMetalRules_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |