# ConfigurationAppearanceColumn.objectType Property

Parent Object: [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumn\_var" is a variable referencing a ConfigurationAppearanceColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationAppearanceColumn_var.objectType ``` ```` |

"configurationAppearanceColumn\_var" is a variable referencing a ConfigurationAppearanceColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceColumn.h>  // Get the value of the property. string propertyValue = configurationAppearanceColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |