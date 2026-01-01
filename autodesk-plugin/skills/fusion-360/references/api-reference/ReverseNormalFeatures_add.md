# ReverseNormalFeatures.add Method

Parent Object: [ReverseNormalFeatures](ReverseNormalFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeatures.h>

## Description

Creates a new Reverse Normal feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeatures\_var" is a variable referencing a [ReverseNormalFeatures](ReverseNormalFeatures.htm) object.```` ``` returnValue = reverseNormalFeatures_var.add(surfaces) ``` ```` |

"reverseNormalFeatures\_var" is a variable referencing a [ReverseNormalFeatures](ReverseNormalFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReverseNormalFeature](ReverseNormalFeature.htm) | Returns the newly created ReverseNormalFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| surfaces | [ObjectCollection](ObjectCollection.htm) | One or more surface bodies (open BRepBodies) containing the faces whose normals are to be reversed. All faces of the input surface bodies get reversed. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [reverseNormalFeatures.add](reverseNormalFeatures_add_Sample.htm) | Demonstrates the reverseNormalFeatures.add method. |
| [Reverse Normal Feature](ReverseNormalFeatureSample_Sample.htm) | Demonstrates creating a new reverse normal feature. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |