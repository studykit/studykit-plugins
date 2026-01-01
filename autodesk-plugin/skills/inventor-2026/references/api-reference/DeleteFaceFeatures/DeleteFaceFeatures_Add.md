# DeleteFaceFeatures.Add Method

Parent Object: [DeleteFaceFeatures](../DeleteFaceFeatures/DeleteFaceFeatures.md)

## Description

Method that creates a new DeleteFaceFeature. The new created DeleteFaceFeature is returned.

## Syntax

DeleteFaceFeatures.**Add**( ***FacesToDelete*** As Object, [***Heal***] As Boolean ) As [DeleteFaceFeature](../DeleteFaceFeature/DeleteFaceFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FacesToDelete | Object | Input object that defines the faces to be deleted. This can either be a FaceCollection or a FaceShell object. If a FaceShell is specified, and it defines a void, this method deletes the void and restores mass to the model. If the FaceShell does not define a void, it results in the deletion of all the faces of the lump that this FaceShell belongs to. |
| Heal | Boolean | Optional input Boolean that specifies whether or not to attempt to heal gaps by extending adjacent faces until they intersect. If specified, this input is used only if a collection of faces is provided in the Faces argument. The default value is False indicating that the faces will not be healed. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |

## Version

Introduced in version 9
