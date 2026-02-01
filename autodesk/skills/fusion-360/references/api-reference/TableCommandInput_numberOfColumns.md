# TableCommandInput.numberOfColumns Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Returns the current number of visible columns displayed. Setting this property has no effect because the number of columns is automatically inferred by the command inputs that have been added to the table. The table automatically adjusts the number of rows displayed so all inputs can be seen.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. integer propertyValue = tableCommandInput_var->numberOfColumns();  // Set the value of the property, where value_var is an integer. bool returnValue = tableCommandInput_var->numberOfColumns(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |