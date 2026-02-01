# ScaleFeatureInput.setToNonUniform Method

Parent Object: [ScaleFeatureInput](ScaleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatureInput.h>

## Description

Sets the scale factor for the x, y, z directions to define a non-uniform scale. Calling this method will cause the isUniform property to be set to false. This will fail if the inputEntities collection contains sketches or components.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatureInput\_var" is a variable referencing a [ScaleFeatureInput](ScaleFeatureInput.htm) object.```` ``` returnValue = scaleFeatureInput_var.setToNonUniform(xScale, yScale, zScale) ``` ```` |

"scaleFeatureInput\_var" is a variable referencing a [ScaleFeatureInput](ScaleFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xScale | [ValueInput](ValueInput.htm) | A ValueInput object that defines the scale in the X direction. |
| yScale | [ValueInput](ValueInput.htm) | A ValueInput object that defines the scale in the Y direction. |
| zScale | [ValueInput](ValueInput.htm) | A ValueInput object that defines the scale in the Z direction. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Scale Feature API Sample](ScaleFeatureSample_Sample.htm) | Demonstrates creating a new scale feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |