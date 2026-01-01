# CircularPatternFeatureInput.totalAngle Property

Parent Object: [CircularPatternFeatureInput](CircularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatureInput.h>

## Description

Gets and sets total angle. A negative angle can be used to reverse the direction. An angle of 360 degrees or 2 pi radians will create a full circular pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatureInput\_var" is a variable referencing a CircularPatternFeatureInput object. |

"circularPatternFeatureInput\_var" is a variable referencing a CircularPatternFeatureInput object. ```` ``` #include <Fusion/Features/CircularPatternFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = circularPatternFeatureInput_var->totalAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = circularPatternFeatureInput_var->totalAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [circularPatternFeatures.add](circularPatternFeatures_add_Sample.htm) | Demonstrates the circularPatternFeatures.add method. To use the sample have a design open that contains at least one body. When you run the script, it will prompt you to select a body, which will be patterned around the base Y-axis. |
| [CircularPattern Feature API Sample](CircularPatternFeatureSample_Sample.htm) | Demonstrates creating a new circular pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |