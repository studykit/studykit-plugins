# ConfigurationMaterialColumn.objectType Property

Parent Object: [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationMaterialColumn_var.objectType ``` ```` |

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialColumn.h>  // Get the value of the property. string propertyValue = configurationMaterialColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |