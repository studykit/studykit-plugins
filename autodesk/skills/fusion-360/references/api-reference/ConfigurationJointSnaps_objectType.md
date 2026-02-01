# ConfigurationJointSnaps.objectType Property

Parent Object: [ConfigurationJointSnaps](ConfigurationJointSnaps.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnaps.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnaps\_var" is a variable referencing a ConfigurationJointSnaps object.  ```` ``` # Get the value of the property. propertyValue = configurationJointSnaps_var.objectType ``` ```` |

"configurationJointSnaps\_var" is a variable referencing a ConfigurationJointSnaps object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnaps.h>  // Get the value of the property. string propertyValue = configurationJointSnaps_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |