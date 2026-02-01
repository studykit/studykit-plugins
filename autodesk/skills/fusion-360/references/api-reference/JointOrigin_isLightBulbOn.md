# JointOrigin.isLightBulbOn Property

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Gets and sets if the light bulb of this jointOrigin as displayed in the browser is on or off. A joint origin will only be visible if the light bulb is switched on. However, the light bulb can be on and the joint origin still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the joint origins folder light bulb is off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a JointOrigin object. |

"jointOrigin\_var" is a variable referencing a JointOrigin object. ```` ``` #include <Fusion/Components/JointOrigin.h>  // Get the value of the property. boolean propertyValue = jointOrigin_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = jointOrigin_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |