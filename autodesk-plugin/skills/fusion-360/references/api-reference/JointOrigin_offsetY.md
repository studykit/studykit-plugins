# JointOrigin.offsetY Property

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Gets the parameter that controls the Y offset direction. The value can be changed using the functionality of the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a JointOrigin object. |

"jointOrigin\_var" is a variable referencing a JointOrigin object. ```` ``` #include <Fusion/Components/JointOrigin.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = jointOrigin_var->offsetY(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |