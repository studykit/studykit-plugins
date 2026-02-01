# ConfigurationColumn.index Property

Parent Object: [ConfigurationColumn](ConfigurationColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumn.h>

## Description

The index position of this column within the table. The first column is at index 0 and does not include the "Name" column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumn\_var" is a variable referencing a ConfigurationColumn object. |

"configurationColumn\_var" is a variable referencing a ConfigurationColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationColumn.h>  // Get the value of the property. uinteger propertyValue = configurationColumn_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |