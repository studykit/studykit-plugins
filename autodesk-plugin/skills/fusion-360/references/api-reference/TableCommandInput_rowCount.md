# TableCommandInput.rowCount Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Returns the number of rows in the table. The actual number of rows in the table is defined by the number of rows that contain command inputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. integer propertyValue = tableCommandInput_var->rowCount(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |