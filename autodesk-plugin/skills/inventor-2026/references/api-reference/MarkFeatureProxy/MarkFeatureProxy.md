# MarkFeatureProxy Object

Derived from: [MarkFeature](../MarkFeature/MarkFeature.md) Object

## Description

Part Mark Feature Proxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MarkFeatureProxy/MarkFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../MarkFeatureProxy/MarkFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../MarkFeatureProxy/MarkFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../MarkFeatureProxy/MarkFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [ResultEdges](../MarkFeatureProxy/MarkFeatureProxy_ResultEdges.md) | Method that gets the result edges created by this mark feature. |
| [SetAffectedBodies](../MarkFeatureProxy/MarkFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../MarkFeatureProxy/MarkFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../MarkFeatureProxy/MarkFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../MarkFeatureProxy/MarkFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../MarkFeatureProxy/MarkFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../MarkFeatureProxy/MarkFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../MarkFeatureProxy/MarkFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../MarkFeatureProxy/MarkFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../MarkFeatureProxy/MarkFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../MarkFeatureProxy/MarkFeatureProxy_ContainingOccurrence.md) | Use F1 key to display help topic. |
| [Definition](../MarkFeatureProxy/MarkFeatureProxy_Definition.md) | Property that gets and sets the MarkDefinition object associated with this feature. |
| [ExtendedName](../MarkFeatureProxy/MarkFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../MarkFeatureProxy/MarkFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../MarkFeatureProxy/MarkFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../MarkFeatureProxy/MarkFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../MarkFeatureProxy/MarkFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../MarkFeatureProxy/MarkFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../MarkFeatureProxy/MarkFeatureProxy_NativeObject.md) | Use F1 key to display help topic. |
| [OwnedBy](../MarkFeatureProxy/MarkFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../MarkFeatureProxy/MarkFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../MarkFeatureProxy/MarkFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../MarkFeatureProxy/MarkFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../MarkFeatureProxy/MarkFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../MarkFeatureProxy/MarkFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../MarkFeatureProxy/MarkFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../MarkFeatureProxy/MarkFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../MarkFeatureProxy/MarkFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2023
