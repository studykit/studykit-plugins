# TableCommandInput.tablePresentationStyle Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets and sets the presentation style the table is currently using for its display.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. TablePresentationStyles propertyValue = tableCommandInput_var->tablePresentationStyle();  // Set the value of the property, where value_var is a TablePresentationStyles. bool returnValue = tableCommandInput_var->tablePresentationStyle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [TablePresentationStyles](TablePresentationStyles.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |