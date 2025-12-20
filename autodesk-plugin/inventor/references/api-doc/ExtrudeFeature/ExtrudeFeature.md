# ExtrudeFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The ExtrudeFeature object represents extruded modeling features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../ExtrudeFeature/ExtrudeFeature_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../ExtrudeFeature/ExtrudeFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ExtrudeFeature/ExtrudeFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ExtrudeFeature/ExtrudeFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ExtrudeFeature/ExtrudeFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ExtrudeFeature/ExtrudeFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ExtrudeFeature/ExtrudeFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ExtrudeFeature/ExtrudeFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ExtrudeFeature/ExtrudeFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ExtrudeFeature/ExtrudeFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ExtrudeFeature/ExtrudeFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ExtrudeFeature/ExtrudeFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ExtrudeFeature/ExtrudeFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ExtrudeFeature/ExtrudeFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../ExtrudeFeature/ExtrudeFeature_Definition.md) | Read-write property that gets and sets the ExtrudeDefinition object associated with this feature. |
| [EndFaces](../ExtrudeFeature/ExtrudeFeature_EndFaces.md) | Property that returns the set of that cap one end of the extrusion. |
| [ExtendedName](../ExtrudeFeature/ExtrudeFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ExtrudeFeature/ExtrudeFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ExtrudeFeature/ExtrudeFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ExtrudeFeature/ExtrudeFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ExtrudeFeature/ExtrudeFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ExtrudeFeature/ExtrudeFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ExtrudeFeature/ExtrudeFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ExtrudeFeature/ExtrudeFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ExtrudeFeature/ExtrudeFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ExtrudeFeature/ExtrudeFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ExtrudeFeature/ExtrudeFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ExtrudeFeature/ExtrudeFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../ExtrudeFeature/ExtrudeFeature_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [StartFaces](../ExtrudeFeature/ExtrudeFeature_StartFaces.md) | Property that returns the set of that cap one end of the extrusion and are coincident with the sketch plane. In the case of a symmetric extrusion these faces are the ones on the positive normal side of the sketch plane. In the case where there aren't any start faces this property will return Nothing. |
| [Suppressed](../ExtrudeFeature/ExtrudeFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ExtrudeFeature/ExtrudeFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ExtrudeFeature/ExtrudeFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ExtrudeDefinition.Parent](../ExtrudeDefinition/ExtrudeDefinition_Parent.md), [ExtrudeFeatureProxy.NativeObject](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_NativeObject.md), [ExtrudeFeatures.Add](../ExtrudeFeatures/ExtrudeFeatures_Add.md), [ExtrudeFeatures.Item](../ExtrudeFeatures/ExtrudeFeatures_Item.md)

## Derived Classes

[ExtrudeFeatureProxy](../ExtrudeFeatureProxy/ExtrudeFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |