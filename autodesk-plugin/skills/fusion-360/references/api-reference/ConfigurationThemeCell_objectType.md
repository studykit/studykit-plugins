# ConfigurationThemeCell.objectType Property

Parent Object: [ConfigurationThemeCell](ConfigurationThemeCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeCell.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationThemeCell\_var" is a variable referencing a ConfigurationThemeCell object.  ```` ``` # Get the value of the property. propertyValue = configurationThemeCell_var.objectType ``` ```` |

"configurationThemeCell\_var" is a variable referencing a ConfigurationThemeCell object. ```` ``` #include <Fusion/Configurations/ConfigurationThemeCell.h>  // Get the value of the property. string propertyValue = configurationThemeCell_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |