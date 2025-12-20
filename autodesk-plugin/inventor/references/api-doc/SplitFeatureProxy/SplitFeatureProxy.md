# SplitFeatureProxy Object

Derived from: [SplitFeature](../SplitFeature/SplitFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SplitFeatureProxy/SplitFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../SplitFeatureProxy/SplitFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../SplitFeatureProxy/SplitFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../SplitFeatureProxy/SplitFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../SplitFeatureProxy/SplitFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../SplitFeatureProxy/SplitFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../SplitFeatureProxy/SplitFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetToSplitBody](../SplitFeatureProxy/SplitFeatureProxy_SetToSplitBody.md) | Method that changes the SplitFeature type to kSplitBody. The original body is consumed by the operation and two new bodies are created. |
| [SetToSplitFaces](../SplitFeatureProxy/SplitFeatureProxy_SetToSplitFaces.md) | Method that changes the SplitFeature type to kSplitFaces. |
| [SetToTrimSolid](../SplitFeatureProxy/SplitFeatureProxy_SetToTrimSolid.md) | Method that changes the SplitFeature type to kTrimSolid. The specified portion of the solid is removed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../SplitFeatureProxy/SplitFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../SplitFeatureProxy/SplitFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../SplitFeatureProxy/SplitFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../SplitFeatureProxy/SplitFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SplitFeatureProxy/SplitFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../SplitFeatureProxy/SplitFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../SplitFeatureProxy/SplitFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../SplitFeatureProxy/SplitFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../SplitFeatureProxy/SplitFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FaceSplitSplitAll](../SplitFeatureProxy/SplitFeatureProxy_FaceSplitSplitAll.md) | Property that returns whether the split feature split all of the faces possible, or a specified subset. This property fails in the case where the split feature defines a part split. This can be determined using the SplitType property. |
| [FeatureDimensions](../SplitFeatureProxy/SplitFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../SplitFeatureProxy/SplitFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../SplitFeatureProxy/SplitFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../SplitFeatureProxy/SplitFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../SplitFeatureProxy/SplitFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SplitFeatureProxy/SplitFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../SplitFeatureProxy/SplitFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../SplitFeatureProxy/SplitFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../SplitFeatureProxy/SplitFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../SplitFeatureProxy/SplitFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RemovePositiveSide](../SplitFeatureProxy/SplitFeatureProxy_RemovePositiveSide.md) | Gets and sets which side of the split body is removed for the trim body operation. This property fails in the case where the split feature defines a face split or a split body operation. |
| [Shared](../SplitFeatureProxy/SplitFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SplitTool](../SplitFeatureProxy/SplitFeatureProxy_SplitTool.md) | Gets and sets the split tool used to create the split feature. The object can be a WorkPlane, WorkSurface, SurfaceBody or a Path. |
| [SplitToolType](../SplitFeatureProxy/SplitFeatureProxy_SplitToolType.md) | Property that returns the split tool type used to create the split feature. |
| [SplitType](../SplitFeatureProxy/SplitFeatureProxy_SplitType.md) | Property that returns the split feature type. Possible values are kSplitFaces and kSplitPart. |
| [Suppressed](../SplitFeatureProxy/SplitFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../SplitFeatureProxy/SplitFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../SplitFeatureProxy/SplitFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |