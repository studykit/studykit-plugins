# ConfigurationPropertyColumn.index Property

Parent Object: [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyColumn.h>

## Description

The index position of this column within the table. The first column is at index 0 and does not include the "Name" column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyColumn\_var" is a variable referencing a ConfigurationPropertyColumn object. |

"configurationPropertyColumn\_var" is a variable referencing a ConfigurationPropertyColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyColumn.h>  // Get the value of the property. uinteger propertyValue = configurationPropertyColumn_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |