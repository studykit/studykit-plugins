# Joint.isLightBulbOn Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Gets and sets if the light bulb of this joint as displayed in the browser is on or off. A joint will only be visible if the light bulb is switched on. However, the light bulb can be on and the joint still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the joints folder is light bulb is off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object. |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. boolean propertyValue = joint_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = joint_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |