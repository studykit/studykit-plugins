# ThickenFeatureInput.thickenType Property

Parent Object: [ThickenFeatureInput](ThickenFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatureInput.h>

## Description

The thicken type used when creating a thicken. The default value is SharpThickenType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. |

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. ```` ``` #include <Fusion/Features/ThickenFeatureInput.h>  // Get the value of the property. ThickenTypes propertyValue = thickenFeatureInput_var->thickenType();  // Set the value of the property, where value_var is a ThickenTypes. bool returnValue = thickenFeatureInput_var->thickenType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThickenTypes](ThickenTypes.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |