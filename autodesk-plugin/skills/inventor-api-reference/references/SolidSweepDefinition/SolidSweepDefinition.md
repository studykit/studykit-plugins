# SolidSweepDefinition Object

## Description

SolidSweepDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../SolidSweepDefinition/SolidSweepDefinition_Copy.md) | Method that creates a copy of this SolidSweepDefinition object. The new SolidSweepDefinition object is independent of any feature. It can be edited and used as input to edit an existing feature or to create a new Sweep feature. |
| [SetOrientationInfo](../SolidSweepDefinition/SolidSweepDefinition_SetOrientationInfo.md) | Method that sets the orientation info. |
| [SetTwistInfo](../SolidSweepDefinition/SolidSweepDefinition_SetTwistInfo.md) | Method that sets the twist angle info. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../SolidSweepDefinition/SolidSweepDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. |
| [AlignToVector](../SolidSweepDefinition/SolidSweepDefinition_AlignToVector.md) | Read-write property that gets and sets the object to define the align to vector. |
| [Application](../SolidSweepDefinition/SolidSweepDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [KeepToolbody](../SolidSweepDefinition/SolidSweepDefinition_KeepToolbody.md) | Read-write property that gets and sets whether to keep the toolbody. |
| [Operation](../SolidSweepDefinition/SolidSweepDefinition_Operation.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. |
| [Orientation](../SolidSweepDefinition/SolidSweepDefinition_Orientation.md) | Read-write property that gets and sets the orientation of sweep. |
| [Parent](../SolidSweepDefinition/SolidSweepDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Path](../SolidSweepDefinition/SolidSweepDefinition_Path.md) | Read-write property that gets and sets the entity that defines the path of the sweep. |
| [ToolBody](../SolidSweepDefinition/SolidSweepDefinition_ToolBody.md) | Read-write property that gets and sets the SurfaceBody object used to define the toolbody of the sweep. |
| [TwistAngle](../SolidSweepDefinition/SolidSweepDefinition_TwistAngle.md) | Read-write property that gets and sets the twist angle of sweep. |
| [TwistAxis](../SolidSweepDefinition/SolidSweepDefinition_TwistAxis.md) | Read-write property that gets and sets the twist axis. |
| [Type](../SolidSweepDefinition/SolidSweepDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[SolidSweepDefinition.Copy](../SolidSweepDefinition/SolidSweepDefinition_Copy.md), [SweepFeature.SolidSweepDefinition](../SweepFeature/SweepFeature_SolidSweepDefinition.md), [SweepFeatureProxy.SolidSweepDefinition](../SweepFeatureProxy/SweepFeatureProxy_SolidSweepDefinition.md), [SweepFeatures.CreateSolidSweepDefinition](../SweepFeatures/SweepFeatures_CreateSolidSweepDefinition.md)

## Version

Introduced in version 2019
