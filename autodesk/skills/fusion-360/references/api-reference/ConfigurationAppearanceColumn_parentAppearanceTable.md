# ConfigurationAppearanceColumn.parentAppearanceTable Property

Parent Object: [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumn.h>

## Description

Returns the parent appearance table this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumn\_var" is a variable referencing a ConfigurationAppearanceColumn object. |

"configurationAppearanceColumn\_var" is a variable referencing a ConfigurationAppearanceColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceColumn.h>  // Get the value of the property. Ptr<ConfigurationAppearanceTable> propertyValue = configurationAppearanceColumn_var->parentAppearanceTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationAppearanceTable](ConfigurationAppearanceTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |