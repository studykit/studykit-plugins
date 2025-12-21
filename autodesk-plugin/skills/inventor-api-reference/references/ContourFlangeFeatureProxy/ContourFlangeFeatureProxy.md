# ContourFlangeFeatureProxy Object

Derived from: [ContourFlangeFeature](../ContourFlangeFeature/ContourFlangeFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendFeature](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_BendFeature.md) | Property that returns the associated bend feature, if there is one. |
| [ConsumeInputs](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Definition.md) | Read-write property that gets and sets the ContourFlangeDefinition object associated with this contour flange feature. |
| [ExtendedName](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
