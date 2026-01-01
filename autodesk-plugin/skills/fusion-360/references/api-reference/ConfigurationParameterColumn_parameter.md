# ConfigurationParameterColumn.parameter Property

Parent Object: [ConfigurationParameterColumn](ConfigurationParameterColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterColumn.h>

## Description

Returns the parameter being controlled by this column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationParameterColumn_var.parameter ``` ```` |

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterColumn.h>  // Get the value of the property. Ptr<Parameter> propertyValue = configurationParameterColumn_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [Parameter](Parameter.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |