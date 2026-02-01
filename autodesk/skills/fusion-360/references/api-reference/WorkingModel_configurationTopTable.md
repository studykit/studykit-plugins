# WorkingModel.configurationTopTable Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

If this design is a configured design or a configuration, this property returns the associated ConfigurationTopTable object. If this is not a configured design or configuration, this property returns null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. Ptr<ConfigurationTopTable> propertyValue = workingModel_var->configurationTopTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTopTable](ConfigurationTopTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |