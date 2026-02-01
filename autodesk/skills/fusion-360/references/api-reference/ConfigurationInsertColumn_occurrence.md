# ConfigurationInsertColumn.occurrence Property

Parent Object: [ConfigurationInsertColumn](ConfigurationInsertColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertColumn.h>

## Description

Returns the occurrence that is associated with this configuration insertion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertColumn\_var" is a variable referencing a ConfigurationInsertColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationInsertColumn_var.occurrence ``` ```` |

"configurationInsertColumn\_var" is a variable referencing a ConfigurationInsertColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertColumn.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = configurationInsertColumn_var->occurrence(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |