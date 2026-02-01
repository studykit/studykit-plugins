# MirrorFeatureDefinition Object

## Description

Part Rectangular Pattern Definition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../MirrorFeatureDefinition/MirrorFeatureDefinition_Copy.md) | Method that creates a copy of this MirrorFeatureDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../MirrorFeatureDefinition/MirrorFeatureDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. This is only ap. |
| [Application](../MirrorFeatureDefinition/MirrorFeatureDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ComputeType](../MirrorFeatureDefinition/MirrorFeatureDefinition_ComputeType.md) | Read-write property that that indicates the method of solution for the pattern. |
| [MirrorOfBody](../MirrorFeatureDefinition/MirrorFeatureDefinition_MirrorOfBody.md) | Read-only property that gets whether this mirror feature resulted from mirroring the SurfaceBody objects. |
| [MirrorPlaneEntity](../MirrorFeatureDefinition/MirrorFeatureDefinition_MirrorPlaneEntity.md) | Read-write property that gets and sets the mirror plane. This can be either a planar face or work plane. |
| [Operation](../MirrorFeatureDefinition/MirrorFeatureDefinition_Operation.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. This is only applied when MirrorOfBody is True. Valid values are kNewBodyOperation and kJoinOperation. |
| [ParentFeatures](../MirrorFeatureDefinition/MirrorFeatureDefinition_ParentFeatures.md) | Read-write property that gets and sets the parent features of the pattern. |
| [RemoveOriginal](../MirrorFeatureDefinition/MirrorFeatureDefinition_RemoveOriginal.md) | Read-write property that gets and sets whether to remove the original portion after the mirror operation. This property only applies if MirrorOfBody is True. |
| [Type](../MirrorFeatureDefinition/MirrorFeatureDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[MirrorFeature.Definition](../MirrorFeature/MirrorFeature_Definition.md), [MirrorFeatureDefinition.Copy](../MirrorFeatureDefinition/MirrorFeatureDefinition_Copy.md), [MirrorFeatureProxy.Definition](../MirrorFeatureProxy/MirrorFeatureProxy_Definition.md), [MirrorFeatures.CreateDefinition](../MirrorFeatures/MirrorFeatures_CreateDefinition.md)

## Version

Introduced in version 2017
