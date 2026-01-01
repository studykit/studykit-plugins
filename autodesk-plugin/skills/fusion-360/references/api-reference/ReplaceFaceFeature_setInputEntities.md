# ReplaceFaceFeature.setInputEntities Method

Parent Object: [ReplaceFaceFeature](ReplaceFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeature.h>

## Description

Method that sets faces to replace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeature\_var" is a variable referencing a [ReplaceFaceFeature](ReplaceFaceFeature.htm) object.```` ``` returnValue = replaceFaceFeature_var.setInputEntities(sourceFaces, isTangentChain) ``` ```` |

"replaceFaceFeature\_var" is a variable referencing a [ReplaceFaceFeature](ReplaceFaceFeature.htm) object.  ```` ``` #include <Fusion/Features/ReplaceFaceFeature.h>  returnValue = replaceFaceFeature_var->setInputEntities(sourceFaces, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceFaces | [ObjectCollection](ObjectCollection.htm) | The collection can contain the faces from a solid and/or from features. All the faces must be on the same body. |
| isTangentChain | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be included. A value of true indicates that tangent faces will be included. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |