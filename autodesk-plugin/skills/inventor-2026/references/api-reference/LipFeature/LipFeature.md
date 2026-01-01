# LipFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The LipFeature object represents a lip feature within the model.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../LipFeature/LipFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../LipFeature/LipFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../LipFeature/LipFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../LipFeature/LipFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../LipFeature/LipFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../LipFeature/LipFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../LipFeature/LipFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../LipFeature/LipFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../LipFeature/LipFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../LipFeature/LipFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../LipFeature/LipFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../LipFeature/LipFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../LipFeature/LipFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../LipFeature/LipFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../LipFeature/LipFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../LipFeature/LipFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../LipFeature/LipFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../LipFeature/LipFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../LipFeature/LipFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../LipFeature/LipFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../LipFeature/LipFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../LipFeature/LipFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../LipFeature/LipFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../LipFeature/LipFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../LipFeature/LipFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../LipFeature/LipFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../LipFeature/LipFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../LipFeature/LipFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[LipFeatureProxy.NativeObject](../LipFeatureProxy/LipFeatureProxy_NativeObject.md), [LipFeatures.Item](../LipFeatures/LipFeatures_Item.md)

## Derived Classes

[LipFeatureProxy](../LipFeatureProxy/LipFeatureProxy.md)

## Version

Introduced in version 2010
