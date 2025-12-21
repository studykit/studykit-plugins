# SweepDefinition Object

## Description

The SweepDefinition object is the base class that defines the variables for sweep features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../SweepDefinition/SweepDefinition_Copy.md) | Method that creates a copy of this SweepDefinition object. The new SweepDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new Sweep feature. |
| [GetSectionTwists](../SweepDefinition/SweepDefinition_GetSectionTwists.md) | Method that gets the twisted sweep sections and the twist conditions at these sections. This method is applicable when the SweepType is kPathAndSectionTwistSweepType. |
| [SetSectionTwists](../SweepDefinition/SweepDefinition_SetSectionTwists.md) | Method that sets the twisted sweep sections and the twist conditions at these sections. This method is applicable when the SweepType is kPathAndSectionTwistSweepType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../SweepDefinition/SweepDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. |
| [AffectedOccurrences](../SweepDefinition/SweepDefinition_AffectedOccurrences.md) | Read-write property that gets and sets the collection of occurrences that should participate in this feature. If this property is not set, all possible occurrences will participate. This property applies only to features in an assembly. |
| [Application](../SweepDefinition/SweepDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [GuideRail](../SweepDefinition/SweepDefinition_GuideRail.md) | Read-write property that gets and sets the guide rail for the sweep which is the guide curve that controls the scaling and twist of the sweep profile. This property is applicable when the SweepType is kPathAndGuideRailSweepType. |
| [GuideSurface](../SweepDefinition/SweepDefinition_GuideSurface.md) | Read-write property that gets and sets the guide surface the normal of which controls the twist of the swept profile about the path. This property is applicable when the SweepType is kPathAndGuideSurfaceSweepType. |
| [Operation](../SweepDefinition/SweepDefinition_Operation.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. |
| [Parent](../SweepDefinition/SweepDefinition_Parent.md) | Property that returns the parent SweepFeature of the definition. |
| [Path](../SweepDefinition/SweepDefinition_Path.md) | Read-write property that gets and sets the entity that defines the path of the sweep. |
| [Profile](../SweepDefinition/SweepDefinition_Profile.md) | Read-write property that gets and sets the profile object used to define the shape of the sweep. |
| [ProfileOrientation](../SweepDefinition/SweepDefinition_ProfileOrientation.md) | Read-write property that gets and sets the orientation of sweep profile. This property is applicable when the SweepType is kPathSweepType and kPathAndSectionTwistSweepType. |
| [ProfileScaling](../SweepDefinition/SweepDefinition_ProfileScaling.md) | Read-write property that gets and sets the scaling direction for sweep profile. This property is applicable when the SweepType is kPathAndGuideRailSweepType. |
| [SweepType](../SweepDefinition/SweepDefinition_SweepType.md) | Read-write property that gets and sets the sweep type. When set this value the properties in this SweepDefinition which are not supported with the sweep type will be reset. |
| [TaperAngle](../SweepDefinition/SweepDefinition_TaperAngle.md) | Read-write property that gets and sets the taper angle of sweep. This property is applicable when the SweepType is kPathSweepType and kPathAndSectionTwistSweepType and when the ProfileOrientation is kNormalToPath. |
| [TwistAngle](../SweepDefinition/SweepDefinition_TwistAngle.md) | Read-write property that gets and sets the twist angle of sweep. This property is applicable when the SweepType is kPathSweepType and the ProfileOrientation is kNormalToPath. |
| [Type](../SweepDefinition/SweepDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SweepDefinition.Copy](../SweepDefinition/SweepDefinition_Copy.md), [SweepFeature.Definition](../SweepFeature/SweepFeature_Definition.md), [SweepFeatureProxy.Definition](../SweepFeatureProxy/SweepFeatureProxy_Definition.md), [SweepFeatures.CreateSweepDefinition](../SweepFeatures/SweepFeatures_CreateSweepDefinition.md)

## Version

Introduced in version 11
