# Occurrence.configurationRow Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

If this occurrence is a configuration, this property returns the row that defines it. If it isn't a configuration, null is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = occurrence_var->configurationRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |