# DraftFeatures.createInput Method

Parent Object: [DraftFeatures](DraftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

Creates a DraftFeatureInput object. Use properties and methods on this object to define the draft you want to create and then use the Add method, passing in the DraftFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object.  ```` ``` #include <Fusion/Features/DraftFeatures.h>  // Uses no optional arguments. returnValue = draftFeatures_var->createInput(inputFaces, plane);  // Uses optional arguments. returnValue = draftFeatures_var->createInput(inputFaces, plane, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftFeatureInput](DraftFeatureInput.htm) | Returns the newly created DraftFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputFaces | BRepFace[] | BRepFace array that contains the faces to which draft will be applied. The picked point on face is always the point returned from pointOnFace property of the first BRepFace in this collection. |
| plane | [Base](Base.htm) | Input object that defines the direction in which the draft is applied. This can be a planar BrepFace, or a ConstructionPlane. |
| isTangentChain | boolean | A boolean value for setting whether or not faces that are tangentially connected to any of the input faces (if any) will also be included. It defaults to true.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [draftFeatures.add](draftFeatures_add_Sample.htm) | Demonstrates the draftFeatures.add method. To use this sample, have a design open that contains at least one body. When you run the sample, you will be prompted to select the face to draft. Because the pull direction is using the base X-Y plane, you need to select a face that is not parallel to the X-Y plane. |
| [Draft Feature API Sample](DraftFeatureSample_Sample.htm) | Demonstrates creating a new draft feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |