# ConfigurationVisibilityColumn.objectType Property

Parent Object: [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationVisibilityColumn_var.objectType ``` ```` |

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityColumn.h>  // Get the value of the property. string propertyValue = configurationVisibilityColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |