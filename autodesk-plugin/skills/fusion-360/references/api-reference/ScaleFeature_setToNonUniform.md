# ScaleFeature.setToNonUniform Method

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

Calling this method will change to a non-uniform scale. Fails of the inputEntities collection contains sketches or components. The isUniform is set to false if successful.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a [ScaleFeature](ScaleFeature.htm) object.```` ``` returnValue = scaleFeature_var.setToNonUniform(xScale, yScale, zScale) ``` ```` |

"scaleFeature\_var" is a variable referencing a [ScaleFeature](ScaleFeature.htm) object.  ```` ``` #include <Fusion/Features/ScaleFeature.h>  returnValue = scaleFeature_var->setToNonUniform(xScale, yScale, zScale); ``` ```` |

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

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |