# FilletFeature.convert Method

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

Method that converts this feature to another fillet feature type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a [FilletFeature](FilletFeature.htm) object.```` ``` returnValue = filletFeature_var.convert(input) ``` ```` |

"filletFeature\_var" is a variable referencing a [FilletFeature](FilletFeature.htm) object.  ```` ``` #include <Fusion/Features/FilletFeature.h>  returnValue = filletFeature_var->convert(input); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the conversion was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [Base](Base.htm) | Input a fillet feature input object that defines the desired fillet. Use the FilletFeatures.create\*Input methods to create a new fillet feature input object. This can be a feature input for fillet type, rule fillet type or full round fillet type. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |