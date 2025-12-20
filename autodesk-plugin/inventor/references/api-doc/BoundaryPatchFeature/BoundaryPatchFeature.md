# BoundaryPatchFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

This is the Part BoundaryPatchFeature object. A BoundaryPatchFeature is produced by the creation of a planar surface within the specified boundary.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BoundaryPatchFeature/BoundaryPatchFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../BoundaryPatchFeature/BoundaryPatchFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../BoundaryPatchFeature/BoundaryPatchFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../BoundaryPatchFeature/BoundaryPatchFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../BoundaryPatchFeature/BoundaryPatchFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../BoundaryPatchFeature/BoundaryPatchFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../BoundaryPatchFeature/BoundaryPatchFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../BoundaryPatchFeature/BoundaryPatchFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../BoundaryPatchFeature/BoundaryPatchFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../BoundaryPatchFeature/BoundaryPatchFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../BoundaryPatchFeature/BoundaryPatchFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BoundaryPatchFeature/BoundaryPatchFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../BoundaryPatchFeature/BoundaryPatchFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../BoundaryPatchFeature/BoundaryPatchFeature_Definition.md) | Property that returns the BoundaryPatchDefinition object which defines the various input used to create the boundary patch feature. |
| [ExtendedName](../BoundaryPatchFeature/BoundaryPatchFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../BoundaryPatchFeature/BoundaryPatchFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../BoundaryPatchFeature/BoundaryPatchFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../BoundaryPatchFeature/BoundaryPatchFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../BoundaryPatchFeature/BoundaryPatchFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../BoundaryPatchFeature/BoundaryPatchFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../BoundaryPatchFeature/BoundaryPatchFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../BoundaryPatchFeature/BoundaryPatchFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../BoundaryPatchFeature/BoundaryPatchFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../BoundaryPatchFeature/BoundaryPatchFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../BoundaryPatchFeature/BoundaryPatchFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../BoundaryPatchFeature/BoundaryPatchFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../BoundaryPatchFeature/BoundaryPatchFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../BoundaryPatchFeature/BoundaryPatchFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../BoundaryPatchFeature/BoundaryPatchFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BoundaryPatchFeatureProxy.NativeObject](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_NativeObject.md), [BoundaryPatchFeatures.Add](../BoundaryPatchFeatures/BoundaryPatchFeatures_Add.md), [BoundaryPatchFeatures.Item](../BoundaryPatchFeatures/BoundaryPatchFeatures_Item.md)

## Derived Classes

[BoundaryPatchFeatureProxy](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy.md)

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |