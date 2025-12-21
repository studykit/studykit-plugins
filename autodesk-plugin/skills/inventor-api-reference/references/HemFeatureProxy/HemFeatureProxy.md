# HemFeatureProxy Object

Derived from: [HemFeature](../HemFeature/HemFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HemFeatureProxy/HemFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../HemFeatureProxy/HemFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../HemFeatureProxy/HemFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../HemFeatureProxy/HemFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../HemFeatureProxy/HemFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../HemFeatureProxy/HemFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../HemFeatureProxy/HemFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../HemFeatureProxy/HemFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../HemFeatureProxy/HemFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../HemFeatureProxy/HemFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../HemFeatureProxy/HemFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HemFeatureProxy/HemFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../HemFeatureProxy/HemFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../HemFeatureProxy/HemFeatureProxy_Definition.md) | Property that gets the HemDefinition object associated with this fold feature. |
| [ExtendedName](../HemFeatureProxy/HemFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../HemFeatureProxy/HemFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../HemFeatureProxy/HemFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../HemFeatureProxy/HemFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../HemFeatureProxy/HemFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../HemFeatureProxy/HemFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../HemFeatureProxy/HemFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../HemFeatureProxy/HemFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../HemFeatureProxy/HemFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../HemFeatureProxy/HemFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../HemFeatureProxy/HemFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../HemFeatureProxy/HemFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../HemFeatureProxy/HemFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../HemFeatureProxy/HemFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../HemFeatureProxy/HemFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
