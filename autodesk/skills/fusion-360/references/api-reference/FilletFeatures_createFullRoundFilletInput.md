# FilletFeatures.createFullRoundFilletInput Method

Parent Object: [FilletFeatures](FilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatures.h>

## Description

Creates a FullRoundFilletFeatureInput object. Use properties and methods on this object to define the fillet you want to create and then use the addFullRoundFillet method, passing in the FullRoundFilletFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object.```` ``` returnValue = filletFeatures_var.createFullRoundFilletInput() ``` ```` |

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FullRoundFilletFeatureInput](FullRoundFilletFeatureInput.htm) | Returns the newly created FullRoundFilletFeatureInput object or null if the creation failed. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |