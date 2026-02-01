# SplitFeatures.SplitFaces Method

Parent Object: [SplitFeatures](../SplitFeatures/SplitFeatures.md)

## Description

Method that creates a new SplitFeature by splitting faces of a part. The new SplitFeature is returned.

## Syntax

SplitFeatures.**SplitFaces**( ***SplitTool*** As Object, [***SplitAll***] As Boolean, [***FacesOrBody***] As Variant ) As [SplitFeature](../SplitFeature/SplitFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplitTool | Object | Input Object that defines the parting line for the split. The input can be a WorkPlane, WorkSurface, SurfaceBody or a Path. Use the CreatePath or CreateSpecifiedPath method on the PartFeatures object to create a Path. Currently, a Path may only consist of 2D sketch elements. |
| SplitAll | Boolean | Optional input Boolean that indicates whether to split all the faces possible on the part. The default is true indicating that all possible faces will be split. If False, the FacesOrBody argument must be supplied as an ObjectCollection and must contain at least one face |
| FacesOrBody | Variant | Optional input Variant that specifies either an ObjectCollection containing the faces to be split or the SurfaceBody object that contains the faces to be split. If an ObjectCollection of faces is supplied, all the faces must belong to the same body. This argument must be specified if the SplitAll argument is False. If the SplitAll argument is True and this argument is not supplied, all the faces on the solid body are split.   This is an optional argument whose default value is null. |

## Version

Introduced in version 6
