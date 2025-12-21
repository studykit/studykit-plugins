# CornerChamferFeatureProxy Object

Derived from: [CornerChamferFeature](../CornerChamferFeature/CornerChamferFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Definition.md) | Property that gets the CornerChamferDefinition object associated with this fold feature. |
| [ExtendedName](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
