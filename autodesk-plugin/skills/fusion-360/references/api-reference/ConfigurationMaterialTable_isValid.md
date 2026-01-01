# ConfigurationMaterialTable.isValid Property

Parent Object: [ConfigurationMaterialTable](ConfigurationMaterialTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. |

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialTable.h>  // Get the value of the property. boolean propertyValue = configurationMaterialTable_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |