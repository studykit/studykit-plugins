# AsBuiltJoint.isLightBulbOn Property

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

Gets and sets if the light bulb of this as-built joint as displayed in the browser is on or off. A joint will only be visible if the light bulb is switched on. However, the light bulb can be on and the joint still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the joints folder is light bulb is off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. |

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. ```` ``` #include <Fusion/Components/AsBuiltJoint.h>  // Get the value of the property. boolean propertyValue = asBuiltJoint_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = asBuiltJoint_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |