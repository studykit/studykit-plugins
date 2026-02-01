# NCProgram.operations Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Gets and sets the operations which will be included in the NC program. Valid input contains any number of operations, setups or folders. For setups and folders all child operations will be added. Operations will be post processed in setup order, with operations from the same setup grouped together. Setting the nc\_program\_orderByTool BooleanParameterValue on the parameters property to true will reorder operations across multiple setups to reduce the number of tool changes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. std::vector<Ptr<OperationBase>> propertyValue = nCProgram_var->operations();  // Set the value of the property, where value_var is an OperationBase. bool returnValue = nCProgram_var->operations(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [OperationBase](OperationBase.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |