# ConfigurationRows.objectType Property

Parent Object: [ConfigurationRows](ConfigurationRows.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRows.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRows\_var" is a variable referencing a ConfigurationRows object.  ```` ``` # Get the value of the property. propertyValue = configurationRows_var.objectType ``` ```` |

"configurationRows\_var" is a variable referencing a ConfigurationRows object. ```` ``` #include <Fusion/Configurations/ConfigurationRows.h>  // Get the value of the property. string propertyValue = configurationRows_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |