# DeleteFaceFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The DeleteFaceFeature object represents a delete face feature on a part. A delete face feature is created interactively by using the Delete Face tool on the Feature toolbar--see Autodesk Inventor user interface help for further information about delete face features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DeleteFaceFeature/DeleteFaceFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../DeleteFaceFeature/DeleteFaceFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../DeleteFaceFeature/DeleteFaceFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../DeleteFaceFeature/DeleteFaceFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../DeleteFaceFeature/DeleteFaceFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../DeleteFaceFeature/DeleteFaceFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../DeleteFaceFeature/DeleteFaceFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../DeleteFaceFeature/DeleteFaceFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../DeleteFaceFeature/DeleteFaceFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../DeleteFaceFeature/DeleteFaceFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../DeleteFaceFeature/DeleteFaceFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DeleteFaceFeature/DeleteFaceFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../DeleteFaceFeature/DeleteFaceFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../DeleteFaceFeature/DeleteFaceFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../DeleteFaceFeature/DeleteFaceFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../DeleteFaceFeature/DeleteFaceFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../DeleteFaceFeature/DeleteFaceFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputFaces](../DeleteFaceFeature/DeleteFaceFeature_InputFaces.md) | Property that specifies the faces that were specified to create the feature. This property will return the faces only when the end of part marker is moved above this feature, else this property will return Nothing. This can either be a FaceCollection or a FaceShell object. |
| [IsOwnedByFeature](../DeleteFaceFeature/DeleteFaceFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../DeleteFaceFeature/DeleteFaceFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../DeleteFaceFeature/DeleteFaceFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../DeleteFaceFeature/DeleteFaceFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../DeleteFaceFeature/DeleteFaceFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../DeleteFaceFeature/DeleteFaceFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../DeleteFaceFeature/DeleteFaceFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../DeleteFaceFeature/DeleteFaceFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../DeleteFaceFeature/DeleteFaceFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../DeleteFaceFeature/DeleteFaceFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../DeleteFaceFeature/DeleteFaceFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DeleteFaceFeatureProxy.NativeObject](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy_NativeObject.md), [DeleteFaceFeatures.Add](../DeleteFaceFeatures/DeleteFaceFeatures_Add.md), [DeleteFaceFeatures.Item](../DeleteFaceFeatures/DeleteFaceFeatures_Item.md)

## Derived Classes

[DeleteFaceFeatureProxy](../DeleteFaceFeatureProxy/DeleteFaceFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |