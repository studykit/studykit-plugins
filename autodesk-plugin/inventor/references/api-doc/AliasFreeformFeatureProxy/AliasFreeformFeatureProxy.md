# AliasFreeformFeatureProxy Object

Derived from: [AliasFreeformFeature](../AliasFreeformFeature/AliasFreeformFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../AliasFreeformFeatureProxy/AliasFreeformFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |