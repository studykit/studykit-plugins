# ConfigurationMaterialTable.objectType Property

Parent Object: [ConfigurationMaterialTable](ConfigurationMaterialTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object.  ```` ``` # Get the value of the property. propertyValue = configurationMaterialTable_var.objectType ``` ```` |

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialTable.h>  // Get the value of the property. string propertyValue = configurationMaterialTable_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |