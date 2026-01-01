# ConfigurationMaterialColumns.objectType Property

Parent Object: [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumns.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumns\_var" is a variable referencing a ConfigurationMaterialColumns object.  ```` ``` # Get the value of the property. propertyValue = configurationMaterialColumns_var.objectType ``` ```` |

"configurationMaterialColumns\_var" is a variable referencing a ConfigurationMaterialColumns object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialColumns.h>  // Get the value of the property. string propertyValue = configurationMaterialColumns_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |