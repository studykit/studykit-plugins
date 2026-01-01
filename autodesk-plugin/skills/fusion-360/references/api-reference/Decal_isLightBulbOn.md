# Decal.isLightBulbOn Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Gets and sets if the light bulb of this decal as displayed in the browser is on or off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object.  ```` ``` # Get the value of the property. propertyValue = decal_var.isLightBulbOn  # Set the value of the property. decal_var.isLightBulbOn = propertyValue ``` ```` |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. boolean propertyValue = decal_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = decal_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |