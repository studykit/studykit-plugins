# Design.configurationTopTable Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

If this design is a configured design or a configuration, this property returns the associated ConfigurationTopTable object. If this is not a configured design or configuration, this property returns null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<ConfigurationTopTable> propertyValue = design_var->configurationTopTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTopTable](ConfigurationTopTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |