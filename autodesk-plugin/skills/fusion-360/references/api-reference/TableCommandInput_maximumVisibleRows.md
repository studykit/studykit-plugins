# TableCommandInput.maximumVisibleRows Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets and sets the maximum number of rows that can be displayed. As rows are added the visible size of the table will grow to show all rows until this maximum number of rows is reached and then a scroll bar will be displayed to allow the user to access all rows. For a new created table, this property defaults to 4.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. integer propertyValue = tableCommandInput_var->maximumVisibleRows();  // Set the value of the property, where value_var is an integer. bool returnValue = tableCommandInput_var->maximumVisibleRows(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |