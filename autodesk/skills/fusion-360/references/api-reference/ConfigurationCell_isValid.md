# ConfigurationCell.isValid Property

Parent Object: [ConfigurationCell](ConfigurationCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCell.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCell\_var" is a variable referencing a ConfigurationCell object. |

"configurationCell\_var" is a variable referencing a ConfigurationCell object. ```` ``` #include <Fusion/Configurations/ConfigurationCell.h>  // Get the value of the property. boolean propertyValue = configurationCell_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |