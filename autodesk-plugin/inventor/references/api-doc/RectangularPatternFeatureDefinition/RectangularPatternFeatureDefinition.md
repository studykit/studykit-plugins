# RectangularPatternFeatureDefinition Object

## Description

Part Rectangular Pattern Definition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_Copy.md) | Method that creates a copy of this RectangularPatternFeatureDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. |
| [AffectedOccurrences](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_AffectedOccurrences.md) | Read-write property that gets and sets the collection of occurrences that should participate in this feature. If this property is not set, all possible occurrences will participate. This property applies only to features in an assembly. |
| [Application](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [BoundarySetting](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_BoundarySetting.md) | Read-write property that gets and sets the PatternBoundarySetting object. |
| [ComputeType](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_ComputeType.md) | Read-write property that that indicates the method of solution for the pattern. |
| [HasBoundarySettingConfigured](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_HasBoundarySettingConfigured.md) | Read-write property that gets and sets whether this pattern has boundary setting configured or not. When set this property it can only be set from True to False to clear the boundary setting. |
| [NaturalXDirection](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_NaturalXDirection.md) | Read-write property that gets and sets the flag that indicates if the direction of the pattern is in the natural direction of the XDirectionEntity or reversed. |
| [NaturalYDirection](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_NaturalYDirection.md) | Read-write property that gets and sets the flag that indicates if the direction of the pattern is in the natural direction of the YDirectionEntity or reversed. |
| [Operation](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_Operation.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. Valid values are kNewBodyOperation and kJoinOperation. |
| [OrientationMethod](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_OrientationMethod.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. Valid values are kNewBodyOperation and kJoinOperation. |
| [ParentFeatures](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_ParentFeatures.md) | Read-write property that gets and sets the parent features of the pattern. |
| [PatternOfBody](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_PatternOfBody.md) | Read-only property that gets whether this pattern resulted from patterning the SurfaceBody objects. |
| [Type](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_Type.md) | Gets the constant that indicates the type of this object. |
| [XCount](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_XCount.md) | Read-write property that gets and sets the number of instances in the X direction. |
| [XDirectionEntity](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_XDirectionEntity.md) | Read-write property that gets and sets the X direction entity. This can be a linear Edge, a WorkAxis, a WorkPlane (normal is used), a planar Face (normal is used), or a GeometryIntent. |
| [XDirectionMidPlanePattern](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_XDirectionMidPlanePattern.md) | Read-write property that gets and sets whether the patterned occurrences should fall on either side of the original in the X direction. |
| [XDirectionSpacingType](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_XDirectionSpacingType.md) | Read-write property that gets and sets the enum that indicates if the occurrences in the x-direction have been fitted within a specified distance. Valid values are kDefault, kFitted and kFitToPathLength. |
| [XDirectionStartPoint](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_XDirectionStartPoint.md) | Read-write property that gets and sets the X direction start point. This can be a vertex, planar sketch point or a 3D sketch point. |
| [XSpacing](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_XSpacing.md) | Read-write property that gets and sets the spacing between instances in the X direction. |
| [YCount](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_YCount.md) | Read-write property that gets and sets the number of instances in the Y direction. |
| [YDirectionEntity](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_YDirectionEntity.md) | Read-write property that gets and sets the Y direction entity. This can be a linear Edge, a WorkAxis, a WorkPlane (normal is used), a planar Face (normal is used), or a GeometryIntent. |
| [YDirectionMidPlanePattern](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_YDirectionMidPlanePattern.md) | Read-write property that gets and sets whether the patterned occurrences should fall on either side of the original in the Y direction. |
| [YDirectionSpacingType](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_YDirectionSpacingType.md) | Read-write property that gets and sets the enum that indicates if the occurrences in the y-direction have been fitted within a specified distance. Valid values are kDefault, kFitted and kFitToPathLength. |
| [YDirectionStartPoint](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_YDirectionStartPoint.md) | Read-write property that gets and sets the Y direction start point. This can be a vertex, planar sketch point or a 3D sketch point. |
| [YSpacing](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_YSpacing.md) | Read-write property that gets and sets the spacing between instances in the Y direction. |

## Accessed From

[RectangularPatternFeature.Definition](../RectangularPatternFeature/RectangularPatternFeature_Definition.md), [RectangularPatternFeatureDefinition.Copy](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_Copy.md), [RectangularPatternFeatureProxy.Definition](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Definition.md), [RectangularPatternFeatures.CreateDefinition](../RectangularPatternFeatures/RectangularPatternFeatures_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Pattern Feature with PatternBoundarySetting Sample](../../sample-programs/CreatePatternBoundarySettingSample_Sample.md) | This sample demonstrates how to create a rectangular pattern feature with boundary settings. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |