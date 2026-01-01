# ThickenFeatureInput.thickness Property

Parent Object: [ThickenFeatureInput](ThickenFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the thickness distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. |

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. ```` ``` #include <Fusion/Features/ThickenFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = thickenFeatureInput_var->thickness();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = thickenFeatureInput_var->thickness(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |