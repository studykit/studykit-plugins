# RefoldFeatureProxy Object

Derived from: [RefoldFeature](../RefoldFeature/RefoldFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RefoldFeatureProxy/RefoldFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [Edit](../RefoldFeatureProxy/RefoldFeatureProxy_Edit.md) | Method that edits an existing refold feature. The stop node should be positioned immediately before this feature before calling this method so that all of the input is available and in a valid state. |
| [GetReferenceKey](../RefoldFeatureProxy/RefoldFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RefoldFeatureProxy/RefoldFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RefoldFeatureProxy/RefoldFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RefoldFeatureProxy/RefoldFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RefoldFeatureProxy/RefoldFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RefoldFeatureProxy/RefoldFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RefoldFeatureProxy/RefoldFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RefoldFeatureProxy/RefoldFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RefoldFeatureProxy/RefoldFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RefoldFeatureProxy/RefoldFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RefoldFeatureProxy/RefoldFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Bends](../RefoldFeatureProxy/RefoldFeatureProxy_Bends.md) | Property that returns the collection of Bend objects refolded by this feature. |
| [ConsumeInputs](../RefoldFeatureProxy/RefoldFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../RefoldFeatureProxy/RefoldFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RefoldFeatureProxy/RefoldFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RefoldFeatureProxy/RefoldFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RefoldFeatureProxy/RefoldFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputSketches](../RefoldFeatureProxy/RefoldFeatureProxy_InputSketches.md) | Property that returns the sketches that were specifies as \input when creating this feature. |
| [IsOwnedByFeature](../RefoldFeatureProxy/RefoldFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RefoldFeatureProxy/RefoldFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../RefoldFeatureProxy/RefoldFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RefoldFeatureProxy/RefoldFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RefoldFeatureProxy/RefoldFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RefoldFeatureProxy/RefoldFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../RefoldFeatureProxy/RefoldFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ResultSketches](../RefoldFeatureProxy/RefoldFeatureProxy_ResultSketches.md) | Property that returns the sketches that were created as a \result of this feature. |
| [Shared](../RefoldFeatureProxy/RefoldFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [StationaryFace](../RefoldFeatureProxy/RefoldFeatureProxy_StationaryFace.md) | Property that returns the Face object that was specified as the stationary face during creation. |
| [Suppressed](../RefoldFeatureProxy/RefoldFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RefoldFeatureProxy/RefoldFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RefoldFeatureProxy/RefoldFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |