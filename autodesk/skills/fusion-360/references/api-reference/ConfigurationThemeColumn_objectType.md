# ConfigurationThemeColumn.objectType Property

Parent Object: [ConfigurationThemeColumn](ConfigurationThemeColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationThemeColumn\_var" is a variable referencing a ConfigurationThemeColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationThemeColumn_var.objectType ``` ```` |

"configurationThemeColumn\_var" is a variable referencing a ConfigurationThemeColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationThemeColumn.h>  // Get the value of the property. string propertyValue = configurationThemeColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |