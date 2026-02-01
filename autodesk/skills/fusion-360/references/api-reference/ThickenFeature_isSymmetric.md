# ThickenFeature.isSymmetric Property

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Gets and sets whether to add thickness symmetrically or only on one side of the face/s to thicken.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a ThickenFeature object.  ```` ``` # Get the value of the property. propertyValue = thickenFeature_var.isSymmetric  # Set the value of the property. thickenFeature_var.isSymmetric = propertyValue ``` ```` |

"thickenFeature\_var" is a variable referencing a ThickenFeature object. ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Get the value of the property. boolean propertyValue = thickenFeature_var->isSymmetric();  // Set the value of the property, where value_var is a boolean. bool returnValue = thickenFeature_var->isSymmetric(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |