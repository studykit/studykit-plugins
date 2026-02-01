# ConfigurationSuppressColumn.objectType Property

Parent Object: [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSuppressColumn\_var" is a variable referencing a ConfigurationSuppressColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationSuppressColumn_var.objectType ``` ```` |

"configurationSuppressColumn\_var" is a variable referencing a ConfigurationSuppressColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationSuppressColumn.h>  // Get the value of the property. string propertyValue = configurationSuppressColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |