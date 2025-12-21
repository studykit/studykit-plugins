# BoundaryPatchDefinition Object

## Description

The BoundaryPatchDefinition object is used to define the input required for creating boundary patch features.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BoundaryPatchDefinition/BoundaryPatchDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BoundaryPatchLoops](../BoundaryPatchDefinition/BoundaryPatchDefinition_BoundaryPatchLoops.md) | Property that specifies the set of boundary loops used to create the boundary patch feature. |
| [GuideRails](../BoundaryPatchDefinition/BoundaryPatchDefinition_GuideRails.md) | Property that gets and sets the guide rail objects for the boundary patch. |
| [Type](../BoundaryPatchDefinition/BoundaryPatchDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BoundaryPatchFeature.Definition](../BoundaryPatchFeature/BoundaryPatchFeature_Definition.md), [BoundaryPatchFeatureProxy.Definition](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Definition.md), [BoundaryPatchFeatures.CreateBoundaryPatchDefinition](../BoundaryPatchFeatures/BoundaryPatchFeatures_CreateBoundaryPatchDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |

## Version

Introduced in version 2008
