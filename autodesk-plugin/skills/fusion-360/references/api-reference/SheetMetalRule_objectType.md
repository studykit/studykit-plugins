# SheetMetalRule.objectType Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object.  ```` ``` # Get the value of the property. propertyValue = sheetMetalRule_var.objectType ``` ```` |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. string propertyValue = sheetMetalRule_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |