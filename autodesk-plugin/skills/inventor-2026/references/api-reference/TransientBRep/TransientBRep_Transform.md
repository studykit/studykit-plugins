# TransientBRep.Transform Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that transforms the input SurfaceBody.

## Remarks

This method is only valid for transient SurfaceBody object.

## Syntax

TransientBRep.**Transform**( ***SurfaceBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***Transform*** As [Matrix](../Matrix/Matrix.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SurfaceBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object. |
| Transform | [Matrix](../Matrix/Matrix.md) | Input Matrix that defines the transform to apply to the input B-Rep entity. This matrix can only define rotations and translations, it cannot define scaling, shearing, or perspective and will fail for these cases. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |
| [Imprint bodies within an assembly.](../../sample-programs/ImprintUsingOccurrences_Sample.md) | This sample demonstrates creating imprinted bodies from two selected occurrences in an assembly. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 2009
