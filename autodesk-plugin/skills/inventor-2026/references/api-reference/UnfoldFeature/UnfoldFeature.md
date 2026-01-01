# UnfoldFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The UnfoldFeature object (together with it's complementary RefoldFeature object) allows sheet metal features to be added when the model is flat (unfolded) and then the model can be refolded.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../UnfoldFeature/UnfoldFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [Edit](../UnfoldFeature/UnfoldFeature_Edit.md) | Method that edits an existing unfold feature. The stop node should be positioned immediately before this feature before calling this method so that all of the input is available and in a valid state. |
| [GetReferenceKey](../UnfoldFeature/UnfoldFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../UnfoldFeature/UnfoldFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../UnfoldFeature/UnfoldFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../UnfoldFeature/UnfoldFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../UnfoldFeature/UnfoldFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../UnfoldFeature/UnfoldFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../UnfoldFeature/UnfoldFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../UnfoldFeature/UnfoldFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../UnfoldFeature/UnfoldFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../UnfoldFeature/UnfoldFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../UnfoldFeature/UnfoldFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Bends](../UnfoldFeature/UnfoldFeature_Bends.md) | Property that returns the collection of Bend objects unfolded by this feature. |
| [ConsumeInputs](../UnfoldFeature/UnfoldFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../UnfoldFeature/UnfoldFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../UnfoldFeature/UnfoldFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../UnfoldFeature/UnfoldFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../UnfoldFeature/UnfoldFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputSketches](../UnfoldFeature/UnfoldFeature_InputSketches.md) | Property that returns the sketches that were specifies as \input when creating this feature. |
| [IsOwnedByFeature](../UnfoldFeature/UnfoldFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../UnfoldFeature/UnfoldFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../UnfoldFeature/UnfoldFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../UnfoldFeature/UnfoldFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../UnfoldFeature/UnfoldFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../UnfoldFeature/UnfoldFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../UnfoldFeature/UnfoldFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ResultSketches](../UnfoldFeature/UnfoldFeature_ResultSketches.md) | Property that returns the sketches that were created as a \result of this feature. The ReferencedEntity property of the sketches returned will return the input sketch this result is based on. |
| [Shared](../UnfoldFeature/UnfoldFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [StationaryFace](../UnfoldFeature/UnfoldFeature_StationaryFace.md) | Property that returns the Face object that was specified as the stationary face during creation. This property can return Nothing in the case where the face has been consumed by another operation and no longer exists in the model. Rolling back the state of the model to a point where the face exists will allow you to access it. |
| [Suppressed](../UnfoldFeature/UnfoldFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../UnfoldFeature/UnfoldFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../UnfoldFeature/UnfoldFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[UnfoldFeatures.Add](../UnfoldFeatures/UnfoldFeatures_Add.md), [UnfoldFeatures.Item](../UnfoldFeatures/UnfoldFeatures_Item.md)

## Derived Classes

[UnfoldFeatureProxy](../UnfoldFeatureProxy/UnfoldFeatureProxy.md)

## Version

Introduced in version 2010
