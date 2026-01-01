# ScaleFeature.setToUniform Method

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

Calling this method will change to a uniform scale. The isUniform is set to true if successful.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a [ScaleFeature](ScaleFeature.htm) object.```` ``` returnValue = scaleFeature_var.setToUniform(scaleFactor) ``` ```` |

"scaleFeature\_var" is a variable referencing a [ScaleFeature](ScaleFeature.htm) object.  ```` ``` #include <Fusion/Features/ScaleFeature.h>  returnValue = scaleFeature_var->setToUniform(scaleFactor); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| scaleFactor | [ValueInput](ValueInput.htm) | A ValueInput object that defines the scale factor. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |