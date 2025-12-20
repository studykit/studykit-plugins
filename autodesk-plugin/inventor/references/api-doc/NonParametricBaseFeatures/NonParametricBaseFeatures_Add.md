# NonParametricBaseFeatures.Add Method

Parent Object: [NonParametricBaseFeatures](../NonParametricBaseFeatures/NonParametricBaseFeatures.md)

## Description

Method that adds a NonParametricBaseFeature to the collection.

## Syntax

NonParametricBaseFeatures.**Add**( ***SurfaceBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), [***Transform***] As Variant ) As [NonParametricBaseFeature](../NonParametricBaseFeature/NonParametricBaseFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SurfaceBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody to create the new NonParametricBaseFeature in the collection. |
| Transform | Variant | Optional input Variant that specifies the transformation for the new NonParametricBaseFeature in the collection. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Imprint bodies within an assembly.](../../sample-programs/ImprintUsingOccurrences_Sample.md) | This sample demonstrates creating imprinted bodies from two selected occurrences in an assembly. |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |