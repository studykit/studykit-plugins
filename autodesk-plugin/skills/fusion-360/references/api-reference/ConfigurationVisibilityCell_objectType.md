# ConfigurationVisibilityCell.objectType Property

Parent Object: [ConfigurationVisibilityCell](ConfigurationVisibilityCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityCell.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityCell\_var" is a variable referencing a ConfigurationVisibilityCell object.  ```` ``` # Get the value of the property. propertyValue = configurationVisibilityCell_var.objectType ``` ```` |

"configurationVisibilityCell\_var" is a variable referencing a ConfigurationVisibilityCell object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityCell.h>  // Get the value of the property. string propertyValue = configurationVisibilityCell_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |