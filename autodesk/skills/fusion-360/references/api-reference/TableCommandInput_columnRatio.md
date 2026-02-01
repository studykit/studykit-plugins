# TableCommandInput.columnRatio Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets and sets the width ratio of the columns. This is defined using a string such as "1:1:1" where this defines that the first three columns are all the same width. A value of "2:1" defines that the first column is twice the width of the second.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object.  ```` ``` # Get the value of the property. propertyValue = tableCommandInput_var.columnRatio  # Set the value of the property. tableCommandInput_var.columnRatio = propertyValue ``` ```` |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. string propertyValue = tableCommandInput_var->columnRatio();  // Set the value of the property, where value_var is a string. bool returnValue = tableCommandInput_var->columnRatio(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |