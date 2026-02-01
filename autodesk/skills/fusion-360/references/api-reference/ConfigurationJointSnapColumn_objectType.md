# ConfigurationJointSnapColumn.objectType Property

Parent Object: [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationJointSnapColumn_var.objectType ``` ```` |

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnapColumn.h>  // Get the value of the property. string propertyValue = configurationJointSnapColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |