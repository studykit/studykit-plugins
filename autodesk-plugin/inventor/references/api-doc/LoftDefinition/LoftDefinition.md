# LoftDefinition Object

## Description

The LoftDefinition object is used to define additional input required for creating loft features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../LoftDefinition/LoftDefinition_Copy.md) | Method that creates and returns a copy of this loft definition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Centerline](../LoftDefinition/LoftDefinition_Centerline.md) | Property that specifies the centerline for the loft. Valid objects includes Profile, Profile3D, EdgeLoop and EdgeCollection. When this LoftDefinition is associative with an existing LoftFeature or if it is copied from an LoftDefinition that is associative with a LoftFeature, then set this property you should follow below rules, otherwise an error would occur:  * If the LoftDefinition.LoftType returns kRegularLoft you can set this property directly. * If the LoftDefinition.LoftType returns kLoftWithRails you need to clear the LoftDefinition.LoftRails before setting this property. * If the LoftDefinition.LoftType returns kLoftWithAreaGraphSections you need to clear the LoftDefinition.LoftSectionDimensions if any before setting this property, |
| [Closed](../LoftDefinition/LoftDefinition_Closed.md) | Property that specifies whether the loft needs to be closed or not. |
| [FirstSectionAngle](../LoftDefinition/LoftDefinition_FirstSectionAngle.md) | Property that specifies the angle of the loft in relation to the sketch plane of the starting section. |
| [FirstSectionCondition](../LoftDefinition/LoftDefinition_FirstSectionCondition.md) | Property that specifies the condition of the loft at the starting section. |
| [FirstSectionDirectionReversed](../LoftDefinition/LoftDefinition_FirstSectionDirectionReversed.md) | Property that specifies whether the takeoff direction for the starting section should be reversed from its default direction. |
| [FirstSectionImpact](../LoftDefinition/LoftDefinition_FirstSectionImpact.md) | Property that specifies the impact the starting section's condition has on the shape of the entire loft. |
| [FirstSectionTangentPlane](../LoftDefinition/LoftDefinition_FirstSectionTangentPlane.md) | Property that specifies the tangent plane for the starting section in the case that the section is a point. |
| [LastSectionAngle](../LoftDefinition/LoftDefinition_LastSectionAngle.md) | Property that specifies the angle of the loft in relation to the sketch plane of the ending section. |
| [LastSectionCondition](../LoftDefinition/LoftDefinition_LastSectionCondition.md) | Property that specifies the condition of the loft at the ending section. |
| [LastSectionDirectionReversed](../LoftDefinition/LoftDefinition_LastSectionDirectionReversed.md) | Property that specifies whether the takeoff direction for the ending section should be reversed from its default direction. |
| [LastSectionImpact](../LoftDefinition/LoftDefinition_LastSectionImpact.md) | Property that specifies the impact the ending section's condition has on the shape of the entire loft. |
| [LastSectionTangentPlane](../LoftDefinition/LoftDefinition_LastSectionTangentPlane.md) | Property that specifies the tangent plane for the ending section in the case that the section is a point. |
| [LoftRails](../LoftDefinition/LoftDefinition_LoftRails.md) | Read-only property that specifies the rails for the loft. If the LoftDefinition.LoftType is not kRegularLoft or kLoftWithRails then set this property will raise error, you should follow below rules to set this property:  * If the LoftDefinition.LoftType returns kRegularLoft you can set this property directly. * If the LoftDefinition.LoftType returns kLoftWithCenterline you need to clear the LoftDefinition.Centerline before setting this property. * If the LoftDefinition.LoftType returns kLoftWithAreaGraphSections you need to clear the LoftDefinition.LoftSectionDimensions if any and LoftDefinition.Centerline before setting this property, |
| [LoftSectionDimensions](../LoftDefinition/LoftDefinition_LoftSectionDimensions.md) | Read-only property that specifies the placed section dimensions for an area-graph type loft. Before adding new LoftSectionDimension into this collection the LoftDefinition.Centerline should be set first, otherwise an error would occur. |
| [LoftType](../LoftDefinition/LoftDefinition_LoftType.md) | Property that gets the type of loft feature. |
| [MapPointCurves](../LoftDefinition/LoftDefinition_MapPointCurves.md) | Property that specifies the mapping to use between sections. |
| [MergeTangentFaces](../LoftDefinition/LoftDefinition_MergeTangentFaces.md) | Property that specifies if the tangent faces of the loft should be merged or not. |
| [Operation](../LoftDefinition/LoftDefinition_Operation.md) | Property that specifies the type of operation used to add the feature to the model. |
| [Sections](../LoftDefinition/LoftDefinition_Sections.md) | Property that specifies the sections used for a loft. |

## Accessed From

[LoftDefinition.Copy](../LoftDefinition/LoftDefinition_Copy.md), [LoftFeature.Definition](../LoftFeature/LoftFeature_Definition.md), [LoftFeatureProxy.Definition](../LoftFeatureProxy/LoftFeatureProxy_Definition.md), [LoftFeatures.CreateLoftDefinition](../LoftFeatures/LoftFeatures_CreateLoftDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |