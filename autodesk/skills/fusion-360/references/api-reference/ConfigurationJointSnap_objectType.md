# ConfigurationJointSnap.objectType Property

Parent Object: [ConfigurationJointSnap](ConfigurationJointSnap.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnap.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object.  ```` ``` # Get the value of the property. propertyValue = configurationJointSnap_var.objectType ``` ```` |

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnap.h>  // Get the value of the property. string propertyValue = configurationJointSnap_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |