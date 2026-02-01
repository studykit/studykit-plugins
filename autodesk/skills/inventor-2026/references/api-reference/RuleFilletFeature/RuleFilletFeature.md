# RuleFilletFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The RuleFilletFeature object represents a rule fillet sheet metal feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RuleFilletFeature/RuleFilletFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RuleFilletFeature/RuleFilletFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RuleFilletFeature/RuleFilletFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RuleFilletFeature/RuleFilletFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RuleFilletFeature/RuleFilletFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RuleFilletFeature/RuleFilletFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RuleFilletFeature/RuleFilletFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RuleFilletFeature/RuleFilletFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RuleFilletFeature/RuleFilletFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RuleFilletFeature/RuleFilletFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RuleFilletFeature/RuleFilletFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RuleFilletFeature/RuleFilletFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../RuleFilletFeature/RuleFilletFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../RuleFilletFeature/RuleFilletFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RuleFilletFeature/RuleFilletFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RuleFilletFeature/RuleFilletFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RuleFilletFeature/RuleFilletFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RuleFilletFeature/RuleFilletFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RuleFilletFeature/RuleFilletFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../RuleFilletFeature/RuleFilletFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RuleFilletFeature/RuleFilletFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RuleFilletFeature/RuleFilletFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RuleFilletFeature/RuleFilletFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../RuleFilletFeature/RuleFilletFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RuleFilletFeature/RuleFilletFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../RuleFilletFeature/RuleFilletFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RuleFilletFeature/RuleFilletFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RuleFilletFeature/RuleFilletFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[RuleFilletFeatureProxy.NativeObject](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_NativeObject.md), [RuleFilletFeatures.Item](../RuleFilletFeatures/RuleFilletFeatures_Item.md)

## Derived Classes

[RuleFilletFeatureProxy](../RuleFilletFeatureProxy/RuleFilletFeatureProxy.md)

## Version

Introduced in version 2010
