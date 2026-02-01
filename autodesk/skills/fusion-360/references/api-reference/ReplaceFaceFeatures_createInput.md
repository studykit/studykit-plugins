# ReplaceFaceFeatures.createInput Method

Parent Object: [ReplaceFaceFeatures](ReplaceFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatures.h>

## Description

Creates a ReplaceFaceFeatureInput object. Use properties and methods on this object to define the replace face you want to create and then use the Add method, passing in the ReplaceFaceFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object.```` ``` returnValue = replaceFaceFeatures_var.createInput(sourceFaces, isTangentChain, targetFaces) ``` ```` |

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReplaceFaceFeatureInput](ReplaceFaceFeatureInput.htm) | Returns the newly created ReplaceFaceFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceFaces | [ObjectCollection](ObjectCollection.htm) | Input the entities that define the source faces (the faces to be replaced). The collection can contain the faces from a solid and/or features. All the faces must be on the same body. |
| isTangentChain | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be included. A value of true indicates that tangent faces will be included. |
| targetFaces | [Base](Base.htm) | Input the entities that define the target faces. The new faces must completely intersect the part. The collection can contain the surface faces, surface bodies and construction planes. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [replaceFaceFeatures.add](replaceFaceFeatures_add_Sample.htm) | Demonstrate the remove replaceFaceFeatures.add method. |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |