# ConfigurationAppearanceColumns.objectType Property

Parent Object: [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumns.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumns\_var" is a variable referencing a ConfigurationAppearanceColumns object.  ```` ``` # Get the value of the property. propertyValue = configurationAppearanceColumns_var.objectType ``` ```` |

"configurationAppearanceColumns\_var" is a variable referencing a ConfigurationAppearanceColumns object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceColumns.h>  // Get the value of the property. string propertyValue = configurationAppearanceColumns_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |