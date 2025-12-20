# FlangeFeatureProxy Object

Derived from: [FlangeFeature](../FlangeFeature/FlangeFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FlangeFeatureProxy/FlangeFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../FlangeFeatureProxy/FlangeFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../FlangeFeatureProxy/FlangeFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../FlangeFeatureProxy/FlangeFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../FlangeFeatureProxy/FlangeFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../FlangeFeatureProxy/FlangeFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../FlangeFeatureProxy/FlangeFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../FlangeFeatureProxy/FlangeFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../FlangeFeatureProxy/FlangeFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../FlangeFeatureProxy/FlangeFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../FlangeFeatureProxy/FlangeFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FlangeFeatureProxy/FlangeFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendFeature](../FlangeFeatureProxy/FlangeFeatureProxy_BendFeature.md) | Property that returns the associated bend feature, if there is one. |
| [ConsumeInputs](../FlangeFeatureProxy/FlangeFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../FlangeFeatureProxy/FlangeFeatureProxy_Definition.md) | Read-only property that returns the FlangeDefinition object that provides access to all of the various settings that define this flange feature. |
| [ExtendedName](../FlangeFeatureProxy/FlangeFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../FlangeFeatureProxy/FlangeFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../FlangeFeatureProxy/FlangeFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../FlangeFeatureProxy/FlangeFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../FlangeFeatureProxy/FlangeFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../FlangeFeatureProxy/FlangeFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../FlangeFeatureProxy/FlangeFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../FlangeFeatureProxy/FlangeFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../FlangeFeatureProxy/FlangeFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../FlangeFeatureProxy/FlangeFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../FlangeFeatureProxy/FlangeFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../FlangeFeatureProxy/FlangeFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../FlangeFeatureProxy/FlangeFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../FlangeFeatureProxy/FlangeFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../FlangeFeatureProxy/FlangeFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |