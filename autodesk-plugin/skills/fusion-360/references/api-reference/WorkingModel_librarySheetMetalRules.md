# WorkingModel.librarySheetMetalRules Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Gets the collection of sheet metal rules in the sheet metal rule library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. Ptr<SheetMetalRules> propertyValue = workingModel_var->librarySheetMetalRules(); ``` ```` |

## Property Value

This is a read only property whose value is a [SheetMetalRules](SheetMetalRules.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |