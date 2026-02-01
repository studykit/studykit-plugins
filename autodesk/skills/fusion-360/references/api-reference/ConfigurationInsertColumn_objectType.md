# ConfigurationInsertColumn.objectType Property

Parent Object: [ConfigurationInsertColumn](ConfigurationInsertColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertColumn\_var" is a variable referencing a ConfigurationInsertColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationInsertColumn_var.objectType ``` ```` |

"configurationInsertColumn\_var" is a variable referencing a ConfigurationInsertColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertColumn.h>  // Get the value of the property. string propertyValue = configurationInsertColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |