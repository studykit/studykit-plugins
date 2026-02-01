# ConfigurationInsertCell.objectType Property

Parent Object: [ConfigurationInsertCell](ConfigurationInsertCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertCell.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertCell\_var" is a variable referencing a ConfigurationInsertCell object.  ```` ``` # Get the value of the property. propertyValue = configurationInsertCell_var.objectType ``` ```` |

"configurationInsertCell\_var" is a variable referencing a ConfigurationInsertCell object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertCell.h>  // Get the value of the property. string propertyValue = configurationInsertCell_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |