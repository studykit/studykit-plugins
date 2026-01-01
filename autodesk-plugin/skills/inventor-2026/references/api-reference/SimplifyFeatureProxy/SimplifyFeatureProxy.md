# SimplifyFeatureProxy Object

Derived from: [SimplifyFeature](../SimplifyFeature/SimplifyFeature.md) Object

## Description

Part Simplify Feature Proxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SimplifyFeatureProxy/SimplifyFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../SimplifyFeatureProxy/SimplifyFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../SimplifyFeatureProxy/SimplifyFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../SimplifyFeatureProxy/SimplifyFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../SimplifyFeatureProxy/SimplifyFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../SimplifyFeatureProxy/SimplifyFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../SimplifyFeatureProxy/SimplifyFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../SimplifyFeatureProxy/SimplifyFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../SimplifyFeatureProxy/SimplifyFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../SimplifyFeatureProxy/SimplifyFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../SimplifyFeatureProxy/SimplifyFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SimplifyFeatureProxy/SimplifyFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../SimplifyFeatureProxy/SimplifyFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../SimplifyFeatureProxy/SimplifyFeatureProxy_ContainingOccurrence.md) | Use F1 key to display help topic. |
| [Definition](../SimplifyFeatureProxy/SimplifyFeatureProxy_Definition.md) | Property that gets and sets the SimplifyDefinition object associated with this simplify feature. |
| [ExtendedName](../SimplifyFeatureProxy/SimplifyFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../SimplifyFeatureProxy/SimplifyFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../SimplifyFeatureProxy/SimplifyFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../SimplifyFeatureProxy/SimplifyFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../SimplifyFeatureProxy/SimplifyFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../SimplifyFeatureProxy/SimplifyFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../SimplifyFeatureProxy/SimplifyFeatureProxy_NativeObject.md) | Use F1 key to display help topic. |
| [OwnedBy](../SimplifyFeatureProxy/SimplifyFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../SimplifyFeatureProxy/SimplifyFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../SimplifyFeatureProxy/SimplifyFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../SimplifyFeatureProxy/SimplifyFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../SimplifyFeatureProxy/SimplifyFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../SimplifyFeatureProxy/SimplifyFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../SimplifyFeatureProxy/SimplifyFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../SimplifyFeatureProxy/SimplifyFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../SimplifyFeatureProxy/SimplifyFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2026
