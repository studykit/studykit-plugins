# ConfigurationRow.objectType Property

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a ConfigurationRow object.  ```` ``` # Get the value of the property. propertyValue = configurationRow_var.objectType ``` ```` |

"configurationRow\_var" is a variable referencing a ConfigurationRow object. ```` ``` #include <Fusion/Configurations/ConfigurationRow.h>  // Get the value of the property. string propertyValue = configurationRow_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |