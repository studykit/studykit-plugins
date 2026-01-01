# SilhouetteSplitFeatures.createInput Method

Parent Object: [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatures.h>

## Description

Creates a SilhouetteSplitFeatureInput object. Use properties and methods on this object to define the silhouette split you want to create and then use the Add method, passing in the SilhouetteSplitFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object.```` ``` returnValue = silhouetteSplitFeatures_var.createInput(viewDirection, targetBody, operation) ``` ```` |

"silhouetteSplitFeatures\_var" is a variable referencing a [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SilhouetteSplitFeatureInput](SilhouetteSplitFeatureInput.htm) | Returns the newly created SilhouetteSplitFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| viewDirection | [Base](Base.htm) | A construction axis, linear BRepEdge, planar BRepFace or a construction plane that defines the view direction where the silhouette is calculated. |
| targetBody | [BRepBody](BRepBody.htm) | Input the single solid body to split |
| operation | [SilhouetteSplitOperations](SilhouetteSplitOperations.htm) | The type of silhouette split operation to perform. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [silhouetteSplitFeatures.add](silhouetteSplitFeatures_add_Sample.htm) | Demonstrates the silhouetteSplitFeatures.add method. The Silhouette Split feature is limited in the bodies it will split. The simplest body to get a valid result is to create a sphere and split it. |
| [Silhouette Split Feature API Sample](SilhouetteSplitFeatureSample_Sample.htm) | Demonstrates creating a new silhouette split feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |