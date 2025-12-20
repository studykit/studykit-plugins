# DirectEditFeatureProxy Object

Derived from: [DirectEditFeature](../DirectEditFeature/DirectEditFeature.md) Object

## Description

Part DirectEdit Feature Proxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DirectEditFeatureProxy/DirectEditFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../DirectEditFeatureProxy/DirectEditFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../DirectEditFeatureProxy/DirectEditFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../DirectEditFeatureProxy/DirectEditFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../DirectEditFeatureProxy/DirectEditFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../DirectEditFeatureProxy/DirectEditFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../DirectEditFeatureProxy/DirectEditFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../DirectEditFeatureProxy/DirectEditFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../DirectEditFeatureProxy/DirectEditFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../DirectEditFeatureProxy/DirectEditFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../DirectEditFeatureProxy/DirectEditFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DirectEditFeatureProxy/DirectEditFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../DirectEditFeatureProxy/DirectEditFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../DirectEditFeatureProxy/DirectEditFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DirectEditOperations](../DirectEditFeatureProxy/DirectEditFeatureProxy_DirectEditOperations.md) | Gets all the operations of this direct edit feature. |
| [ExtendedName](../DirectEditFeatureProxy/DirectEditFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../DirectEditFeatureProxy/DirectEditFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../DirectEditFeatureProxy/DirectEditFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../DirectEditFeatureProxy/DirectEditFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../DirectEditFeatureProxy/DirectEditFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../DirectEditFeatureProxy/DirectEditFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../DirectEditFeatureProxy/DirectEditFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../DirectEditFeatureProxy/DirectEditFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../DirectEditFeatureProxy/DirectEditFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../DirectEditFeatureProxy/DirectEditFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../DirectEditFeatureProxy/DirectEditFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../DirectEditFeatureProxy/DirectEditFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../DirectEditFeatureProxy/DirectEditFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../DirectEditFeatureProxy/DirectEditFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../DirectEditFeatureProxy/DirectEditFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../DirectEditFeatureProxy/DirectEditFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |