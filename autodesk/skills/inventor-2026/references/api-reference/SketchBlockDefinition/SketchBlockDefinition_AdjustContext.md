# SketchBlockDefinition.AdjustContext Method

Parent Object: [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md)

## Description

Method that returns the specified sketch object scoped into this sketch block definition, trimming any portion of the context from any sketch block in which this definition has been instanced. In other words, for the given object, this method returns the corresponding object in the context of this sketch block definition, by trimming the sketch block path.

## Syntax

SketchBlockDefinition.**AdjustContext**( ***SketchObject*** As Object ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchObject | Object | Input object that specifies the object to trim the context of. This can be a SketchEntity, SketchBlock, SketchImage or a TextBox. |

## Version

Introduced in version 2010
