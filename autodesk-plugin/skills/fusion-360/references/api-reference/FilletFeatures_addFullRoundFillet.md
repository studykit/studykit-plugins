# FilletFeatures.addFullRoundFillet Method

Parent Object: [FilletFeatures](FilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatures.h>

## Description

Creates a new full round fillet feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object.```` ``` returnValue = filletFeatures_var.addFullRoundFillet(input) ``` ```` |

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FilletFeature](FilletFeature.htm) | Returns the newly created FilletFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [FullRoundFilletFeatureInput](FullRoundFilletFeatureInput.htm) | A FullRoundFilletFeatureInput object that defines the desired fillet. Use the createFullRoundFilletInput method to create a new FullRoundFilletFeatureInput object and then use methods on it (the FullRoundFilletFeatureInput object) to define the fillet. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |