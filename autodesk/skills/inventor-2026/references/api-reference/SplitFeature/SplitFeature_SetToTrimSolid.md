# SplitFeature.SetToTrimSolid Method

Parent Object: [SplitFeature](../SplitFeature/SplitFeature.md)

## Description

Method that changes the SplitFeature type to kTrimSolid. The specified portion of the solid is removed.

## Syntax

SplitFeature.**SetToTrimSolid**( ***SplitTool*** As Object, ***Body*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), [***RemovePositiveSide***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplitTool | Object | Input Object that specifies the entity that will be used to define the split. The input can be a WorkPlane, WorkSurface, or 2D Path. Use the CreatePath or CreateSpecifiedPath method on the PartFeatures object to create a Path. Currently, a Path may only consist of 2D sketch elements. |
| Body | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that specifies the body to be trimmed. Only solid bodies are valid. |
| RemovePositiveSide | Boolean | Optional input Boolean that indicates which portion of the split body is to be removed. The default value is True, which indicates that the positive side will be removed. |

## Version

Introduced in version 2010
