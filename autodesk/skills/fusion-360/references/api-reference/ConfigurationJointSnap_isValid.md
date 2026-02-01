# ConfigurationJointSnap.isValid Property

Parent Object: [ConfigurationJointSnap](ConfigurationJointSnap.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnap.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. |

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnap.h>  // Get the value of the property. boolean propertyValue = configurationJointSnap_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |