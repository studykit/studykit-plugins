# HoleFeatureInput.setPositionAtCenter Method

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Defines the position of the hole at the center of a circular or elliptical edge of the face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a [HoleFeatureInput](HoleFeatureInput.htm) object.```` ``` returnValue = holeFeatureInput_var.setPositionAtCenter(planarEntity, centerEdge) ``` ```` |

"holeFeatureInput\_var" is a variable referencing a [HoleFeatureInput](HoleFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane. |
| centerEdge | [BRepEdge](BRepEdge.htm) | A circular or elliptical edge whose center point will be the position of the hole. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [holeFeatures.add with Countersink](holeFeaturesCounterSink_add_Sample.htm) | Demonstrates the holeFeatures.add method using the createCountersinkInput method and postions the hole in the center of a selected circular edge. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |