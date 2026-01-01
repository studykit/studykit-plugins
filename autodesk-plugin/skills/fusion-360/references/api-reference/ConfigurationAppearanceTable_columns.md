# ConfigurationAppearanceTable.columns Property

Parent Object: [ConfigurationAppearanceTable](ConfigurationAppearanceTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceTable.h>

## Description

Returns the collection that provides access to this table's columns and the ability to create new columns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceTable\_var" is a variable referencing a ConfigurationAppearanceTable object. |

"configurationAppearanceTable\_var" is a variable referencing a ConfigurationAppearanceTable object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceTable.h>  // Get the value of the property. Ptr<ConfigurationAppearanceColumns> propertyValue = configurationAppearanceTable_var->columns(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |