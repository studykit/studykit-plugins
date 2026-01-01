# ThickenFeature.thickenType Property

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Gets and sets the thicken type for the thicken.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a ThickenFeature object.  ```` ``` # Get the value of the property. propertyValue = thickenFeature_var.thickenType  # Set the value of the property. thickenFeature_var.thickenType = propertyValue ``` ```` |

"thickenFeature\_var" is a variable referencing a ThickenFeature object. ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Get the value of the property. ThickenTypes propertyValue = thickenFeature_var->thickenType();  // Set the value of the property, where value_var is a ThickenTypes. bool returnValue = thickenFeature_var->thickenType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThickenTypes](ThickenTypes.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |