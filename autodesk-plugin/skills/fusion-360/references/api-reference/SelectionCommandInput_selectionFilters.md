# SelectionCommandInput.selectionFilters Property

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Gets or sets the list of selection filters.

## Remarks

The valid list of selection filters can be found here: [Selection Filters](SelectionFilters_UM.htm).

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. |

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. ```` ``` #include <Core/UserInterface/SelectionCommandInput.h>  // Get the value of the property. std::vector<string> propertyValue = selectionCommandInput_var->selectionFilters();  // Set the value of the property, where value_var is a string. bool returnValue = selectionCommandInput_var->selectionFilters(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |