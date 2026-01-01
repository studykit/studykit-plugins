# ConfigurationParameterCell.value Property

Parent Object: [ConfigurationParameterCell](ConfigurationParameterCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterCell.h>

## Description

Gets and sets the value of the parameter in database units. You can use the units property of the associated Parameter object, which you can get from the column, to determine the type of units this parameter is defined in. Setting this property will overwrite any existing expression. This property behaves as read-only when the table is obtained from a DataFile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. |

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterCell.h>  // Get the value of the property. double propertyValue = configurationParameterCell_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = configurationParameterCell_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |