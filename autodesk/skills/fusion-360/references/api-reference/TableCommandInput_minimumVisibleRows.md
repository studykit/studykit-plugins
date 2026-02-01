# TableCommandInput.minimumVisibleRows Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets and sets the minimum number of rows displayed. This is the minimum amount of space taken up on the command dialog, even if the table doesn't yet contain any rows. For a newly created table, this property defaults to 2.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. integer propertyValue = tableCommandInput_var->minimumVisibleRows();  // Set the value of the property, where value_var is an integer. bool returnValue = tableCommandInput_var->minimumVisibleRows(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |