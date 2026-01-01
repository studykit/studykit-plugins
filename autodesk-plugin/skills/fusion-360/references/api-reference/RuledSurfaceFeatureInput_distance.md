# RuledSurfaceFeatureInput.distance Property

Parent Object: [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the Ruled Surface distance. If the value input is a real value it will define the distance in centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. |

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = ruledSurfaceFeatureInput_var->distance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = ruledSurfaceFeatureInput_var->distance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |