# TransientBRep.ImprintBodies Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that finds regions of faces on two bodies which overlap and creates new bodies where the faces are split at the edges of the overlaps. This does not modify the original bodies but creates new transient bodies that contain the imprints.

## Remarks

The picture below shows an example of imprinting. The picture on the left shows the initial two bodies that are positioned so there are coincident faces. The picture on the right shows the two bodies individually so you can see the result of the imprint and how the coincident faces were split.

![](../Images/ImprintBodies.png)

The ability to imprint solids can be important to applications that need to mesh models. By creating edges at the poins where solids connect, it guarantees that there will be mesh nodes along those boundaries.

## Syntax

TransientBRep.**ImprintBodies**( ***InputBodyOne*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***InputBodyTwo*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***ImprintCoincidentEdges*** As Boolean, ***OutputBodyOne*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***OutputBodyTwo*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***BodyOneOverlappingFaces*** As [Faces](../Faces/Faces.md), ***BodyTwoOverlappingFaces*** As [Faces](../Faces/Faces.md), ***BodyOneOverlappingEdges*** As [Edges](../Edges/Edges.md), ***BodyTwoOverlappingEdges*** As [Edges](../Edges/Edges.md), [***Tolerance***] As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputBodyOne | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody that will participate in the imprint operation. This body can be either a parametric or transient body. |
| InputBodyTwo | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody that will participate in the imprint operation. This body can be either a parametric or transient body. |
| ImprintCoincidentEdges | Boolean | Input Boolean that indicates if overlapping edges should be included in the result. The picture below shows an example of when this argument will make a difference. The two bodies have overlapping faces and there is also an overlapping edge. If this argument is True, then the edge shown in red below will be included in the output as an overlapping edge. If False it will not be included and only the edges of the overlapping faces will be in the overlapping faces collections. ![](../Images/ImprintOverlappingEdges.png) |
| OutputBodyOne | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Output transient SurfaceBody that contains the imprinted body that corresponds to the body provided through InputBodyOne argument. |
| OutputBodyTwo | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Output transient SurfaceBody that contains the imprinted body that corresponds to the body provided through InputBodyTwo argument. |
| BodyOneOverlappingFaces | [Faces](../Faces/Faces.md) | Output Faces collection that contains the overlapping faces that are part of OutputBodyOne. The faces from OutputBodyTwo are returned in the BodyTwoOverlappingFaces argument. Faces at the same index within the two collections are overlapping. |
| BodyTwoOverlappingFaces | [Faces](../Faces/Faces.md) | Output Faces collection that contains the overlapping faces that are part of OutputBodyTwo. The faces from OutputBodyOne are returned in the BodyOneOverlappingFaces argument. Faces at the same index within the two collections are overlapping. |
| BodyOneOverlappingEdges | [Edges](../Edges/Edges.md) | Output Edges collection that returns edges in body one that overlap with edges in body two, which are returned in the BodyTwoOverlappingEdges argument. Edges as the same index within the two collection are overlapping. |
| BodyTwoOverlappingEdges | [Edges](../Edges/Edges.md) | Output Edges collection that returns edges in body two that overlap with edges in body one, which are returned in the BodyOneOverlappingEdges argument. Edges as the same index within the two collection are overlapping. |
| Tolerance | Double | Optional Input Double that specifies the tolerance to use when comparing the bodies. If not specified, or a value of zero is specified, the internal modeling tolerance will be used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |
| [Imprint bodies within an assembly.](../../sample-programs/ImprintUsingOccurrences_Sample.md) | This sample demonstrates creating imprinted bodies from two selected occurrences in an assembly. |

## Version

Introduced in version 2014
