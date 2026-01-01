# ConfigurationTable.objectType Property

Parent Object: [ConfigurationTable](ConfigurationTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTable.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTable\_var" is a variable referencing a ConfigurationTable object.  ```` ``` # Get the value of the property. propertyValue = configurationTable_var.objectType ``` ```` |

"configurationTable\_var" is a variable referencing a ConfigurationTable object. ```` ``` #include <Fusion/Configurations/ConfigurationTable.h>  // Get the value of the property. string propertyValue = configurationTable_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |