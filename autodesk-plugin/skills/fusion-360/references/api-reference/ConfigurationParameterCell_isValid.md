# ConfigurationParameterCell.isValid Property

Parent Object: [ConfigurationParameterCell](ConfigurationParameterCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterCell.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. |

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterCell.h>  // Get the value of the property. boolean propertyValue = configurationParameterCell_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |