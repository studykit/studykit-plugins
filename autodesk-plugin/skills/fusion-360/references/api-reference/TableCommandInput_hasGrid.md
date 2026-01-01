# TableCommandInput.hasGrid Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets and sets whether a grid is displayed for the table. For a newly created table, this property defaults to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. boolean propertyValue = tableCommandInput_var->hasGrid();  // Set the value of the property, where value_var is a boolean. bool returnValue = tableCommandInput_var->hasGrid(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |