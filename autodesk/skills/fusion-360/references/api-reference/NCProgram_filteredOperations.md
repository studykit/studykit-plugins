# NCProgram.filteredOperations Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Gets all valid operations derived from the operations property. The list is ordered with respect to the nc\_program\_oderByTool parameter and considers the number of instances in a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. std::vector<Ptr<OperationBase>> propertyValue = nCProgram_var->filteredOperations(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [OperationBase](OperationBase.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |