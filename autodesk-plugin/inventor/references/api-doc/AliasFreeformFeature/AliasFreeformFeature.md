# AliasFreeformFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../AliasFreeformFeature/AliasFreeformFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../AliasFreeformFeature/AliasFreeformFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../AliasFreeformFeature/AliasFreeformFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../AliasFreeformFeature/AliasFreeformFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../AliasFreeformFeature/AliasFreeformFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../AliasFreeformFeature/AliasFreeformFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../AliasFreeformFeature/AliasFreeformFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../AliasFreeformFeature/AliasFreeformFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../AliasFreeformFeature/AliasFreeformFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../AliasFreeformFeature/AliasFreeformFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../AliasFreeformFeature/AliasFreeformFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AliasFreeformFeature/AliasFreeformFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../AliasFreeformFeature/AliasFreeformFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../AliasFreeformFeature/AliasFreeformFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../AliasFreeformFeature/AliasFreeformFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../AliasFreeformFeature/AliasFreeformFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../AliasFreeformFeature/AliasFreeformFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../AliasFreeformFeature/AliasFreeformFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../AliasFreeformFeature/AliasFreeformFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../AliasFreeformFeature/AliasFreeformFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../AliasFreeformFeature/AliasFreeformFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../AliasFreeformFeature/AliasFreeformFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../AliasFreeformFeature/AliasFreeformFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../AliasFreeformFeature/AliasFreeformFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../AliasFreeformFeature/AliasFreeformFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../AliasFreeformFeature/AliasFreeformFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../AliasFreeformFeature/AliasFreeformFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../AliasFreeformFeature/AliasFreeformFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AliasFreeformFeatures.Item](../AliasFreeformFeatures/AliasFreeformFeatures_Item.md)

## Derived Classes

[AliasFreeformFeatureProxy](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |