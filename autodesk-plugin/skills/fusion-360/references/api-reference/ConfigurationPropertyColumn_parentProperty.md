# ConfigurationPropertyColumn.parentProperty Property

Parent Object: [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyColumn.h>

## Description

Returns the property whose value is controlled by this column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyColumn\_var" is a variable referencing a ConfigurationPropertyColumn object. |

"configurationPropertyColumn\_var" is a variable referencing a ConfigurationPropertyColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyColumn.h>  // Get the value of the property. Ptr<Property> propertyValue = configurationPropertyColumn_var->parentProperty(); ``` ```` |

## Property Value

This is a read only property whose value is a [Property](Property.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |