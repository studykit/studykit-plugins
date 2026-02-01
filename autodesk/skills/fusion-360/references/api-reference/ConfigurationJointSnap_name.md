# ConfigurationJointSnap.name Property

Parent Object: [ConfigurationJointSnap](ConfigurationJointSnap.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnap.h>

## Description

Gets and sets the name of the snap.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. |

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnap.h>  // Get the value of the property. string propertyValue = configurationJointSnap_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = configurationJointSnap_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |