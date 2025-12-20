# CircularPatternFeatureDefinition Object

## Description

Part Circular Pattern Definition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Copy.md) | Method that creates a copy of this CircularPatternFeatureDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. |
| [AffectedOccurrences](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_AffectedOccurrences.md) | Read-write property that gets and sets the collection of occurrences that should participate in this feature. If this property is not set, all possible occurrences will participate. This property applies only to features in an assembly. |
| [Angle](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Angle.md) | Read-write property that gets and sets the angle of the pattern. |
| [Application](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [BoundarySetting](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_BoundarySetting.md) | Read-write property that gets and sets the PatternBoundarySetting object. |
| [ComputeType](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_ComputeType.md) | Read-write property that that indicates the method of solution for the pattern. |
| [Count](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Count.md) | Read-write property that gets and sets the number of instances. |
| [HasBoundarySettingConfigured](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_HasBoundarySettingConfigured.md) | Read-write property that gets and sets whether this pattern has boundary setting configured or not. When set this property it can only be set from True to False to clear the boundary setting. |
| [LockRotation](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_LockRotation.md) | Read-write property that gets and sets whether the patterned occurrences keep the same rotation as their parent features. |
| [MidPlanePattern](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_MidPlanePattern.md) | Read-write property that gets and sets whether the patterned occurrences should fall on either side of the original. |
| [NaturalRotationAxisDirection](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_NaturalRotationAxisDirection.md) | Read-write property that gets and sets the flag that indicates if the direction of the pattern is in the natural direction of the RotationAxis or reversed. |
| [Operation](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Operation.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. Valid values are kNewBodyOperation and kJoinOperation. |
| [ParentFeatures](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_ParentFeatures.md) | Read-write property that gets and sets the parent features of the pattern. |
| [PatternOfBody](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_PatternOfBody.md) | Read-only property that gets whether this pattern resulted from patterning the SurfaceBody objects. |
| [PatternRadiusPoint](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_PatternRadiusPoint.md) | Read-write property that gets and sets the point used to define the pattern radius against the rotation axis. |
| [PositioningMethod](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_PositioningMethod.md) | Read-write property that gets and sets the enum indicating the positioning method used for pattern creation. |
| [RotationAxis](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_RotationAxis.md) | Read-write property that gets and sets the entity as rotation axis. This can be a linear Edge, a WorkAxis, a cylindrical or conical Face (axis is used). |
| [Type](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[CircularPatternFeature.Definition](../CircularPatternFeature/CircularPatternFeature_Definition.md), [CircularPatternFeatureDefinition.Copy](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_Copy.md), [CircularPatternFeatureProxy.Definition](../CircularPatternFeatureProxy/CircularPatternFeatureProxy_Definition.md), [CircularPatternFeatures.CreateDefinition](../CircularPatternFeatures/CircularPatternFeatures_CreateDefinition.md)

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |