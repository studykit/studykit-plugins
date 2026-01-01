# ConfigurationCell.objectType Property

Parent Object: [ConfigurationCell](ConfigurationCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCell.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCell\_var" is a variable referencing a ConfigurationCell object.  ```` ``` # Get the value of the property. propertyValue = configurationCell_var.objectType ``` ```` |

"configurationCell\_var" is a variable referencing a ConfigurationCell object. ```` ``` #include <Fusion/Configurations/ConfigurationCell.h>  // Get the value of the property. string propertyValue = configurationCell_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |