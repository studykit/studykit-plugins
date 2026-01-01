# SheetMetalRuleValue.objectType Property

Parent Object: [SheetMetalRuleValue](SheetMetalRuleValue.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRuleValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRuleValue\_var" is a variable referencing a SheetMetalRuleValue object.  ```` ``` # Get the value of the property. propertyValue = sheetMetalRuleValue_var.objectType ``` ```` |

"sheetMetalRuleValue\_var" is a variable referencing a SheetMetalRuleValue object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRuleValue.h>  // Get the value of the property. string propertyValue = sheetMetalRuleValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |