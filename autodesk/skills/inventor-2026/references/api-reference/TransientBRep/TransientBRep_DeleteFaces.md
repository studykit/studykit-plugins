# TransientBRep.DeleteFaces Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that modifies an existing transient surface body by deleting specified faces.

## Remarks

This method allows you to either delete or save a list of specified faces. If you don't want the original SurfaceBody to be modified you can use the TransientBRep.Copy method to create a copy of the body to use as input.

## Syntax

TransientBRep.**DeleteFaces**( ***Faces*** As Object, ***DeleteSpecifiedFaces*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | Object | Input Object to specifies the Face object(s) to either delete or save. This argument can be a single Face object or it can be a FaceCollection to specify more than one face. Depending on the value of the second argument these faces will be deleted or saved in the SurfaceBody. If a FaceCollection is provided as input all of the input faces must exist within the same transient SurfaceBody object. |
| DeleteSpecifiedFaces | Boolean | Input Boolean that indicates if the face(s) specified in the Faces argument should be deleted or saved. If True, then the specified face(s) will be deleted from the SurfaceBody. If False, the specified face(s) will be saved and all other faces in the SurfaceBody will be deleted. |

## Version

Introduced in version 2009
