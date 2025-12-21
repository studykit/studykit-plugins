# AssemblyComponentDefinition.RepositionObject Method

Parent Object: [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md)

## Description

Method that repositions the specifies object(s) to the new position within the collection of the object in the document.

## Syntax

AssemblyComponentDefinition.**RepositionObject**( ***TargetObject*** As Object, ***Before*** As Boolean, ***StartObject*** As Object, [***EndObject***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetObject | Object | Input the Object that specifies the target object to move other objects next to. Valid object includes: PartFeature, ComponentOccurrence, Sketch, Sketch3D, WorkFeature. |
| Before | Boolean | Input Boolean that indicates whether to position other object(s) before or after the target object.  A value of True indicates that the object(s) will be positioned before the target object. |
| StartObject | Object | Input Object that specifies the object to be repositioned.  Valid object includes: PartFeature, ComponentOccurrence, Sketch, Sketch3D, WorkFeature. |
| EndObject | Variant | Optional input Object that specifies the object to be repositioned.  If specified, all the objects from the StartObject to the EndObject, both inclusive, will be repositioned to the specified position in the document.  If not specified, only the StartObject will be repositioned. Valid object includes: PartFeature, ComponentOccurrence, Sketch, Sketch3D, WorkFeature. |

## Version

Introduced in version 2025
