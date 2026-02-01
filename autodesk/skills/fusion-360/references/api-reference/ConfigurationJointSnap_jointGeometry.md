# ConfigurationJointSnap.jointGeometry Property

Parent Object: [ConfigurationJointSnap](ConfigurationJointSnap.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnap.h>

## Description

Gets and sets the JointGeometry object for this snap.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. |

"configurationJointSnap\_var" is a variable referencing a ConfigurationJointSnap object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnap.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationJointSnap_var->jointGeometry();  // Set the value of the property, where value_var is a Base. bool returnValue = configurationJointSnap_var->jointGeometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |