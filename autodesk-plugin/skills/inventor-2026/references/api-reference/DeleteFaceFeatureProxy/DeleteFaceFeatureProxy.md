# DeleteFaceFeatureProxy Object

Derived from: [DeleteFaceFeature](../DeleteFaceFeature/DeleteFaceFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputFaces](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_InputFaces.md) | Property that specifies the faces that were specified to create the feature. This property will return the faces only when the end of part marker is moved above this feature, else this property will return Nothing. This can either be a FaceCollection or a FaceShell object. |
| [IsOwnedByFeature](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
