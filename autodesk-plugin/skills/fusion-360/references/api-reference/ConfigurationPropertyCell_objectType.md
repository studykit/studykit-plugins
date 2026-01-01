# ConfigurationPropertyCell.objectType Property

Parent Object: [ConfigurationPropertyCell](ConfigurationPropertyCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyCell.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object.  ```` ``` # Get the value of the property. propertyValue = configurationPropertyCell_var.objectType ``` ```` |

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyCell.h>  // Get the value of the property. string propertyValue = configurationPropertyCell_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |