# KnitFeatures.Add Method

Parent Object: [KnitFeatures](../KnitFeatures/KnitFeatures.md)

## Description

Method that creates a new knit feature.

## Syntax

KnitFeatures.**Add**( ***Surfaces*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***MaximumTolerance***] As Double, [***MaintainAsSurface***] As Boolean ) As [KnitFeature](../KnitFeature/KnitFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surfaces | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that defines the input surfaces for the knit feature. Valid objects for the surfaces are WorkSurface objects and the result solid body obtained from PartComponentDefinition.SurfaceBodies.Item(1). |
| MaximumTolerance | Double | Optional Input Double that defines the maximum distance between the edges of two faces before being knit together. This value is defined in centimeters. |
| MaintainAsSurface | Boolean | Optional input Boolean that specifies if the resulting SurfaceBody should, if closed should continue to be treated as a surface or a solid. If the result is not closed it will always result in a surface.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Adding a new stitch (knit) feature](../../sample-programs/KnitFeature_Sample.md) | This sample demonstrates the creation of a stitch feature (known as the Knit feature in the API). The sample creates two work surfaces using surface extrusions and stitches them together. |

## Version

Introduced in version 2008
