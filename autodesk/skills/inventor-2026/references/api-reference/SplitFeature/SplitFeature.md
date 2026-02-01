# SplitFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The Part SplitFeature object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SplitFeature/SplitFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../SplitFeature/SplitFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../SplitFeature/SplitFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../SplitFeature/SplitFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../SplitFeature/SplitFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../SplitFeature/SplitFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../SplitFeature/SplitFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetToSplitBody](../SplitFeature/SplitFeature_SetToSplitBody.md) | Method that changes the SplitFeature type to kSplitBody. The original body is consumed by the operation and two new bodies are created. |
| [SetToSplitFaces](../SplitFeature/SplitFeature_SetToSplitFaces.md) | Method that changes the SplitFeature type to kSplitFaces. |
| [SetToTrimSolid](../SplitFeature/SplitFeature_SetToTrimSolid.md) | Method that changes the SplitFeature type to kTrimSolid. The specified portion of the solid is removed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../SplitFeature/SplitFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../SplitFeature/SplitFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../SplitFeature/SplitFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../SplitFeature/SplitFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SplitFeature/SplitFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../SplitFeature/SplitFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../SplitFeature/SplitFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../SplitFeature/SplitFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FaceSplitSplitAll](../SplitFeature/SplitFeature_FaceSplitSplitAll.md) | Property that returns whether the split feature split all of the faces possible, or a specified subset. This property fails in the case where the split feature defines a part split. This can be determined using the SplitType property. |
| [FeatureDimensions](../SplitFeature/SplitFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../SplitFeature/SplitFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../SplitFeature/SplitFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../SplitFeature/SplitFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../SplitFeature/SplitFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../SplitFeature/SplitFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../SplitFeature/SplitFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../SplitFeature/SplitFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../SplitFeature/SplitFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RemovePositiveSide](../SplitFeature/SplitFeature_RemovePositiveSide.md) | Gets and sets which side of the split body is removed for the trim body operation. This property fails in the case where the split feature defines a face split or a split body operation. |
| [Shared](../SplitFeature/SplitFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SplitTool](../SplitFeature/SplitFeature_SplitTool.md) | Gets and sets the split tool used to create the split feature. The object can be a WorkPlane, WorkSurface, SurfaceBody or a Path. |
| [SplitToolType](../SplitFeature/SplitFeature_SplitToolType.md) | Property that returns the split tool type used to create the split feature. |
| [SplitType](../SplitFeature/SplitFeature_SplitType.md) | Property that returns the split feature type. Possible values are kSplitFaces and kSplitPart. |
| [Suppressed](../SplitFeature/SplitFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../SplitFeature/SplitFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../SplitFeature/SplitFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SplitFeatureProxy.NativeObject](../SplitFeatureProxy/SplitFeatureProxy_NativeObject.md), [SplitFeatures.Item](../SplitFeatures/SplitFeatures_Item.md), [SplitFeatures.SplitBody](../SplitFeatures/SplitFeatures_SplitBody.md), [SplitFeatures.SplitFaces](../SplitFeatures/SplitFeatures_SplitFaces.md), [SplitFeatures.TrimSolid](../SplitFeatures/SplitFeatures_TrimSolid.md)

## Derived Classes

[SplitFeatureProxy](../SplitFeatureProxy/SplitFeatureProxy.md)

## Version

Introduced in version 5
