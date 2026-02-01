# ConfigurationParameterCell.expression Property

Parent Object: [ConfigurationParameterCell](ConfigurationParameterCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterCell.h>

## Description

Gets and sets the expression that defines the value of the associated parameter when the parent row is active. This property behaves as read-only when the table is obtained from a DataFile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. |

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterCell.h>  // Get the value of the property. string propertyValue = configurationParameterCell_var->expression();  // Set the value of the property, where value_var is a string. bool returnValue = configurationParameterCell_var->expression(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |